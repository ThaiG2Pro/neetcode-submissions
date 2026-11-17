class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s): 
            return ""
        
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
            
        window = {} # Sổ nháp của cửa sổ
        
        have = 0
        need = len(countT) 
        
        res = [-1, -1]
        resLen = float("infinity")
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            # 1. R nuốt chữ cái vào cửa sổ
            window[c] = window.get(c, 0) + 1
            
            # 2. Cập nhật tiến độ: Nếu chữ vừa nuốt là chữ cần thiết và vừa đạt đủ số lượng
            if c in countT and window[c] == countT[c]:
                have += 1
                
            # 3. Khi ĐÃ GOM ĐỦ (have == need) -> Bắt đầu VẮT KIỆT độ dài
            while have == need:
                # Cập nhật kỷ lục nếu tìm được cửa sổ ngắn hơn
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # Bắt đầu ép đuôi L lên để loại bỏ chữ cái thừa
                left_char = s[l]
                window[left_char] -= 1
                
                # Cực kỳ quan trọng: Nếu lỡ nhả mất một chữ cái quan trọng khiến nó rớt chuẩn
                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1 # Trạng thái gom đủ bị phá vỡ!
                    
                l += 1 # Đuôi L chính thức thu hẹp
                
        # Trích xuất chuỗi kết quả dựa trên tọa độ đã lưu
        l, r = res
        return s[l: r+1] if resLen != float("infinity") else ""