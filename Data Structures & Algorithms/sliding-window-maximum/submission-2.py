class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # l = 0
        # r = l + k - 1
        # maxnum = []
        # maxnum.append(max(nums[l:r + 1]))
        # l += 1
        # r += 1
        # while r < len(nums):
        #     if nums[l - 1] != maxnum[l - 1]:
        #         maxnum.append(max(maxnum[l - 1], nums[r]))
        #     else:
        #         maxnum.append(max(nums[l:r + 1]))
        #     l += 1
        #     r += 1
        # return maxnum

        q = collections.deque()
        l = r = 0
        maxnum = []

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
        
            if q[0] < l:
                q.popleft()

            if r + 1 >= k:
                maxnum.append(nums[q[0]]) 
                l += 1
            r += 1
        
        return maxnum