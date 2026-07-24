class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n-1

        while(i<j):
            # print(s[i]," ",s[j])
            while not s[i].isalnum() and i<j:
                i+=1
            while not s[j].isalnum() and i<j:
                j-=1
            if s[i].lower()!=s[j].lower():
                return False
            
            i+=1
            j-=1
        
        return True