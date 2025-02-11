import random
import my_module

random_number = random.randint(0, 100)
print(random_number)

print(my_module.my_fav_number)

ran_number_0_1 = random.random() * 10
print(ran_number_0_1)

random_float = random.uniform(1, 10)
print(random_float)

random_0_or_1 = random.randint(0,1)

if random_0_or_1 == 0:
    print('Heads')
else:
    print('Tails')