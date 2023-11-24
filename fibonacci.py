def get_fibonacci_sequence(length):
    deret = [1, 1]
    for _ in range(2, length):
        deret.append(deret[-1] + deret[-2])
    return deret