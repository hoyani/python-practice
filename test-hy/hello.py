
'''
a = int(input('정수입력:'))

if a % 2 ==0:
    print('짝수에요')
else :
    print('홀수에요')

for i in range(5):    
    for j in range(5):
        print('*', end='')
    print('')
        

print(list(range(5,11,2)))
print('hi', end='\t')
print('eg', end='')
print('be', end='')



i=0
for x in [1,4,23,'ts', 3]:
    print(x,end=' ')
    i+=1
print('\n',i,'번 반복')
    
'''
for a in range(2,10):
    for b in range(1,10):
        x = a * b
        print("{} x {} = {}".format(a,b,x))
    print("-" * 10)