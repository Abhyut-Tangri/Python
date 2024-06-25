#write a program that asks user 5 options, and then asks them again till they click 5, escape
choice=int(input('please choose one of the options from the list /n 1. Eat food /n 2. Sleep /n 3.Go outside /n 4.Play a game /n 5.Exit'))

escape=5
numofchoice=0
while choice != escape:
    if choice==1:
        print('you chose 1')
        choice=int(input('please choose one of the options from the list /n 1. Eat food /n 2. Sleep /n 3.Go outside /n 4.Play a game /n 5.Exit'))
        numofchoice=numofchoice+1
    elif choice==2:
        print('you chose 2')
        choice=int(input('please choose one of the options from the list /n 1. Eat food /n 2. Sleep /n 3.Go outside /n 4.Play a game /n 5.Exit'))
        numofchoice=numofchoice+1
    elif choice==3:
        print('you chose 3')
        choice=int(input('please choose one of the options from the list /n 1. Eat food /n 2. Sleep /n 3.Go outside /n 4.Play a game /n 5.Exit'))
        numofchoice=numofchoice+1
    elif choice==4:
        print('you chose 4')
        choice=int(input('please choose one of the options from the list /n 1. Eat food /n 2. Sleep /n 3.Go outside /n 4.Play a game /n 5.Exit'))
        numofchoice=numofchoice+1
    elif choice==5:
        print('you chose to exit')
        numofchoice=numofchoice+1
        break
    else:
        print('please put a number between 1 and 5')
        choice=int(input('please choose one of the options from the list /n 1. Eat food /n 2. Sleep /n 3.Go outside /n 4.Play a game /n 5.Exit'))
    
    
    

if choice == escape:
    print('you chose to exit')
    print('you made {} choices'.format(numofchoice))

#alt solution 

