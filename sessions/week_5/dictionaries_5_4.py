if __name__ == '__main__':

    fruit_bowl = {}

    fruit_bowl['apple'] = 4
    fruit_bowl['banana'] = 2

    print(fruit_bowl)

    adding_fruit = input("What kind of fruit are you adding? ")
    fruit_bowl[adding_fruit] = 1 + fruit_bowl.get(adding_fruit, 0)

    print(fruit_bowl)

    for fruit in fruit_bowl:
        fruit_bowl[fruit] -= 1
        print(fruit, fruit_bowl[fruit])

    if "pear" in fruit_bowl:
        print("You must have added a pear!")
