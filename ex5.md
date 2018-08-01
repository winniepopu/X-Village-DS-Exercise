# Question 1 Python的some_list.sort()跟sorted(some_list)差別在哪?
Answer :
ex:list=[]
- sorted(list) 不會直接影響原list,而是產生新的已排序好的list
- list.sort() 會直接改變原本的list，將原本list排序好，不用另外花時間建構一個新的序列回傳。

# Question 2 Python的sorted()是用哪種排序演算法?¶
Answer:
Timsort 融合Natural Merge Sort 和Insertion Sort 兩種排序演算法。
個數少用就是Insertion Sort；個數多則用Natural Merge Sort，其概念是「在現實情況中，大部分的序列裡面會藏有部分早就排序好的小片段，由於這些小片段不需要再花時間排序，所以抓出這些小片段就可以減少排序的時間」