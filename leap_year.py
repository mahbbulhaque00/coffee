year = input("enter a year for test : ")
year = int(year)
if year % 4 != 0 :
  print("No ")
else:
   if year % 100 == 0 :
     if year % 400 == 0 :
        print("yes")
     else:
         print("no")

   else:
      print("yes")
   
 
