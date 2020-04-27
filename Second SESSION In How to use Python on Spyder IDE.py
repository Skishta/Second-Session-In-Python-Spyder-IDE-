'''بسم الله الرحمن الرحيم'''               
#اولا البايثون هي أحدث اللغات المستخدمة للبرمجة
#In this training program
#you will learn how to collect
#analyze and visualize any size of data
#Learn ٍsome-NOT ALL- Python basics.
#Learn simplest way in OOP (Object-Oriented Programming) and data structures in python
#Be able to implement some algorithms or program using python
#Learn the most needed data science algorithms

             '''Second SESSION In How to use Python on Spyder IDE'''
#عايزين نطبق على اللى فات بعمل برنامج fake يطلب من اليوزر يدخل سنة ثم هقول لليوزر انت هتموت عن السن كذا 
#هجمع رقم 20 على الرقم اللى اليوزر هيدخل-يعنى لو دخل ليا ان سنة 60 هقولة انت هتموت عن سن 80 -
#امر الترحيب بالمستخدم اولا
username=input("Plz enter your name: ")
#print [Hello 'the user name']
print("Hello" + " " + username)
#امر معرفة سن المستخدم لعمل عملية ويادة ال 20 سنة على السنة اللى تم ادخالها من المستخدم
#we add int to change the type of unput so we can using add on it
userage=input("plz enter your age: ")
#to print [you are 'the userage' years old]
print("You are" + " " + userage + " Years Old")
#store the "userage" in another int variable to add "20"
user_age=int(userage)
#prediction (fake) of the death
diedate=user_age+20
#store the "diedate" in another str variable tp print it
die_date=str(diedate)
#to print the diedate to the user
print("you will die at " +die_date+"Years Old")