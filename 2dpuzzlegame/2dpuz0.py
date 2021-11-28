'''
Point : x, y, isInside
'''

import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def isInside(self, x1, x2, y1, y2):
        if x1 < self.x < x2 and y1 < self.y < y2:
            print("congratulations! Your point is inside the rectangle.")
        else:
            print("Your point isn't in the rectangle.")

        print("(x1, y1) :", (x1, y1))
        print("(x2, y2) :", (x2, y2))

x1 = random.randint(1, 19)
x2 = random.randint(x1 + 1, 20)
y1 = random.randint(1, 19)
y2 = random.randint(y1 + 1, 20)

guess_x = int(input("Enter your x value :"))
guess_y = int(input("Enter your y value :"))

p = Point(guess_x, guess_y)
p.isInside(x1, x2, y1, y2)
