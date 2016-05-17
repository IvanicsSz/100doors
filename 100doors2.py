
def change(state):
    if state==1: return 0
    if state==0: return 1


doors=[0]*101
start=1
stop=len(doors)
print (len(doors))
print (range(len(doors)))
k=0
for i in range(start,stop):
    #print (i,end=" ")

    for j in range(start,stop):

        if (j%i==0):
            doors[j]=change(doors[j])
        k+=1

for i in range(len(doors)):
    if doors[i]==1:
        print (i, end=" ")

#print (k)
