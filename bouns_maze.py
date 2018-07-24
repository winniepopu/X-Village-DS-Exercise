from lib.stack import Stack

def base_converter (dec, base):
    binary=''
    s=Stack()

    while dec!=0:
        if base>16 or base<2: //若base輸入值不符合範圍，輸出error
            return "error"

        tmp=dec%base
        dec=dec//base
        
        if tmp >=10:
            d=tmp%10            
            tmp =chr(65+d)
        s.push(tmp)
    
    while s.size()!=0:
        a=s.pop()
        binary+=str(a)
    return binary

a=input("enter the number : ")
a=int(a)
base=input("enter the base : ")
base=int(base)

print("in base =",base,": ",base_converter(a, base))

# print(base_converter(1000, 16))  # 回傳 3E8
# print(base_converter(700, 12))   # 回傳 4A4