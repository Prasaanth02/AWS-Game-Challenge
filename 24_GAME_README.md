# 24 Game - Mathematical Puzzle Challenge

A sophisticated terminal-based mathematical puzzle game where players must use four random numbers (1-9) with basic arithmetic operations to create expressions that equal exactly 24. Perfect for developing logical thinking, mental arithmetic, and problem-solving skills!

## 🎯 Game Overview

The 24 Game is a classic mathematical puzzle that challenges players to use all four given numbers exactly once, combining them with arithmetic operations (+, −, ×, ÷) and parentheses to reach the target number 24. This implementation features multiple difficulty levels, intelligent hint systems, and comprehensive solution validation.

## 🎮 How to Play

### Objective
Create a mathematical expression using all four given numbers exactly once to equal 24.

### Basic Rules
- **Use all four numbers**: Each number must be used exactly once
- **Arithmetic operations**: Combine numbers with +, −, ×, ÷
- **Parentheses allowed**: Control order of operations with parentheses
- **Target**: The result must equal exactly 24
- **Whole numbers only**: Division must result in whole numbers (no decimals)

### Example Solutions
```
Numbers: [3, 3, 8, 8]  →  (8 ÷ 8 + 3) × 3 = 24
Numbers: [1, 2, 3, 4]  →  (1 + 2 + 3) × 4 = 24
Numbers: [4, 1, 8, 7]  →  (8 − 4) × (7 − 1) = 24
Numbers: [2, 2, 6, 6]  →  (6 + 6) × (2 + 2) = 24
```

## 🚀 Getting Started

### Quick Start (Windows)
1. **Easy Method**: Double-click `run_24_game.bat`
   - Automatically checks Python installation
   - Provides game instructions
   - Launches the game

### Manual Start (All Platforms)
```bash
# Linux/Mac
python3 twenty_four_game.py

# Windows
python twenty_four_game.py
```

### System Requirements
- Python 3.6 or higher
- Terminal/Command prompt
- No additional dependencies required

## 🎯 Difficulty Levels

### Easy Mode
- **Operators**: Addition (+) and Subtraction (−) only
- **Purpose**: Learn basic number combinations
- **Strategy**: Focus on grouping numbers to reach 24

### Normal Mode (Default)
- **Operators**: All four operations (+, −, ×, ÷)
- **Purpose**: Standard 24 Game experience
- **Strategy**: Use multiplication and division strategically

### Hard Mode
- **Operators**: All four operations
- **Features**: Time pressure and performance tracking
- **Purpose**: Speed and accuracy challenges

### Expert Mode
- **Operators**: All four operations
- **Features**: Challenging number combinations
- **Purpose**: Advanced puzzles with complex solutions
- **Note**: Ensures puzzles are solvable but not trivial

## ⌨️ Commands and Controls

### Game Commands
```
Expression Input    - Type mathematical expressions (e.g., (8+8)*(3-1))
hint               - Get strategic hints for current puzzle
solution           - Show one possible solution
new                - Generate new random numbers
stats              - Display game statistics
difficulty [level] - Change difficulty (easy/normal/hard/expert)
quit               - Exit the game
```

### Expression Format
- **Numbers**: Use the four given numbers
- **Operators**: +, −, ×, ÷ (or +, -, *, /)
- **Parentheses**: Use () to control order of operations
- **Spaces**: Optional (expressions are cleaned automatically)

### Valid Expression Examples
```
8 + 8 + 4 + 4
(8 + 8) × (4 - 1)
8 × (4 - 1) + 0
(8 ÷ 4 + 1) × 8
```

## 🧮 Mathematical Strategies

### Common Patterns
1. **Multiplication to 24**: Find factors of 24 (1×24, 2×12, 3×8, 4×6)
2. **Addition then multiplication**: (a + b) × c = 24
3. **Subtraction patterns**: Use differences to create factors
4. **Division tricks**: Create fractions that simplify nicely

### Mental Math Tips
- **Factors of 24**: 1, 2, 3, 4, 6, 8, 12, 24
- **Common combinations**: 
  - 6 × 4 = 24
  - 8 × 3 = 24
  - 12 × 2 = 24
- **Order of operations**: Remember PEMDAS/BODMAS
- **Fraction thinking**: Sometimes division creates useful fractions

