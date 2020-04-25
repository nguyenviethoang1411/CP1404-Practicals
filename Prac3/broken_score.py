"""
CP1404/CP5632 - Practical
Broken program to determine score status
github link: https://github.com/nguyenviethoang1411/CP140-Practicals
"""
import random

def get_score(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score:"))

    if 50 <= score < 90:
        print("Passable")
    elif score >= 90:
        print("Excellent")
    else:
        print("Bad")
    return

number=random.randint(1,100)
print("{} is".format(number))
get_score(number)