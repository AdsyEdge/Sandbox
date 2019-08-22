"""
Adam Edgar
"""
password_secret = ""
password = str(input("Please enter your password: "))
while len(password) < 6 or len(password) > 16:
    print("Password length is invalid!")
    password = str(input("Please enter your password: "))
for i in range(len(password)):
    password_secret += "*"
print("Ok, your password is " + password_secret)
