wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key, value in wardrobe.items():
    for i in value:
        print("{} {}".format(value, key))
'''       
Here is your output:
red shirt
blue shirt
white shirt
blue jeans
black jeans
'''
