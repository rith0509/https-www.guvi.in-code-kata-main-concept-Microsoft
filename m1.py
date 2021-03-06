n,k=input().split()
if(k<n):
  nn,nn1=[],[]
  for i in range(0,int(n)):
      x=input()
      nn.insert(i,x)
  [nn1.append(i) for i in nn if i not in nn1]
  nn1.sort()
  print(int(nn1[int(k)-1]))
else:
  print("-1")
