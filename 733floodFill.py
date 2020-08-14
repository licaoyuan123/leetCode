class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor=image[sr][sc]
        if newColor==oldColor:
            return image
        self.dfs(image, sr, sc, oldColor, newColor)
        return image
        
    def dfs(self, image, x, y, oldColor, newColor):


        if x<0 or y<0 or x>len(image)-1 or y>len(image[0])-1 or image[x][y]!=oldColor:
            return
        image[x][y]=newColor
        self.dfs(image, x-1, y, oldColor, newColor)
        self.dfs(image, x+1, y, oldColor, newColor)
        self.dfs(image, x, y-1, oldColor, newColor)
        self.dfs(image, x, y+1, oldColor, newColor)
        

        
#Below is scanline solution, use stack instead of recursion
#if the image is very large, there may too many level of recursion
#         oldColor= image[sr][sc]
#         if oldColor==newColor:
#             return image
        
#         stack=[(sr, sc)]
#         height=len(image)
#         length=len(image[0])
#         while stack:
#             x, y=stack.pop()
            
#             #To the left most position
#             while y>=0 and image[x][y]==oldColor:
#                 y-=1
#             y+=1
#             above, below =False, False
#             while y<length and image[x][y]==oldColor:
#                 image[x][y]=newColor
#                 if x>0:
#                     if not above and image[x-1][y]==oldColor:
#                         stack.append((x-1, y))
#                         above=True
#                     elif above and image[x-1][y]!=oldColor:
#                         above=False
#                 if x<height-1:
#                     if not below and image[x+1][y]==oldColor:
#                         stack.append((x+1, y))
#                         below=True
#                     elif below and image[x+1][y]!=oldColor:
#                         below=False
#                 y+=1
#         return image
            
        
        
