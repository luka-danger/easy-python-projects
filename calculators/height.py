#Pseudocode:  
#When a user inputs heights (in cm)
#Count the number of inputted heights 
#Add heights together
#Divide the sum of heights by the total number of inputs
#Print the average height 

#Instructions: Make sure to read documentation top down! 

#To input user heights (Line 2)
student_heights = input("Input a list of student heights\n").split()
#These line place the inputted heights into a list
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n]) 

#Sets variables to 0
heights_in_list = 0 
total = 0
#Use for loop to find the number of heights in the list (Line 3)
for i in student_heights:
    heights_in_list+=1 
#Finds the sum of all heights added together (Line 4)
sum_of_heights = sum(student_heights)
#Divides the sum of all heights by the number of heights in list (Line 5)
average_height = sum_of_heights / heights_in_list
#Prints the average height (Line 6)
#Use round() to get an integer 
print(round(average_height)) 
