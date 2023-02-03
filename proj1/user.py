# this class will only have definition, not implementation or method calling
# method calling will happen from main1.py file

class User:
    def __init__(self, name, password, email, current_job_title):
        self.name = name
        self.password = password
        self.email = email
        self.current_job_title = current_job_title

    # Its called method in class, not function
    def get_user_info(self):
        print(f"username = {self.name}")
        print(f"email = {self.email}")
        print(f"job title = {self.current_job_title}")
        print("#########")

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def change_username(self, new_username):
        self.name = new_username

    def change_password(self, new_password):
        self.password = new_password


