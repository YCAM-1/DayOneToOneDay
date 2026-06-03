class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
nums = list(map(int, input(" Nhap day so vao di, cach nhau bang space nhe: ").split()))
target = int(input("Ban muon tong la bao nhieu: "))
s = Solution()
result = s.twoSum(nums, target)
print(result)