print("Enter numbers and type 'Stop' to stop entering")
list=[]
flg = 0
while True:
    var = input("Your command please : ")
    if (var == "Stop"):
        break
    list.append(int(var))
print("The positive numbers are :-")
for i in list:
    if(i>=0):
     print(i)
     flg = 1
if (flg == 0):
    print("No positive number entered")

     
       
