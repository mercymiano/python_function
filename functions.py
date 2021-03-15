
#creating a function
def my_function():
    print("Today is wensday")
#calling a function   
my_function()

#functions as arguments
def sum(x,y,z):
    a=x+y+z
    print("The sum is",a)
sum(10,20,40)
sum(501,958,1)

def product(x,y):
    a=x*y
    print("The product is",a)
product(10,20)
#using return
def sum(x,y):
     a=x+y
     return a
print(sum(2,4))
 
 #*agrs
def courses(*args):
     for subject in args:
         print(subject) 
courses ("big data","ccna","oops")

def Tel(*stations):
    for subject in stations:
        return subject
print(Tel("ntv","citizen","ktn","k24"))

 #*key 
def courses(**kwargs):
     for key,value in kwargs.items():
       print("{}:{}".format(key,value))
courses(first='Big data',second='ccna',third='HCIA')
 
 
 #default parameter value
def kenya(county = "momabasa"):
     print("I am from"+ county)

kenya()
kenya("Nairobi")
kenya("Kiambu")
kenya("Nyeri")

 #passing a list as an argument
def my_function(food):
     for x in food:
         print(x)
fruits =["apple","banana","cherry"] 
my_function(fruits)
 #passing a dictornary as an argument
car = {"brand": "Ford","model": "Mustang","year" : 1964}
my_function(car)

  #Area of a circle
def Area(i,r):
     x=i*r*r
     return x
print(Area(3.142,7))
 #Area of a rectangel
def Area(l):
     x=l*l
     return x
print(Area(7))
