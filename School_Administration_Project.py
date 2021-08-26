import csv

def write_into_csv(std_info):
    with open ('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell()==0 :
            writer.writerow(["Unique ID","Name","Age","Year","Semester","Mobile No.","Email ID"])
        writer.writerow(std_info)
if __name__=='__main__':
    condition = True
    
    while condition:
        flag = 0
        val = input("Enter student details in (UID, Name, Age, Year, Sem, MobileNumber, EmailID) format : ")
        std_details = val.split(", ")
        if (len(std_details[5])== 10 and (int(std_details[2]) >10 and int(std_details[2])<100) and std_details[6].islower()):    
            print("The student details are :")
            print("UID :" +std_details[0]
                +"\nName: "+ std_details[1]
                +"\nAge: " + std_details[2]
                +"\nYear: " + std_details[3]
                +"\nSem: " + std_details[4]
                +"\nMobile Number: " + std_details[5]
                +"\nEmailID: " + std_details[6])
            var = input("Please  review and confirm the information entered by entering c and incase of error entering e : ")
            if var == "c":
                write_into_csv(std_details)   
            elif var == "e":
                flag = 1
        else:
            flag = 1
        if(flag == 1):
            print("Check and reenter the student details")
        if(flag == 0):
            val = input("Enter y to continue entering details for other students: ")
            if val == "y":
                condition = True
            else:
                condition = False

     
       
   
     
      