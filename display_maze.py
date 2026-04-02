try:
    import curses
    from curses import window
    import time
    import random
    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
    import pygame
except ModuleNotFoundError as e:
    print("Error detected at top level:", e.name)
except Exception as e:
    print("Error detected at top level:", e)


check_wall = {"north": 1, "east": 2, "south": 4, "west": 8}

pygame.mixer.init()
pygame.mixer.music.load(
    "YTDown.com_YouTube_Lost-Woods-The-Legend-of-Zelda-"
    "Ocarina-o_Media_V9so9y-8Dgk_009_128k.mp3")
sound = pygame.mixer.Sound("videoplayback (mp3cut.net)t3am.mp3")
sound2 = pygame.mixer.Sound("videoplayback (mp3cut.net) 4M.mp3")
pygame.mixer.music.play(-1)


def draw_maze(
        stdscr: window, path: list, config: dict, entry: tuple,
        exit: tuple, show_path: bool,
        rotate_color: int,
        blocked_42: list,
        one_time: bool
        ) -> None:
    """
    Draw the maze in the terminal.

    Args:
        stdscr: Curses window.
        path: Solution path.
        config: Maze configuration.
        entry: Entry coordinates.
        exit: Exit coordinates.
        show_path: Whether to display solution.
        rotate_color: Color scheme.
        blocked_42: Blocked cells map.
    """
    maze = config['grid']

    width = config['width']
    height = config['height']
    cell_height = 2
    cell_width = 4

    exist_42 = 1
    if width > 9 and height > 9:
        exist_42 = 0

    for y in range(height):
        for x in range(width):
            if one_time:
                stdscr.refresh()
                time.sleep(0.02)
            # border up
            if check_wall["north"] & maze[y][x]:
                stdscr.addstr(y * cell_height, x * cell_width, "+---",
                              curses.color_pair(rotate_color))
            else:
                stdscr.addstr(y * cell_height, x * cell_width, "+   ",
                              curses.color_pair(rotate_color))

        #     ## border left
            if check_wall["west"] & maze[y][x]:
                stdscr.addstr(y * cell_height + 1, x * cell_width, "|",
                              curses.color_pair(rotate_color))
            else:
                stdscr.addstr(y * cell_height + 1, x * cell_width, " ",
                              curses.color_pair(rotate_color))

            if (x, y) == entry:
                stdscr.addstr(y * cell_height + 1, x * cell_width + 2, "🔵",
                              curses.color_pair(1))
            if (x, y) == exit:
                stdscr.addstr(y * cell_height + 1, x * cell_width + 2, "🏁",
                              curses.color_pair(2))

            if blocked_42[y][x] is True:
                stdscr.addstr(y * cell_height + 1, x * cell_width + 2, "⬜",
                              curses.color_pair(4))

        stdscr.addstr(y * cell_height, width * cell_width, "+",
                      curses.color_pair(rotate_color))
        # ## border right
        if check_wall["east"] & maze[y][x]:
            stdscr.addstr(y * cell_height + 1, width * cell_width, "|",
                          curses.color_pair(rotate_color))

    for x in range(width):
        # border down
        if check_wall["south"] & maze[y][x]:
            stdscr.addstr(height * cell_height, x * cell_width, "+---",
                          curses.color_pair(rotate_color))

    stdscr.addstr(height * cell_height, width * cell_width, "+",
                  curses.color_pair(rotate_color))

    if show_path:
        for x, y in path[1:len(path) - 1]:
            stdscr.addstr(y * cell_height + 1, x * cell_width + 2, "⭐",
                          curses.color_pair(1))
            time.sleep(0.04)
            stdscr.refresh()

    stdscr.addstr((height) * cell_height + 1, 0, "=== A-Maze-ing ===")
    stdscr.addstr((height) * cell_height + 2, 0, "[r]. Re-generate a new maze")
    stdscr.addstr((height) * cell_height + 3, 0,
                  "[s/h]. Show/Hide path from entry to exit")
    stdscr.addstr((height) * cell_height + 4, 0, "[c]. Rotate maze colors")
    stdscr.addstr((height) * cell_height + 5, 0, "[b]. Back")
    if exist_42:
        stdscr.addstr((height) * cell_height + 8, 0,
                      "The maze size doesn't support '42' pattern "
                      "!! minimum (9, 9)", curses.color_pair(1))


