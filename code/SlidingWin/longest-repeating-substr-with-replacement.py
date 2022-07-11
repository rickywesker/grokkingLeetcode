def longest_repeating_substr_replace(str1,k):
    win_start, max_repeating_cnt = 0 , 0
    freq_dict = {}
    max_length = 0
    #the freq procedure
    for win_end in range(len(str1)):
        right_char = str1[win_end]
        if right_char not in freq_dict:
            freq_dict[right_char] = 0
        freq_dict[right_char] += 1
        max_repeating_cnt = max(max_repeating_cnt,freq_dict[right_char])
    #check the current window 
        if win_end - win_start + 1 - max_repeating_cnt > k: #remaining 可替代的数量
            left_char = str1[win_start]
            freq_dict[left_char] -= 1
            win_start += 1 #shrinking the win ahead

        max_length = max(max_length,win_end - win_start + 1)#直接计算窗口长度作为答案，因为符合要求

    return max_length
def length_of_longest_substring(arr, k):
      # TODO: Write your code here
    win_start, ones_cnt, max_length = 0, 0, 0
    for win_end in range(len(arr)):
        if arr[win_end] == 1:
            ones_cnt += 1


        if win_end - win_start + 1 - ones_cnt > k and arr[win_start] == 1:
            ones_cnt -= 1
        win_start += 1

        max_length = max(max_length,win_end - win_start + 1)

    return max_length
print(longest_repeating_substr_replace("abbcb",0))