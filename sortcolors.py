class colors(object):
    def __init__(self, data = None, c= None):
        self.data = data
        self.c = c
    # 0 1 111 222 000 111
    # 0000 (red )1111111 222(blue)
    #The idea is to sweep all 0s to the left and all 2s to the right, then all 1s are left in the middle.
    # Two pointers: red and blue.
#     Complexity:
# O(n) time
# O(1) space

# When swap nums[i] and nums[blue], back i one step since we don't know what is old nums[blue] value, 
# we need to check it again. However, when swap nums[i] and nums[red], 
# we don't need to check it since nums[red] is 0 or 1, which is checked before.
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red = 0

        blue = len(nums) - 1
        i = 0
        while i <= blue:
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                red += 1
            elif nums[i] == 2:
                nums[i], nums[blue] = nums[blue] , nums[i]
                blue -= 1
                # 换过来的数 从后面来的，并不能确定他的值，需要blue 向前一步
                i -= 1
            i += 1 
            
        
#         //sort k colors, extend by sort 3 colors
#TIME: O(KN)
# class Solution{
# public:
#     /**
#      * @param colors: A list of integer
#      * @param k: An integer
#      * @return: nothing
#      */    
#     void sortColors2(vector<int> &colors, int k) {
#         if (colors.size() == 0) return;
#         // write your code here
#         int lowColor = 1, highColor = k;
#         int lpartition = 0, hpartition = colors.size() - 1;
#         while (lowColor < highColor) {
#             for (int i = lpartition; i <= hpartition; ) {
#                 if (colors[i] == lowColor) {
#                     swap(colors[i], colors[lpartition]); lpartition++; i++;
#                 } else if (colors[i] == highColor) {
#                     swap(colors[i], colors[hpartition]); hpartition--;
#                 } else {
#                     i++;
#                 }
#             }
#             lowColor++; highColor--;
#         }
#     }
# };
        