import os
from dotenv import load_dotenv, find_dotenv
load_dotenv (find_dotenv())
print(os.getenv('MYSQL_HOST'))
print(os.getenv('MYSQL_PORT'))
print(os.getenv('MYSQL_USER'))
print(os.getenv('MYSQL_PWD'))
