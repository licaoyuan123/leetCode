from collections import deque
def shortestCellPath(grid, sr, sc, tr, tc):
  visited = set([])
  queue= deque([])
  queue.append((sr, sc, 0))
  count =0
  while queue:
    curr, curc, distance = queue.popleft()
    if curr==tr and curc==tc:
      return distance
    
    visited.add((curr, curc))
    #visited[curr][curc] = True
    if curr-1>=0:
      if grid[curr-1][curc] and not (curr-1, curc) in visited:
        queue.append((curr-1, curc, distance+1))
    if curr+1<len(grid):
      if grid[curr+1][curc] and not (curr+1, curc) in visited:
        queue.append((curr+1, curc, distance+1))
    if curc-1>=0:
      if grid[curr][curc-1] and not (curr, curc-1) in visited:
        queue.append((curr, curc-1, distance+1))
    if curc+1<len(grid[0]):
      if grid[curr][curc+1] and not (curr, curc+1) in visited:
        queue.append((curr, curc+1, distance+1))
  return -1
