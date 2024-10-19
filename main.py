def summation():
    n=int(input())
    lst1,lst2=[],[]
    for x in range(n):lst1.append(int(input()))
    for y in range(n):lst2.append(int(input()))
    updated_list=[lst1[i]+lst2[i] for i in range(n)]
    return updated_list
result=summation()
print(result)
def find_min_max():
    result.sort()
    result_min_max=result[0],result[(len(result))-1]
    return result_min_max
result1=find_min_max()
print(result1)
