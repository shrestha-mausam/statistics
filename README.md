# Statistics Calculator - Multi-Paradigm Implementation

This project implements a statistics calculator that computes basic statistics (mean, median, and mode) on a list of integers using three different programming languages and paradigms:

- **C** - Procedural programming approach
- **OCaml** - Functional programming approach
- **Python** - Object-oriented programming approach

## Problem Requirements

Given a list of integers, calculate the following statistics:
- **Mean**: The average of all integers in the list
- **Median**: The middle value of the list when sorted
- **Mode**: The most frequently occurring integer(s) in the list

## Implementation Details

### 1. C Implementation (Procedural)
- **File**: `statistics.c`
- **Paradigm**: Procedural programming
- **Key Features**:
  - Prompts the user to enter a list of integers separated by spaces
  - Functions for calculating mean, median, and mode
  - Manual memory management with `malloc` and `free`
  - Array-based data structures
  - Direct sorting and counting logic
  - Error handling for memory allocation

**Key Functions**:
- `read_integers()` - Reads a line of user input and parses integers
- `calculate_mean()` - Computes arithmetic mean
- `calculate_median()` - Computes median with sorting
- `calculate_mode()` - Finds most frequent values, returns no mode if all values occur equally
- `print_array()` - Utility for displaying data

### 2. OCaml Implementation (Functional)
- **File**: `statistics.ml`
- **Paradigm**: Functional programming
- **Key Features**:
  - Prompts the user to enter a list of integers separated by spaces
  - Immutable data structures
  - Higher-order functions (`List.fold_left`, `List.map`, `List.filter`)
  - Pattern matching and recursion
  - No mutable state
  - Functional composition

**Key Functions**:
- `read_integers` - Reads a line of user input and parses integers
- `calculate_mean` - Uses `List.fold_left` for summation
- `calculate_median` - Uses `List.sort` and pattern matching
- `calculate_mode` - Uses `List.fold_left` for frequency counting, returns no mode if all values occur equally
- `count_frequencies` - Functional frequency counting

### 3. Python Implementation (Object-Oriented)
- **File**: `statistics.py`
- **Paradigm**: Object-oriented programming
- **Key Features**:
  - Prompts the user to enter a list of integers separated by spaces
  - `StatisticsCalculator` class with encapsulated methods
  - Properties and data encapsulation
  - Caching for performance optimization
  - Comprehensive data summary methods
  - Type hints for better code clarity

**Key Methods**:
- `read_integers_from_input()` - Reads a line of user input and parses integers
- `calculate_mean()` - Instance method for mean calculation
- `calculate_median()` - Instance method for median calculation
- `calculate_mode()` - Instance method for mode calculation, returns no mode if all values occur equally
- `get_data_summary()` - Returns comprehensive statistics
- `add_data()` / `add_multiple_data()` - Dynamic data addition

## Building and Running

### Prerequisites
- **C**: GCC compiler
- **OCaml**: OCaml compiler (`ocamlc`)
- **Python**: Python 3.x

### Quick Start
```bash
# Compile and run all programs
make run

# Or compile all programs
make all

# Run individual programs
make run_c      # C program
make run_ocaml  # OCaml program
make run_python # Python program
```

### Manual Compilation

**C Program**:
```bash
gcc -Wall -Wextra -std=c99 -O2 -o statistics_c statistics.c
./statistics_c
```

**OCaml Program**:
```bash
ocamlc -o statistics_ocaml statistics.ml
./statistics_ocaml
```

**Python Program**:
```bash
python3 statistics.py
```

## Usage

When you run any of the programs, you will be prompted:

```
Enter a list of integers separated by spaces:
```

Type your list (e.g., `4 2 7 2 9 4 1 7 4 8 2`) and press Enter. The program will then display the calculated mean, median, and mode. If all values occur equally, the program will indicate that there is no mode.

## Example Output

```
=== Statistics Calculator (C - Procedural) ===

Enter a list of integers separated by spaces: 4 2 7 2 9 4 1 7 4 8 2
Input data: [4, 2, 7, 2, 9, 4, 1, 7, 4, 8, 2]

Mean: 4.55
Median: 4.00
Mode: [2, 4]
```

## Paradigm-Specific Features Demonstrated

### C (Procedural)
- Manual memory management
- Array manipulation
- Function-based organization
- Error handling with return codes
- Direct algorithm implementation

### OCaml (Functional)
- Immutable data structures
- Higher-order functions
- Pattern matching
- Recursive algorithms
- Functional composition
- List processing with `fold`, `map`, `filter`

### Python (Object-Oriented)
- Class-based design
- Encapsulation with private attributes
- Properties for controlled access
- Method overloading and polymorphism
- Data abstraction
- Caching and optimization

## Additional Features

Each implementation includes:
- User input for data (no hardcoded datasets)
- Error handling for edge cases
- Comprehensive output formatting
- Additional utility functions
- Paradigm-specific demonstrations

## File Structure
```
statistics/
├── statistics.c      # C implementation (procedural)
├── statistics.ml     # OCaml implementation (functional)
├── statistics.py     # Python implementation (object-oriented)
├── Makefile         # Build and run scripts
└── README.md        # This file
```

## Dependencies Installation

### macOS (with Homebrew)
```bash
brew install gcc ocaml
```

### Ubuntu/Debian
```bash
sudo apt-get install gcc ocaml python3
```

### CentOS/RHEL
```bash
sudo yum install gcc ocaml python3
```

## Cleanup
```bash
make clean  # Remove compiled files
```

## Help
```bash
make help  # Show available make targets
```

## Educational Value

This project demonstrates:
1. **Language Paradigms**: How the same problem can be solved using different programming paradigms
2. **Algorithm Implementation**: Different approaches to implementing the same algorithms
3. **Memory Management**: From manual (C) to automatic (Python/OCaml)
4. **Code Organization**: From procedural functions to object-oriented classes
5. **Performance Considerations**: Different optimization strategies for each language

Each implementation showcases the strengths and idiomatic patterns of its respective language and paradigm, making it an excellent learning resource for understanding programming language differences and design patterns. 