def secondLargest(arr):
    if not arr:
        return None

    count = 0
    max, preMax = arr[0], -1

    for i in range(1, len(arr)):
        if arr[i] >= max:
            preMax = max
            max = arr[i]
        else:
            if arr[i] > preMax:
                preMax = arr[i]

    return preMax

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    print(secondLargest(arr))