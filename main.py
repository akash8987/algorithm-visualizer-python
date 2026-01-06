def bubble_sort_steps(data):
    steps = []
    arr = data.copy()

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append(arr.copy())
    return steps


def run():
    data = [5, 3, 8, 4, 2]
    steps = bubble_sort_steps(data)

    for step in steps:
        pass


if __name__ == "__main__":
    run()
