print("Welcome to the Average Calculator!")
grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
grade3 = float(input("Enter the third grade: "))

def calculateAverage(grade1, grade2, grade3):
  average = (grade1 + grade2 + grade3) / 3
  return average

final_average = calculateAverage(grade1, grade2, grade3)
print("The average of the grades is:", final_average)