import datetime
# from datetime import datetime

user_input = input("Enter your goal with a deadline separated by colon = ")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%m.%d.%Y")
print(f"deadline for goal completion = {deadline_date}")
today_date = datetime.datetime.today()
print(f"today's date = {today_date}")

time_till = deadline_date - today_date
hours_till = int(time_till.total_seconds() / 60 / 60)
print(f"time remaining to complete goal - {goal} = {time_till.days} days or {hours_till} hours ")
