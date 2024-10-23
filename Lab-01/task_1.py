numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

idx = numbers.index(None)  # Index of missed value
lst = numbers[:idx] + numbers[idx+1:]   # List without missed value
numbers[idx] = sum(lst) / len(numbers)  # Calc average and replace missed value

print("Измененный список:", numbers)
