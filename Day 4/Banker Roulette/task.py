import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_friend = random.choice(friends)
print(random_friend)


random_friend_index = random.randint(0, len(friends) -1)
print(random_friend_index)
random_friend_item = friends[random_friend_index]
print(random_friend_item)
