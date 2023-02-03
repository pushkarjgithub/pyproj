

def days_to_units(number_of_days, units):
    if units == "hours":
        calculation_to_units = 24
        print(f"calculate {number_of_days} days = {number_of_days * calculation_to_units} {units}")
    elif units == "min":
        calculation_to_units = 24 * 60
        print(f"calculate {number_of_days} days = {number_of_days * calculation_to_units} {units}")
    else:
        print(f"unsupported unit \"{units}\" entered...plz try again!")

    # print(message)
    # return f"calculate {number_of_days} days = {number_of_days * calculation_to_units} {unit_type}"


def validate_input():
    try:
        # if days_input.isdigit():
        num_of_days_element = int(days_and_units_dictionary["days"])
        if int(num_of_days_element) > 0:
            # print(num_of_days_element)
            # print(days_and_units_dictionary["units"])
            days_to_units(num_of_days_element, days_and_units_dictionary["units"])
        elif num_of_days_element == "exit":
            print("Exit as input entered - Not Allowed")
        else:
            print("Invalid number entered...try again!")
    except ValueError:
        print(f"Input - \"{num_of_days_element}\" is not a number...plz try again!")


days_input = ""

while days_input != "exit":
    # days_input, message_input = input("Enter number of days for conversation = "), input("Enter message here = ")
    days_input = input("Enter number of days and conversion unit in this (days:units) format = ")
    days_and_units = days_input.split(":")
    print(days_and_units)

    days_and_units_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    print(f"type of dictionary = {type(days_and_units_dictionary)}")
    print(f"dictionary elements =  {days_and_units_dictionary}")

    validate_input()
    print("\n")


""" message_input = input("Enter message here = ")
# days_input_number = int(days_input) """


# calculated_value = days_to_units(days_input)
# print(calculated_value)
