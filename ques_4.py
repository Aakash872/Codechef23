# def decimalToBinary(n):
#     return bin(n).replace("0b","")


# def binaryToDecimal(n):
#     return int(n,2)
 
# print(decimalToBinary(7))

T=int(input())
for i in range(T):
    ANS=[]
    N=int(input())
    OR=list(map(int,input().split()))
    AND=list(map(int,input().split()))
    for j in range(len(OR)):
         ANS.append(OR[j]^AND[j])
    for m in ANS:
        print(m)