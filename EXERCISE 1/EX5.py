class Stack:
    def __init__(self):
        self.st = []

    def push(self, el):
        self.st.append(el)

    def pop(self):
        return self.st.pop()

    def isEmpty(self):
        return len(self.st) == 0

    def size(self):
        return len(self.st)

    def top(self):
        return self.st[0]


temp = ''

if __name__ == '__main__':
    st = Stack()
    decNum = int(input("Enter the decimal number: "))
    while decNum != 0:
        st.push(decNum % 2)
        decNum = decNum // 2
    while st.size() != 0:
        temp = temp + str(st.pop())
    print("The binary number: ", temp)
