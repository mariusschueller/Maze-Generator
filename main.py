import random


class MazeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[1 for _ in range(width)] for _ in range(height)]

    def generate_maze(self, start_x, start_y):
        if not (0 <= start_x < self.width and 0 <= start_y < self.height):
            raise ValueError("Start position is out of bounds.")

        if self.grid[start_y][start_x] != 1:
            raise ValueError("Start position must be on a wall.")

        self._dfs(start_x, start_y)
        self.grid[start_y][start_x] = 0  # Ensure the start position is open
        self._place_end()
        return self.grid

    def _dfs(self, x, y):
        self.grid[y][x] = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2

            if 0 <= nx < self.width and 0 <= ny < self.height and self.grid[ny][nx] == 1:
                self.grid[ny - dy][nx - dx] = 0  # Knock down the wall
                self._dfs(nx, ny)

    def _place_end(self):
        open_positions = [(x, y) for y in range(self.height) for x in range(self.width) if self.grid[y][x] == 0]
        end_x, end_y = random.choice(open_positions)
        self.grid[end_y][end_x] = -1


def print_maze(maze):
    for row in maze:
        print(" ".join(str(cell) for cell in row))


if __name__ == "__main__":
    width, height = 15, 15  # Define maze size
    start_x, start_y = 0, 0  # Define starting location
    maze_gen = MazeGenerator(width, height)
    maze = maze_gen.generate_maze(start_x, start_y)
    print_maze(maze)
