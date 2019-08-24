
import statistics
temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]
missing_3value = [33,66,65,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]

# assign a variable to the list of temperatures

# 1. Calculate the minimum of the list and print the value using print()
min_temp = min(temperatures_C)
print("The minimum is:")
print(min_temp)
print ( 10 * '*')

# 2. Calculate the maximum of the list and print the value using print()
max_temp = max(temperatures_C)
print("The maximum is :")
print(max_temp)
print ( 10 * '*')

# 3. Items in the list that are greater than 70ºC and print the result
over_70 = 0
not_over = 0
for f in temperatures_C:
    if f > 70:
        over_70 += 1
    else:
        not_over += 1
print("The temp went over 70 C: ")
print(over_70, "times")
print ( 10 * '*')

# 4. Calculate the mean temperature throughout the day and print the result
mean_temp = sum(temperatures_C)/len(temperatures_C)
print("The mean tmeperature is :", mean_temp, "C'")
print ( 10 * '*')

# 5.1 Solve the fault in the sensor by estimating a value
print("The missing value is at 3:00 am is calculated to be:")
value_3 = (sum(missing_3value)/len(missing_3value))
print(value_3)

# 5.2 Update of the estimated value at 03:00 on the list
temperatures_C[3] = int(value_3)
print("The new temp lise should be:")
print(temperatures_C)

#The decision
'''

more than 4 hours with temperatures greater than or equal to 70ºC
some temperature higher than 80ºC
average was higher than 65ºC throughout the day If any of these three is met, the cooling system must be changed.
'''
newMean = sum(temperatures_C) / len(temperatures_C)
print(newMean)
decision = True


if decision is True:
    if newMean > 65:
        print("The average was higher than 65ºC throughout the day, please change the cooling system.")
        decision = False
    for x in temperatures_C:
        if x > 80:
            print("The temperature was higher than 80º C, please change the cooling system.")
            decision = False
    for x in temperatures_C:
        if x >= 70:
            over_70_4_hours += 1
            if over_70_4_hours == 4:
                print("For more than 4 hours the temperatures were greater than or equal to 70ºC,",
                        "please change the cooling system."
                        )
                decision = False
    else:
        print("Do not replace the system at this time")
        decision = False
