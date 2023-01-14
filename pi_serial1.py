
import datetime


size=1000000
sum=1
i=1
e= datetime.datetime.now()
for x in range(size):
    val=2*i
    sum=((val)
    /(val-1)*(val)
    /(val+1)*(sum))
    
    i+=1
print (sum*2)
f=datetime.datetime.now()

print("Czas szeregowy : " + str((f-e).total_seconds()*1000)+"ms\n")
