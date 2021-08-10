var = int(input("Enter the no.of terms in fibonacci series : "))
print("The fibonacci series you wanteed is :-")
if(var == 1):
    print("0.")
elif(var == 2):
    print( "0,1.")
else:
    print("0,1,",end="")
    a = 0
    b = 1
    for i in range(var-2):
         c =  a + b
         if (i!= var-3):
           print (c,end= ",")
         else:
           print(c,end= ".")
         a = b
         b = c 