### Advanced Techniques
1. **Cross multiplication**: (a/b) × (c/d) patterns
2. **Nested operations**: Complex parentheses structures
3. **Zero creation**: Make one term equal zero to simplify
4. **Unit creation**: Make one term equal one for multiplication

## 📊 Features and Statistics

### Game Statistics Tracked
- **Games Played**: Total puzzles attempted
- **Games Solved**: Successfully completed puzzles
- **Success Rate**: Percentage of puzzles solved
- **Average Time**: Mean time per solved puzzle
- **Best Time**: Fastest solution time
- **Current Difficulty**: Active difficulty level

### Intelligent Hint System
- **Easy Mode**: Suggests available operators
- **Normal Mode**: Provides structural hints about parentheses
- **Hard/Expert**: Minimal hints showing required operators
- **Progressive**: Hints become more specific over time

### Solution Validation
- **Expression parsing**: Robust mathematical expression evaluation
- **Number verification**: Ensures all numbers used exactly once
- **Operator restrictions**: Enforces difficulty-level limitations
- **Result precision**: Handles floating-point arithmetic accurately
- **Error handling**: Clear feedback for invalid expressions

## 🎓 Educational Benefits

### Mathematical Skills
- **Mental arithmetic**: Quick calculation abilities
- **Order of operations**: Understanding PEMDAS/BODMAS
- **Algebraic thinking**: Pattern recognition and manipulation
- **Problem decomposition**: Breaking complex problems into steps
- **Number sense**: Understanding relationships between numbers

### Cognitive Benefits
- **Logical reasoning**: Systematic approach to problem-solving
- **Creative thinking**: Finding multiple solution paths
- **Persistence**: Working through challenging puzzles
- **Pattern recognition**: Identifying mathematical structures
- **Strategic planning**: Choosing optimal operation sequences

### Programming Concepts Demonstrated
- **Recursive algorithms**: Solution finding through backtracking
- **Expression evaluation**: Parsing and evaluating mathematical expressions
- **Combinatorial generation**: Creating all possible arrangements
- **Input validation**: Robust user input handling
- **State management**: Tracking game progress and statistics

## 🔧 Technical Implementation

### Core Algorithms
1. **Solution Generator**: Uses recursive backtracking to find all solutions
2. **Expression Evaluator**: Safe mathematical expression evaluation
3. **Permutation Engine**: Generates all number and operator combinations
4. **Validation System**: Comprehensive input and result verification

### Key Features
- **Fraction Arithmetic**: Uses Python's `fractions` module for exact calculations
- **Safe Evaluation**: Restricted `eval()` usage with controlled namespace
- **Pattern Matching**: Regular expressions for input parsing
- **Error Handling**: Graceful handling of edge cases and invalid input

### Code Structure
```
twenty_four_game.py
├── TwentyFourGame class
│   ├── Number generation and validation
│   ├── Solution finding algorithms
│   ├── Expression evaluation
│   ├── Game state management
│   └── Statistics tracking
├── User interface functions
├── Command processing
└── Main game loop
```

## 🎯 Challenge Modes and Variations

### Self-Imposed Challenges
1. **Speed Challenges**:
   - Solve 10 puzzles in under 5 minutes
   - Beat your best time consistently
   - Maintain >90% success rate

2. **Accuracy Challenges**:
   - Solve 20 puzzles without using hints
   - Find multiple solutions for each puzzle
   - Complete expert mode puzzles

3. **Learning Challenges**:
   - Explain your solution strategy
   - Find the most elegant solution
   - Identify patterns in number combinations

### Custom Variations
- **Different targets**: Modify code to target numbers other than 24
- **More numbers**: Extend to use 5 or 6 numbers
- **Limited operations**: Restrict to specific operators
- **Time limits**: Add countdown timers for pressure

## 🏆 Tips for Success

### Beginner Strategies
1. **Start simple**: Look for obvious multiplication patterns
2. **Use factors**: Think about what multiplies to make 24
3. **Try grouping**: Use parentheses to group operations
4. **Practice mental math**: Improve calculation speed
5. **Don't panic**: Take time to think through possibilities

### Advanced Strategies
1. **Work backwards**: Start with 24 and think what could make it
2. **Use fractions**: Sometimes division creates useful intermediate values
3. **Pattern recognition**: Learn common solution structures
4. **Multiple approaches**: Try different operation orders
5. **Systematic search**: Methodically try different combinations

