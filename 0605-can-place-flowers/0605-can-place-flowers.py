class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        if len(flowerbed)==1:
            if flowerbed[0]==0 and n <= 1 or n==0:
                return True
            return False

        if len(flowerbed)==3:
            if flowerbed[1]==1 and n > 0:
                return False
            if flowerbed[0]==0 or flowerbed[2]==0 and n <= 1:
                return True
            if flowerbed[0]==1 and flowerbed[2]==1 and n > 0:
                return False
            return True

        if flowerbed[0]==0 and flowerbed[1]==0:
            count += 1

        for i in range(2, len(flowerbed)-1, 2):
            if flowerbed[i]==0 and flowerbed[i-1]==flowerbed[i] and flowerbed[i+1]==flowerbed[i]:
                count += 1

            if i == len(flowerbed)-3:
                if flowerbed[i+2]==0 and flowerbed[i+1]==0:
                    count += 1

        if count >= n:
            return True

        count = 0

        for i in range(1, len(flowerbed)-1, 2):
            if flowerbed[i]==0 and flowerbed[i-1]==flowerbed[i] and flowerbed[i+1]==flowerbed[i]:
                count += 1

            if i == len(flowerbed)-3:
                if flowerbed[i+2]==0 and flowerbed[i+1]==0:
                    count += 1

        if count >= n:
            return True

        count = 0

        for i in range(2, len(flowerbed)-1, 2):
            if flowerbed[i]==0 and flowerbed[i-1]==flowerbed[i] and flowerbed[i+1]==flowerbed[i]:
                count += 1

            if i == len(flowerbed)-3:
                if flowerbed[i+2]==0 and flowerbed[i+1]==0:
                    count += 1

        if count >= n:
            return True

        return False