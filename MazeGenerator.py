import random


class MazeGenerator:
    def __init__(
        self, width: int, height: int,
            seed: int | None, perfect: bool, config: dict) -> None:
        self.width = width
        self.height = height
        self.perfect = perfect
        from a_maze_ing import Cell
        self.grid = [[Cell() for _ in range(width)]
                     for _ in range(height)]
        self.visited = [[False for _ in range(width)]
                        for _ in range(height)]
        self.blocked = [[False for _ in range(width)]
                        for _ in range(height)]
        self.seed = seed
        self.config = config

    def check_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def open_between(self, x1: int, y1: int, x2: int, y2: int) -> None:
        if self.check_bounds(x1, y1) and self.check_bounds(x2, y2):
            if (x1 == x2 - 1) and (y1 == y2):
                self.grid[y1][x1].open_wall("east")
                self.grid[y2][x2].open_wall("west")
            elif (x1 == x2 + 1) and (y1 == y2):
                self.grid[y1][x1].open_wall("west")
                self.grid[y2][x2].open_wall("east")
            elif (x1 == x2) and (y1 == y2 + 1):
                self.grid[y1][x1].open_wall("north")
                self.grid[y2][x2].open_wall("south")
            elif (x1 == x2) and (y1 == y2 - 1):
                self.grid[y1][x1].open_wall("south")
                self.grid[y2][x2].open_wall("north")
            else:
                raise ValueError("The cells are not neighbors !!")
        else:
            raise ValueError("The coordinates are out of the maze's bounds !!")

    def close_between(self, x1: int, y1: int, x2: int, y2: int) -> None:
        if self.check_bounds(x1, y1) and self.check_bounds(x2, y2):
            if (x1 == x2 - 1) and (y1 == y2):
                self.grid[y1][x1].close_wall("east")
                self.grid[y2][x2].close_wall("west")
            elif (x1 == x2 + 1) and (y1 == y2):
                self.grid[y1][x1].close_wall("west")
                self.grid[y2][x2].close_wall("east")
            elif (x1 == x2) and (y1 == y2 + 1):
                self.grid[y1][x1].close_wall("north")
                self.grid[y2][x2].close_wall("south")
            elif (x1 == x2) and (y1 == y2 - 1):
                self.grid[y1][x1].close_wall("south")
                self.grid[y2][x2].close_wall("north")
            else:
                raise ValueError("The cells are not neighbors !!")
        else:
            raise ValueError("The coordinates are out of the maze !!")

    def check_connection(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        if self.check_bounds(x1, y1) and self.check_bounds(x2, y2):
            if (x1 == x2 - 1) and (y1 == y2):
                if not (self.grid[y1][x1].has_wall("east")):
                    if not (self.grid[y2][x2].has_wall("west")):
                        return True
                return False
            elif (x1 == x2 + 1) and (y1 == y2):
                if not self.grid[y1][x1].has_wall("west"):
                    if not self.grid[y2][x2].has_wall("east"):
                        return True
                return False
            elif (x1 == x2) and (y1 == y2 + 1):
                if not self.grid[y1][x1].has_wall("north"):
                    if not self.grid[y2][x2].has_wall("south"):
                        return True
                return False
            elif (x1 == x2) and (y1 == y2 - 1):
                if not self.grid[y1][x1].has_wall("south"):
                    if not self.grid[y2][x2].has_wall("north"):
                        return True
                return False
            else:
                raise ValueError("The cells are not neighbors !!")
        else:
            raise ValueError("The coordinates are out of the maze !!")

    def get_unvisited_neighbors(self, x: int, y: int) -> list[tuple[int, int]]:
        neighbors = []

        if self.check_bounds(x - 1, y) and not self.visited[y][x - 1]:
            if not self.blocked[y][x - 1]:
                neighbors.append((x - 1, y))
        if self.check_bounds(x + 1, y) and not self.visited[y][x + 1]:
            if not self.blocked[y][x + 1]:
                neighbors.append((x + 1, y))
        if self.check_bounds(x, y + 1) and not self.visited[y + 1][x]:
            if not self.blocked[y + 1][x]:
                neighbors.append((x, y + 1))
        if self.check_bounds(x, y - 1) and not self.visited[y - 1][x]:
            if not self.blocked[y - 1][x]:
                neighbors.append((x, y - 1))
        return neighbors

    def forty_two_cells(self) -> None:
        centre_x = (self.width - 1) // 2
        centre_y = (self.height - 1) // 2
        pattern_coordinates = [
            (centre_x + 1, centre_y), (centre_x + 2, centre_y),
            (centre_x + 3, centre_y),

            (centre_x + 3, centre_y - 1),
            (centre_x + 3, centre_y - 2),
            (centre_x + 2, centre_y - 2),
            (centre_x + 1, centre_y - 2),

            (centre_x + 1, centre_y + 1),
            (centre_x + 1, centre_y + 2),

            (centre_x + 2, centre_y + 2),
            (centre_x + 3, centre_y + 2),

            (centre_x - 1, centre_y),
            (centre_x - 2, centre_y),
            (centre_x - 3, centre_y),

            (centre_x - 3, centre_y - 1),
            (centre_x - 3, centre_y - 2),

            (centre_x - 1, centre_y + 1),
            (centre_x - 1, centre_y + 2)
        ]
        if self.height >= 9 and self.width >= 9:
            for x, y in pattern_coordinates:
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.blocked[y][x] = True
        else:
            print(
                "The maze size doesn't support '42' pattern !! minimum (9, 9)")

    def is_open_3x3_block(self, start_x: int, start_y: int) -> bool:
        if start_x < 0 or start_y < 0:
            return False
        if start_x + 2 >= self.width or start_y + 2 >= self.height:
            return False
        for y in range(start_y, start_y + 3):
            for x in range(start_x, start_x + 2):
                if not self.check_connection(x, y, x + 1, y):
                    return False
        for y in range(start_y, start_y + 2):
            for x in range(start_x, start_x + 3):
                if not self.check_connection(x, y, x, y + 1):
                    return False

        return True

    def has_open_3x3_area(self) -> bool:
        for start_y in range(self.height - 2):
            for start_x in range(self.width - 2):
                if self.is_open_3x3_block(start_x, start_y):
                    return True
        return False

    def get_extra_wall_candidates(
        self
         ) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        candidates = []
        for y in range(self.height):
            for x in range(self.width):
                if self.blocked[y][x]:
                    continue
                if self.check_bounds(x + 1, y):
                    if not self.blocked[y][x + 1]:
                        if not self.check_connection(x, y, x + 1, y):
                            candidates.append(((x, y), (x + 1, y)))
                if self.check_bounds(x, y + 1):
                    if not self.blocked[y + 1][x]:
                        if not self.check_connection(x, y, x, y + 1):
                            candidates.append(((x, y), (x, y + 1)))

        return candidates

    def make_non_perfect(self, extra_openings: int = 5) -> None:
        candidates = self.get_extra_wall_candidates()
        random.shuffle(candidates)
        opened = 0
        for (x1, y1), (x2, y2) in candidates:
            self.open_between(x1, y1, x2, y2)
            if self.has_open_3x3_area():
                self.close_between(x1, y1, x2, y2)
            else:
                opened += 1
            if opened == extra_openings:
                break

    def generate(self) -> None:
        if self.seed is not None:
            random.seed(self.seed)
        stack = []
        x, y = 0, 0
        self.visited[y][x] = True

        while True:
            neighbors = self.get_unvisited_neighbors(x, y)
            if neighbors:
                stack.append((x, y))
                nx, ny = random.choice(neighbors)
                self.open_between(x, y, nx, ny)
                x, y = nx, ny
                self.visited[y][x] = True
            elif stack:
                x, y = stack.pop()
            else:
                break
        if not self.perfect:
            self.make_non_perfect((self.width * self.height) // 12)

    def set_entry_exit(self) -> None:
        self.entry = self.config['ENTRY']
        self.exit = self.config['EXIT']
        if self.blocked[self.entry[1]][self.entry[0]]:
            raise ValueError("The cell is reserved for 42")
        if self.blocked[self.exit[1]][self.exit[0]]:
            raise ValueError("The cell is reserved for 42")

    def get_connected_neighbors(self, x: int, y: int) -> list[tuple]:
        connected = []
        try:
            if self.check_connection(x, y, x - 1, y):
                connected.append((x - 1, y))
        except Exception:
            pass
        try:
            if self.check_connection(x, y, x + 1, y):
                connected.append((x + 1, y))
        except Exception:
            pass
        try:
            if self.check_connection(x, y, x, y - 1):
                connected.append((x, y - 1))
        except Exception:
            pass
        try:
            if self.check_connection(x, y, x, y + 1):
                connected.append((x, y + 1))
        except Exception:
            pass
        return connected

    def find_shortest_path(self) -> list[tuple[int, int]]:
        start = self.entry
        end = self.exit

        queue = [start]
        visited = {start}
        parent = {}
        found = False
        while queue:
            current = queue.pop(0)
            if current == end:
                found = True
                break
            x, y = current
            neighbors = self.get_connected_neighbors(x, y)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)
        if not found:
            return []
        path = []
        current = end
        while current != start:
            path.append(current)
            current = parent[current]
        path.append(start)
        path.reverse()
        return path

    def path_to_directions(self, path: list[tuple[int, int]]) -> str:
        if not path or len(path) == 1:
            return ""
        directions = []
        for i in range(len(path) - 1):
            x1, y1 = path[i]
            x2, y2 = path[i + 1]
            if x2 == x1 + 1 and y2 == y1:
                directions.append("E")
            elif x2 == x1 - 1 and y2 == y1:
                directions.append("W")
            elif x2 == x1 and y2 == y1 + 1:
                directions.append("S")
            elif x2 == x1 and y2 == y1 - 1:
                directions.append("N")
            else:
                raise ValueError(
                    f"Invalid path step: {(x1, y1)} -> {(x2, y2)}")
        return "".join(directions)

    def write_output(self, path: list[tuple]) -> None:
        grid_hex = [[format(cell.walls, 'X') for cell in row]
                    for row in self.grid]
        path_directions = self.path_to_directions(path)
        with open(self.config['OUTPUT_FILE'], 'w+') as f:
            for row in grid_hex:
                for char in row:
                    f.write(char)
                f.write("\n")
            f.write(f"\n{self.entry}\n{self.exit}")
            f.write(f"\n{path_directions}\n")

    def get_data(self, path: list[tuple]) -> dict:
        data = {}
        data['width'] = self.width
        data['height'] = self.height
        data['grid'] = [[cell.walls for cell in row]
                        for row in self.grid]
        data['path'] = self.path_to_directions(path)
        return data

    def display(self, path: list[tuple[int, int]] | None = None) -> None:
        path_set = set(path) if path else set()

        top = "+"
        for x in range(self.width):
            if self.grid[0][x].has_wall("north"):
                top += "---+"
            else:
                top += "   +"
        print(top)

        for y in range(self.height):
            middle = ""
            bottom = "+"

            for x in range(self.width):
                cell = self.grid[y][x]

                if x == 0:
                    if cell.has_wall("west"):
                        middle += "|"
                    else:
                        middle += " "

                if self.blocked[y][x]:
                    middle += " # "
                elif (x, y) in path_set:
                    middle += " * "
                elif self.visited[y][x]:
                    middle += " . "
                else:
                    middle += "   "

                if cell.has_wall("east"):
                    middle += "|"
                else:
                    middle += " "

                if cell.has_wall("south"):
                    bottom += "---+"
                else:
                    bottom += "   +"

            print(middle)
            print(bottom)
