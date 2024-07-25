def factorize(*numbers):
    result = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        result.append(factors)
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
    print(f"Time taken: {end_time - start_time} seconds")






