# FOR FINDING LARGEST NUMBER IN LIST:

# number = [15,65,45,75,85,95,100]
# largest = 0
#
# for num in number:
#     if num > largest:
#         largest = num
#
# print("largest numbers is", largest)

# ========================================================================================================================

# number = [15,65,45,75,85,95,100]
# largest = 100
# secondlargest = 0
#
# for num in number:
#     if num < largest:
#         num = secondlargest
#
#
# print("largest numbers is", secondlargest)
# print("second largest number is",secondlargest)


# ==========================================================================================================================


number = [15,65,45,75,85,95,100]
largest = 0
sl2 = 0

for num in number:
    if num > largest:
        sl2 = largest
        largest = num


    elif num > sl2 and sl2 != largest:
        sl2 = num

print("secondlargest no. is" , sl2)




