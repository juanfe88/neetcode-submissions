class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tracker = defaultdict(int)
        left , right = 0, 0
        res = 0
        def max_freq(dic):
            if len(tracker)>0:
                return max(dic.values())
            return 0
        while right<len(s):
            tracker[s[right]] += 1
            length = right-left + 1
            most_frequent = max_freq(tracker)
            while length - most_frequent > k and left <= right:
                tracker[s[left]] -= 1
                left +=1
                length = right-left + 1
                most_frequent = max_freq(tracker)
            right += 1
            res = max(res,length)
        return res 
