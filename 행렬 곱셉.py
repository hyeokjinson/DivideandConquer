n,m=map(int,input().split())
arr1=[list(map(int,input().split()))for _ in range(n)]
m,k=map(int,input().split())
arr2=[list(map(int,input().split()))for _ in range(m)]

ans=[]

for i in range(len(arr1)):
    for j in range(len(arr2[0])):
        result=0
        for t in range(len(arr1[0])):
            result+=arr1[i][t]*arr2[t][j]
        ans.append(result)


cnt=0
for i in ans:
    print(i, end=' ')
    cnt+=1
    if cnt==k:
        print()
        cnt=0
