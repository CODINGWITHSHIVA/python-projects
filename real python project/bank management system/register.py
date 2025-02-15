# User Registration signin Signup
from database import *
def SignUp():
    username=input("Create Username: ")
    temp = cursor.execute(f"SELECT user name FROM customers where username='{username}';")
    print(temp)
