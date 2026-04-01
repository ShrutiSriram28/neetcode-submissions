class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # # Not O(n)
        # l = 0
        # r = l + k - 1
        # max_ele = [max(nums[l:r + 1])]
        # l += 1
        # r += 1
        # while r < len(nums):
        #     if nums[l - 1] == max_ele[l - 1]:
        #         max_ele.append(max(nums[l: r + 1]))
        #     else:
        #         max_ele.append(max(max_ele[l - 1], nums[r]))
        #     l += 1
        #     r += 1

        # return max_ele

        # # O(n)
        q = []
        max_nums = []
        l = 0
        r = 0

        for r in range(len(nums)):
            while len(q) != 0 and nums[r] >= nums[q[-1]]:
                q.pop(-1)
            q.append(r)

            if l > q[0]:
                q.pop(0)
            
            if r + 1 >= k:
                max_nums.append(nums[q[0]])
                l += 1
            
        return max_nums 