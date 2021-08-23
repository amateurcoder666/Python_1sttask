#pattern_1
for i in range(0,5):
    for j in range(0,5-i):
        print(" ",end = "")
    for k in range(0,i):
        print("*",end= " ")
    print("\r")
#loops
import random
dict1 = {"Y": "Yes/Continue", "N" :  "Discontinue"}
print(dict1)
val = input("Do u want to generate random numbers between 1 to 100? ")
if val == "Y":
   while True:
     for i in range(0,10):
        print(random.randint(1,100))
     var = input("if you want to continue generating enter 'Y': ")
     if (var == "Y"):
         continue
     else:
         break
#dict_functions
mydict = {"Physics":"77","Chemistry":"79","Maths":"77","Comp Science":"95","Student":{"Name": "Kaustav Das","Age": "19",}}
student_dict = mydict.copy()
print(student_dict)
full_marks = ("Physics","Chemistry","Maths")
marks = 100
marks_dict = dict.fromkeys (full_marks,marks)
print(marks_dict)
print(mydict.get("Student"))
print(marks_dict.items())
print(mydict.keys())
mydict.pop("Physics")
print(mydict)
marks_dict.update({"English":"100"})
print(marks_dict)
marks_dict.popitem()
print(marks_dict)
print(marks_dict.setdefault("English","Not Needed"))
print(marks_dict)
print(mydict.values())
marks_dict.clear()
print(marks_dict)       