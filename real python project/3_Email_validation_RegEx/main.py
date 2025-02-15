# #a-z
# #0-9
# #. _ at a time 1 uses of special charecter
# # @ time 1
# # . 2,3 positon from the last

import re

# Corrected regex pattern for validating an email address
email_condition = r"^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$"  

user_email = input("Enter your Email: ")

if re.search(email_condition, user_email):
    print("Right Email")
else:
    print("Wrong Email")




import re

email_condition = r"^[a-z A-Z 0-9]+[\._]?[a-z A-Z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("ENter you email:")
if re.search(email_condition, user_email):
    print("Right email")
else:
    print("Wrong email")
