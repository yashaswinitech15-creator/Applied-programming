class Solution:
    diff = [0,1,0,-1,0]
    def dfs(self, image: List[List[int]], sr: int, sc: int, R: int, C: int, og: int, newcolor: int) -> None:
        if(image[sr][sc] == newcolor): return None
        image[sr][sc] = newcolor
        for di in range(4):
            adjR,adjC = sr+self.diff[di], sc+self.diff[di+1]
            if(adjR>=0 and adjR<R and adjC>=0 and adjC<C and image[adjR][adjC] == og):
                self.dfs(image,adjR,adjC,R,C,og,newcolor)
        

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R,C = len(image),len(image[0])
        self.dfs(image,sr,sc,R,C,image[sr][sc],color)
        return image