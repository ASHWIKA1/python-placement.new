def find_largest(array):
    largest = array[0]
    for num in array:
        if num > largest:
            largest = num
    return largest

def find_smallest(array):
    smallest = array[0]
    for num in array:
        if num < smallest:
            smallest = num
    return smallest

def display_array(array):
    print("Array elements are:")
    for element in array:
        print(element)

def store_elements(n):
    array = []
    print(f"Enter {n} numbers:")
    for i in range(n):
        element = float(input(f"Number {i + 1}: "))
        array.append(element)
    return array

n = int(input("How many numbers do you want to store in the array? "))
array = store_elements(n)
display_array(array)

largest = find_largest(array)
smallest = find_smallest(array)

print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")
