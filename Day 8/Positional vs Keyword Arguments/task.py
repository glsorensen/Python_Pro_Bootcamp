# # Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")


#Functions with more than one input

# def greet_with(name, location):
#     print(f"Hello {name}!")
#     print(f"What is it like in {location}?")
#
# greet_with("Gunnnar", "Denver")
#
# greet_with(location = "Denver", name = "Gunnnar")

# def calculate_love_score(name1, name2):
#     def true_test(name1):
#         name1_lower = name1.lower()
#         count_t = name1_lower.count("t")
#         count_r = name1_lower.count("r")
#         count_u = name1_lower.count("u")
#         count_e = name1_lower.count("e")
#         return true_test(count_t)
#     print(true_test(name1))
#     def love_test(name1):
#         count_l = name1.lower.count("l")
#         count_o = name1.lower.count("o")
#         count_v = name1.lower.count("v")
#         count_e = name1.lower.count("e")
#
# # Call your function with hard coded values
# calculate_love_score("Kanye West", "Kim Kardashian")


def calculate_love_score(name1, name2):
    # Combine both names into a single string and convert to lowercase
    combined_names = (name1 + name2).lower()
    print(combined_names)

    # Count occurrences of each letter in "TRUE"
    true_count = sum(combined_names.count(char) for char in "true")
    print(true_count)
    # Count occurrences of each letter in "LOVE"
    love_count = sum(combined_names.count(char) for char in "love")
    print(love_count)
    # Combine the counts to form the love score
    love_score = int(str(true_count) + str(love_count))
    print(love_score)
    # Print the love score
    print(f"Love Score = {love_score}")


# Call the function with hard-coded values
calculate_love_score("Kanye West", "Kim Kardashian")