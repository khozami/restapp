"""
This is the people module and supports all the ReST actions for the
PEOPLE collection
"""

# System modules
from datetime import datetime
import db_mng 

# 3rd party modules
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        json string of list of people
    """
    # Create the list of people from our data
    return db_mng.db_read_all() 


def read_one(lname):
    """
    This function responds to a request for /api/people/{lname}
    with one matching person from people

    :param lname:   last name of person to find
    :return:        person matching last name
    """
    # Does the person exist in people?
    person = db_mng.db_readline(lname)
    
    if person != []:
        person = dict(zip(["fname","lname","timestamp"], person ))
    # otherwise, nope, not found
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )

    return person


def create(person):
    """
    This function creates a new person in the people structure
    based on the passed in person data

    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    person = db_mng.db_readline(lname)

    # Does the person exist already?
    if person == [] and lname is not None:
        db_mng.db_insert(fname, lname, get_timestamp())

        return make_response(
            "{lname} successfully created".format(lname=lname), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Person with last name {lname} already exists".format(lname=lname),
        )


def update(lname, person):
    """
    This function updates an existing person in the people structure

    :param lname:   last name of person to update in the people structure
    :param person:  person to update
    :return:        updated person structure
    """
    last_name_to_lookup = lname

    lname = person.get("lname", None)
    fname = person.get("fname", None)
    
    fetched_person = db_mng.db_readline(last_name_to_lookup)

    # Does the person exist already?
    if fetched_person != []:
        db_mng.db_update(last_name_to_lookup, fname, lname, get_timestamp())    
        return lname

    # otherwise, nope, that's an error
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )


def delete(lname):
    """
    This function deletes a person from the people structure

    :param lname:   last name of person to delete
    :return:        200 on successful delete, 404 if not found
    """
    fetched_person = db_mng.db_readline(lname)

    # Does the person to delete exist?
    if fetched_person != []:
        db_mng.db_delete(lname)
        return make_response(
            "{lname} successfully deleted".format(lname=lname), 200
        )

    # Otherwise, nope, person to delete not found
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )
