class Solution:
    def maxArea(self, height):
        # Initialize two pointers at the extreme ends
        left = 0
        right = len(height) - 1
        max_area = 0
        
        # Loop until the pointers meet
        while left < right:
            # 1. Height is limited by the shorter bar
            current_height = min(height[left], height[right])
            
            # 2. Width is the number of bars strictly between them
            current_width = right - left - 1
            
            # 3. Calculate current area and update max_area if it's larger
            current_area = current_height * current_width
            max_area = max(max_area, current_area)
            
            # 4. Move the pointer pointing to the shorter bar
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area