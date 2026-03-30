*This project has been created as part of the 42 curriculum by <login1>[, <login2>[, <login3>[...]]].*

# 🧩 A-Maze-ing

## 📖 Description
A-Maze-ing is a project focused on generating and solving mazes using algorithmic techniques.  
The goal is to create a program capable of building a valid maze and optionally finding a path from a start point to an end point.

---

## ⚙️ Instructions

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
# Configuration File Structure

The configuration file uses a simple key=value format.

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
```bash
 had part chra7 fiha chno darti okk
Recursive Backtracking (DFS) 

The maze is generated using a depth-first search approach:

Start from a cell
Visit a random neighbor
Remove the wall between cells
Repeat recursively
Backtrack when needed

❓ Why This Algorithm
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
Grid system → reusable for any 2D problem
DFS/BFS logic → usable in pathfinding
Parser → reusable for config handling

## 👥 Team & Project Management

### Roles of Each Team Member
- login :akoudri – Maze generation (DFS), algorithm optimization , Configuration parsing  input handling 

chra7 l3ibat dyalk hana okkk *explain*


### login :oait-all
- Visualization, testing & debugging , integration , final testing , makefile

> - **Visualization:** We used the `curses` library to draw the maze in the terminal. Each cell is represented with walls and paths, with colors that can rotate dynamically. Special symbols like 🧙 (player), 💎 (gems), and 🏆 (exit) improve readability and interactivity.  
> - **Player Movement Logic:** The player moves with arrow keys. Movement is blocked by walls, ensuring the maze rules are respected. Collecting gems and reaching the exit triggers sound effects via `pygame`.  
> - **Integration of Modules:** The project is modular: maze generation, configuration parsing, visualization, and sound handling are separate. They communicate through shared data structures, making it easy to extend or modify any part.  
> - **Project Organization:** The code is structured with clear separation of concerns. The Makefile handles running, linting, debugging, and cleaning. Configuration is externalized in `config.txt` for flexibility.

---

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
