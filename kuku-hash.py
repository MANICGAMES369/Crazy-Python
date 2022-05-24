#KUKU HASH
#CRASHES WITH LARGE FILES
#SLOW SLOW

import os
import hashlib
from pickle import FALSE

l_db=[] #file list
hash_db=[]
b=0

def database(location):
    a=[]
    try:
        a=os.scandir(location)
    except FileNotFoundError:
        print("Invalid Directory!")
        return -1
    b=0
    x=0
    #make file database
    for i in a:
        if os.path.isfile(location+i.name):
            l_db.insert(b,location+i.name)
            b=b+1
    print("Completed generated file database")
        
    #make hash file database
    for i in l_db:
        t=open(i,"rb")
        if t:
           stream=t.read()
           hash_db.insert(x,hashlib.sha256(stream).hexdigest())
           print(l_db[x],"->>",hash_db[x])
           x=x+1
           t.close()
        else:
            print("error")
    print("Completed generated hash database")
        
           
def init():
    s=input("Directory:>")
    if database(s) == -1:
        return -1
    
    while True:
        cmd=input(">")
        if(cmd=="gen"):
             s=input("Directory:>")
             if database(s) == -1:
                return -1
             
        
            
#inilialized file database
init()


            
  



  
    
    
    
    
