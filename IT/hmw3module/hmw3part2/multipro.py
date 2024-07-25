from multiprocessing import Pool, cpu_count

def factorize_single(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize(*numbers):
    with Pool(cpu_count()) as pool:
        result = pool.map(factorize_single, numbers)
    return result

if __name__ == "__main__":
    import time

    numbers = [128, 255, 99999, 10651060]
    start_time = time.time()
    a, b, c, d = factorize(*numbers)
    end_time = time.time()

    print(f"Factors of {numbers[0]}: {a}")
    print(f"Factors of {numbers[1]}: {b}")
    print(f"Factors of {numbers[2]}: {c}")
    print(f"Factors of {numbers[3]}: {d}")
    print(f"Time taken with multiprocessing: {end_time - start_time} seconds")