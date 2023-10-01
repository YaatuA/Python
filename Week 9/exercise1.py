# Write a program in python using if condition . Input the temperature (user input) . Check if the temperature is less than 98 display the result as cold. otherwise  if the temperature more than 98 , display the result as Hot . otherwise display them as normal . 

input_string_temperature = int(input("Enter the temperature: "))

if (input_string_temperature < 98):
    print("The temperature is cold.")
elif (input_string_temperature > 98):
    print("The temperature is hot.")
else:
    print("The temperature is normal.")