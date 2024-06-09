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