def draw_maze_game(
        stdscr: window,
        config: dict,
        entry: tuple,
        exit: tuple,
        rotate_color: int,
        blocked_42: list
        ) -> None:
    """
    Run interactive maze game.

    Player moves inside the maze, collects items,
    and tries to reach the exit.

    Args:
        stdscr: Curses window.
        config: Maze configuration.
        entry: Start position.
        exit: Goal position.
        rotate_color: Color scheme.
        blocked_42: Blocked cells map.
    """
    maze = config['grid']

    width = config['width']
    height = config['height']
    cell_height = 2
    cell_width = 4
    found_entry = 0
    player_y = 0
    player_x = 0
    exit_y = -1
    exit_x = -1
    food_y = random.randint(2, height - 1)
    food_x = random.randint(0, width - 1)
    while True:
        if blocked_42[food_y][food_x] is False:
            break
        else:
            food_y = random.randint(0, len(maze) - 1)
            food_x = random.randint(0, len(maze[0]) - 1)
    stop_food = True
    score = 0
    while True:
        max_y, max_x = stdscr.getmaxyx()
        while max_y < (height * 2) + 6:
            stdscr.clear()
            stdscr.addstr("too small", curses.color_pair(1))
            stdscr.refresh()
            max_y, max_x = stdscr.getmaxyx()
            if max_y > (height * 2) + 6:
                break
        while max_x < (width * 4) + 5:
            stdscr.clear()
            stdscr.addstr("too small", curses.color_pair(1))
            stdscr.refresh()
            max_y, max_x = stdscr.getmaxyx()
            if max_x > (width * 4) + 5:
                break
        stdscr.clear()

        for y in range(height):
            for x in range(width):

                # border up
                if check_wall["north"] & maze[y][x]:
                    stdscr.addstr(y * cell_height, x * cell_width, "+---",
                                  curses.color_pair(rotate_color))
                else:
                    stdscr.addstr(y * cell_height, x * cell_width, "+   ",
                                  curses.color_pair(rotate_color))
            #     ## border left
                if check_wall["west"] & maze[y][x]:
                    stdscr.addstr(y * cell_height + 1, x * cell_width, "|",
                                  curses.color_pair(rotate_color))
                else:
                    stdscr.addstr(y * cell_height + 1, x * cell_width, " ",
                                  curses.color_pair(rotate_color))

                if not found_entry:
                    if (x, y) == entry:
                        stdscr.addstr(y * cell_height + 1, x * cell_width + 2,
                                      "🧙", curses.color_pair(1))
                        player_y = y
                        player_x = x
                        found_entry = 1
                if score >= 3:
                    if (x, y) == exit:
                        stdscr.addstr(y * cell_height + 1, x * cell_width + 2,
                                      "🏆", curses.color_pair(2))
                        exit_y = y
                        exit_x = x
                        stop_food = False

                if stop_food:
                    stdscr.addstr(
                        food_y * cell_height + 1, food_x * cell_width + 2,
                        "💎")

                if blocked_42[y][x] is True:
                    stdscr.addstr(y * cell_height + 1, x * cell_width + 2, "⬜",
                                  curses.color_pair(4))

            stdscr.addstr(y * cell_height, width * cell_width, "+",
                          curses.color_pair(rotate_color))
            # ## border right
            if check_wall["east"] & maze[y][x]:
                stdscr.addstr(y * cell_height + 1, width * cell_width, "|",
                              curses.color_pair(rotate_color))

        for x in range(width):
            # border down
            if check_wall["south"] & maze[y][x]:
                stdscr.addstr(height * cell_height, x * cell_width, "+---",
                              curses.color_pair(rotate_color))
        stdscr.addstr(height * cell_height, width * cell_width, "+",
                      curses.color_pair(rotate_color))

        if food_y == player_y and food_x == player_x and stop_food:
            food_y = random.randint(0, height - 1)
            food_x = random.randint(0, width - 1)
            sound.play()
            while True:
                if blocked_42[food_y][food_x] is False:
                    break
                else:
                    food_y = random.randint(0, len(maze) - 1)
                    food_x = random.randint(0, len(maze[0]) - 1)
            score += 1

        if player_y == exit_y and player_x == exit_x:
            sound2.play()
            stdscr.clear()
            stdscr.addstr(max_y // 2, max_x // 2, "YOU WIN")
            stdscr.refresh()
            time.sleep(1)
            stdscr.addstr(max_y // 2, max_x // 2, "YOU WIN.")
            stdscr.refresh()
            time.sleep(1)
            stdscr.addstr(max_y // 2, max_x // 2, "YOU WIN..")
            stdscr.refresh()
            time.sleep(1)
            stdscr.addstr(max_y // 2, max_x // 2, "YOU WIN...")
            stdscr.refresh()
            time.sleep(1)
            stdscr.refresh()
            break

        key = stdscr.getch()
        if found_entry:
            stdscr.addstr(player_y * cell_height + 1,
                          player_x * cell_width + 2, "🧙", curses.color_pair(1))

            if (
                key == curses.KEY_UP
                and player_y > 0
                and not check_wall["north"] & maze[player_y][player_x]
            ):
                player_y -= 1
            elif (
                key == curses.KEY_DOWN
                and player_y < len(maze) - 1
                and not check_wall["south"] & maze[player_y][player_x]
            ):
                player_y += 1
            elif (
                key == curses.KEY_LEFT
                and player_x > 0
                and not check_wall["west"] & maze[player_y][player_x]
            ):
                player_x -= 1
            elif (
                key == curses.KEY_RIGHT
                and player_x < len(maze[0])
                and not check_wall["east"] & maze[player_y][player_x]
            ):
                player_x += 1

        if key == ord("b"):
            break
        stdscr.addstr((height + 1) * cell_height, 0, f"score {score}")
        stdscr.addstr((height + 1) * cell_height + 1, 0, "[b]. Back")
        stdscr.refresh()
        time.sleep(0.05)
