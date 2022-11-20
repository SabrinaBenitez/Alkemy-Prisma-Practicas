import sqlalchemy as db
from decouple import config
from sqlalchemy import MetaData, Table, Column
from src.customer import Customer

DB_USER=config('DB_USER')
DB_PASSWORD=config('DB_PASSWORD')
DB_HOST=config('DB_HOST')
DB_DATABASE=config('DB_DATABASE')

class Database():
    engine = db.create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}')
    def __init__(self):
        self.connection = self.engine.connect()
  
    def fetchByQuery(self,query):
        fetchQuery = self.connection.execute(f"select * from {query}")

        for data in fetchQuery.fetchall():
            print(data)

    def savedata(self,customer):
        self.connection.execute(f"""insert into Customer(name,age,email,address,zip_code)
                                values ('{customer.name}',
                                       '{customer.age}',
                                       '{customer.email}',
                                       '{customer.address}',
                                       '{customer.zip_code}')""") 

    def fetchUserByName(self): 
        meta = MetaData()
        customer = Table('customer',meta,Column('name'))
        data = self.connection.execute(customer.select())    
        for cust in data:
            print(cust)                         
                              

dbase=Database()
custumer = Customer("Leonel",28,"leo@gmail.com","Av. Rivadavia 2500","1455") 

dbase.savedata(custumer)
dbase.fetchByQuery('public.customer')  
dbase.fetchUserByName()                                      
