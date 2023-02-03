import requests

# response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
response = requests.get("https://api.github.com/users/pushkarjgithub/repos")
my_projects = response.json()
# print(type(my_projects))
print(my_projects)

for project in my_projects:
#    print(f"project Name: {project['name']}\nProject Url: {project['web_url']}\n")
    print(f"Account Name: {project['full_name']}")
    print(f"Repo Name: {project['name']}")
    print(f"Repo url: {project['html_url']}")
