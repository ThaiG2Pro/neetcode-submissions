class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        
        for num in nums_set:
            # Chỉ bắt đầu đếm nếu num là điểm khởi đầu của chuỗi
            if num - 1 not in nums_set:
                current_num = num
                current_len = 1
                
                # Đếm tiến lên
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_len += 1
                    
                max_len = max(max_len, current_len)
                
        return max_len