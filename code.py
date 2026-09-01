class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d={}
        nums.sort()
        for num in nums:
            if num%2==0 :
                if  num not in d:
                    d[num]=1
                else:
                    d[num]+=1
        if len(d)==0:
            return -1
        minv=0
        for v in d.values():
            minv=max(v,minv)
        for k,v in d.items():
            if v==minv:
                return k



        
