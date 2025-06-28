class LinearSearch:
    def __init__(self, data):
        self.data = data

    def find(self, target):
        for i, val in enumerate(self.data):
            if val == target:
                return i
        return -1

def main():
    data = list(map(int, input("Enter the list of numbers (space-separated): ").split()))
    target = int(input("Enter the number to search: "))
    searcher = LinearSearch(data)
    result = searcher.find(target)
    if result != -1:
        print("Element found at index:", result)
    else:
        print("Element not found.")

if __name__ == "__main__":
    main()
