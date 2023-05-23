# In this project we make communication with python App and GitLab App

import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")

# printing text from text file
print(response.json())
print(type(response.json()))
print(response.json()[0])

# json() is a function which converts actual data type into python data type
my_project = response.json()

# we are extracting the name and web_url from the project
for project in my_project:
    print(f" Project Name : {project['name']}\n Project URL : {project['web_url']}\n")