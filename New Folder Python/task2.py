password = input("Please enter your password: ")
while len(password) < 8:
    print("Error,8 Character Minimum, Please Try Again.")
    password = input("Please enter your password: ")
print("Password accepted.")
