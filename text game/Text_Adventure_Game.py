import os

name = input("Before you begin please enter the name of one of your friends").upper()
print()

def next():
    n = input('''Press anykey to continue ''')

def list_of_decision(n):
    for index,choice in enumerate(n):
        print("{0}.{1}".format(index+1,choice))

def begin():
    os.system('clear')
    print('''You wake up in a small, dark, unfamiliar room. You then realize
    that your favorite throwing card is missing. You have to get it back''')
    print("<type the number of your choice then enter>")

    stage1 = ["Check the door","Check the window","Observe your surroundings"]

    list_of_decision(stage1)

    choice = int(input("Your choice: "))

    if choice == 1:
        os.system('clear')
        print("The door is unlocked. It looks like your kidnapper wasn't very smart.")
        next()
        stage2()
    elif choice == 2:
        os.system('clear')
        print("A fallen tree blocks your escape")
        next()
        begin()
    elif choice == 3:
        os.system('clear')
        print('''You woke up on the floor of what appears to be an empty,
    abandoned shed in the middle of the woods. You can tell you are in the woods
    because there is one window in the shed, however a fallen tree is partially blocking the window''')
        next()
        begin()

def stage2():
    print("Your are now outside. Forest surrounds you in all directions.")
    print("You see a campsite to your left")
    print()
    a = ["Go toward the campsite","Explore the forest","Observe your surroundings"]

    list_of_decision(a)

    choice = int(input("Your choice: "))

    if choice == 1:
        os.system('clear')
        stage3()
    elif choice == 2:
        os.system('clear')
        print('''You explore the forest. When you get back you realize the tent is gone,
        and the thief has escaped with your throwing card''')
        next()
        os.system('clear')
        print("GAME OVER")
    elif choice == 3:
        os.system('clear')
        print("You are a well lit forest in the peak of autumn.")
        print('''The leaves are colorful and almost...
        ...Dream like. To your left you see a campsite with a blue tent,
        and a picnic table made from logs.''')
        next()
        stage2()

def stage3():
    print('''You see your throwing card on the table.
    Excellent! Now to bring the thief to justice''')
    print("1. Enter tent")
    choice = int(input("Your choice: "))
    if choice == 1:
        print('''You see {0} sleeping in the tent. You ask him why he took your
        throwing card.'''.format(name))
        next()
        over()
    else:
        print("Wrong input")
        os.system('clear')
        next()
        stage3()
def over():
    os.system('clear')
    print('''{0} responds 'I was mad becasau I put too much deodorant on.
    So I took your card'.''')
    print("Wait, what?")
    os.system('clear')
    print("You wake up. It was just a weird dream.")
    next()
    os.system('clear')
    print("YOU WIN")
# --- MAIN ---
begin()
