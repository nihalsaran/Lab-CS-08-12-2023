import time
import random

# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Fibonacci Search
def fibonacci_search(arr, target):
    fib_m2, fib_m1 = 0, 1
    fib_m = fib_m2 + fib_m1

    while fib_m < len(arr):
        fib_m2, fib_m1 = fib_m1, fib_m
        fib_m = fib_m2 + fib_m1

    offset = -1

    while fib_m > 1:
        i = min(offset + fib_m2, len(arr) - 1)

        if arr[i] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif arr[i] > target:
            fib_m = fib_m2
            fib_m1 -= fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i

    if fib_m1 and offset + 1 < len(arr) and arr[offset + 1] == target:
        return offset + 1

    return -1

# Interpolation Search
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        pos = low + (target - arr[low]) * (high - low) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Function to generate a random array
def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]  # You can adjust the range as needed

# Function to get a random index from an array
def get_random_index(array):
    return random.randint(0, len(array) - 1)

# Function to sort an array
def sort_array(arr):
    return sorted(arr)

def main():
    while True:
        range_input = input("Enter the range for the array: ")
        if range_input.isdigit():
            range_size = int(range_input)
            break
        else:
            print("Please enter a valid integer.")

    data = generate_random_array(range_size)
    sorted_data = sort_array(data)

    random_index = get_random_index(sorted_data)
    target_value = sorted_data[random_index]

    print(f"Randomly generated array: {data}")
    print(f"Sorted array: {sorted_data}")
    print(f"Randomly selected index: {random_index}")
    print(f"Target value: {target_value}")

    # Measure execution time for Linear Search on sorted array
    linear_search_start = time.time_ns()
    linear_search(sorted_data, target_value)
    linear_search_end = time.time_ns()
    linear_search_time = linear_search_end - linear_search_start
    print(f"Linear Search Time on Sorted Array: {linear_search_time} nanoseconds")

    # Measure execution time for Binary Search on sorted array
    binary_search_start = time.time_ns()
    binary_search(sorted_data, target_value)
    binary_search_end = time.time_ns()
    binary_search_time = binary_search_end - binary_search_start
    print(f"Binary Search Time on Sorted Array: {binary_search_time} nanoseconds")

    # Measure execution time for Fibonacci Search on sorted array
    fibonacci_search_start = time.time_ns()
    fibonacci_search(sorted_data, target_value)
    fibonacci_search_end = time.time_ns()
    fibonacci_search_time = fibonacci_search_end - fibonacci_search_start
    print(f"Fibonacci Search Time on Sorted Array: {fibonacci_search_time} nanoseconds")

    # Measure execution time for Interpolation Search on sorted array
    interpolation_search_start = time.time_ns()
    interpolation_search(sorted_data, target_value)
    interpolation_search_end = time.time_ns()
    interpolation_search_time = interpolation_search_end - interpolation_search_start
    print(f"Interpolation Search Time on Sorted Array: {interpolation_search_time} nanoseconds")

if __name__ == "__main__":
    main()
