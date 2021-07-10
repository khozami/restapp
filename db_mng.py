import sqlite3

db_name = 'people.db'

def db_config():
    # Connect to sqlite database
    conn = sqlite3.connect(db_name)
    # cursor object
    cursor = conn.cursor()
    # drop query
    cursor.execute("DROP TABLE IF EXISTS PEOPLE")
    # create query
    query = """CREATE TABLE PEOPLE( ID INTEGER PRIMARY KEY, fname CHAR(20), lname CHAR(20), timestamp CHAR(50) )"""
    cursor.execute(query)
    # commit and close
    conn.commit()
    conn.close()

def db_insert(fname, lname, timestamp):
    conn = sqlite3.connect(db_name)
    qry = "INSERT INTO PEOPLE (fname,lname,timestamp) VALUES ('{}', '{}', '{}')".format(fname, lname, timestamp)
    conn.execute(qry)
    conn.commit()
    conn.close()


def db_readline(lname):
    conn = sqlite3.connect(db_name)
    qry = "SELECT fname, lname, timestamp FROM PEOPLE WHERE lname='{}'".format(lname)
    cur = conn.execute(qry)
    fetched_data = cur.fetchone() 
    data= []

    if fetched_data != None:
        data = list(fetched_data)
    conn.close()
    return list(data)

def db_read_all():
    conn = sqlite3.connect(db_name)
    qry = "SELECT fname, lname, timestamp FROM PEOPLE"
    cur = conn.execute(qry)
    fetched_data = cur.fetchall() # [(x,y,z),(w,u,v),(...)]
    data= []

    if fetched_data != None:
        data= [dict(zip(('fname','lname','timestamp'), el)) for el in fetched_data]
    conn.close()
    return list(data)


def db_update(last_name_to_lookup, fname, lname, timestamp):
    conn = sqlite3.connect(db_name)
    qry = "UPDATE PEOPLE set fname = '{}', lname = '{}', timestamp = '{}' where lname = '{}'".format(fname, lname, timestamp, last_name_to_lookup)
    conn.execute(qry)
    conn.commit()
    conn.close()


def db_delete(lname):
    conn = sqlite3.connect(db_name)
    qry = "DELETE FROM PEOPLE where lname = '{}';".format(lname)
    conn.execute(qry)
    conn.commit()
    conn.close()
