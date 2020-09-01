# Muhammad Faraz Sohail


# function to check the password entered
def pwdChek(psswd):
    # local vartiables
    num = 0
    up = 0
    lw = 0

    # checks the lngth of password
    if(len(psswd) < 8):
        return False

    # loop to check individual characters of the password
    for w in psswd:
        if(w.isnumeric()):  # checks for numeric literals in the password
            num = num+1
        elif(w.isupper()):  # checks for capital literals in the password
            up = up+1
        elif (w.islower()):  # checks for lower literals in the password
            lw = lw+1

    # returns the results of the testing we did earlier
    if(num > 0 and up > 0 and lw > 0):
        return True
    else:
        return False


# password input from user
pwd = input("Please enter a password:")

# this prints the result we got after testing
if(pwdChek(pwd)):
    print("This is a good password.")
else:
    print("This is not a good password.")
