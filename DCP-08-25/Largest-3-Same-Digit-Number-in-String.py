class Solution(object):
    def largestGoodInteger(self, num):
        d=['999','888','777','666','555','444','333','222','111','000'] 
        #creating a dictionary of all possible results
        for i in d:
            if i in num:
                #matching them to the a subset from num length 3
                return i
        return ''

            