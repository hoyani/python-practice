'''
a = int(input('입력: '))

if a in (10,15,66):
    print('in your pocket')
'''
'''

n = int(input('n까지 : '))

for a in range(1,n+1):
    for b in range (1,n+1):
        print(b,end=' ') 
    a+=n
    print()
'''  
  
'''  
for i in range (0,3):
    
    for j in range (1,4):
        print(3*i+j, end=' ')
    print()
 
print()
print()
 
n=int(input('n까지 할 숫자 입력:'))
a=int(input('증감수 a 입력:'))

for i in range (0,n):
    
    for j in range (1,n+a,a):
        print(n*i+j, end=' ')
    print()


print()
print()


 
for i in range(3):
    for j in range(4):
        print(i, j, '|', end=' ')
    print()


'''  

dan=0
dap=0

for dan in range (2,10):
    for i in range (1,10):
        dap=dan*i
        print(dan, 'x', i, '=', dap, end=' ')
        print()
    print()