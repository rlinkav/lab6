list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
set1=set(list1)
set2=set(list2)
result=set1-set2
print(*result)