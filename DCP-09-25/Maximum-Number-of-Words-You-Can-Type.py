class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c = 0
        new_text = text.split()
        for word in new_text:
            flag = False
            for brokenletter in brokenLetters:
                if brokenletter in word:
                    flag = True
            if flag == False: c+=1
        return c

