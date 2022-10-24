def max_sub_array_of_size_k(k,arr):
    best_sum = 0
    moving_sum = 0
    pt_front = 0
    for i in range(len(arr)):
        if i > k - 1:
            moving_sum -= arr[pt_front]
            pt_front += 1
        moving_sum += arr[i]
        best_sum = max(best_sum,moving_sum)
    return best_sum

print(max_sub_array_of_size_k(3,[1,2,3,4,5,6]))
