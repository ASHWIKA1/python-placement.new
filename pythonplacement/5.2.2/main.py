def sort_array(array):
    array.sort()

def store_elements(n):
    array = []
    print(f"Enter {n} elements:")
    elements = input().split()
    for i in range(n):
        array.append(int(elements[i]))
    return array

size = int(input("Enter the size of the array: "))
array = store_elements(size)

sort_array(array)

print("Sorted array in ascending order:")
for element in array:
    print(element, end=" ")
