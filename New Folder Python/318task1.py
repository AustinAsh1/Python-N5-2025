#  Create a program that contains an array of 7 daily temperatures (in celsius). Traverse the 1D array
#  to calculate and display the average temperature (sum of 7 days/7).

temperatures = [22.5, 24.0, 21.5, 23.0, 25.5, 20.0, 22.0]
total_temperature = 158.5
for temp in temperatures:
    total_temperature + temp
average_temperature = total_temperature / len(temperatures)
print("Average temperature over 7 days:", round(average_temperature, 2), "°C")
