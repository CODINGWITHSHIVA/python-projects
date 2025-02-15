from register import *
print("Welome to Mohit Banking Project")

while True:
    try:
        register=int(input("1. SignUp\n"
                           "2. SignIn\n"))
        if register == 1 or register==2:
            if register==1:
                SignUp()

        else:
            print("Please Enter Vaild Input From Options")
        
    except ValueError:
        print("Invalid Input Try Again with Numbers")






