class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for img in image:
            img.reverse()
        
        for img in image:
            for j in range(len(img)):
                if img[j]==1:
                    img[j]=0
                else:
                    img[j]=1
        return image
