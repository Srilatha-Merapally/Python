Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2 + 2
4
2 * 3
6
6% 2
0
2 /4
0.5
4 /3
1.3333333333333333
 5 %4
 
SyntaxError: unexpected indent
5 %4
1
print('heelo' + 'hi')
heelohi
print('heelo' + ''+'hi')
heelohi
print('heelo' +''+'hi')
heelohi
print('heelo' + '' +'hi')
heelohi
print('heelo' +' ' +'hi')
heelo hi
print('heelo' + ' ' +'hi')
heelo hi
print('heelo' + ' '   +'hi')
heelo hi
print('heelo' + ' '+'hi')
heelo hi
print('heelo' +   ' '+'hi')
heelo hi
print('heelo' ++'hi')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print('heelo' ++'hi')
TypeError: bad operand type for unary +: 'str'
print('heelo' '+' 'hi')
heelo+hi
print('heelo'+'' 'hi')
heelohi
print('heelo'+''+ 'hi')
heelohi
print('hi'+ ' ' 'ithika')
hi ithika
print('hi'+ ' ''ithika')
hi ithika
print('hi'+ 'Ithika')
hiIthika
print('hi'? 'ithika')
SyntaxError: invalid syntax
print('hi'+ 'Ithika')
hiIthika
print('hi' +'ithika')
hiithika
print('hi' + 'ithiak')
hiithiak
print('hi'+ '' 'ithika')
hiithika
print('hi' + '' 'ithiuka')
hiithiuka
print('hi' + '' 'ithiak')
hiithiak
print('hi' + ' ' 'ithika')
hi ithika
print('hi' + ' '' ' 'ithika')
hi  ithika
print('ithi' + ' ' 'how are you')
ithi how are you
print('hello ' *2)
hello hello 
print('hello' *3)
hellohellohello
print('hello' ' ' *3)
hello hello hello 
print('hello' ' '' ' *3)
hello  hello  hello  
a='amma'
b='nana'
print(a+b)
ammanana
print(a+ ' ' b)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(a + ' ' b)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(a + ' ' +b)
amma nana
print(a " '' +b)
      
SyntaxError: incomplete input
a=10age=10
      
SyntaxError: invalid decimal literal
age = 10
      
print (age + 5)
      
15
type(1)
      
<class 'int'>
type('1')
      
<class 'str'>
type(0.01)
      
<class 'float'>
type(true)
      
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
type(0)
      
<class 'int'>
a = 1
      
type(a)
      
<class 'int'>
a = '1'
      
print('your age is:' +a)
      
your age is:1
a='1'
      
type(a)
      
<class 'str'>
age = '1'
      
print('your age' +age)
      
your age1
age = '12'
      
print('your age' +age)
      
your age12
age=12
      
print('ur agr'+age)
      
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print('ur agr'+age)
TypeError: can only concatenate str (not "int") to str
age = 12
      
type(age)
      
<class 'int'>
 age = '12'
      
SyntaxError: unexpected indent
type(age)
      
<class 'int'>
age = 12
      
type(age)
      
<class 'int'>
age = '12'
      
type(age)
      
<class 'str'>
age = 22
      
str(age)
      
'22'
print('your age is:+age)
      
SyntaxError: incomplete input
print('your age is:'+age)
      
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    print('your age is:'+age)
TypeError: can only concatenate str (not "int") to str
print('your age is:'+str(age))
      
your age is:22
a=1
      
a==1
      
True
a==2
      
False
a==3
      
False
a==1
      
True
a=5
      
b=6
      
if a<b
      
SyntaxError: incomplete input
if a<b:
      print('a is lessthan b)
            
SyntaxError: incomplete input
if a<b:
      print('a is lessthan b')

            
a is lessthan b
if a>b
            
SyntaxError: incomplete input
if a>b:
            print('b is greater than a)
...                   
SyntaxError: incomplete input
>>> if a>b:
...             print('b is greater than a')
... 
...                   
>>> a= 20
...                   
>>> b=10
...                   
>>> if a< b:
...                   print('a is lessthan b')
...                   else:
...                       
SyntaxError: invalid syntax
>>> else:
...     
SyntaxError: invalid syntax
>>> a= 20
>>> b =10
>>> if a < b:
...     print('ais less than b')
... else:
...     print('b is greater than a')
... 
...     
b is greater than a
>>> input()
hi
'hi'
>>> input('please enter your name')
please enter your namesrilatha
'srilatha'
>>> a_name=input('enter your name')
enter your namesri
>>> if name='sri'
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> if a_name='sri'
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> print('hi')
hi
