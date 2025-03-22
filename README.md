Connect Four Game with Minimax AI

Overview: This project implements a Connect Four game with an intelligent computer opponent using the minimax algorithm. The implementation demonstrates fundamental concepts in game theory, decision tree algorithms, and adversarial search techniques through a classic board game interface.

Features
- Command-line based Connect Four game with customizable board dimensions
- Adjustable AI difficulty levels (0-5 ply depth)
- Multiple tie-breaking strategies (left-biased, right-biased, or random)
- Player vs. AI and Player vs. Player gameplay modes
- Well-documented codebase with object-oriented design principles

Technical Implementation
The AI uses a minimax algorithm with the following key components:
- Recursive game state evaluation with configurable lookahead depth
- Position scoring based on winning, losing, and neutral game states
- Intelligent move selection with customizable tie-breaking strategies
- Efficient board representation and manipulation

Project Structure
Copyconnect4_minimax/
├── board.py       # Board class and game state management
├── player.py      # Player classes (Human and AI) with decision algorithms
├── connect4.py        # Game controller and user interface
└── README.md      # Project documentation

AI Difficulty Levels
- Level 0: Makes decisions based only on the current board state
- Level 1: Looks ahead one move (responds to immediate threats/opportunities)
- Level 2: Looks ahead two moves (basic strategy)
- Level 3: Looks ahead three moves (intermediate strategy)
- Level 4: Looks ahead four moves (advanced strategy)
- Level 5: Looks ahead five moves (expert level)

Algorithm Details
The minimax implementation evaluates game states recursively by:
1. Exploring all possible moves from the current position
2. Assessing resulting board states at a specified depth
3. Propagating values upward, assuming optimal play from both players
5. Selecting the move that maximizes the AI's advantage

The evaluation function assigns:
- WIN (100.0) for positions where the AI wins
- LOSE (0.0) for positions where the opponent wins
- DRAW (50.0) for neutral positions
- FULL (-1) for invalid moves (full columns)

Future Enhancements
- Alpha-beta pruning for more efficient search
- Improved evaluation function with positional heuristics
- GUI interface with animations
- Game state saving/loading
- Tournament mode

Skills Demonstrated
- Algorithm design and implementation
- Game theory application
- Object-oriented programming
- Recursive problem-solving
- Command-line interface design