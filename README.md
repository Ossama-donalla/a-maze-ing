*This project has been created as part of the 42 curriculum by akoudri, oait-all.*

# A-Maze-ing

## Description
A-Maze-ing is a project focused on generating and solving mazes using algorithmic techniques.  
The goal is to create a program capable of building a valid maze and optionally finding a path from a start point to an end point.

---

## Instructions

### Compilation & Running
This project uses a Makefile for running, debugging, linting, and cleaning.

### Commands
```bash
# Run the project
make run

# Install dependencies
make install

# Debug with pdb
make debug

# Clean temporary files
make clean

# Lint code (flake8 + mypy)
make lint
```
## Resources
- **Maze Generation & Algorithms:**  
  - [Wikipedia – Maze generation algorithms](https://en.wikipedia.org/wiki/Maze_generation_algorithm)  
  - [GeeksforGeeks – Depth First Search (DFS) for maze generation](https://www.geeksforgeeks.org/maze-generation-using-depth-first-search/)  
  - [Red Blob Games – Grid-based pathfinding](https://www.redblobgames.com/pathfinding/a-star/introduction.html)  
- **Python Libraries & Tutorials:**  
  - [Python `curses` Documentation](https://docs.python.org/3/library/curses.html)  
  - [Pygame Documentation](https://www.pygame.org/docs/)  
- **AI & Assistance Usage:**  
  - Used ChatGPT to help understand maze algorithms


# Configuration File Structure

The configuration file uses a simple key=value format:
- width=10
- height=10
- entry=2,2
- exit=1,1
- output_file=output.txt
- perfect=True
- seed=4
### Fields
- width, height: Maze dimensions
- entry, exit: Entry and exit coordinates (x,y)
- output_file: Optional file to save maze
- perfect: True = maze has a single unique solution
- seed: Random seed for reproducibility

## Maze Generation Algorithm
The maze is generated using a depth-first search approach:
it starts from a cell wich is the entry we get from the config.txt , then visit a random neighbor and mark it visited keep exploring that cell and breaking walls until a deadend , and it backtracks when needed, and repeats and it must visit every cell in the grid only once

## Why This Algorithm
Simple and efficient
Produces perfect mazes (one unique path)
Easy to implement and debug
Flexible for extensions
```
<!-- Game Logic / Features
Terminal rendering using curses
Player character: 🧙, exit: 🏆, gems: 💎, path: ⭐
Interactive controls:
Arrow keys → Move the player
r → Regenerate a new maze
s/h → Show/Hide solution path
c → Rotate maze colors
b → Back / exit
Sound effects with pygame:
Background music plays in loop
Sound for collecting gems 💎
Sound for reaching the exit 🏆
Special blocked cells (blocked_42) and dynamic features like random gem placement -->

## Reusable Code
The MazeGenerator class where i did my algorithmes logique in a standalone module and in a package for future usage

## 👥 Team & Project Management

### Roles of Each Team Member
### login : akoudri 
– Parsing the config file, Maze generation (DFS), Find shortest path(BFS), Makefile, and all what is related to the maze's base 
### login : oait-all
- Visualization, testing & debugging , integration , final testing , Readme , and all what is related to the maze's interface and display 


### Anticipated Planning & Evolution
- **Initial Plan:**  
  - Define project architecture  
  - Implement core maze generation algorithm (DFS / Recursive Backtracking)  
  - Set up configuration file parsing  
  - Develop basic visualization with `curses`  

- **Evolution:**  
  - Added interactive features (player movement, gem collection, exit unlocking)  
  - Integrated sound and background music using `pygame`  
  - Implemented dynamic path visualization and color rotation  
  - Refactored code for modularity and reusability  
  - Created Makefile for running, linting, debugging, and cleaning  

### What Worked Well
- Clear task distribution (even as a solo contributor, modular approach helped)  
- Modular and reusable code  
- Frequent testing ensured fewer bugs  
- Terminal visualization with symbols and colors made gameplay intuitive  

### What Could Be Improved
- Time management for implementing advanced features  
- Earlier integration of sound and path visualization  
- More extensive automated testing for edge cases  

### Tools Used
- **Programming & Debugging:** Python, `pdb`, `flake8`, `mypy`  
- **Visualization & Interaction:** `curses` library  
- **Sound & Music:** `pygame`  
- **Project Management:** GitHub, Makefile