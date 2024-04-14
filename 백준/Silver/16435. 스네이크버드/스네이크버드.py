N , L = map(int,input().split())   

arr = list(map(int,input().split())) 
arr.sort()                           
for _ in arr:                      
    if _ <= L:                     
        L += 1                    
print(L)                           