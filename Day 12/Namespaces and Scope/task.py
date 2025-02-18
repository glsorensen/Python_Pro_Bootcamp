enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


def a_function(a_parameter):
    a_variable = 15
    return a_parameter


a_function(10)
print(a_variable)
