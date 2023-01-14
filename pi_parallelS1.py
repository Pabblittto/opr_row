#!/usr/bin/env python
import sys
import pymp as p
import datetime
from mpi4py import MPI

#mpirun -np 2 python3 -m mpi4py pi_parallel.py


count=1000000

   

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank == 0:
    
    e= datetime.datetime.now()
    for x in range(size):
        comm.send(count/(size-1)*x,dest=x)
    values = []
    for x in range(size):
        value = (comm.recv(source=x))
        values.append(value)
    
    sum=(0)
    for x in values:
        sum= (sum)+(x)
    print(sum/(size-1))
    f=datetime.datetime.now()
    print("PI is: \n3.14159265358979323846264338327950288419716939937510582097494")    
    print ("Czas rownolegly : " + str((f-e).total_seconds()*1000) + "ms\n")
else:
    insidecount=comm.recv(source=0)
    i=1
    sum=p.shared.array((1,), dtype='float')
    parel=1
    
    with p.Parallel(parel) as pa:
        for x in pa.range(int(insidecount), int(insidecount+count/(size-1))):
            val=2*i
            if i!=1:
                insideSum=((val)
                /(val-1)*(val)
                /(val+1)*(insideSum))
            else :
                insideSum=((val)
                /(val-1)*(val)
                /(val+1))
            i+=1
        sum[0]+= insideSum*2
        
    comm.send(sum[0]/parel,dest=0)


