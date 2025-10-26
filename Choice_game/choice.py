print("🕵️.The Lost Treasure")
print("You are an explorer deep in an ancient jungle.\n"
"Legends say a proceless treasure lies hidden somewhere\n" 
"within. After hours of walking ,you reach a fork in the path ")

              

while True:
    print("\nChoice 1: Go left toward the sound of running water\n"
          "Choice 2: Go right toward a dark cave entrance.\n")
    Choice = input("Choice: ")
    if Choice == "1":
       print("\nYou reach a wide river. The current looks strong.\n"
             "There's a pile of wood nearby.\n"
             "You must decide what to do")
       print("Choice 1: Try to swim across.\n"
             "Choice 2: Build a raft from wood.\n"
             "Choice 3: Go Back to The Fork.\n")
       while True:
         Choice = input("Choice: ")
         if Choice == "1":
            print("\nThe current sweeps you away.\n"
                  "\nGAME OVER! ")
            exit()
         elif Choice =="2":
            print("You cross safely and discover a chest of gold.You win!🥳")
            exit()
         elif Choice == "3":
            break
         else:
            print("Invalid Choice")
            continue   
    elif Choice == "2":
        print("\nYou step into dark cave.it's cold and echoes\n"
              "with strange noises.\n"
              "You have a matchbox in your pocket.\n")
        print("\nChoice 1: Light atorch.\n"
              "Choice 2: Walk ahead in darkness.\n" 
              "Choice 3: Go back to the fork. ")
        while True:
            Choice = input("\nChoice: ")
            if Choice == "1":
               print("You scare away a swarm of bats \n"
                     "and spot a golden idol.You win!🥳")
               exit()
            elif Choice == "2":
               print("You fall into a hidden pit\n"
                     "Game Over.")
               exit()
            elif Choice == "3":
               break
            else:
               print("Invalid Choice.")
               continue
    else :
        print("Invalid choice")
        continue
       
