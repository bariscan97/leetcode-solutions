class TextEditor:

    def __init__(self):
        self.stack,self.cursor="",0
    def addText(self, text: str) -> None:
        self.stack=self.stack[:self.cursor]+text+self.stack[self.cursor:]
        self.cursor+=len(text)
    def deleteText(self, k: int) -> int:
        if k>self.cursor:
            ex=self.cursor
            self.stack=self.stack[self.cursor:]  
            self.cursor=0
            return ex
        else:
            self.stack=self.stack[:self.cursor-k]+self.stack[self.cursor:]  
            self.cursor-=k
            return k
    def cursorLeft(self, k: int) -> str:
        if k>self.cursor:
            self.cursor=0
            return ""
        else:
            if self.cursor-k<0:self.cursor=0
            else:self.cursor-=k
            if self.cursor<10:return self.stack[:self.cursor]
            else:return self.stack[self.cursor-10:self.cursor]

    def cursorRight(self, k: int) -> str:
        
        if len(self.stack)<self.cursor+k:self.cursor=len(self.stack)
        else:self.cursor+=k
        if self.cursor<10:return self.stack[:self.cursor]
        else:return self.stack[self.cursor-10:self.cursor]

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)