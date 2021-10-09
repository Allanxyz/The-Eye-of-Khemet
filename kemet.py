input("\nWelcome to Karnak. Beware of the Eye. [Press 'Enter' to continue]")


print('-' * 30)
print(
"""INSTRUCTIONS: Type in your choice as given in the choices provided.
Press 'Enter' when prompted '>'""")
print('-' * 30)
yes_no = input("Do you wish to continue? Y/N : ")
print('-' * 30)


if(yes_no == 'Y'):
    yes = True
else:
    exit()

loop = 1
while (yes):
    while loop == 1:
        input("[The number that you're calling is out of coverage. Please try again later.]>")
        input("\n\"What's going on? Abhi to network tha\">")
        input("\n\".....Whatever\">")
        input("\n\"What should I do....?\">")
        walk = input("\nGo back inside(A) Take a walk(B)")
        if (walk == 'B'):
            loop = 2
        else:
            loop = 5
    while loop == 2:
        input("\n[You call out Sheldon who comes out the window wrapped in a blanket]")
        input("\n\"I'm going out for a walk! Do you need anything!?\">")
        input("\n\"Right now?!\">")
        input("\n\"Yeah! Have to make some calls too!\">")
        input("\n\"Bring me something to eat!\">")
        input("You come across a museum entrance")
        enter_museum = input("Enter or no?")
        if (enter_museum == 'yes'):
            loop = 3
        else:
            loop = 5
    
    while loop == 3:
        input("You get tickets to visit")
        input("You see basement named Khemet")
        enter_khemet = input("Enter khemet")
        if (enter_khemet == 'yes'):
            loop = 4
        else:
            loop = 5
            
    while loop == 4:
        input("You see that these are mostly Egyptian relics")
        input("lights go off")
        back = input("Go back or no?")
        if (back == "yes"):
            loop = 6
        else:
            loop =5
    
    while loop == 6:
        input("There's no one here.")
        input("A book is lying down in front of you.")
        pick = input("Pick up book or no?")
        if (pick == "yes"):
            loop = 7
        else:
            loop = 5
    
    while loop == 7:
        input("Wet footsteps like meat being hit on floor")
        input("You reach the dark ground floor to see silhouettes standing all around you")
        give = input("'arjaeha")
        if (give == "yes"):
            loop = 8
        else:
            loop = 5
    
    while loop ==8:
        input("You're back at the entrance now fully dark and sealed outside. You call your friend to ask what he wants")
        input("Icecream")
        loop = 5
    
    
    while loop == 5:
        exit()