fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# fruit["lime"] = "great with tequila"
# print(fruit)
# del fruit["lemon"]
# fruit.clear()
# print(fruit)
# print(fruit["tomato"])
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("we don't have a "+ dict_key)
# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print("="*40)

# ordered_keys = sorted(list(fruit.keys()))
# ordered_keys.sort()
# for f in ordered_keys:
#     print(f + " = " + fruit[f])
# for f in sorted(fruit.keys()):
#     print(f + " = " +fruit[f])
# for val in fruit.values():
#     print(val)
#
# print('=' * 40)
#
# for key in fruit:
#     print(fruit[key])
#
# fruit_keys = fruit.keys()
# print(fruit_keys)
#
#
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)

print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " = " + description)

print(dict(f_tuple))