#解二元一次方程式
#ax2 + bx + c = 0, where
#a, b and c are real numbers and
#a ≠ 0

import cmath

print('ax**2+bx+c=0')
a=float(input('a='))
if a == 0:
    print('a不能=0')
else:
    b=float(input('b='))
    c=float(input('c='))
d=print(cmath.sqrt(b**2-4*a*c))
x1 = (-b-cmath.sqrt(b**2-4*a*c))/(2*a)
x2 = (-b+cmath.sqrt(b**2-4*a*c))/(2*a)
print(f'the answer x is {x1} or {x2}')
