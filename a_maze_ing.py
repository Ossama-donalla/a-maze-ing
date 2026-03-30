from MazeGenerator import MazeGenerator
from parsing import parse_config
from display_maze import draw_maze, draw_maze_game
import random
import curses
import time

wall_values = {"north": 1, "east": 2, "south": 4, "west": 8}


class Cell:
    def __init__(self) -> None:
        self.walls = 15

    def has_wall(self, direction: str) -> int:
        return (self.walls & wall_values[direction])

    def open_wall(self, direction: str) -> None:
        if self.has_wall(direction):
            self.walls -= wall_values[direction]
        else:
            raise ValueError(
                f"The cell doesnt have this wall: {direction}")

    def close_wall(self, direction: str) -> None:
        if not self.has_wall(direction):
            self.walls += wall_values[direction]
        else:
            raise ValueError(
                f"The cell already has the wall closed : {direction}")


if __name__ == "__main__":
    try:
        config = parse_config()
    except Exception as e:
        print(e)
        exit()
    entry = config['ENTRY']
    exit = config['EXIT']
    if config:

        path = None

        def generate_maze():
            maze = MazeGenerator(config['WIDTH'], config['HEIGHT'], config['SEED'],
                                 config['PERFECT'], config)
            maze.forty_two_cells()
            maze.generate()
            maze.set_entry_exit()
            global path
            path = maze.find_shortest_path()
            maze.write_output(path)
            # maze.display(path)
            return {"output": maze.get_data(path), "blocked": maze.blocked}
        try:
            output = generate_maze()
            found_player = 0
            stdscr = curses.initscr()
            stdscr.keypad(True)
            stdscr.nodelay(True)
            curses.curs_set(0)
            curses.start_color()
            curses.use_default_colors()
            curses.init_pair(1, curses.COLOR_RED, -1)
            curses.init_pair(2, curses.COLOR_GREEN, -1)
            curses.init_pair(3, curses.COLOR_BLUE, -1)
            curses.init_pair(4, curses.COLOR_YELLOW, -1)
            curses.init_pair(5, curses.COLOR_MAGENTA, -1)
            curses.init_pair(6, curses.COLOR_CYAN, -1)
            curses.init_pair(7, curses.COLOR_WHITE, -1)
            menu = ["START MAZE", "START GAME", "EXIT"]
            current = 0
            while True:
                stdscr.clear()
                max_y, max_x = stdscr.getmaxyx()
                while max_y < (config["HEIGHT"] * 2) + 6 or max_x < (config['WIDTH'] * 4):
                    stdscr.clear()
                    stdscr.addstr("too small")
                    stdscr.refresh()
                    max_y, max_x = stdscr.getmaxyx()
                    if max_y > (config["HEIGHT"] * 2) + 6 and max_x > (config["WIDTH"] * 4):
                        break

                for i, item in enumerate(menu):
                    if i == current:
                        stdscr.addstr((max_y // 2) + i, (max_x // 2) - len(item) // 2, item, curses.color_pair(4))
                    else:
                        stdscr.addstr((max_y // 2) + i, (max_x // 2) - len(item) // 2, item)

                key = stdscr.getch()

                if key == curses.KEY_UP and current > 0:
                    current -= 1
                if key == curses.KEY_DOWN and len(menu) - 1 > current:
                    current += 1

                if key in [curses.KEY_ENTER, 10, 13]:
                    if menu[current] == "START MAZE":
                        rotate_color = 6
                        show_path = False
                        while True:

                            max_y, max_x = stdscr.getmaxyx()
                            while max_y < (config["HEIGHT"] * 2) + 9:
                                stdscr.clear()
                                stdscr.addstr("too small", curses.color_pair(1))
                                stdscr.refresh()
                                max_y, max_x = stdscr.getmaxyx()
                                if max_y > (config["HEIGHT"] * 2) + 9:
                                    break
                            while max_x < (config["WIDTH"] * 4) + 6:
                                stdscr.clear()
                                stdscr.addstr("too small", curses.color_pair(1))
                                stdscr.refresh()
                                max_y, max_x = stdscr.getmaxyx()
                                if max_x > (config["WIDTH"] * 4) + 6:
                                    break

                            if not show_path:
                                stdscr.clear()

                            draw_maze(stdscr, path, output["output"], entry, exit, show_path, rotate_color, output["blocked"])
                            key = stdscr.getch()

                            if key == ord('s'):
                                show_path = True
                            if key == ord('h'):
                                show_path = False
                                stdscr.clear()

                            if key == ord('r'):
                                config['SEED'] = random.randint(0, 1000)
                                output = generate_maze()
                                stdscr.clear()
                            if key == ord('c'):
                                rotate_color = random.randint(2, 7)
                            if key == ord('b'):
                                break
                            stdscr.refresh()
                            time.sleep(0.05)
                    elif menu[current] == "START GAME":
                                draw_maze_game(stdscr, output["output"], entry, exit, 6, output["blocked"])
                                stdscr.refresh()
                                time.sleep(0.05)
                    elif menu[current] == "EXIT":
                        break
                time.sleep(0.06)

            curses.endwin()
        except BaseException:
            curses.endwin()
            print("EXIT")
