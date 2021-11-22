import bisect
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.dic = {}
        for i in range(len(arr)):
            if arr[i] in self.dic:
                self.dic[arr[i]].append(i)
            else:
                self.dic[arr[i]] = [i]
    
    def query(self, left: int, right: int, value: int) -> int:
        if value in self.dic:
            left_ind = bisect.bisect_left(self.dic[value],left)
            right_ind = bisect.bisect_right(self.dic[value],right)
            return right_ind-left_ind
        return 0    

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)