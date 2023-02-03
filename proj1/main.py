# import dictionary
# import dictionary as dict
# from dictionary import *
from dictionary import validate_input, user_input_message
# if you use from you don't need to mention module name to reference its function, vars.
# If you use import you need to use module_name.function_name/var

days_input = ""
while days_input != "exit":
    # days_input, message_input = input("Enter number of days for conversation = "), input("Enter message here = ")
    days_input = input(user_input_message)
    days_and_units = days_input.split(":")
    print(days_and_units)

    days_and_units_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    print(f"type of dictionary = {type(days_and_units_dictionary)}")
    print(f"dictionary elements =  {days_and_units_dictionary}")

    validate_input(days_and_units_dictionary)
    print("\n")