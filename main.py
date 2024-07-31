import random
"""
 1 : snake
-1 : water
 0 : gun
 """


# computer    = -1

# now to generate randm nu: 
computer    = random.choice([-1,0,1])
youstr      = input("\nEnter your choice: ")
youDict     = {"s":1     ,"w":-1     ,"g":0}
reverseDict = { 1:"Snake", -1:"Water", 0: "Gun"}
you         = youDict[youstr]

# by now we have 2 numbers(variable), which is you and computer.

print(f"\nYou Chose     : {reverseDict[you]},\nComputer Chose: {reverseDict[computer]},\n")


if (computer == you):
    print("It's a Draw!\n")

else:

    if (computer == -1 and you == 1):
            print("\"YOU WIN!\"\n")

    elif(computer == -1 and you == 0):
            print("\"YOU LOSE!\"\n")

    elif (computer ==  1 and you ==-1):
            print("\"YOU LOSE!\"\n")

    elif (computer ==  1 and you == 0):
            print("\"YOU WIN!\"\n")

    elif (computer == 0 and you == -1):
            print("\"YOU WIN!\"\n")

    elif (computer == 0 and you == 1):
            print("\"YOU LOSE!\"\n")

    else:
            print("someting went wrong...\n")