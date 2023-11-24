def get_fibonacci_sequence(length):
    if length <= 0:
        return "Invalid input. Please provide a positive integer."
    
    fibonacci_sequence = [1] if length == 1 else [1, 1] if length == 2 else [0, 1]

    while len(fibonacci_sequence) < length:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

    return fibonacci_sequence