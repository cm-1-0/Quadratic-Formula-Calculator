from math import *

varB = input("Enter for B: ")
varA = input("Enter for A: ")
varC = input("Enter for C: ")
discriminant = pow(float(varB), 2) - (4 * float(varA) * float(varC))

result = float(varB) * -1 + sqrt(discriminant)
result2 = float(varB) * -1 - sqrt(discriminant)
final_result = float(result) / (2 * float(varA))
final_result2 = float(result2) / (2 * float(varA))

print("Answer: " + str(final_result))
print("Answer2: " + str(final_result2))
