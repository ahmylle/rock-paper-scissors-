import random 
play_again=True
print("welcome to rock paper scissoes!")
while play_again:


    p2 = random.randint(1,3)
    print (p2)

    choice =int(input ("enter \n 1 for rock \n 2 for paper \n 3 for scissors:"))

    print ("p2 chose", p2)

    if p2 == choice:
        print("its a tie")
    elif p2 == 2 or choice == 1:
        print ("you lose")
    elif p2==1 and choice ==2:
        print ("you lose")
    elif p2==3 and choice==2:
        print ("you lose")
    elif choice >3  or choice < 1:
        print("that option is not allowed")
    else:
        print("you win")

        user_input= input("do you want to play again")
        if user_input== "no":
            play_again=False

print()
print("thanks for playing") 