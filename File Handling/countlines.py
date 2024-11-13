counter=0
f=open("calculator.txt","r")
r=f.read()
f.close()
n=r.split("\n")
for i in n:
    if i:
        counter+=1

print(counter)