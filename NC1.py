class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #4 possible movements
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # get grid dimensions
        ROWS, COLS = len(grid), len(grid[0])
        #counter for number of islands
        islands = 0

        #helper function
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or    #stop DFS if out of bounds or if the cell is water- 0
                c >= COLS or grid[r][c] == "0"
            ):
                return
                
            #mark the current land as visited
            grid[r][c] = "0"

            #recursively visit all connected land cells
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        #traverse the grid, loop through every row and column
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1": # found an unvisited island
                    dfs(r, c) # perform dfs to mark all connected land as visited
                    islands += 1 # increment the island count

        return islands