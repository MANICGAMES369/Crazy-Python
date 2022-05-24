#use case: help me find the location of a function or variable within a library
#author darkhorse369
#music: down with the sickness

import os

#search for string inside imported libraries
def search_func(search):
    a=0
    #t and arr ar 1:1, keep in the same order
    t=[os]
    arr=["os"]
    size=len(arr)
   
    for i in range(0,size,1):
       name=arr[i]
       content=dir(t[i])
    
       
       for b in content:
           if search==b:
            return name
        
print(search_func("access"))



       
    


 
    
