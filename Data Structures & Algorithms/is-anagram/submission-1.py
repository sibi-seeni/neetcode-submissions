class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}
        for items in s.lower():
            count1[items] = count1.get(items, 0) + 1
        for items in t.lower():
            count2[items] = count2.get(items, 0) + 1
        if count1 == count2:
            return True
        else:
            return False