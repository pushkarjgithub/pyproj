from user import User
from post import Post


user1 = User("chris", "pwd1", "abc@gmail.com", "painter")
# print(user1.name)
user1.get_user_info()
user1.change_username("jordan")
user1.get_user_info()

user2 = User("tom", "pwd1", "abc@gmail.com", "devops")
user2.get_user_info()

new_post = Post("learn python high priority", user2.name)
new_post.get_post_info()