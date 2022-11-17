import sqlalchemy as db

class Database():
    engine = db.create_engine('postgresql+psycopg://postgres:test_password@localhost:5432/test')
    def __init__(self):
        self.connection = self.engine.connect()
  
    def fetchByQuery(self,query):
        fetchQuery = self.connection(f"select from {query}")

        for data in fetchQuery.fetchall():
            print(data)

    def savedata(self,customer):
        self.connection.execute(f"""insert into customer(
                                name,age,email,address,zip_code)
                                values '{customer.name}',
                                       '{customer.age}',
                                       '{customer.email}',
                                       '{customer.address}',
                                       '{customer.zip_code}')""")

class Customer():
    def __init__(self,name,age,email,address,zip_code):
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.zip_code = zip_code


database = Database()
custumer = Customer("Leonel",28,"leo@gmail.com","Av. Rivadavia 2500","1455") 

database.savedata(custumer)
database.fetchByQuery('public.customer')                                       

