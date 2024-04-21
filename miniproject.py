import random
import matplotlib.pyplot as plt

def generate_maze(width, height):
    # Create an empty grid with walls between all cells
    maze = [['#'] * (width*2+1) for _ in range(height*2+1)]

    # Define the starting and ending points
    start = (1, 1)
    end = (height*2-1, width*2-1)

    # Create a graph with vertices and edges
    vertices = [(x, y) for y in range(1, height*2, 2) for x in range(1, width*2, 2)]
    edges = []

    # Add edges to the graph
    for y in range(1, height*2, 2):
        for x in range(1, width*2, 2):
            vertices_above = [(x-2, y), (x+2, y)] if x > 1 else [(x+2, y)]
            vertices_below = [(x-2, y), (x+2, y)] if x < width*2-1 else [(x-2, y)]
            vertices_left = [(x, y-2), (x, y+2)] if y > 1 else [(x, y+2)]
            vertices_right = [(x, y-2), (x, y+2)] if y < height*2-1 else [(x, y-2)]

            for v in vertices_above + vertices_below + vertices_left + vertices_right:
                if v in vertices:
                    edges.append(((x, y), v))

    # Shuffle the edges and apply Kruskal's algorithm
    random.shuffle(edges)
    mst = []
    pset = {v: v for v in vertices}

    def find(v):
        if pset[v] != v:
            pset[v] = find(pset[v])
        return pset[v]

    def union(v1, v2):
        pset[find(v1)] = find(v2)

    for e in edges:
        v1, v2 = e
        if find(v1) != find(v2):
            mst.append(e)
            union(v1, v2)

    # Remove the walls corresponding to the MST edges
    for e in mst:
        x1, y1 = e[0]
        x2, y2 = e[1]
        if x1 == x2:
            if y1 < y2:
                maze[y1][x1] = ' '
            else:
                maze[y2][x2] = ' '
        else:
            if y1 < y2:
                maze[y1][x1] = ' '
            else:
                maze[y2][x2] = ' '

    # Print the maze
    plt.imshow([[0 if cell == '#' else 1 for cell in row] for row in maze], cmap='gray')
    plt.xticks([])
    plt.yticks([])
    plt.xlim(0, width*2)
    plt.ylim(0, height*2)
    plt.show()

# Generate a maze with 10x10 size


generate_maze(random.randint(1,5), random.randint(2,3))