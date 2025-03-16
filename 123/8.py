def count_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    count = [0] * range_val
    output = [0] * len(arr)

    for i in arr:
        count[i - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in arr[::-1]:
        output[count[i - min_val] - 1] = i
        count[i - min_val] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]