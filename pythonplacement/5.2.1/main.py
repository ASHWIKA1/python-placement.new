def remove_duplicates(array):
    unique_elements = []
    for element in array:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

def store_elements(n):
    array = []
    print(f"Input {n} elements in an array:")
    elements = input().split()
    for i in range(n):
        array.append(int(elements[i]))
    return array

size = int(input("Enter the array size: "))
array = store_elements(size)

unique_elements = remove_duplicates(array)

print("The unique elements found in the array are:")
for element in unique_elements:
    print(element, end=" ")
