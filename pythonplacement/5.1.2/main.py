def search_element(array, element):
    for index, value in enumerate(array):
        if value == element:
            return index
    return -1

def display_array(array):
    print("Array elements are:")
    for element in array:
        print(element)

def store_elements(n):
    array = []
    print(f"Enter {n} elements:")
    for i in range(n):
        element = input(f"Element {i + 1}: ")
        array.append(element)
    return array

n = int(input("How many elements do you want to store in the array? "))
array = store_elements(n)
display_array(array)

search_term = input("Enter the element you want to search for: ")
position = search_element(array, search_term)

if position != -1:
    print(f"Element '{search_term}' found at position: {position}")
else:
    print(f"Element '{search_term}' not found in the array.")
