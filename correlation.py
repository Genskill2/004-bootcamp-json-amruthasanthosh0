import json
import math
# Add the functions in this file
def load_journal(name):
  f=open(name,'r')
  data=f.read()
  f.close()
  parsed=json.loads(data)
  return parsed

def compute_phi(name,event):
  n11=n10=n01=n00=n1x=n0x=nx0=nx1=0
  d=load_journal(name)
  for i in d:
    if event in i['events']:
      n1x += 1
      if i['squirrel']:
        n11 += 1
        nx1 += 1
      else:
        n10 += 1
        nx0 += 1
    else:
      n0x += 1
       if i['squirrel']:
        n10 += 1
        nx0 += 1
      else:
        n00 += 1
        nx0 += 1
   return (n11*n00-n10*n01)/math.sqrt(nx1*nx0*n1x*n10)
def compute_correlations(name):
  result={}
  d=load_journal(name)
  for i in d:
    for j in i['events']:
      if j not in result.keys():
        result[j]=compute_phi(name,j)
  return result
def diagnose(name):
  p=n=''
  result=compute_correlations(name)
  values=sorted(result.values())
  for k,v in result.items():
    if v==values[0]:
      n=k
    if v=values[-1]:
      p=k
  return [p,n]
      
  
  
  
