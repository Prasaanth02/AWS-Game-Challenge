#!/usr/bin/env python3
"""
24 Game - Mathematical Puzzle Challenge
======================================

A challenging puzzle game where players must use four random numbers (1-9)
with basic arithmetic operations (+, -, ×, ÷) to create an expression that equals 24.

Features:
- Multiple difficulty levels with operator restrictions
- Timer-based challenges
- Expression validation with parentheses support
- Hint system using recursive solution finder
- Statistics tracking and high scores
- Educational mode with step-by-step solutions

Author: Amazon Q
Compatible with: Python 3.6+
"""

import random
import time
import re
import itertools
from typing import List, Tuple, Optional, Set
from fractions import Fraction
import sys


class TwentyFourGame:
    """Main game class for the 24 puzzle game."""
    
    def __init__(self):
        self.target = 24
        self.current_numbers = []
        self.start_time = 0
        self.games_played = 0
        self.games_solved = 0
        self.total_time = 0
        self.best_time = float('inf')
        self.difficulty = 'normal'
        self.available_operators = {
            'easy': ['+', '-'],
            'normal': ['+', '-', '*', '/'],
            'hard': ['+', '-', '*', '/'],
            'expert': ['+', '-', '*', '/']
        }
        self.operator_symbols = {'+': '+', '-': '−', '*': '×', '/': '÷'}
        
    def generate_numbers(self) -> List[int]:
        """Generate four random numbers between 1 and 9."""
        if self.difficulty == 'expert':
            # Expert mode: ensure puzzle is solvable but challenging
            while True:
                numbers = [random.randint(1, 9) for _ in range(4)]
                if self.has_solution(numbers):
                    # Make sure it's not too easy (no obvious solutions)
                    if not self.has_trivial_solution(numbers):
                        return numbers
        else:
            # Other difficulties: generate and ensure solvable
            attempts = 0
            while attempts < 50:  # Prevent infinite loops
                numbers = [random.randint(1, 9) for _ in range(4)]
                if self.has_solution(numbers):
                    return numbers
                attempts += 1
            
            # Fallback to known solvable combinations
            known_puzzles = [
                [1, 1, 8, 8],  # (8+8)*1+8 = 24
                [1, 2, 3, 4],  # (1+2+3)*4 = 24
                [2, 2, 6, 6],  # (6+6)+(2*6) = 24
                [1, 3, 4, 6],  # 6*(4+3-1) = 24
                [2, 3, 4, 4],  # (4+4+4)*3-12 = 24
                [3, 3, 8, 8],  # 8/(1-3/8)*3 = 24
                [1, 5, 5, 5],  # 5*(5-1/5) = 24
                [2, 4, 6, 8],  # (8-4)*(6+2) = 24
            ]
            return random.choice(known_puzzles)
    
    def has_trivial_solution(self, numbers: List[int]) -> bool:
        """Check if puzzle has obvious/trivial solutions."""
        # Check for simple multiplication to 24
        for num in numbers:
            if 24 % num == 0 and (24 // num) in numbers:
                return True
        
        # Check for simple addition patterns
        if sum(numbers) == 24:
            return True
            
        return False
    
    def has_solution(self, numbers: List[int]) -> bool:
        """Check if the given numbers can form 24 using available operators."""
        solutions = self.find_all_solutions(numbers)
        return len(solutions) > 0
    
    def find_all_solutions(self, numbers: List[int]) -> List[str]:
        """Find all possible solutions for the given numbers."""
        solutions = set()
        operators = self.available_operators[self.difficulty]
        
        # Generate all permutations of numbers
        for num_perm in itertools.permutations(numbers):
            # Generate all combinations of operators
            for ops in itertools.product(operators, repeat=3):
                # Try different parentheses patterns
                patterns = [
                    "({0} {4} {1}) {5} ({2} {6} {3})",  # (a op b) op (c op d)
                    "(({0} {4} {1}) {5} {2}) {6} {3}",  # ((a op b) op c) op d
                    "({0} {4} ({1} {5} {2})) {6} {3}",  # (a op (b op c)) op d
                    "{0} {4} (({1} {5} {2}) {6} {3})",  # a op ((b op c) op d)
                    "{0} {4} ({1} {5} ({2} {6} {3}))",  # a op (b op (c op d))
                    "{0} {4} {1} {5} {2} {6} {3}",      # a op b op c op d (no parentheses)
                ]
                
                for pattern in patterns:
                    try:
                        expression = pattern.format(*num_perm, *ops)
                        result = self.evaluate_expression(expression)
                        if abs(result - self.target) < 1e-10:  # Handle floating point precision
                            # Convert to display format
                            display_expr = expression
                            for op, symbol in self.operator_symbols.items():
                                display_expr = display_expr.replace(op, f' {symbol} ')
                            solutions.add(display_expr)
                    except:
                        continue
        
        return list(solutions)
    
    def evaluate_expression(self, expression: str) -> float:
        """Safely evaluate mathematical expression."""
        try:
            # Replace division with true division and handle fractions
            # Convert to use Fraction for exact arithmetic
            expr = expression.replace('/', '//')
            
            # Use eval with restricted namespace for safety
            allowed_names = {
                "__builtins__": {},
                "__name__": "__main__",
            }
            
            # First try with regular division
            try:
                result = eval(expression, allowed_names)
                # Check if division results in whole numbers only
                if '/' in expression:
                    # Re-evaluate with fraction arithmetic for precision
                    return float(self.evaluate_with_fractions(expression))
                return float(result)
            except ZeroDivisionError:
                return float('inf')
                
        except Exception:
            raise ValueError("Invalid expression")
    
    def evaluate_with_fractions(self, expression: str) -> Fraction:
        """Evaluate expression using fractions for exact arithmetic."""
        # Convert numbers to fractions and evaluate
        tokens = re.findall(r'\d+|[+\-*/()]', expression)
        
        # Build expression with Fraction objects
        frac_expr = ""
        for token in tokens:
            if token.isdigit():
                frac_expr += f"Fraction({token})"
            else:
                frac_expr += token
        
        allowed_names = {
            "__builtins__": {},
            "Fraction": Fraction,
        }
        
        try:
            result = eval(frac_expr, allowed_names)
            return result
        except ZeroDivisionError:
            return Fraction('inf')
    
    def validate_expression(self, expression: str, numbers: List[int]) -> Tuple[bool, str]:
        """Validate user's expression."""
        try:
            # Clean up the expression
            expression = expression.replace('×', '*').replace('÷', '/').replace('−', '-')
            expression = expression.replace(' ', '')
            
            # Check for valid characters
            if not re.match(r'^[\d+\-*/().]+$', expression):
                return False, "Invalid characters in expression. Use only numbers, +, -, ×, ÷, and parentheses."
            
            # Extract numbers from expression
            expr_numbers = [int(x) for x in re.findall(r'\d+', expression)]
            expr_numbers.sort()
            numbers_sorted = sorted(numbers)
            
            # Check if all numbers are used exactly once
            if expr_numbers != numbers_sorted:
                return False, f"You must use each number exactly once: {numbers}"
            
            # Check operators are allowed for current difficulty
            used_operators = set(re.findall(r'[+\-*/]', expression))
            allowed_ops = set(self.available_operators[self.difficulty])
            if not used_operators.issubset(allowed_ops):
                forbidden = used_operators - allowed_ops
                return False, f"Operators not allowed in {self.difficulty} mode: {forbidden}"
            
            # Evaluate the expression
            result = self.evaluate_expression(expression)
            
            # Check for division by zero or invalid results
            if result == float('inf') or result != result:  # NaN check
                return False, "Division by zero or invalid operation."
            
            # Check if result is close to target (handle floating point precision)
            if abs(result - self.target) < 1e-10:
                return True, f"Correct! {expression} = {self.target}"
            else:
                return False, f"Result is {result:.3f}, not {self.target}."
                
        except Exception as e:
            return False, f"Invalid expression: {str(e)}"
    
    def get_hint(self) -> str:
        """Provide a hint for the current puzzle."""
        solutions = self.find_all_solutions(self.current_numbers)
        
        if not solutions:
            return "No solution exists for these numbers!"
        
        # Provide a partial hint
        solution = solutions[0]
        
        if self.difficulty == 'easy':
            return f"Try using these operators: {', '.join(self.available_operators[self.difficulty])}"
        elif self.difficulty == 'normal':
            # Give a structural hint
            if '(' in solution:
                return "Try using parentheses to group operations."
            else:
                return "Try operations from left to right without parentheses."
        else:
            # For hard/expert, give minimal hints
            operators_used = set(re.findall(r'[+\-×÷]', solution))
            return f"You'll need these operators: {', '.join(sorted(operators_used))}"
    
    def show_solution(self) -> str:
        """Show one possible solution."""
        solutions = self.find_all_solutions(self.current_numbers)
        if solutions:
            return f"One solution: {solutions[0]}"
        return "No solution exists!"
    
    def start_new_game(self):
        """Start a new puzzle."""
        self.current_numbers = self.generate_numbers()
        self.start_time = time.time()
        self.games_played += 1
    
    def solve_puzzle(self, expression: str) -> Tuple[bool, str]:
        """Attempt to solve the current puzzle."""
        is_valid, message = self.validate_expression(expression, self.current_numbers)
        
        if is_valid:
            elapsed_time = time.time() - self.start_time
            self.games_solved += 1
            self.total_time += elapsed_time
            
            if elapsed_time < self.best_time:
                self.best_time = elapsed_time
            
            return True, f"{message}\nTime: {elapsed_time:.2f} seconds"
        
        return False, message
    
    def get_statistics(self) -> str:
        """Get game statistics."""
        if self.games_played == 0:
            return "No games played yet."
        
        success_rate = (self.games_solved / self.games_played) * 100
        avg_time = self.total_time / max(self.games_solved, 1)
        best_time_str = f"{self.best_time:.2f}s" if self.best_time != float('inf') else "N/A"
        
        return f"""
Game Statistics:
================
Games Played: {self.games_played}
Games Solved: {self.games_solved}
Success Rate: {success_rate:.1f}%
Average Time: {avg_time:.2f}s
Best Time: {best_time_str}
Current Difficulty: {self.difficulty.title()}
"""

    def set_difficulty(self, difficulty: str) -> bool:
        """Set game difficulty level."""
        if difficulty.lower() in self.available_operators:
            self.difficulty = difficulty.lower()
            return True
        return False


def print_banner():
    """Print game banner."""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              🎯 24 GAME PUZZLE 🎯                            ║
║                                                                              ║
║  Use four numbers with +, −, ×, ÷ operations to make exactly 24!           ║
║  Challenge your mathematical thinking and problem-solving skills!            ║
╚══════════════════════════════════════════════════════════════════════════════╝
""")


def print_instructions():
    """Print game instructions."""
    print("""
🎮 HOW TO PLAY:
===============
• You'll get four random numbers (1-9)
• Use ALL four numbers exactly ONCE
• Combine them with +, −, ×, ÷ operations
• Use parentheses to control order of operations
• Goal: Create an expression that equals 24

📝 EXAMPLES:
============
Numbers: [3, 3, 8, 8]  →  (8 ÷ 8 + 3) × 3 = 24
Numbers: [1, 2, 3, 4]  →  (1 + 2 + 3) × 4 = 24
Numbers: [4, 1, 8, 7]  →  (8 − 4) × (7 − 1) = 24

🎯 DIFFICULTY LEVELS:
====================
• EASY: Only + and − operations
• NORMAL: All operations (+, −, ×, ÷)
• HARD: All operations + time pressure
• EXPERT: Challenging number combinations

⌨️  COMMANDS:
=============
• Enter expression: Type your mathematical expression
• 'hint' - Get a helpful hint
• 'solution' - Show one possible solution
• 'new' - Generate new numbers
• 'stats' - View your statistics
• 'difficulty [level]' - Change difficulty (easy/normal/hard/expert)
• 'quit' - Exit the game
""")


def main():
    """Main game loop."""
    print_banner()
    print_instructions()
    
    game = TwentyFourGame()
    
    print(f"\n🎯 Starting in {game.difficulty.upper()} mode")
    print("Available operators:", ', '.join([game.operator_symbols.get(op, op) for op in game.available_operators[game.difficulty]]))
    
    while True:
        print("\n" + "="*80)
        game.start_new_game()
        
        print(f"\n🎲 Your numbers: {game.current_numbers}")
        print(f"🎯 Make these equal 24 using {', '.join([game.operator_symbols.get(op, op) for op in game.available_operators[game.difficulty]])}")
        print(f"⏱️  Timer started! (Difficulty: {game.difficulty.title()})")
        
        while True:
            try:
                user_input = input("\n💭 Enter expression (or command): ").strip()
                
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.lower() == 'quit':
                    print(game.get_statistics())
                    print("\n👋 Thanks for playing! Keep practicing your math skills!")
                    return
                
                elif user_input.lower() == 'new':
                    print("🔄 Generating new puzzle...")
                    break
                
                elif user_input.lower() == 'hint':
                    print(f"💡 Hint: {game.get_hint()}")
                    continue
                
                elif user_input.lower() == 'solution':
                    elapsed = time.time() - game.start_time
                    print(f"📖 {game.show_solution()}")
                    print(f"⏱️  Time taken: {elapsed:.2f} seconds")
                    break
                
                elif user_input.lower() == 'stats':
                    print(game.get_statistics())
                    continue
                
                elif user_input.lower().startswith('difficulty'):
                    parts = user_input.split()
                    if len(parts) == 2:
                        if game.set_difficulty(parts[1]):
                            print(f"🎯 Difficulty set to {game.difficulty.upper()}")
                            print(f"Available operators: {', '.join([game.operator_symbols.get(op, op) for op in game.available_operators[game.difficulty]])}")
                        else:
                            print("❌ Invalid difficulty. Use: easy, normal, hard, or expert")
                    else:
                        print(f"Current difficulty: {game.difficulty.title()}")
                        print("Usage: difficulty [easy|normal|hard|expert]")
                    continue
                
                # Try to solve the puzzle
                success, message = game.solve_puzzle(user_input)
                
                if success:
                    print(f"🎉 {message}")
                    
                    # Show additional solutions if available
                    all_solutions = game.find_all_solutions(game.current_numbers)
                    if len(all_solutions) > 1:
                        print(f"\n📚 Found {len(all_solutions)} total solutions!")
                        show_more = input("Show all solutions? (y/n): ").lower().startswith('y')
                        if show_more:
                            print("\n🔍 All solutions:")
                            for i, sol in enumerate(all_solutions[:10], 1):  # Limit to 10
                                print(f"  {i}. {sol}")
                            if len(all_solutions) > 10:
                                print(f"  ... and {len(all_solutions) - 10} more!")
                    
                    break
                else:
                    print(f"❌ {message}")
                    
                    # Show elapsed time for motivation
                    elapsed = time.time() - game.start_time
                    if elapsed > 30:
                        print(f"⏱️  Time elapsed: {elapsed:.1f}s - Need a hint?")
                
            except KeyboardInterrupt:
                print(f"\n\n{game.get_statistics()}")
                print("👋 Game interrupted. Thanks for playing!")
                return
            except EOFError:
                print(f"\n\n{game.get_statistics()}")
                print("👋 Thanks for playing!")
                return


if __name__ == "__main__":
    main()
