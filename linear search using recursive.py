def linear_search_recursive(arr, target, index=0):
    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    return linear_search_recursive(arr, target, index + 1)

arr = list(map(int, input("Enter the list of numbers (space-separated): ").split()))
target = int(input("Enter the number to search: "))
result = linear_search_recursive(arr, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")
