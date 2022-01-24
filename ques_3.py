N,k=map(int,input().split())
steps=list(map(int,input().split()))
Finish = 0
total_steps=0
while Finish<=N:
    toy=0
    fight=Finish
    for i in steps*10:
        if N-fight>=i:
            fight+=i
            toy+=1
        else:
            continue
    Finish=fight
    total_steps+=toy
    
print(total_steps)


    

