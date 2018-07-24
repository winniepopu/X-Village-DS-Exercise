from lib.stack import Stack

def  dec_to_bin(dec):
    binary=''
    s = Stack()
    while dec!=0:
        tmp=dec%2
        dec=dec//2
        s.push(tmp)


    while s.size()!=0:
        a=s.pop()
        binary+=str(a)
    return binary


a=input("enter the number : ")
a=int(a)
print("in binary : ",dec_to_bin(a))

# dec_to_bin(42)   # 回傳 101010
# dec_to_bin(100)  # 回傳 1100100