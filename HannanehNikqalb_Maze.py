import random 
import os

mazePoshti = [] # Maze poshte kar
mazeJelo = [] # Maze ke namayesh dade mishe

noghateDideShode = [(2, 0)] # noghati ke baraye sakht maze dide mishan 
# va dar back tracking pak mishe
makaneHaal = noghateDideShode[len(noghateDideShode) - 1]

masireDorost = [(3, 0)]
allWays = []

stPosition = (3, 0)
endPoint = ()

def printMaze(maze):
    for i in range(len(maze)):
        for j in range(len(maze)):
            print(maze[i][j] , end=" ")
        print()


def mazeFiller(n):
    mTemp1 = []
    for i in range(n):
        mTemp2 = []
        for j in range(n):
            mTemp2.append(0)
        mTemp1.append(mTemp2)

    return mTemp1


def sakhteMazePosht(maze):
    for i in range(len(maze)):
        for j in range(len(maze)):
            if ((i % 2) != 0 ) or ((j % 2) != 0):
                maze[i][j] = chr(9646) # aski moraba



def sakhteMazeJelo(maze):
    mTemp1 = []
    for i in range(len(maze)):
        mTemp2 = []
        for j in range(len(maze)):
            if maze[i][j] == 0 or maze[i][j] == chr(9646):
                mTemp2.append(chr(9646))
            else:
                mTemp2.append(maze[i][j])
        mTemp1.append(mTemp2)

    return mTemp1


def possibleDirections(currentPos: tuple, maze: list):
    pds = []

    if currentPos[0] >= 2 and maze[currentPos[0] - 2][currentPos[1]] == 0: # top
        pds.append((currentPos[0] - 2, currentPos[1]))

    if currentPos[1] <= len(maze) - 3 and maze[currentPos[0]][currentPos[1] + 2] == 0: # right 
        pds.append((currentPos[0], currentPos[1] + 2))

    if currentPos[0] <= len(maze) - 3 and maze[currentPos[0] + 2][currentPos[1]] == 0: # bottom
        pds.append((currentPos[0] + 2, currentPos[1]))

    if currentPos[1] >= 2 and maze[currentPos[0]][currentPos[1] - 2] == 0: # left
        pds.append((currentPos[0], currentPos[1] - 2))

    return random.choice(pds)


def masirSaz(mazePoshti):
    global makaneHaal
    global noghateDideShode

    makaneQabl = ()
    while len(noghateDideShode) > 0:
    
        makaneQabl = makaneHaal

        try:
            makaneHaal = possibleDirections(makaneHaal, mazePoshti)
            noghateDideShode.append(makaneHaal)
        except:
            noghateDideShode.pop()
            try:
                makaneHaal = noghateDideShode[len(noghateDideShode) - 1]
            except:
                break
        

        if makaneHaal[0] < makaneQabl[0]: # age rafi bala
            mazePoshti[makaneHaal[0]][makaneHaal[1]] = chr(32)
            mazePoshti[makaneQabl[0]][makaneQabl[1]] = chr(32)
            mazePoshti[makaneHaal[0] + 1][makaneHaal[1]] = chr(32)
        
        if makaneHaal[1] > makaneQabl[1]: # age rafti rast
            mazePoshti[makaneHaal[0]][makaneHaal[1]] = chr(32)
            mazePoshti[makaneQabl[0]][makaneQabl[1]] = chr(32)
            mazePoshti[makaneHaal[0]][makaneHaal[1] - 1] = chr(32)
        
        if makaneHaal[0] > makaneQabl[0]: # age rafti pain
            mazePoshti[makaneHaal[0]][makaneHaal[1]] = chr(32)
            mazePoshti[makaneQabl[0]][makaneQabl[1]] = chr(32)
            mazePoshti[makaneHaal[0] - 1][makaneHaal[1]] = chr(32)
                
        if makaneHaal[1] < makaneQabl[1]: # age rafti chap
            mazePoshti[makaneHaal[0]][makaneHaal[1]] = chr(32)
            mazePoshti[makaneQabl[0]][makaneQabl[1]] = chr(32)
            mazePoshti[makaneHaal[0]][makaneHaal[1] + 1] = chr(32)



