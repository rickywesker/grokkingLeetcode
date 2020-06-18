#brute force
def find_average_of_subarray(K,arr):
    result = []
    for i in range(len(arr) - K + 1):
        _sum = 0.0
        for j in range(i,i+K):
            _sum += arr[j]
        result.append(_sum/K)
    return result

#sliding window
def find_avg_slidingVer(K,arr):
    result = []
    _sum = 0.0
    front = 0
    for i in range(len(arr)):
        _sum += arr[i]
        if i >= K - 1:
            result.append(_sum/K)
            _sum -= arr[front]
            front += 1
    return result

def main():
    K = 5
    result = find_average_of_subarray(K,[1,3,2,6,-1,4,1,8,2])
    result_2 = find_avg_slidingVer(K,[1,3,2,6,-1,4,1,8,2])
    print(f"Average of subarray of size {K}: " + str(result))
    print(f"Average of subarray of size {K}: " + str(result_2))
main()
