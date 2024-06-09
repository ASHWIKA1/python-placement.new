def calculate_mean(array):
    total_sum = sum(array)
    return total_sum / len(array)

def calculate_variance(array, mean):
    variance = sum((x - mean) ** 2 for x in array) / len(array)
    return variance

def calculate_deviation(variance):
    deviation = variance ** 0.5
    return deviation

def store_elements(n):
    array = []
    print(f"Enter {n} numbers:")
    for i in range(n):
        element = float(input(f"Number {i + 1}: "))
        array.append(element)
    return array

n = int(input("How many numbers do you want to store in the array? "))
array = store_elements(n)

mean = calculate_mean(array)
variance = calculate_variance(array, mean)
deviation = calculate_deviation(variance)

print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Deviation: {deviation}")
