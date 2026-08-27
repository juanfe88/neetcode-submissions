class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        look_up_map = {}
        for char in t:
            count = look_up_map.get(char,0) + 1
            look_up_map[char] = count
        res = float('inf')
        l,r = 0,0
        tracker = {}
        resps = {}
        have,need = 0, len(look_up_map)
        # def check():
        #     for k,v in look_up_map.items():
        #         if tracker.get(k,0)< v:
        #             return False
        #     return True
        while r < len(s):
            count = tracker.get(s[r],0) + 1
            tracker[s[r]] = count
            if s[r] in look_up_map and count == look_up_map[s[r]]:
                have += 1
            while have == need:
                current_lenght = r - l + 1
                res = min(res,current_lenght)
                if current_lenght==res:
                    resps[res] = l
                tracker[s[l]] -= 1
                if s[l] in look_up_map and tracker[s[l]] < look_up_map[s[l]]:
                    have -= 1
                l += 1
            r +=1
        if resps:
            lb = resps[res]
            rb = lb + res  
            return s[lb:rb]  
        else: return ""
                
