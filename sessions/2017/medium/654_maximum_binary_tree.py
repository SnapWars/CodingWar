class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if len(nums) == 0:
            return None

        _max = max(nums)
        index = nums.index(_max)

        root = TreeNode(_max)
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])

        return root
