# code by Easht Modi
# @eashtmodi

while True:
    while True:
        try: numberOfPlayers=int(input("Tell the number of players: "))
        except: print("enter an integer")
        else:
            if numberOfPlayers>1 and numberOfPlayers<5:
                break
            else:
                print("choose from 2,3,4")


    players=[]
    for i in range(0,numberOfPlayers):
        while True:
            name=input("Enter Name of players: ")
            if name.isalpha():
                break
            else:
                print("enter alphabets")
        players.append(name)


    while True:
        while True:
            try:
                numberOfGoals=int(input("Please enter number of Goals played in one round: "))
                break
            except: print("please enter an integer")
        if numberOfGoals == 9 or numberOfGoals == 18:
            break
        else:
            print("choose from 9 or 18")

    while True:
        par=input("Please enter par: ")
        try:
            par=int(par)
        except:
            print("enter integer")
        else:
            break
    print("Number of players",numberOfPlayers)
    print("Names of players",players)
    print("Number of goals that are played",numberOfGoals)

    player1score=[]
    player2score=[]
    player3score=[]
    player4score=[]

    while True:
        verify=str(input("Please enter yes if data displayed is right otherwise no for re-entering: "))
        if verify =="yes" or verify =="no":
            break
        else:
            print("enter yes or no")

    if verify=="yes":
        break
    elif verify =="no":
        pass




for x in range(0,numberOfPlayers):
    for i in range(0,numberOfGoals):
        if x==0:
            while True:
                try:
                    strokes=int(input("Enter the strokes for "+str(players[x])+" goal number "+str(i+1)+": "))
                    confirmstrokes=int(input("Enter the strokes for "+str(players[x])+" goal number "+str(i+1)+" for confirmation: "))
                    if confirmstrokes==strokes:
                        player1score.append(strokes)
                        break
                    else:
                        print("enter same value")
                except: print("enter a integer")
        if x==1:
            while True:
                try:
                    strokes = int(input("Enter the strokes for " + str(players[x]) + " goal number " + str(i + 1)+": "))
                    confirmstrokes = int(input("Enter the strokes for " + str(players[x]) + " goal number " + str(
                        i + 1) + " for confirmation: "))
                    if confirmstrokes == strokes:
                        player2score.append(strokes)
                        break
                    else:
                        print("enter same value")
                except:
                    print("enter a integer")
        if x==2:
            while True:
                try:
                    strokes = int(input("Enter the strokes for " + str(players[x]) + " goal number " + str(i + 1)+": "))
                    confirmstrokes = int(input("Enter the strokes for " + str(players[x]) + " goal number " + str(
                        i + 1) + " for confirmation: "))
                    if confirmstrokes == strokes:
                        player3score.append(strokes)
                        break
                    else:
                        print("enter same value")
                except:
                    print("enter a integer")
        if x==3:
            while True:
                try:
                    strokes = int(input("Enter the strokes for " + str(players[x]) + " goal number " + str(i + 1)+": "))
                    confirmstrokes = int(input("Enter the strokes for " + str(players[x]) + " goal number " + str(
                        i + 1) + " for confirmation: "))
                    if confirmstrokes == strokes:
                        player4score.append(strokes)
                        break
                    else:
                        print("enter same value")
                except:
                    print("enter a integer")
        if x==4:
            break




totalscoreplayer1=0
totalscoreplayer2=0
totalscoreplayer3=0
totalscoreplayer4=0

for i in player1score:
    totalscoreplayer1=totalscoreplayer1+i
for i in player2score:
    totalscoreplayer2=totalscoreplayer2+i
for i in player3score:
    totalscoreplayer3=totalscoreplayer3+i
for i in player4score:
    totalscoreplayer4=totalscoreplayer4+i

if len(player1score)!=0:
    print(" ")
    print("score of player1 is",player1score)
    print("total is",totalscoreplayer1)
    player1average=totalscoreplayer1/numberOfGoals
    print("average is",player1average)
    if totalscoreplayer1 < par:
        print(players[0], "scored", par - totalscoreplayer1, "under par \n")
    elif totalscoreplayer1 > par:
        print(players[0], "scored", totalscoreplayer1 - par, "over par \n")
    else:
        print(players[0], "scored same as par \n")
    print(" ")
