def validate_input(arr):
    return isinstance(arr, list)

def linear_search_modular(arr, target):
    if not validate_input(arr):
        return -1
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def main():
    arr = list(map(int, input("Enter the list of numbers (space-separated): ").split()))
    target = int(input("Enter the number to search: "))
    result = linear_search_modular(arr, target)
    if result != -1:
        print("Element found at index:", result)
    else:
        print("Element not found.")

if __name__ == "__main__":
    main()
