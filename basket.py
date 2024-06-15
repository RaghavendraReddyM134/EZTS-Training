def subarr(n,k,arr):
    curr_score=0
    for i in range(0,n-1):
        for j in range(1,k):
            max_score=j*arr[i]+(j+1)*arr[i+1]
            if max_score>curr_score:
                curr_score=max_score
    return curr_score
n=int(input())
k=int(input())
arr= list(map(int, input().split()))


print(subarr(n,k,arr))


