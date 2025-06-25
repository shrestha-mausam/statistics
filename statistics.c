#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to calculate mean of integers
double calculate_mean(int arr[], int size) {
    if (size == 0) return 0.0;
    
    double sum = 0.0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum / size;
}

// Function to compare integers for qsort
int compare_ints(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

// Function to calculate median of integers
double calculate_median(int arr[], int size) {
    if (size == 0) return 0.0;
    
    // Create a copy of the array to sort
    int* sorted_arr = malloc(size * sizeof(int));
    if (sorted_arr == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 0.0;
    }
    
    memcpy(sorted_arr, arr, size * sizeof(int));
    qsort(sorted_arr, size, sizeof(int), compare_ints);
    
    double median;
    if (size % 2 == 0) {
        // Even number of elements - average of two middle elements
        median = (sorted_arr[size/2 - 1] + sorted_arr[size/2]) / 2.0;
    } else {
        // Odd number of elements - middle element
        median = sorted_arr[size/2];
    }
    
    free(sorted_arr);
    return median;
}

// Function to calculate mode of integers
void calculate_mode(int arr[], int size, int* modes, int* mode_count) {
    if (size == 0) {
        *mode_count = 0;
        return;
    }
    
    // Find the range of values
    int min_val = arr[0], max_val = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] < min_val) min_val = arr[i];
        if (arr[i] > max_val) max_val = arr[i];
    }
    
    int range = max_val - min_val + 1;
    int* frequency = calloc(range, sizeof(int));
    if (frequency == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        *mode_count = 0;
        return;
    }
    
    // Count frequency of each value
    for (int i = 0; i < size; i++) {
        frequency[arr[i] - min_val]++;
    }
    
    // Find maximum frequency
    int max_freq = 0;
    for (int i = 0; i < range; i++) {
        if (frequency[i] > max_freq) {
            max_freq = frequency[i];
        }
    }
    
    // Find all values with maximum frequency
    *mode_count = 0;
    for (int i = 0; i < range; i++) {
        if (frequency[i] == max_freq) {
            modes[*mode_count] = i + min_val;
            (*mode_count)++;
        }
    }
    
    // If all values occur equally, return no mode
    if (*mode_count == range) {
        *mode_count = 0;
    }
    
    free(frequency);
}

// Function to print array
void print_array(int arr[], int size) {
    printf("[");
    for (int i = 0; i < size; i++) {
        printf("%d", arr[i]);
        if (i < size - 1) printf(", ");
    }
    printf("]\n");
}

// Function to print modes
void print_modes(int modes[], int mode_count) {
    if (mode_count == 0) {
        printf("No mode (all values occur equally)\n");
        return;
    }
    
    printf("[");
    for (int i = 0; i < mode_count; i++) {
        printf("%d", modes[i]);
        if (i < mode_count - 1) printf(", ");
    }
    printf("]\n");
}

// Function to read integers from user input
int read_integers(int arr[], int max_size) {
    printf("Enter a list of integers separated by spaces: ");
    
    char line[1000];
    if (fgets(line, sizeof(line), stdin) == NULL) {
        return 0;
    }
    
    int count = 0;
    char* token = strtok(line, " \t\n");
    
    while (token != NULL && count < max_size) {
        arr[count] = atoi(token);
        count++;
        token = strtok(NULL, " \t\n");
    }
    
    return count;
}

int main() {
    printf("=== Statistics Calculator (C - Procedural) ===\n\n");
    
    int data[1000]; // Maximum 1000 integers
    int size = read_integers(data, 1000);
    
    if (size == 0) {
        printf("No valid integers entered.\n");
        return 1;
    }
    
    printf("Input data: ");
    print_array(data, size);
    printf("\n");
    
    // Calculate and display statistics
    double mean = calculate_mean(data, size);
    printf("Mean: %.2f\n", mean);
    
    double median = calculate_median(data, size);
    printf("Median: %.2f\n", median);
    
    int modes[100]; // Assuming max 100 different modes
    int mode_count;
    calculate_mode(data, size, modes, &mode_count);
    printf("Mode: ");
    print_modes(modes, mode_count);
    
    return 0;
} 