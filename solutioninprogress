temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]
missing_3value = [33,66,65,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]

# assign a variable to the list of temperatures

# 1. Calculate the minimum of the list and print the value using print()
print("The minimum is:")
print(min(temperatures_C))
print ( 10 * '*')

# 2. Calculate the maximum of the list and print the value using print()
print("The maximum is :")
print(max(temperatures_C))
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
print("The mean tmeperature is :")
print(sum(temperatures_C)/len(temperatures_C), "C")
print ( 10 * '*')

# 5.1 Solve the fault in the sensor by estimating a value
# 5.2 Update of the estimated value at 03:00 on the list
print("The missing value is at 3:00 am is calculated to be:")
value_3 = (sum(missing_3value)/len(missing_3value))
temperatures_C[3] = int(value_3)
print(temperatures_C)
