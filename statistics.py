#!/usr/bin/env python3
"""
Statistics Calculator in Python - Object-Oriented Approach
"""

from collections import Counter
from typing import List, Optional


class StatisticsCalculator:
    """
    A class to calculate basic statistics (mean, median, mode) on a list of integers.
    Demonstrates object-oriented programming principles.
    """
    
    def __init__(self, data: Optional[List[int]] = None):
        """
        Initialize the StatisticsCalculator with optional data.
        
        Args:
            data: Optional list of integers to calculate statistics on
        """
        self._data = data if data is not None else []
    
    @property
    def data(self) -> List[int]:
        """Get the current data."""
        return self._data.copy()  # Return a copy to maintain encapsulation
    
    @data.setter
    def data(self, new_data: List[int]):
        """Set new data."""
        self._data = new_data.copy()  # Store a copy to maintain encapsulation
    
    def calculate_mean(self) -> float:
        """
        Calculate the mean (average) of the data.
        
        Returns:
            The mean of the data, or 0.0 if data is empty
        """
        if not self._data:
            return 0.0
        return sum(self._data) / len(self._data)
    
    def calculate_median(self) -> float:
        """
        Calculate the median of the data.
        
        Returns:
            The median of the data, or 0.0 if data is empty
        """
        if not self._data:
            return 0.0
        
        sorted_data = sorted(self._data)
        n = len(sorted_data)
        
        if n % 2 == 0:
            # Even number of elements - average of two middle elements
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            return (mid1 + mid2) / 2.0
        else:
            # Odd number of elements - middle element
            return float(sorted_data[n // 2])
    
    def calculate_mode(self) -> List[int]:
        """
        Calculate the mode(s) of the data.
        
        Returns:
            List of modes (most frequently occurring values)
        """
        if not self._data:
            return []
        
        counter = Counter(self._data)
        max_frequency = max(counter.values())
        
        # Find all values with maximum frequency
        modes = [value for value, freq in counter.items() if freq == max_frequency]
        
        # If all values occur equally, return empty list (no mode)
        if len(modes) == len(counter):
            return []
        
        return sorted(modes)
    
    def print_statistics(self):
        """Print all statistics in a formatted way."""
        if not self._data:
            print("No data available.")
            return
        
        print(f"Input data: {self._data}")
        print()
        print(f"Mean: {self.calculate_mean():.2f}")
        print(f"Median: {self.calculate_median():.2f}")
        
        modes = self.calculate_mode()
        if modes:
            print(f"Mode: {modes}")
        else:
            print("Mode: No mode (all values occur equally)")


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
    """Main function to demonstrate the StatisticsCalculator class."""
    print("=== Statistics Calculator (Python - Object-Oriented) ===\n")
    
    # Read data from user input
    data = read_integers_from_input()
    
    if not data:
        print("No valid integers entered.")
        return
    
    # Create calculator instance with user data
    calculator = StatisticsCalculator(data)
    
    # Display statistics using the class method
    calculator.print_statistics()


if __name__ == "__main__":
    main()  # type: ignore