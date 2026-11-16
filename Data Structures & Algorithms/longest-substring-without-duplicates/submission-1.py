class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        bucket = set()
        result = 0
        
        for r in range(len(s)):
            # Nếu ký tự s[r] đã có trong bucket, thu hẹp cửa sổ từ bên trái
            while s[r] in bucket:
                bucket.remove(s[l])
                l += 1
            
            # Thêm ký tự hiện tại vào cửa sổ
            bucket.add(s[r])
            
            # Cập nhật độ dài lớn nhất
            result = max(result, r - l + 1)
            
        return result