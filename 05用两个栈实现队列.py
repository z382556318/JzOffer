class Solution:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    def push(self,node):
        self.stack1.append(node)

if __name__ == '__main__':
    s = Solution()
    s.push(1)
    s.push(2)
    s.push(3)
    # print(s.stack1,s.stack2,bool(s.stack2))
    print(s.pop())
    print(s.pop())