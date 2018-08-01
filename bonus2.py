## MinHeap實作

class MinHeap:
    def __init__(self):
        self.node=[0]
        self.size=0
    
    # build a new heap from a list of keys
    def build_heap(self, keys):

        self.size=len(keys)+1
        for num in keys:             #intialize
            self.node.append(num)

        for index in range(self.size//2,0,-1):    
            self.min_act(index)
        
    def min_act(self,now_pointer):
        i=now_pointer
        if i <= (self.size-1)//2 :  # 當i是有小孩時

            if i ==(self.size//2) and self.size%2!=0 : #若i只有一個小孩(只可能在最右邊有小孩的index)
                if self.node[2*i]<self.node[i] :  #左小孩比父小時，交換
                    tmp=self.node[i]
                    self.node[i]=self.node[2*i]
                    self.node[2*i]=tmp

                    self.min_act(2*i)      #檢查被交換的值重複動作，直到不能再與小孩互換為止，表示其比兩個小孩都大

            else:               #若i有兩個小孩時
                if self.node[2*i+1]<self.node[i] and self.node[2*i+1]<=self.node[2*i]: #右小孩比父小也比左小孩小時，與父交換
                    tmp=self.node[i]
                    self.node[i]=self.node[2*i+1]
                    self.node[2*i+1]=tmp         
                    self.min_act(2*i+1)   #檢查被交換的值重複動作，直到不能再與小孩互換為止，表示其比兩個小孩都大

                elif self.node[2*i]<self.node[i] and self.node[2*i]<self.node[2*i+1]:  #左小孩比父及右小孩小時，左小孩與父換
                    tmp=self.node[i]
                    self.node[i]=self.node[2*i]
                    self.node[2*i]=tmp
                    self.min_act(2*i)     #檢查被交換的值重複動作，直到不能再與小孩互換為止，表示其比兩個小孩都大    

    # add a new item to the heap
    def insert(self, item):
        self.size=self.size+1
        self.node.append(item)

        for index in range(self.size//2,0,-1):  #開始從最右邊有小孩的index值開始比大小    
            self.min_act(index)


    # return the item with the minimum key value, removing the item from the heap
    def del_min(self):
        min=self.node[1]
        self.node[1]=self.node[self.size-1]
        self.size-=1

        self.node.pop()                         #將最後一個node刪掉
        for index in range(self.size//2,0,-1):  #開始從最右邊有小孩的index值開始比大小      
            self.min_act(index)        
        
        return min
    
    # print the minimum heap on the screen
    def display(self):
        print(self.node[1])
        

heap = MinHeap()

heap.build_heap([9, 5, 6, 2, 3])
heap.display()

heap.insert(1)
heap.insert(7)
heap.display() 

print(heap.del_min())
print(heap.del_min())
heap.display()