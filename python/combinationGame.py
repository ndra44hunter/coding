# import dependencies
import math
import sys

""" fungsi kombinasi string """
def rules(cntr,string,dummy):
    cntr[-1]+=1
    try:
        if cntr[-1]>(len(string)-1):
            cntr[-1]=0
            cntr[-2]+=1
        for i in reversed([x for x in range(len(cntr)-1)]):
            if cntr[i]>(len(string)-1):
                cntr[i] = 0
                cntr[i-1]+=1
        dummy+=" "
        return cntr,dummy
    except:
        dummy+=" "
        return cntr,dummy


def combinations(times,string):
    rumusDalam=int(len(string)**(math.ceil((times/2))))
    rumusLuar=int(len(string)**(times//2))

    counters=[0 for _ in range(times)]
    
    arr=[[] for _ in range(rumusLuar)]
    for i in range(rumusLuar):
        arr2=[None for _ in range(rumusDalam)]
        dummy=""
        for j in range(rumusDalam):
            # print(counters)
            arr2[j]=counters.copy()
            dummy+="".join([string[x] for x in counters])
            # print([string[x] for x in counters])
            # counters,dummy=rules(counters,string,dummy).copy()
            hasil = rules(counters,string,dummy)
            counters= hasil[0].copy()
            dummy=hasil[1]
        # arr[i]=arr2
        arr[i]=dummy
    
    return arr
  
isLanjut=False

string=input("masukkan string ")
while not isLanjut:
    try:
        times=int(input("masukkan pangkat "))
        isLanjut=True
    except ValueError:
        print("please input number...")
        
print("Hasil\n")
for x in combinations(times,string):
    print(x)
    
print()


# schematics
""" 
E^1
[
    [0 1 2]
]

E^2
[
    [00 01 02],
    [10 11 12],
    [20 21 22]
]

E^3
[
    [xxx xxx xxx xxx xxx xxx xxx xxx xxx],
    [xxx xxx xxx xxx xxx xxx xxx xxx xxx],
    [xxx xxx xxx xxx xxx xxx xxx xxx xxx]
]

E^4
[
    [xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx]
    [xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx]
    [xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx]
    [xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx]
    [xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx]
    [xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx]
    [xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx]
    [xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx]
    [xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx]
]

....
"""