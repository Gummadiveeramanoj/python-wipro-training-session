import time
import math
from multiprocessing import Pool, cpu_count

numbers = [50000, 60000, 55000, 45000, 70000]

def calculate_factorial(n):
    return math.factorial(n)

def main():
    # -----------------------------
    # Sequential Execution
    # -----------------------------
    start_time = time.time()
    sequential_results = [calculate_factorial(n) for n in numbers]
    sequential_time = time.time() - start_time
    print(f"Sequential Time: {sequential_time:.2f} seconds")

    # -----------------------------
    # Multiprocessing Execution
    # -----------------------------
    start_time = time.time()
    with Pool(cpu_count()) as pool:
        parallel_results = pool.map(calculate_factorial, numbers)
    parallel_time = time.time() - start_time
    print(f"Multiprocessing Time: {parallel_time:.2f} seconds")

    # -----------------------------
    # Display Results (SAFE)
    # -----------------------------
    for num in numbers:
        print(f"Factorial of {num} calculated successfully")

if __name__ == "__main__":
    main()
