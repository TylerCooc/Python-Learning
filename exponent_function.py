#takes a number and raises it to a certain power

print(2**3) #simple way to use 2 raised to the third power

def raise_to_power(base_num, power_num): #function will continuously multiply the base number by itself using a for loop and the desired exponent
    result = 1
    for index in range(power_num): #will loop based off power num times
        result = result * base_num
    return result

print(raise_to_power(3,4))