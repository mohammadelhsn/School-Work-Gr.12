#############################################################################
#Author: Mohammad El-Hassan
#Description: Mini Assingment #63
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

nums = []
num1 = int(input("Enter one number "))
nums.append(num1 * num1)
num2 = int(input("Enter another number "))
nums.append(num2 * num2)
num3 = int(input("Enter another number "))
nums.append(num3 * num3)
num4 = int(input("Enter another number "))
nums.append(num4 * num4)
num5 = int(input("Enter another number "))
nums.append(num5 * num5)
nums.sort()
print(nums)
