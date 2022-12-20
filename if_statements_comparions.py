#comparison operators in python are:
# == equal
# != not equal
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

# to note single = sign is a assignments
# whereas == is a comparison

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(5,6253,7))