# 3 parts of the program are: registration of user, log in and main loop that will run the program.
 

# Registration
import csv
userEmail = input("Please enter your email :")
userPassword = input("Please enter your password :")
userPassword2 = input("Please re-enter your password :")
if userPassword == userPassword2:
    with open("Database.csv", "w", newline= "") as d:
        writer = csv.writer(d, delimiter= ",")
        writer.writerow(["Email", "Password", "Password2"])
        writer.writerow([userEmail, userPassword, userPassword2])

