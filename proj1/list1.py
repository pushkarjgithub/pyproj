calculation_to_units = 24 * 60
# number_of_days = 20
unit_type = "minutes"


def days_to_units(number_of_days):
    print(f"calculate {number_of_days} days = {number_of_days * calculation_to_units} {unit_type}")
    # print(message)
    # return f"calculate {number_of_days} days = {number_of_days * calculation_to_units} {unit_type}"


def validate_input():
    try:
        # if days_input.isdigit():
        if int(num_of_days_element) > 0:
            days_to_units(int(num_of_days_element))
        elif num_of_days_element == "exit":
            print("Exit as input entered - Not Allowed")
        else:
            print("Invalid number entered...try again!")
    except ValueError:
        print(f"Input - \"{num_of_days_element}\" is not a number...plz try again!")


days_input = ""

while days_input != "exit":
    # days_input, message_input = input("Enter number of days for conversation = "), input("Enter message here = ")
    days_input = input("Enter number of days as comma separated list or conversation = ")
    list_of_days = days_input.split(",")

    print(f"type of list = {type(list_of_days)}")
    print(f"list of days = {list_of_days}")

    print(f"type of set = {type(set(list_of_days))}")
    print(f"set of days = {set(list_of_days)}")

    for num_of_days_element in set(list_of_days):
        validate_input()
    print("\n")


""" message_input = input("Enter message here = ")
# days_input_number = int(days_input) """


# calculated_value = days_to_units(days_input)
# print(calculated_value)
