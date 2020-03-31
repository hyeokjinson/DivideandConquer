def quad_tree(x,y,n):
    global matrix,n1,n2,n3
    number=matrix[x][y]
    double_break=False
    for i in range(x,x+n):
        if double_break:
            break
        for j in range(y,y+n):
            if matrix[i][j]!=number:
                for a in range(3):
                    for b in range(3):

                        quad_tree(x+n//3*a,y+n//3*b,n//3)
                return

    if number==-1:
        n1+=1
    elif number==0:
        n2+=1
    else:
        n3+=1
n=int(input())
matrix=[list(map(int,input().split()))for _ in range(n)]
n1=0
n2=0
n3=0
quad_tree(0,0,n)
print(n1)
print(n2)
print(n3)