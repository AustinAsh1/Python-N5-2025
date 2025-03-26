
#Enter 5 daily temperatures between -20 and +50 C
#Display all temperatures
#Calculate and display the average temperature
#your program should use input validation, a 1-D array and fixed loops.

dailytemperatures = []
temparature = int(input("Enter 5 daily tempratures between -20 and +50"))
while temparature <-20 or temparature > 50:
    print("These are invalid temparature")
    temparature = int(input("Enter 5 daily tempratures between -20 and +50"))