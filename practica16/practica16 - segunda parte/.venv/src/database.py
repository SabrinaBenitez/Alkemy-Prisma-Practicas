from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from decouple import config
from src.customer import Customer

DB_USER=config('DB_USER')
DB_PASSWORD=config('DB_PASSWORD')
DB_HOST=config('DB_HOST')
DB_DATABASE=config('DB_DATABASE')

class Database():
    engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}')
    
    def fetchAllUsers(self):
        self.session  = Session(bind=self.engine)
        customer = self.session.query(Customer).all()
        for curs in customer:
            print(curs)

    def saveData(self,customer):
        session  = Session(bind=self.engine)
        session.add(customer)
        session.commit()

    def updateCustomer(self,customerName,address):   
        session  = Session(bind = self.engine)
        dataToUpdate = {Customer.address:address}
        customerData = session.query(Customer).filter(Customer.name == customerName)
        customerData.update(dataToUpdate)
        session.commit()

    def deleteCustomer(self,customer): 
        session  = Session(bind = self.engine)
        customerData = session.query(Customer).filter(Customer.name == customer).first()
        session.delete(customerData)
        session.commit()



db = Database()
customer = Customer("Sabrina",28,"sabrina@gmail.com","Av. Rivadavia 3500","1555")
db.saveData(customer) 
db.updateCustomer('Paul','Rio de Janeiro 1233')
db.deleteCustomer('Felipe')
db.fetchAllUsers()