from InsertionSort import insertion_sort_descending;

# Test cases
test_cases = [
    [12, 11, 13, 5, 6],
    [3, 1, 4, 1, 5, 9],
    [10, -2, 33, 5, 5, 0],
    [1, 2, 3, 4, 5],
    [50, 40, 30, 20, 10]
]

# Running each test case and printing the results
for i, test_case in enumerate(test_cases, 1):
    insertion_sort_descending(test_case)
    print(f"Sorted array for test case {i} in decreasing order:", test_case)
