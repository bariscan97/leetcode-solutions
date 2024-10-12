class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        arr = [[-j,i] for i, j in Counter(barcodes).items()]
        heapify(arr)
        res = []
        while arr:
            A = []
            for _ in range(2):
                if not arr :
                    break
                cnt, barcode = heappop(arr)
                A.append([cnt + 1, barcode])
                res.append(barcode)
            for cnt, barcode in A:
                if cnt:
                    heappush(arr, [cnt , barcode])
        return res