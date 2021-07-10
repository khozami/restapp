# REST and RPC topics

### Install dependencies and keep a frozen version as requirements 

- $ pip3 install pysqlite3 connexion flask 'connexion[swagger-ui]' 
- $ pip3 freeze > requirements.txt
- $ docker build -t wa .
- $ docker run -d -p 5000:5000 wa

### Results
- To get the result visit: <localhost:5000/api/people> 
- To get the Swagger ui visit: <localhost:5000/api/ui>  

### Thanks to
- <https://realpython.com/flask-connexion-rest-api/#what-rest-is>
- <https://medium.com/analytics-vidhya/sqlite-database-crud-operations-using-python-3774929eb799>
