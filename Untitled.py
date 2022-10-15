#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[6]:


a=int(input())
print(a*2)


# In[7]:


a=int(input())
print(a**2)


# In[15]:


def foo(h, m, s):
    hour=h*3600
    min=m*60
    local=hour+min+s
    return local
a = int(input())
b = int(input())
c = int(input())
x=foo(a,b,c)
print(x)
print(x/24/3600)


# In[29]:


a = int(input())
if a%10==7:
    print("TRUE")
else:
    print("FALSE")



# In[40]:


def foo(a,b,c):
    if a==0:
        x1=-c/b
        print(x1)
    else: 
        d=b**2-4*a*c
        if d<0:
            print("НЕТ КОРНЕЙ")
        if d==0:
            x1=-b//(2*a)
            print(x1)
        else :
            x1=(-b+d)**(1/2)/(2*a)
            x2=(-b-d)**(1/2)/(2*a)
            print(x1,x2)  
a = int(input())
b = int(input())
c = int(input())
foo(a, b, c)


# In[ ]:


a=int(input())
b=int(input())
c=int(input())
if a<b:
    print(max(b,c))
else:
    print(max(a,c))


# In[ ]:


a=int(input())
n = 0 
b = 0
for i in range(1, a+1):
    if i%5==0 or i%2==0:
        b+=i
        n+=1
print(float('{:.2f}'.format(b/n)))


# In[ ]:





# In[ ]:




