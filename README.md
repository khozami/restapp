# REST and RPC topics

# Prior settings: run the following commands to install dependencies and keep a frozen version as requirements 

- $ pip3 install pysqlite3 connexion flask 'connexion[swagger-ui]' 
- $ pip3 freeze > requirements.txt
- $ docker build -t wa .
- $ docker run -d -p 5000:5000 wa

# Result
- Visit <localhost:5000/api/people> to get the result
- Visit <localhost:5000/api/ui> to get the Swagger ui 