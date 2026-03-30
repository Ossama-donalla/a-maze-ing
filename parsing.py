import sys


def parse_config() -> dict:
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
            config = {}
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
                            value = int(value)
                            if value <= 0:
                                raise ValueError()
                        except ValueError:
                            raise ValueError(
                                f"{key} must be a positive integer !!")
                        else:
                            config[key] = value
                            in_file.append(key)
                    elif key == 'HEIGHT':
                        if key in config.keys():
                            continue
                        try:
                            value = int(value)
                            if value <= 0:
                                raise ValueError()
                        except ValueError:
                            raise ValueError(
                                f"{key} must be a positive integer !!")
                        else:
                            config[key] = value
                            in_file.append(key)
                    elif key == 'ENTRY':
                        if key in config.keys():
                            continue
                        try:
                            entry_x, entry_y = value.split(',')
                            entry_x = int(entry_x)
                            if 'WIDTH' not in config or 'HEIGHT' not in config:
                                raise ValueError(
                                    "you must provide"
                                    " WIDTH and HEIGHT first !!")
                            if entry_x >= config['WIDTH'] or entry_x < 0:
                                raise ValueError(
                                    "Entry is out of the maze's bounds !!")
                            entry_y = int(entry_y)
                            if entry_y >= config['HEIGHT'] or entry_y < 0:
                                raise ValueError(
                                    "Entry is out of the maze's bounds !!")
                            config[key] = (entry_x, entry_y)
                            in_file.append(key)
                        except Exception as e:
                            print(f"[{key}]", e)
                            exit()
                    elif key == 'EXIT':
                        if key in config.keys():
                            continue
                        try:
                            exit_x, exit_y = value.split(',')
                            exit_x = int(exit_x)
                            if 'WIDTH' not in config or 'HEIGHT' not in config:
                                raise ValueError(
                                    "you must provide"
                                    " WIDTH and HEIGHT first !!")
                            if exit_x >= config['WIDTH'] or exit_x < 0:
                                raise ValueError(
                                    "Exit is out of the maze's bounds !!")
                            exit_y = int(exit_y)
                            if exit_y >= config['HEIGHT'] or exit_y < 0:
                                raise ValueError(
                                    "Exit is out of the maze's bounds !!")
                            config[key] = (exit_x, exit_y)
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
                                value = int(value)
                                config[key] = value
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
