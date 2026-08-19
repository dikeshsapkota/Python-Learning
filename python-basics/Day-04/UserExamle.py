"""
create User
        ├── Customer
        └── Admin
"""
class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
class Customer(User):
    def __init__(self,name,email,address):
        super().__init__(name,email)
        self.address=address
    def add_product(self):
        return (f"{self.name} added a product")
class Admin(User):
    def __init__(self,name,email):
        super().__init__(name,email)
       
    def delete_product(self):
        return (f"{self.name} deleted a product") 
customer=Customer("Dikesh","dieksh@email.com","ktm")
print(customer.add_product())
admin=Admin("KING","king@gmail.com")
print(admin.delete_product())