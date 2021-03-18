def non_repeat_substring(str1):
    win_start = 0
    alpha_index = {}
    max_length = 0
    for win_end in range(len(str1)):
        right_char = str1[win_end]
        #update the start_pointer
        if right_char in alpha_index:
            win_start = max(win_start,alpha_index[right_char]+1)
            #win_start = alpha_index[right_char]+1 ?
        #insert the current char INDEX into the dict
        alpha_index[right_char] = win_end
        max_length = max(max_length,win_end-win_start+1)
    return max_length

print(non_repeat_substring("cde"))