import numpy as np
#Mexican Hat Net

R1=3
R2=8
C1=0.4
C2=-0.3
tmax=10
# creating a Xnew by adding extra zeroes
X=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
Xnew=[0]*R2+X+[0]*R2
print("Input: ",np.array(Xnew))
# creating a weight vector
w1=[C2]*(R2-R1)
w2=[C1]*(2*R1+1)
w3=[C2]*(R2-R1)
w=np.array(w1+w2+w3)
print("Weights: ",w)
ans=[0]*len(X)
# sliding Window Technique
for i in range(0,len(X)):
    Xnew=list(Xnew)
    ans[i]=round(np.dot(w,np.array(Xnew[i:i+len(w)])),2)

print("Output: ",ans)
# print([-0.15,0.04 , 0.33, 0.51, 0.58 , 0.51 , 0.33 , 0.04 ,-0.15])