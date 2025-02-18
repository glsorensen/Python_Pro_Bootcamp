# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# print(format_name("AnGEla", "YU"))


def is_leap_year(year):
    # Check if the year is divisible by 400
    if year % 400 == 0:
        return True
    # If not, check if the year is divisible by 100
    elif year % 100 == 0:
        return False
    # If not, check if the year is divisible by 4
    elif year % 4 == 0:
        return True
    # If none of the above conditions are met, it's not a leap year
    else:
        return False

# Call your function with hard-coded values
print(is_leap_year(2400))  # Example Input 1, Expected Output: True
print(is_leap_year(1989))  # Example Input 2, Expected Output: False


def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)