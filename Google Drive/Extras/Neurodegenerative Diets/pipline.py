from db_classes import *

def create_user():
    first = input("Enter First Name:")
    last = input("Enter Last Name:")
    email = input("Enter email address:")
    diagnosis = input("Enter Your Most Recent Diagnosis:")
    # user = User(email= email, first= first, last= last, diagnosis=diagnosis)
    # session.add(user)
    print(f'First= {first}, Last= {last}, Email= {email}')

create_user()