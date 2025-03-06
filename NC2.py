#define a class named solution 
class Solution:
    #declare a function that takes a string 's' as input and returns a boolean
    def isValid(self, s: str) -> bool:
        #loop to check if brackets are in string 
        while any(pair in s for pair in ["()", "[]", "{}"]):
            #iterate through the valid bracket pairs
            for pair in ["()","[]","{}"]:
                #remove the first occurence of each bracket
                s = s.replace(pair,"")

        return s == ""