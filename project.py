import re
import os

pattern = re.compile(r"\w+@(gmail.com|yahoo.com|hotmail.com)")

accepted_emails = []


# open the inventory file for reading
fobject = open("inventory.txt", "r")

results = fobject.readlines()

if os.path.exists("accepted_users.txt"):
    os.remove("accepted_users.txt")

f = open("accepted_users.txt", "a")

f.write ("Firstname,Lastname,Email,Username\n")

for result in results:
    if result != "Firstname.Lastname,Email,Username\n":
        pattern_result=pattern.search(result)

        if pattern_result == None:
            # write the accepted emails to a file
            accepted_emails.append(result)

           
            f.write(result)

print(accepted_emails)            