else:
    pass

if len(player2score)!=0:
    print(" ")
    print("score of player2 is",player2score)
    print("total is",totalscoreplayer2)
    player2average=totalscoreplayer2/numberOfGoals
    print("average is",player2average)
    if totalscoreplayer2 < par:
        print(players[1], "scored", par - totalscoreplayer2, "under par \n")
    elif totalscoreplayer2 > par:
        print(players[1], "scored", totalscoreplayer2 - par, "over par \n")
    else:
        print(players[1], "scored same as par \n")
    print(" ")
else:
    pass

if len(player3score)!=0:
    print(" ")
    print("score of player 3 is",player3score)
    print("total is",totalscoreplayer3)
    player3average=totalscoreplayer3/numberOfGoals
    print("average is",player3average)
    if totalscoreplayer3<par:
        print(players[2],"scored",par-totalscoreplayer3,"under par \n")
    elif totalscoreplayer3>par:
        print(players[2],"scored",totalscoreplayer3-par,"over par \n")
    else:
        print(players[2],"scored same as par \n")
    print(" ")

else:
    pass

if len(player4score)!=0:
    print(" ")
    print("score of player 4 is",player4score)
    print("total is",totalscoreplayer4)
    player4average=totalscoreplayer4/numberOfGoals
    print("average is",player4average)
    if totalscoreplayer4<par:
        print(players[3],"scored",par-totalscoreplayer4,"under par \n")
    elif totalscoreplayer4>par:
        print(players[3],"scored",totalscoreplayer4-par,"over par \n")
    else:
        print(players[3],"scored same as par \n")

else:
    pass


if numberOfPlayers==2:
    playerdict = {
        totalscoreplayer1: players[0],
        totalscoreplayer2: players[1]

    }
if numberOfPlayers==3:
    playerdict = {
        totalscoreplayer1: players[0],
        totalscoreplayer2: players[1],
        totalscoreplayer3: players[2]

    }
if numberOfPlayers==4:
    playerdict = {
        totalscoreplayer1 : players[0],
        totalscoreplayer2 : players[1],
        totalscoreplayer3 : players[2],
        totalscoreplayer4 : players[3]

    }

if numberOfPlayers==2:
    winningscore=min(totalscoreplayer1,totalscoreplayer2)
if numberOfPlayers==3:
    winningscore=min(totalscoreplayer1,totalscoreplayer2,totalscoreplayer3)
if numberOfPlayers==4:
    winningscore=min(totalscoreplayer1,totalscoreplayer2,totalscoreplayer4)

goal_averages=[]

for i in range(0,numberOfGoals):
    if len(player2score) != 0:
        sum=player1score[i]+player2score[i]
        avrg=sum/2
        goal_averages.append(avrg)
    else:
        pass
    if len(player3score) != 0:
        sum=player1score[i]+player2score[i]+player3score[i]
        avrg=sum/3
        goal_averages.append(avrg)
    else:
        pass
    if len(player4score) != 0:
        sum=player1score[i]+player2score[i]+player3score[i]+player4score[i]
        avrg=sum/4
        goal_averages.append(avrg)
    else:
        pass

print("average strocks of goals",goal_averages)

if len(player1score)!=0:
    for index, x in enumerate(player1score):
        if int(x) == 1:
            print(players[0],"scored goal number",index+1,"in one strock")
        else:
            pass
else:
    pass

if len(player2score)!=0:
    for index, x in enumerate(player2score):
        if int(x) == 1:
            print(players[1], "scored goal number", index+1, "in one strock")
        else:
            pass
else:
    pass

if len(player3score)!=3:
    for index, x in enumerate(player3score):
        if int(x) == 1:
            print(players[2],"scored goal number",index+1,"in one strock")
        else:
            pass
else:
    pass

if len(player4score)!=4:
    for index, x in enumerate(player4score):
        if int(x) == 1:
            print(players[3], "scored goal number", index+1, "in one strock")
        else:
            pass
else:
    pass

print("so winning score is",winningscore)
winnername=playerdict.get(winningscore)
print("\nHence winner is",winnername,"!")