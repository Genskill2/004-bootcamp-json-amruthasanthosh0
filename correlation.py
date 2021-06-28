import json
import math

# Add the functions in this file

def load_journal(name):
    f = open(name,'r')
    data =f.read()
    f.close()
    pdata= json.loads(data)
    return pdata

def compute_phi(name, event):
    data= load_journal(name)
    n11=n10=n01=n00=n1x=n0x=nx0=nx1=0
    for i in data:
        if event in i['events']:
            n1x +=1
            if i['squirrel']:
                n11 +=1
                nx1 +=1
            else:
                n10 +=1
                nx0 +=1
        else:
            n0x +=1
            if i['squirrel']:
                n01 +=1
                nx1 +=1
            else:
                n00 +=1
                nx0 +=1
    return (n11 * n00 - n10 * n01) / math.sqrt(n1x * n0x * nx1 * nx0)

def compute_correlations(name):
    data = load_journal(name)
    result = {}
    for i in data:
        for e in i['events']:
            if e not in result.keys():
                result[e]=compute_phi(name,e)
    return result

def diagnose(name):
    result = compute_correlations(name)
    values=sorted(result.values())
    p=n=''
    for k,v in result.items():
        if v == values[0]:
            n=k
        if v == values[-1]:
                p=k
    return [p,n]
