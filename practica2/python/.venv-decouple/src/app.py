from decouple import config

print(config('MYSQL_HOST'))
print(config('MYSQL_PORT'))
print(config('MYSQL_USER'))
print(config('MYSQL_PWD'))
print(config('MYSQL_DB'))

print('Host : {HOST} - Puerto : {PORT}'.format(HOST = config('MYSQL_HOST'),PORT = config('MYSQL_PORT')))