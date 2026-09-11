from queue import Queue

class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        openBracket, closeBracket = ['(', '{', '['] , [')', '}', ']']
        index = 0
        while(index < len(s)):
            if(s[index] in openBracket):
                queue.append(s[index])
            elif(s[index] in closeBracket):
                try:
                    prev = queue.pop()
                except:
                    return(False)
                if((prev == '(' and s[index] != ')') or (prev == '{' and s[index] != '}') or (prev == '[' and s[index] != ']')):
                    return False
            index += 1
        return(len(queue) == 0)
        

        