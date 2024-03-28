def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print("Step", i+1, ":", arr)
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print("Step", i+1, ":", arr)
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print("Step", i, ":", arr)
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        print("Merging:", arr)
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print("Pivot:", pivot)
    print("Left:", left)
    print("Middle:", middle)
    print("Right:", right)
    return quick_sort(left) + middle + quick_sort(right)

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        print("Step", n-i, ":", arr)

    return arr

def counting_sort(arr):
    max_val = max(arr)
    counts = [0] * (max_val + 1)
    for num in arr:
        counts[num] += 1
    sorted_arr = []
    for i in range(max_val + 1):
        sorted_arr.extend([i] * counts[i])
    print("Sorted Array:", sorted_arr)
    return sorted_arr

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(n):
        arr[i] = output[i]
    print("Sorted Array:", arr)

def print_menu():
    print("================================================")
    print("Array:", arr)
    print("[1] Bubble Sort")
    print("[2] Selection Sort")
    print("[3] Insertion Sort")
    print("[4] Merge Sort")
    print("[5] Quick Sort")
    print("[6] Heap Sort")
    print("[7] Counting Sort")
    print("[8] Radix Sort")
    print("[9] Exit")

def main():
    global arr
    arr = [7, 23, 1, 0, 29, 2, 23, 24]
    while True:
        print_menu()
        choice = int(input("Enter your choice: "))
        print("================================================")
        if choice == 1:
            print("Sorted Array:", bubble_sort(arr[:]))
        elif choice == 2:
            print("Sorted Array:", selection_sort(arr[:]))
        elif choice == 3:
            print("Sorted Array:", insertion_sort(arr[:]))
        elif choice == 4:
            print("Sorted Array:", merge_sort(arr[:]))
        elif choice == 5:
            print("Sorted Array:", quick_sort(arr[:]))
        elif choice == 6:
            print("Sorted Array:", heap_sort(arr[:]))
        elif choice == 7:
            print("Sorted Array:", counting_sort(arr[:]))
        elif choice == 8:
            print("Sorted Array:", radix_sort(arr[:]))
        elif choice == 9:
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
