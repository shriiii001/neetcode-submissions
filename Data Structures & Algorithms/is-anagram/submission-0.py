class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table_one = {}
        hash_table_two = {}

        for i in range(len(s)):
            if s[i] not in hash_table_one:
                hash_table_one[s[i]] = 1
            else:
                hash_table_one[s[i]] += 1 
        for i in range(len(t)):
            if t[i] not in hash_table_two:
                hash_table_two[t[i]] = 1
            else:
                hash_table_two[t[i]] += 1 
        if hash_table_one == hash_table_two:
            return True
        
        return False
     


            

        