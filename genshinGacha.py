import random

star3 = ["Dave", "Kevin", "Steve", "Phil", "Tim", "Tom", "Larry", "John"]
star4 = ["Mike", "Paul", "Jerry", "Darwin"]
star5 = ["KingBob", "Ken"]

def gachaMachine(counter4, counter5):
    if counter5 < 76 or counter5 > 85:
        item = random.randint(0, 999)
        global star3, star4, star5
        if (counter4 < 10) or (counter5 < 90):

            if item < 933:
                gotItem = star3[(random.randint(0, len(star3)-1))]
            if 933 <= item < 993 :
                gotItem = star4[(random.randint(0, len(star4)-1))]
            if 993 <= item :
                gotItem = star5[(random.randint(0, len(star5)-1))]
        if (counter4 == 10):
            gotItem = star4[(random.randint(0, len(star4)-1))]

        if (counter5 == 90):
            if len(star5) == 0:
                star5 = ["KingBob", "Ken"]
            
            gotItem = star5[(random.randint(0, len(star5)-1))]
            star5.remove(gotItem)


    if 76 <= counter5 < 85:
        item = random.randint(0, 4964)
        if (counter4 < 10) or (counter5 < 90):

            if item < 3732:
                gotItem = star3[(random.randint(0, len(star3)-1))]
            if 3732 <= item < 3972 :
                gotItem = star4[(random.randint(0, len(star4)-1))]
            if 3972 <= item :
                gotItem = star5[(random.randint(0, len(star5)-1))]
        if (counter4 == 10):
            gotItem = star4[(random.randint(0, len(star4)-1))]

        if (counter5 == 90):
            if len(star5) == 0:
                star5 = ["KingBob", "Ken"]
            
            gotItem = star5[(random.randint(0, len(star5)-1))]
            star5.remove(gotItem)

    return gotItem

def playGacha():
    global star3, star4, star5
    counter4 = 0
    counter5 = 0
    chioce = input("Do you want to play? (Y or N) :")
    while chioce == "Y":
        n = int(input("Select 1 or 10 times :"))
        for a in range(n):
            counter4 += 1
            counter5 += 1
            userItem = gachaMachine(counter4, counter5)
            print("counter :", counter4, counter5, userItem)
            
            if (counter4 == 10):
                counter4 = 0
            if (userItem) in star4:
                counter4 = 0
            if (counter5 == 90):
                counter5 = 0
            if (userItem) in star5:
                counter5 = 0
        chioce = input("Do you want to play? (Y or N) :")

playGacha()
