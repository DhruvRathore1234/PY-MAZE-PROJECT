from pyMaze import maze, agent, COLOR, textLabel

from collections import deque

def BFS(m):
    bfs_path = {}
    start = (m.rows, m.cols)
    target = (1, 1)
    frontier = deque([start])
    explored = [start]
    while len(frontier) > 0:
        curr_cell = frontier.popleft()
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
                    bfs_path[child_cell] = curr_cell
    
    final_path = {}
    while start != target:
        final_path[bfs_path[target]] = target
        target = bfs_path[target]
    return final_path

if __name__ == '__main__':
    
    m = maze(20, 25)
    m.CreateMaze(loopPercent=50)
    path = BFS(m)
    a = agent(m, footprints=True, color='red', shape='arrow')
    m.tracePath({a:path})
    l = textLabel(m, 'length of shortest path', len(path)+1)
    m.run()

    # m=maze(5,5)
    # m.CreateMaze(loadMaze='bfs.csv')
    # bSearch,bfsPath,fwdPath=BFS(m)
    # a=agent(m,footprints=True,color=COLOR.green,shape='square')
    # b=agent(m,footprints=True,color=COLOR.yellow,shape='square',filled=False)
    # c=agent(m,1,1,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(m.rows,m.cols))
    # m.tracePath({a:bSearch},delay=500)
    # m.tracePath({c:bfsPath})
    # m.tracePath({b:fwdPath})

    # m.run()


    m=maze(12,10)
    # m.CreateMaze(5,4,loopPercent=100)
    m.CreateMaze(loopPercent=10,theme='light')
    bSearch,bfsPath,fwdPath=BFS(m)
    a=agent(m,footprints=True,color=COLOR.yellow,shape='square',filled=True)
    b=agent(m,footprints=True,color=COLOR.red,shape='square',filled=False)
    # c=agent(m,5,4,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(m.rows,m.cols))
    c=agent(m,1,1,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(m.rows,m.cols))
    m.tracePath({a:bSearch},delay=100)
    m.tracePath({c:bfsPath},delay=100)
    m.tracePath({b:fwdPath},delay=100)

    m.run()