def outerWalls(maze):
    global endPoint
    mTemp = mazeFiller(len(maze) + 2) #ham az chap ham az rast bayad fasele bede divaro

    for i in range(len(mTemp)):
        for j in range(len(mTemp)):
            if i == 0 or j == 0 or i == len(mTemp) - 1 or j == len(mTemp) - 1:
                mTemp[i][j] = chr(9646) #inja divar sakht
            else:
                mTemp[i][j] = maze[i - 1][j - 1] #anasore maze koochikoo beriz too in bozorge
                # onsore 1 va 1 bozorg mishe 0 va 0 koochik pas menhaye 1 mikonim

    mTemp[3][0] = chr(9670) #makne shoro divare birooni

    noEscapeHole = True
    while noEscapeHole:    #vase gozashtan endpoint be komak random
        lastCollum = random.randint(1, len(mTemp) - 2)
        if mTemp[lastCollum][len(mTemp) - 2] == chr(32): #age yeki moonde be akhari khali bood
            mTemp[lastCollum][len(mTemp) - 1] = chr(32)  #khode akhari ham khali kon
            endPoint = (lastCollum, len(mTemp) - 1)
            noEscapeHole = False

    return mTemp


def gamePlay(maze):

    global stPosition


    getDirection = input("Enter direction(w/d/s/a/ h for Hint)--> ")

    if getDirection == "w":
        if maze[stPosition[0] - 1][stPosition[1]] != chr(9646) and maze[stPosition[0] - 1][stPosition[1]] != chr(9670): #bala ro check mikone age moraba ya lozi nabood
            maze[stPosition[0] - 1][stPosition[1]] = chr(9670) #age shart bala barqarar bood lozish kon
            stPosition = (stPosition[0] - 1, stPosition[1]) #moqeiyat jayi k raftio beriz oo st position
        elif maze[stPosition[0] - 1][stPosition[1]] == chr(9670): # age lozi bood
            maze[stPosition[0]][stPosition[1]] = chr(32) #jayi k hasio khali kon
            stPosition = (stPosition[0] - 1, stPosition[1]) 

    
    if getDirection == "d":
        if maze[stPosition[0]][stPosition[1] + 1] != chr(9646) and maze[stPosition[0]][stPosition[1] + 1] != chr(9670): #Forward
            maze[stPosition[0]][stPosition[1] + 1] = chr(9670)
            stPosition = (stPosition[0], stPosition[1] + 1)
        elif maze[stPosition[0]][stPosition[1] + 1] == chr(9670):# Backward
            maze[stPosition[0]][stPosition[1]] = chr(32)
            stPosition = (stPosition[0], stPosition[1] + 1)


    if getDirection == "s":
        if maze[stPosition[0] + 1][stPosition[1]] != chr(9646) and maze[stPosition[0] + 1][stPosition[1]] != chr(9670):
            maze[stPosition[0] + 1][stPosition[1]] = chr(9670)
            stPosition = (stPosition[0] + 1, stPosition[1])
        elif maze[stPosition[0] + 1][stPosition[1]] == chr(9670):
            maze[stPosition[0]][stPosition[1]] = chr(32)
            stPosition = (stPosition[0] + 1, stPosition[1])


    if getDirection == "a":
        if maze[stPosition[0]][stPosition[1] - 1] != chr(9646) and maze[stPosition[0]][stPosition[1] - 1] != chr(9670):
            maze[stPosition[0]][stPosition[1] - 1] = chr(9670)
            stPosition = (stPosition[0], stPosition[1] - 1)
        elif maze[stPosition[0]][stPosition[1] - 1] == chr(9670):
            maze[stPosition[0]][stPosition[1]] = chr(32)
            stPosition = (stPosition[0], stPosition[1] - 1)

    if getDirection == "h":
        return True

    return maze


