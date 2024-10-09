def read_numbers(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()]
    return numbers

def add(numbers):
    return sum(numbers)

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def write_results(file_path, addition_result, multiplication_result):
    with open(file_path, 'w') as file:
        file.write(f"Addition Result: {addition_result}\n")
        file.write(f"Multiplication Result: {multiplication_result}\n")

def main():
    numbers = read_numbers('data/numbers.txt')
    addition_result = add(numbers)
    multiplication_result = multiply(numbers)
    write_results('data/results.txt', addition_result, multiplication_result)
    print("Results written to results.txt")

if __name__ == "__main__":
    main()
