class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        stack = [[image[sr][sc],sr,sc]]
        base = stack[0][0]
        while stack != []:
            temp = stack.pop()
            image[temp[1]][temp[2]] = color
            if temp[1]-1>=0 and image[temp[1]-1][temp[2]] == base and image[temp[1]-1][temp[2]] != color:
                stack.append([image[temp[1]-1][temp[2]],temp[1]-1,temp[2]])
            if temp[1]+1<len(image) and image[temp[1]+1][temp[2]] == base and image[temp[1]+1][temp[2]] != color:
                stack.append([image[temp[1]+1][temp[2]],temp[1]+1,temp[2]])
            if temp[2]-1>=0 and image[temp[1]][temp[2]-1] == base and image[temp[1]][temp[2]-1] != color:
                stack.append([image[temp[1]][temp[2]-1],temp[1],temp[2]-1])
            if temp[2]+1<len(image[0]) and image[temp[1]][temp[2]+1] == base and image[temp[1]][temp[2]+1] != color:
                stack.append([image[temp[1]][temp[2]+1],temp[1],temp[2]+1])    
        return image
