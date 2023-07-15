#!/usr/bin/env python
# coding: utf-8

# Q-1 Explain class and object with respect to object oriented programming .Give a suitable example.

# CLASS-Class is used as a template for declaring and creating the object.
#     OBJECT-Object is an intance of class

# In[5]:


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("Neha Rana",20)
print(p1.name)
print(p1.age)


# Q-2 Name the four pillars of oops.

# In[6]:


'''
Four pillars of oops
1- inheritance
2-encapsulation
3-abstraction
4-polymorphism
               '''


# Q-3 Explain why the  __init__ () function is used .Give a suitable exapmle.

# In[11]:


# The __init__() function  is a spacial method that is automatically called when an object is created from a class .It is used to initialize the attribute of a class and perform any necessory setup operation
class person2:
    def __init__(self,name,age,num):
        self.name=name
        self.age=age
        self.num=num
p2=person2("Neha Rana",20,8394098673)
print(p2.name)
print(p2.age)
print(p2.num)


# Q-4 Why self is used in oops?

# In[8]:


'''
self parameter used for current instance of class and is used to access variable that belongs to the class.
It does not have to be named self you can call whatever you like but it has to be first parameter of any function in class.
'''


# Q-5 What is inharitance ? Give an example for each type of inheritance.

# #Inharitance is the capacity of a class to obtain or inharit properties from another class and then use them when required

# In[18]:


# single inheritance
 
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")
 
# Derived class
 
class Child(Parent):
    def func2(self):
        print("This function is in child class.")
 
 
# Driver's code
object = Child()
object.func1()
object.func2()


# In[19]:


#multiple inharitance
#Base class 1
class Mother:
    mothername=""
    
    def mother (self):
        print(self.mothername)
        
# Base class2


class Father:
    fathername=""
    
    def father(self):
        print(self.fathername)
        
#Derived class 

class son(Mother,Father):
    def parent(self):
        print("Father:",self.fathername)
        print("Mother:",self.mothername)
        
#Deriver's code
s1=son()
s1.fathername="RAM"
s1.mothername="SITA"
s1.parent()


# In[ ]:




