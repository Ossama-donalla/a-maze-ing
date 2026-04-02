import sys
from typing import Dict


def parse_config() -> dict:
    """
    Parse and validate a configuration file for maze generation.

    This function reads a configuration file (`config.txt`) passed as a
    command-line argument, validates its contents, and returns a dictionary
    containing the parsed configuration values.

    The configuration file must follow a KEY=VALUE format, with
    optional comments starting with '#'. Mandatory keys must be present,
    and values must respect specific constraints depending on the key.

    Expected command:
        python3 a_maze_ing.py config.txt

    Supported keys:
        - WIDTH (int): Width of the maze (must be > 0)
        - HEIGHT (int): Height of the maze (must be > 0)
        - ENTRY (tuple[int, int]): Entry coordinates within bounds
        - EXIT (tuple[int, int]): Exit coordinates within bounds
        - OUTPUT_FILE (str): Output file name
            (must not overwrite critical files)
        - PERFECT (bool): Whether the maze is perfect ("TRUE" or "FALSE")
        - SEED (int | None, optional): Random seed

    Returns:
        dict: A dictionary containing validated configuration values.

    Raises:
        ValueError: If:
            - Incorrect number of command-line arguments
            - Invalid file name
            - Invalid key or missing mandatory key
            - Incorrect value format or out-of-bounds values
            - ENTRY and EXIT are identical

    Notes:
        - Lines starting with '#' or empty lines are ignored.
        - Inline comments (after values) are supported.
        - Duplicate keys are ignored after first occurrence.
        - The function exits the program on most errors
            after printing messages.
    """
    try:
        if len(sys.argv) != 2:
            raise ValueError("Try this : python3 a_maze_ing.py config.txt")
        elif len(sys.argv) == 2:
            if sys.argv[1] != 'config.txt':
                raise ValueError("the argv[1] must be 'config.txt'")
        with open(sys.argv[1]) as f:
            mandatory = ['WIDTH', 'HEIGHT', 'ENTRY', 'EXIT',
                         'OUTPUT_FILE', 'PERFECT']
            forbiden = ['config.txt', 'a_maze_ing.py', 'parsing.py',
                        'MazeGenerator.py', 'Makefile', 'README.md']
            in_file = []
            config: Dict = {}
            while True:
                content = f.readline()
                if not content:
                    break
                content = content.strip()
                if not content:
                    continue
                if content.startswith('#'):
                    continue
                key, value = content.split('=', 1)
                key = key.strip().upper()
                value = value.strip()
                if not key or not value:
                    raise ValueError(
                        "Each line should be in KEY=VALUE format !!")
                if key not in mandatory and key != 'SEED':
                    raise ValueError("Invalid key !!")
                else:
                    if '#' in value:
                        first, second = value.split(' ', 1)
                        second = second.strip()
                        if second.startswith('#'):
                            value = first
                    if key == 'WIDTH':
                        if key in config.keys():
                            continue
                        try:
                            val = int(value)
                            if val <= 0:
                                raise ValueError()
                        except ValueError:
                            raise ValueError(
                                f"{key} must be a positive integer !!")
                        else:
                            config[key] = int(value)
                            in_file.append(key)
                    elif key == 'HEIGHT':
                        if key in config.keys():
                            continue
                        try:
                            val = int(value)
                            if val <= 0:
                                raise ValueError()
                        except ValueError:
                            raise ValueError(
                                f"{key} must be a positive integer !!")
                        else:
                            config[key] = int(value)
                            in_file.append(key)
                    elif key == 'ENTRY':
                        if key in config.keys():
                            continue
                        try:
                            entry_x, entry_y = value.split(',')
                            entr_x = int(entry_x)
                            if 'WIDTH' not in config or 'HEIGHT' not in config:
                                raise ValueError(
                                    "you must provide"
                                    " WIDTH and HEIGHT first !!")
                            if entr_x >= config['WIDTH'] or entr_x < 0:
                                raise ValueError(
                                    "Entry is out of the maze's bounds !!")
                            entr_y = int(entry_y)
                            if entr_y >= config['HEIGHT'] or entr_y < 0:
                                raise ValueError(
                                    "Entry is out of the maze's bounds !!")
                            config[key] = (entr_x, entr_y)
                            in_file.append(key)
                        except Exception as e:
                            print(f"[{key}]", e)
                            exit()
                    elif key == 'EXIT':
                        if key in config.keys():
                            continue
                        try:
                            exit_x, exit_y = value.split(',')
                            exitt_x = int(exit_x)
                            if 'WIDTH' not in config or 'HEIGHT' not in config:
                                raise ValueError(
                                    "you must provide"
                                    " WIDTH and HEIGHT first !!")
                            if exitt_x >= config['WIDTH'] or exitt_x < 0:
                                raise ValueError(
                                    "Exit is out of the maze's bounds !!")
                            exitt_y = int(exit_y)
                            if exitt_y >= config['HEIGHT'] or exitt_y < 0:
                                raise ValueError(
                                    "Exit is out of the maze's bounds !!")
                            config[key] = (exitt_x, exitt_y)
                            in_file.append(key)
                        except Exception as e:
                            print(f"[{key}]", e)
                            exit()
                    elif key == 'OUTPUT_FILE':
                        if key in config.keys():
                            continue
                        if value in forbiden:
                            raise ValueError(
                                "You can't override essential files !!")
                        else:
                            try:
                                if value[0] in ('/', '\\'):
                                    raise ValueError(
                                        "Can't open a"
                                        " file starting with any of "
                                        "the slashes !!")
                                file = open(value, 'w')
                                file.close()
                                config[key] = value
                                in_file.append(key)
                            except Exception as e:
                                print(f"[{key}]", e)
                                exit()
                    elif key == 'PERFECT':
                        if key in config.keys():
                            continue
                        try:
                            value = value.upper()
                            if value not in ('TRUE', 'FALSE'):
                                raise ValueError(
                                    "Provide a boolean value describing"
                                    " the maze's state !!")
                            config[key] = (value == 'TRUE')
                            in_file.append(key)
                        except Exception as e:
                            print(f"[{key}]", e)
                            exit()
                    elif key == 'SEED':
                        if key in config.keys():
                            continue
                        try:
                            value = value.capitalize()
                            if value == 'None':
                                config[key] = None
                            else:
                                val = int(value)
                                config[key] = val
                            in_file.append(key)
                        except Exception as e:
                            print(f"[{key}]", e)
                            exit()
        if 'SEED' not in in_file:
            config['SEED'] = None
        if config.get('ENTRY') == config.get('EXIT'):
            raise ValueError("ENTRY and EXIT must be different !!")
        try:
            left = [key for key in mandatory if key not in in_file]
            if left:
                raise ValueError('missing mandatory keys : ')
        except Exception as e:
            print(e, end='')
            for le in left:
                print(le, end=' ')
            print()
            exit()
        else:
            return config
    except Exception as e:
        print("[MAIN EXCEPTION]", e)
        exit()
