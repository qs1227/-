def bucket_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    bucket_count = len(arr)
    bucket_width = (max_val - min_val) / bucket_count

    buckets = [[] for _ in range(bucket_count)]

    for i in arr:
        index = int((i - min_val) // bucket_width)
        if index == bucket_count:
            index -= 1
        buckets[index].append(i)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    for i in range(len(arr)):
        arr[i] = sorted_arr[i]