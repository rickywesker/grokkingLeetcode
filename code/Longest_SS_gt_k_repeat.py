class Solution:

    def longestSubstring(self, s: str, k: int) -> int:
        unique = set()
        for val in s:
            unique.add(val)
        unique_num = len(unique)
        max_list = []
        for u_num in range(1,unique_num+1):
            left_pt = 0
            max_val = 0
            dic_cnt = {}
            for i,val in enumerate(s):
                if val not in dic_cnt:
                    dic_cnt[val] = 0
                dic_cnt[val] += 1
                while(len(dic_cnt.keys()) > u_num):
                    dic_cnt[s[left_pt]] -= 1
                    if dic_cnt[s[left_pt]] == 0:
                        del dic_cnt[s[left_pt]]
                    left_pt += 1

                if min(dic_cnt.values()) >= k:
                    max_val = max(max_val,len(s[left_pt:i+1]))
            max_list.append(max_val)
        return max(max_list) 


s = Solution()
s.longestSubstring('aaabb',3)