def choosePath(currentPos, maze): #vase peyda kardane masir dorost
    global masireDorost
    global allWays
    pds = []
    
    #up
    if currentPos[0] > 0 and maze[currentPos[0] - 1][currentPos[1]] == chr(32) and (currentPos[0] - 1, currentPos[1]) not in allWays:
    # age balash khali bood va balash too masiraye dide shode nbood 
        pds.append((currentPos[0] - 1, currentPos[1])) #balayisho bezar too jahai k mitoonim berim
    #right
    if currentPos[1] < len(maze) - 1 and maze[currentPos[0]][currentPos[1] + 1] == chr(32) and (currentPos[0], currentPos[1] + 1) not in allWays:
        pds.append((currentPos[0], currentPos[1] + 1))
    #down
    if currentPos[0] < len(maze) - 1 and maze[currentPos[0] + 1][currentPos[1]] == chr(32) and (currentPos[0] + 1, currentPos[1]) not in allWays:
        pds.append((currentPos[0] + 1, currentPos[1]))
    #left
    if currentPos[1] > 0 and maze[currentPos[0]][currentPos[1] - 1] == chr(32) and (currentPos[0], currentPos[1] - 1) not in allWays:
        pds.append((currentPos[0], currentPos[1] - 1))

    chosenD = random.choice(pds) #az oonayi k mishe raft yekio random bardar

    return chosenD


def rightPathFinder(endPoint, maze): #az oonayi k mishe raft masir dorosto enekhab mikone
    global masireDorost
    global allWays
    currentPos = (3, 0) #khoone i k azash shoroo mikoni

    while currentPos != endPoint:  #ta khoone akhar naresidi becharkh
        try:
            nextPos = choosePath(currentPos, maze)
            masireDorost.append(nextPos)
            allWays.append(nextPos)
            currentPos = masireDorost[len(masireDorost) - 1]
        except:
            masireDorost.pop() #age peida nakardi masiri yedoone pak kon
            currentPos = masireDorost[len(masireDorost) - 1]


def hint(stPosition, masireDorost, maze):
    #dadane rahnamyi ckek  mikone az range nazane biroon dar masir dorost hast ya na va lozi nbashe
    
    if stPosition[0] > 0 and (stPosition[0] - 1, stPosition[1]) in masireDorost and maze[stPosition[0] - 1][stPosition[1]] != chr(9670): # up
        print("Go Up!") 
    
    elif stPosition[1] < len(maze) - 1 and (stPosition[0], stPosition[1] + 1) in masireDorost and maze[stPosition[0]][stPosition[1] + 1] != chr(9670): # right
        print("Go right!")

    elif stPosition[0] < len(maze) - 1 and (stPosition[0] + 1, stPosition[1]) in masireDorost and maze[stPosition[0] + 1][stPosition[1]] != chr(9670): # down
        print("Go down!")
    
    elif stPosition[1] > 0 and (stPosition[0], stPosition[1] - 1) in masireDorost and maze[stPosition[0]][stPosition[1] - 1] != chr(9670): # left
        print("Go Left!")
    
    else: #age oona nbod bayad roo khodesh bargarde aqab
        if maze[stPosition[0] - 1][stPosition[1]] == chr(9670):
            print("Go Up!")

        if maze[stPosition[0]][stPosition[1] + 1] == chr(9670):
            print("Go Right!")

        if maze[stPosition[0] + 1][stPosition[1]] == chr(9670):
            print("Go Down!")

        if maze[stPosition[0]][stPosition[1] - 1] == chr(9670):
            print("Go Left!")


mazePoshti = mazeFiller(7)
sakhteMazePosht(mazePoshti)

masirSaz(mazePoshti)
mazeJelo = sakhteMazeJelo(mazePoshti)



showingMaze = outerWalls(mazeJelo)

printMaze(showingMaze)

print()
rightPathFinder(endPoint, showingMaze)


gameOn = True
while gameOn:
    hintFlag = gamePlay(showingMaze)
    os.system('cls')
    printMaze(showingMaze)
    if hintFlag == True:
        hint(stPosition, masireDorost, showingMaze)


    if stPosition == endPoint:
        print("You Won!!")
        gameOn = False

    