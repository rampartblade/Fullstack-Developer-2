#1
x = 0
y = 5

if x < y:
    print('yes x < y')

if x > y:
    print('yes x > y')

if x:
    print('x')

if y:
    print('y')

#2
weather = 'nice'

if weather == 'nice':
    print('Mow the lawn')
    print('Weed the garden')
print('Take a dog for a walk')

#3
if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
print('After conditional')

#4
x = 20

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

#5
buku = 20000
majalah = 5000
uang = 5000

if uang >= buku:
    print('beli buku')
elif uang >= majalah:
    print('beli majalah')
else:
    print('uang tidak cukup')

#6
if 'f' in 'foo': print('1'); print('2'); print('3')
        
#7
raining = False
print("Let's go to the", 'beach' if not raining else 'library')

#8
n = 5
while n > 0:
    n -= 1
    print(n)

#9
i = 1
while i < 6:
  print(i)
  i += 1

#10
n = 5
while n > 0:
    n-= 1
    if n == 2 :
        break
    print(n)
print('Loop ended.')

#11
n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')

#12
a = ['foo', 'bar', 'baz']
for i in a:
    print(i)

#13
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

for k in d:
    print(d[k])

#14
for n in (0, 1, 2, 3, 4):
    print(n)

#15
for i in ['foo', 'bar', 'baz', 'qux']:
  if i == 'baz':
    break
  print(i)
else:
  print('Done.') 