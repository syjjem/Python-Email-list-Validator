import re

email="James@email.com"

# create your pattern

# pattern = re.compile(r"\w{2,}@\w{4,}\.com")

# pattern = re.compile(r"\w+@\w+\.\w+")

email = "james@yahoo.com"

pattern = re.compile(r"\w+@(gmail.com|yahoo.com)")

result = pattern.search(email)

print(result)

  
