arr = list(map(int, input("Enter the list of numbers : ").split()))
target = int(input("Enter the number to search: "))

found = False
for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found.")