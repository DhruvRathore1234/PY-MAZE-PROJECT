from pyMaze import maze,COLOR, agent


m = maze(25, 25) # default 10 X 10
# m = maze(20, 25) # use to define the size of maze

m.CreateMaze()
# m.CreateMaze(5,4) # change destination to given coordinate
# m.CreateMaze(pattern="v") # increase more vertical path 
# m.CreateMaze(pattern="h") # increase more horizontal paths 
# m.CreateMaze(loopPercent=100) # increase number of paths
# m.CreateMaze(saveMaze=True) #use to save a file of the generated maze 
# m.CreateMaze(loadMaze='maze--2024-06-02--23-03-46.csv') # use to generate the saved maze file again 
# m.CreateMaze(theme="cyan") # use to define the background color and wall lines for maxe

# m.CreateMaze(5,5,pattern='v',theme=COLOR.cyan, loopPercent=100)


# a = agent(m) # use to provide starting point
# a = agent(m, 6, 5)
# print(a.x)
# print(a.y)
# print(a.position)

a=agent(m,footprints=True,filled=True, shape="arrow", color='yellow')
b=agent(m,5,5,footprints=True,color='red')
c=agent(m,4,1,footprints=True,color='green',shape='arrow')

# m.enableArrowKey(a)
# m.enableWASD(b)

path2=[(5,4),(5,3),(4,3),(3,3),(3,4),(4,4)]
path3='WWNNES'

# l1=textLabel(m,'Total Cells',m.rows*m.cols)
# l1=textLabel(m,'Total Cells',m.rows*m.cols)
# l1=textLabel(m,'Total Cells',m.rows*m.cols)
# l1=textLabel(m,'Total Cells',m.rows*m.cols)

m.tracePath({a:m.path,b:path2,c:path3},delay=200,kill=True)

m.run()


