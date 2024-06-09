def display_array(array):
    print("Array elements are:")
    for element in array:
        print(element)

def insert_element(array, element, index):
    array.insert(index, element)

def delete_element(array, index):
    del array[index]

def store_elements(n):
    array = []
    print(f"Enter {n} numbers:")
    for i in range(n):
        element = float(input(f"Number {i + 1}: "))
        array.append(element)
    return array

def manipulate_array(n, operations):
    array = store_elements(n)
    display_array(array)

    for operation in operations:
        if operation[0] == 'i':
            insert_element(array, operation[1], operation[2])
        elif operation[0] == 'd':
            delete_element(array, operation[1])
        display_array(array)

n = int(input("How many numbers do you want to store in the array? "))
operations = []
num_operations = int(input("How many operations do you want to perform? "))

for i in range(num_operations):
    operation = input("Enter operation (i for insert, d for delete), index, and element separated by spaces: ").split()
    operations.append((operation[0], int(operation[1]), float(operation[2])))

manipulate_array(n, operations)