### Expert Tips
1. **Memorize factors**: Know all factor pairs of 24 instantly
2. **Quick elimination**: Rapidly rule out impossible combinations
3. **Structural thinking**: Recognize expression patterns
4. **Efficiency focus**: Find solutions quickly and accurately
5. **Teaching others**: Explaining solutions deepens understanding

## 🔍 Troubleshooting

### Common Issues

**"No solution exists"**
- Very rare with proper number generation
- Try the hint system for guidance
- Use 'solution' command to verify

**"Invalid expression" errors**
- Check that all four numbers are used exactly once
- Verify operators are allowed in current difficulty
- Ensure proper parentheses matching

**Slow performance**
- Solution finding is computationally intensive
- Normal for complex puzzles in expert mode
- Consider using hints for difficult puzzles

### Input Format Help
```
✅ Valid formats:
   8 + 8 + 4 + 4
   (8+8)*(4-1)
   8 × (4 - 1) + 0
   (8÷4+1)×8

❌ Invalid formats:
   8 + 8 + 4        (missing one number)
   8 + 8 + 4 + 4 + 1 (extra number)
   8 ^ 2 + 8        (invalid operator)
   8 + + 8 + 4 + 4  (syntax error)
```

## 📈 Performance and Optimization

### Algorithm Complexity
- **Solution finding**: O(n! × 4^3 × p) where n=4, p=parentheses patterns
- **Expression evaluation**: O(expression length)
- **Validation**: O(expression length)

### Optimization Features
- **Early termination**: Stops searching when solution found (for hints)
- **Memoization**: Could be added for repeated number combinations
- **Efficient parsing**: Regex-based input validation
- **Lazy evaluation**: Solutions generated on-demand

## 🤝 Extending the Game

### Possible Enhancements
1. **Graphical Interface**: GUI version with drag-and-drop
2. **Multiplayer Mode**: Competitive puzzle solving
3. **Daily Challenges**: Curated difficult puzzles
4. **Achievement System**: Unlock rewards for milestones
5. **Solution Database**: Store and share interesting solutions

### Educational Extensions
1. **Step-by-step solver**: Show solution process
2. **Difficulty analysis**: Rate puzzle complexity
3. **Learning mode**: Guided tutorials
4. **Progress tracking**: Long-term skill development
5. **Classroom features**: Teacher dashboard and student progress

## 📜 Mathematical Background

### The 24 Game History
- **Origin**: Traditional Chinese arithmetic game
- **Educational use**: Widely used in mathematics education
- **Variations**: Different target numbers and operator sets
- **Complexity**: Demonstrates computational thinking concepts

### Related Mathematical Concepts
- **Combinatorics**: Counting possible arrangements
- **Graph theory**: Solution space as a search tree
- **Computational complexity**: NP-complete problem variants
- **Number theory**: Properties of integers and operations

## 🎮 Game Interface

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                              🎯 24 GAME PUZZLE 🎯                            ║
║                                                                              ║
║  Use four numbers with +, −, ×, ÷ operations to make exactly 24!           ║
║  Challenge your mathematical thinking and problem-solving skills!            ║
╚══════════════════════════════════════════════════════════════════════════════╝

🎯 Starting in NORMAL mode
Available operators: +, −, ×, ÷

================================================================================

🎲 Your numbers: [3, 3, 8, 8]
🎯 Make these equal 24 using +, −, ×, ÷
⏱️  Timer started! (Difficulty: Normal)

💭 Enter expression (or command): (8 ÷ 8 + 3) × 3

🎉 Correct! (8 ÷ 8 + 3) × 3 = 24
Time: 15.23 seconds

📚 Found 4 total solutions!
Show all solutions? (y/n): y

🔍 All solutions:
  1. (8 ÷ 8 + 3) × 3
  2. 3 × (8 ÷ 8 + 3)
  3. (3 + 8 ÷ 8) × 3
  4. 3 × (3 + 8 ÷ 8)
```

## 📊 Statistics Display

```
Game Statistics:
================
Games Played: 15
Games Solved: 12
Success Rate: 80.0%
Average Time: 45.3s
Best Time: 8.7s
Current Difficulty: Normal
```

---

**Ready to challenge your mathematical thinking? Launch the game and see how many puzzles you can solve!** 🚀

*This game demonstrates the power of logical thinking, recursive algorithms, and mathematical problem-solving - perfect for the AWS Q CLI environment!*
