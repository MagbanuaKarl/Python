def linear_search(arr, target):
    print("Performing Linear Search...")
    for i in range(len(arr)):
        print(f"Checking index {i}: {arr[i]}")
        if arr[i] == target:
            return i  # return the index where the target is found
    return -1  # return -1 if the target is not found in the array

def binary_search(arr, target):
    print("Performing Binary Search...")
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        print(f"Checking index {mid}: {arr[mid]}")
        if arr[mid] == target:
            return mid  # return the index where the target is found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # return -1 if the target is not found in the array

def search_menu():
    print("=================================================")
    print("Search Algorithms:")
    print("[1] Linear Search")
    print("[2] Binary Search")
    print("[3] Exit")

def search(arr, target, choice):
    if choice == 1:
        return linear_search(arr, target)
    elif choice == 2:
        return binary_search(arr, target)
    else:
        return -1  # Exit option

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    search_menu()
    choice = int(input("Enter your choice: "))
    print("=================================================")
    if choice == 3:
        print("Exiting...")
        break
    target = int(input("Enter the target value to search: "))
    result = search(arr, target, choice)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print("Element not found")
