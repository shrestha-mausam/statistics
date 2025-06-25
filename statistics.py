#!/usr/bin/env python3
"""
Statistics Calculator in Python - Object-Oriented Approach
"""

from collections import Counter
from typing import List


def calculate_mean(data: List[int]) -> float:
    """
    Calculate the mean (average) of the data.
    
    Args:
        data: List of integers
        
    Returns:
        The mean of the data, or 0.0 if data is empty
    """
    if not data:
        return 0.0
    return sum(data) / len(data)


def calculate_median(data: List[int]) -> float:
    """
    Calculate the median of the data.
    
    Args:
        data: List of integers
        
    Returns:
        The median of the data, or 0.0 if data is empty
    """
    if not data:
        return 0.0
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    if n % 2 == 0:
        # Even number of elements - average of two middle elements
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2.0
    else:
        # Odd number of elements - middle element
        return float(sorted_data[n // 2])


def calculate_mode(data: List[int]) -> List[int]:
    """
    Calculate the mode(s) of the data.
    
    Args:
        data: List of integers
        
    Returns:
        List of modes (most frequently occurring values)
    """
    if not data:
        return []
    
    counter = Counter(data)
    max_frequency = max(counter.values())
    
    # Find all values with maximum frequency
    modes = [value for value, freq in counter.items() if freq == max_frequency]
    
    # If all values occur equally, return empty list (no mode)
    if len(modes) == len(counter):
        return []
    
    return sorted(modes)


def read_integers_from_input() -> List[int]:
    """
    Read integers from user input separated by spaces.
    
    Returns:
        List of integers entered by the user
    """
    try:
        user_input = input("Enter a list of integers separated by spaces: ")
        # Split by spaces and convert to integers, filtering out invalid inputs
        integers = []
        for word in user_input.split():
            try:
                integers.append(int(word.strip()))
            except ValueError:
                # Skip invalid integers
                continue
        return integers
    except (EOFError, KeyboardInterrupt):
        return []


def main():
    """Main function to demonstrate the statistics calculations."""
    print("=== Statistics Calculator (Python - Object-Oriented) ===\n")
    
    # Read data from user input
    data = read_integers_from_input()
    
    if not data:
        print("No valid integers entered.")
        return
    
    print(f"Input data: {data}")
    print()
    
    # Calculate and display statistics
    mean = calculate_mean(data)
    print(f"Mean: {mean:.2f}")
    
    median = calculate_median(data)
    print(f"Median: {median:.2f}")
    
    modes = calculate_mode(data)
    if modes:
        print(f"Mode: {modes}")
    else:
        print("Mode: No mode (all values occur equally)")


if __name__ == "__main__":
    main() 