class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        tracker = defaultdict(int)
        for char in s1:
            tracker[char] +=1
        l = 0
        print(tracker)
        while l < len(s2):
            if s2[l] in tracker:
                copy_tracker = tracker.copy()
                pointer = l
                dec = copy_tracker[s2[pointer]] - 1
                while pointer < len(s2) and dec >= 0:
                    # print(s2[pointer])
                    #print(dec)
                    # print(copy_tracker)
                    if dec == 0:
                        del copy_tracker[s2[pointer]]
                    else:
                        copy_tracker[s2[pointer]] -=1
                    if len(copy_tracker) == 0:
                        return True
                    pointer += 1
                    if pointer == len(s2):
                        break
                    dec = copy_tracker[s2[pointer]] - 1
            l += 1

        return False