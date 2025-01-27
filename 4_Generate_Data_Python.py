import random
from random import randint
import datetime


item = []
for i in range(400000001,400050000):
    item.append(str(i))
    
seller = []
for i in range(200000001,200020000): 
    seller.append(str(i))

buyer = []
for i in range(1000000001,1000025000):   
    buyer.append(str(i))
    


#create dates
def dob():
 start_date = datetime.date(1955, 1, 1)
 end_date = datetime.date(2000, 1, 1)

 time_between_dates = end_date - start_date
 days_between_dates = time_between_dates.days
 random_number_of_days = random.randrange(days_between_dates)
 random_date = start_date + datetime.timedelta(days=random_number_of_days)
 return str(random_date)

def start_d():
 start_date1 = datetime.date(1988, 1, 1)
 end_date1 = datetime.date(2023, 10, 13)

 time_between_dates = end_date1 - start_date1
 days_between_dates = time_between_dates.days
 random_number_of_days = random.randrange(days_between_dates)
 random_date1 = start_date1 + datetime.timedelta(days=random_number_of_days)
 return str(random_date1)

def end():
 start_date = datetime.date(1988, 1, 1)
 end_date = datetime.date(2023, 10, 13)

 time_between_dates = end_date - start_date
 days_between_dates = time_between_dates.days
 random_number_of_days = random.randrange(days_between_dates)
 random_start = start_date + datetime.timedelta(days=random_number_of_days)
 
 time_between_dates2 = end_date - random_start
 days_between_dates2 = time_between_dates2.days
 random_number_of_days2 = random.randrange(days_between_dates2)
 random_end = random_start + datetime.timedelta(days=random_number_of_days2)
 
 return str(random_end)


# create data for tables

# create data for E_store Table   
with open("E_store.txt", "w") as f:
        f.write("EStore"+",")
        f.write("www.EStore.com"+",")
        f.write("1 Street City XX 12345"+","+"\n")


# create data for Item Table   
with open("item.txt", "w") as f:
    for i in range(400000001,400050000):
        f.write(str(i)+",")
        f.write("ItemName"+str(i-400000000)+",")
        f.write(str(round(random.uniform(1,500),2))+",")
        f.write("Category"+str(randint(1,99))+",")
        f.write(str(randint(1,20))+","+"\n")
 
     
        
# create data for Employee Table         
with open("employee.txt", "w") as f:
    for i in range(301,650):
        f.write(str(i)+",")
        #f.write(random.choice(random_w_five_digits())+",")
        f.write("FirstLastEmployee"+str(i-300)+",")
        f.write(dob()+",")
        f.write(random_with_N_digits(1)+",")
        f.write(str(randint(24000,155000))+"\n")


# create data for Seller Table   
with open("seller.txt", "w") as f:
    for i in range(200000001,200020000):
        f.write(str(i)+",")
        #f.write(random.choice(random_w_nine_digits())+",")
        f.write("paSSwor1001d"+str(i-200000000)+",")
        f.write("FirstLastSeller"+str(i-200000000)+",")
        f.write(str(i-200000000)+" Street City XX 12345"+",")
        f.write("seller"+str(i-200000000)+"@xyz.com"+","+"\n")



# create data for Buyer Table   
with open("buyer.txt", "w") as f:
    for i in range(1000000001,1000025000):
        f.write(str(i)+",")
        f.write("FirstLastBuyer"+str(i-1000000000)+",")
        f.write("paSSwor1001d"+str(i-1000000000)+",")
        f.write(random_with_N_digits(7)+",")
        f.write(str(i-1000000000)+" Street City XX 12345"+",")
        f.write("buyer@xyz.com"+str(i-1000000000)+","+"\n")


# create data for Department Table   
with open("department.txt", "w") as f:
    for i in range(1,9):
        f.write(str(i)+",")
        f.write("DepartmentName"+str(i)+","+"\n")     


# create data for Hosts Table   
with open("hosts.txt", "w") as f:
    for i in range(400000001,400050000): #same range as Item
        f.write("EStore"+",")
        f.write(str(i)+","+"\n")

        

# create data for Employs Table   
with open("employs.txt", "w") as f:
    for i in range(301,600): #past employees
        f.write("EStore"+",")
        f.write(str(i)+",")
        f.write(start_d()+",")
        f.write(end()+","+"\n")  
    for j in range(601,650): #current employees
        f.write("EStore"+",")
        f.write(str(j)+",")
        f.write(start_d()+",")
        f.write(str(datetime.date.today())+","+"\n")        


# create data for Pays Table         
with open("pays.txt", "w") as f:
    for i in range(500000001,500018000):
        f.write(str(i)+",")
        f.write("EStore"+",")
        f.write(random.choice(seller)+",")
        f.write(start_d()+",")
        f.write(str(round(random.uniform(1,1000),2))+","+"\n")


# create data for CollectsFrom Table         
with open("collectsFrom.txt", "w") as f:
    for i in range(1,22000): 
        f.write("EStore"+",")
        f.write(random.choice(buyer)+",")
        f.write(start_d()+","+"\n")


# create data for Buy Table         
with open("buy.txt", "w") as f:
    for i in range(1,35000): 
        f.write(random.choice(buyer)+",")
        f.write(random.choice(item)+",")
        f.write(start_d()+","+"\n")


# create data for Post Table         
with open("post.txt", "w") as f:
    for i in range(1,10): 
        f.write(random.choice(item)+",")
        f.write(random.choice(seller)+",")
        f.write(start_d()+","+"\n")
        

# create data for WorksIn Table         
with open("worksIn.txt", "w") as f:
    for i in range(601,650): 
        f.write(str(i)+",")
        f.write(random_with_N_digits(1)+","+"\n")

