class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Khởi tạo
        bucket = {} # Sổ đếm tần suất
        freq = [[] for _ in range(len(nums) + 1)] # Dàn rổ, index = tần suất
        
        # 2. Đếm tần suất (Code cũ của bạn chuẩn rồi)
        for i in range(len(nums)):
            bucket[nums[i]] = bucket.get(nums[i], 0) + 1
            
        # 3. Phân phối vào rổ
        # Duyệt qua các cặp (con số, tần suất) trong sổ
        for num, count in bucket.items():
            # Mở cái rổ ở index "count", ném "num" vào trong
            freq[count].append(num)
            
        # 4. Thu hoạch từ rổ to nhất về rổ nhỏ nhất
        result = []
        # Đi lùi từ index lớn nhất (len(nums)) về 1
        for i in range(len(freq) - 1, 0, -1):
            # Trong rổ freq[i] có thể chứa nhiều số, nhặt từng số ra
            for num in freq[i]:
                result.append(num)
                # Đủ K phần tử thì lập tức trả về kết quả
                if len(result) == k:
                    return result
                    
        return result