class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i]))+"#"+strs[i]
        return "".join(strs)
    def decode(self, s: str) -> List[str]:
        result = []
        j = 0 
        while j < len(s):
            # Cử trinh sát i đi tìm dấu "#"
            i = j
            while s[i] != "#":
                i += 1
            
            # Lúc này:
            # - j đang đứng ở chữ số đầu tiên
            # - i đang đứng ngay tại dấu "#"
            # Toàn bộ khoảng s[j:i] CHẮC CHẮN là con số độ dài (dù là 1, 10, hay 999)
            length = int(s[j:i])
            
            # Lấy nội dung chuỗi: bắt đầu từ ngay sau dấu "#" (tức là i+1)
            # Kéo dài thêm một đoạn bằng đúng length
            word = s[i + 1 : i + 1 + length]
            result.append(word)
            
            # Dời j qua khỏi chữ vừa đọc, chuẩn bị vòng lặp mới
            j = i + 1 + length
            
        return result        
