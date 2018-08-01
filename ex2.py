from lib.queue import Queue


def hot_potato(name_list, num):
    q = Queue()
    for name in name_list:
        q.enqueue(name)
       
    while q.size()>1:
        for j in range(num):
            person=q.dequeue()
            q.enqueue(person)
        q.dequeue()
    
    remaining_person=q.dequeue()


    
    return remaining_person

print(hot_potato(["Susan","Brad","Kent","David"], 6))               # 回傳 "Brad"
print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"], 7)) # 回傳 "Susan"