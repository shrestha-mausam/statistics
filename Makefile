# Makefile for Statistics Calculator Programs

# Compiler settings
CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -O2

# OCaml compiler
OCAMLC = ocamlc

# Python interpreter
PYTHON = python3

# Default target
all: statistics_c statistics_ocaml statistics_python

# C program (Procedural)
statistics_c: statistics.c
	$(CC) $(CFLAGS) -o statistics_c statistics.c

# OCaml program (Functional)
statistics_ocaml: statistics.ml
	$(OCAMLC) -o statistics_ocaml statistics.ml

# Python program (Object-Oriented)
statistics_python: statistics.py
	chmod +x statistics.py

# Run all programs
run: all
	@echo ""
	@echo "=================================================="
	@echo "              STATISTICS CALCULATOR"
	@echo "=================================================="
	@echo ""
	@echo "Running C program (Procedural):"
	@echo "================================"
	./statistics_c
	@echo ""
	@echo ""
	@echo "Running OCaml program (Functional):"
	@echo "==================================="
	./statistics_ocaml
	@echo ""
	@echo ""
	@echo "Running Python program (Object-Oriented):"
	@echo "========================================="
	$(PYTHON) statistics.py
	@echo ""

# Run individual programs
run_c: statistics_c
	./statistics_c

run_ocaml: statistics_ocaml
	./statistics_ocaml

run_python: statistics_python
	$(PYTHON) statistics.py

# Clean up compiled files
clean:
	rm -f statistics_c statistics_ocaml *.cmi *.cmo *.o

# Install dependencies (for systems that need them)
install_deps:
	@echo "Installing dependencies..."
	@echo "For C: gcc should be installed"
	@echo "For OCaml: ocamlc should be installed"
	@echo "For Python: python3 should be installed"
	@echo ""
	@echo "On macOS with Homebrew:"
	@echo "  brew install gcc ocaml"
	@echo ""
	@echo "On Ubuntu/Debian:"
	@echo "  sudo apt-get install gcc ocaml python3"
	@echo ""
	@echo "On CentOS/RHEL:"
	@echo "  sudo yum install gcc ocaml python3"

# Help target
help:
	@echo "Available targets:"
	@echo "  all          - Compile all programs"
	@echo "  run          - Compile and run all programs"
	@echo "  run_c        - Compile and run C program"
	@echo "  run_ocaml    - Compile and run OCaml program"
	@echo "  run_python   - Run Python program"
	@echo "  clean        - Remove compiled files"
	@echo "  install_deps - Show dependency installation instructions"
	@echo "  help         - Show this help message"

.PHONY: all run run_c run_ocaml run_python clean install_deps help 