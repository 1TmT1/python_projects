def main():
    arr = [2, 7, 1, 5, 3]
    for x in range(len(arr)):
        if arr[x] == min(arr):
            mini = arr[x]
            last = arr[len(arr) - 1]
            arr[len(arr) - 1] = mini
            arr[x] = last
    print(arr)
    print(len(arr))


if __name__ == '__main__':
    main()
