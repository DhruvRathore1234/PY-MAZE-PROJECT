from pyMaze import maze, agent, COLOR, textLabel

def DFS(m):
    dfs_path = {}
    start = (m.rows, m.cols)
    target = (1, 1)
    frontier = [start]
    explored = [start]
    while len(frontier) > 0:
        curr_cell = frontier.pop()
        if curr_cell == target:
            break
        for d in 'ESNW':
            if m.maze_map[curr_cell][d] == True:
                if d == 'E':
                    child_cell = (curr_cell[0], curr_cell[1]+1)
                elif d == 'S':
                    child_cell = (curr_cell[0]+1, curr_cell[1])
                elif d == 'N':
                    child_cell = (curr_cell[0]-1, curr_cell[1])
                elif d == 'W':
                    child_cell = (curr_cell[0], curr_cell[1]-1)
                
                if child_cell in explored:
                    continue
                else:
                    frontier.append(child_cell)
                    explored.append(child_cell)
                    dfs_path[child_cell] = curr_cell
    
    final_path = {}
    while start != target:
        final_path[dfs_path[target]] = target
        target = dfs_path[target]
    return final_path

if __name__ == '__main__':
    m = maze(20, 25)
    m.CreateMaze(loopPercent=50)
    path = DFS(m)
    a = agent(m, footprints=True, color='red', shape='arrow')
    m.tracePath({a:path})
    l = textLabel(m, 'length of shortest path', len(path)+1)
    m.run()

if __name__=='__main__':
    
    m=maze(10,10) # Change to any size
    m.CreateMaze(2,4) # (2,4) is Goal Cell, Change that to any other valid cell

    dSeacrh,dfsPath,fwdPath=DFS(m,(5,1)) # (5,1) is Start Cell, Change that to any other valid cell

    a=agent(m,5,1,goal=(2,4),footprints=True,shape='square',color=COLOR.green)
    b=agent(m,2,4,goal=(5,1),footprints=True,filled=True)
    c=agent(m,5,1,footprints=True,color=COLOR.yellow)
    m.tracePath({a:dSeacrh},showMarked=True)
    m.tracePath({b:dfsPath})
    m.tracePath({c:fwdPath})
    m.run()

    ## The code below will generate the maze shown in video

    # m=maze()
    # m.CreateMaze(loadMaze='dfs.csv')

    # dSeacrh,dfsPath,fwdPath=DFS(m)

    # a=agent(m,footprints=True,shape='square',color=COLOR.green)
    # b=agent(m,1,1,goal=(5,5),footprints=True,filled=True,color=COLOR.cyan)
    # c=agent(m,footprints=True,color=COLOR.yellow)
    # m.tracePath({a:dSeacrh},showMarked=True)
    # m.tracePath({b:dfsPath})
    # m.tracePath({c:fwdPath})
    # m.run()
















