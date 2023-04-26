
import pandas
import matplotlib.pyplot as plt

def mdiv(a,b):
    if b!=0:
        return a/b
    else:
        return int(0)

f = open("results.out", "r")
l1=[]
for i in f.readlines():
    l1.append(i)
i=0

result=dict({})
while (i<len(l1)):
    a=l1[i]
    b=l1[i+1].split()
    c=l1[i+2].split()
    p=l1[i+3].split()
    q=l1[i+4].split()
    r=l1[i+5].split()
    s=l1[i+6].split()
    t=l1[i+7].split()

    # print(a.split("-")[-5])
    if a.split()[3].split(".xz")[0] in result.keys():
     
        result[a.split()[3].split(".xz")[0]][a.split("-")[-5]]={"IPC":float(b[4]),"L1D PREFETCH ACCESS" : mdiv(int(c[7]),int(c[3])),"L1D PREFETCH  REQUESTED":mdiv(int(p[7]),int(p[3])),"L2C PREFETCH  ACCESS":mdiv(int(q[7]),int(q[3])),"L2C PREFETCH  REQUESTED":mdiv(int(r[7]),int(r[3])),"LLC PREFETCH  ACCESS": mdiv(int(s[7]),int(s[3])),"LLC PREFETCH  REQUESTED":mdiv(int(t[7]),int(t[3]))}
    else:
   
        result[a.split()[3].split(".xz")[0]]=dict({a.split("-")[-5]:{"IPC":float(b[4]),"L1D PREFETCH ACCESS" : mdiv(int(c[7]),int(c[3])),"L1D PREFETCH  REQUESTED":mdiv(int(p[7]),int(p[3])),"L2C PREFETCH  ACCESS":mdiv(int(q[7]),int(q[3])),"L2C PREFETCH  REQUESTED":mdiv(int(r[7]),int(r[3])),"LLC PREFETCH  ACCESS": mdiv(int(s[7]),int(s[3])),"LLC PREFETCH  REQUESTED":mdiv(int(t[7]),int(t[3]))}})
    i+=8
    

print(result)
for i in result.keys():
    data = pandas.DataFrame(result[i])
    # print(data)
    # data.rename(columns={"ipcp_b":"Riscy"},inplace=True)
    # print(data)
    

    ax = data.plot(y=["ipcp_b","ipcp_o"], kind="bar",linewidth=1)
    ax.figure.savefig(f'{i}.png')

    
    # plot.savefig(f"{i}.jpg")
    
