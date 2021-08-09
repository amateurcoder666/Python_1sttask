r = (input("Input the radius of the circle : "))
"print(type(r))"
k = 1
s = 0
#using Leibniz's formula
for i in range(1000000):  
     if i % 2 == 0:
        s += 4/k
     else:
        s -= 4/k
     k += 2

area = (s*r**2)
print("The area of the circle with raidus %f " %r ,end ="is %0.15f" %area)


