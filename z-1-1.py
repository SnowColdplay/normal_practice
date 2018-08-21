
"先发者的收益"
def first(A,start,end):
    if start==end:
        return A[start]
    else:
        return max(A[start]+last(A,start+1,end),A[end]+last(A,start,end-1))

"后发者的收益"
"作为后者者，收益是总的减去先发者的，先发者肯定会留一个小值给他"
"后发者，在start+1,end上先发，先发者肯定会让 后发者是先发时，收益小"
def last(A,start,end):
    if start==end:
        return 0
    else:
        return min(first(A,start+1,end),first(A,start,end-1))

def count(A):
    return max(first(A,0,len(A)-1),last(A,0,len(A)-1))

result=count([1,2,3,10])
print(result)

def dptwo(A):
    dpfirst=[[0 for _ in range(len(A))] for _ in range(len(A))]
    dplast=[[0 for _ in range(len(A))] for _ in range(len(A))]
    for end in range(len(A)):
        for start in range(end,-1,-1):
            if start==end:
                dpfirst[start][end]=A[start]
            else:
                dpfirst[start][end] = max(A[start] + dplast[start + 1][end], A[end] + dplast[start][end - 1])
                dplast[start][end] =min(dpfirst[start + 1][end],dpfirst[start][end -1])
    return max(dpfirst[0][-1],dplast[0][-1])

result=dptwo([1,2,3,10])
print(result)




