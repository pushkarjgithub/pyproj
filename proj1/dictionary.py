
user_input_message = "Enter number of days and conversion unit in this (days:units) format = "

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


def validate_input(days_and_units_dictionary):
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




