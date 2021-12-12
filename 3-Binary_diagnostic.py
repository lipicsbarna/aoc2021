## bits = input file as multiline gigantic string
bits_list = bits.split("\n")


## What is the power consumption of the submarine?
bit_dict = {}
for i in range(0,12):
    bit_dict[i] = []

gamma = []
epsilon = []
for metric in bits_list:
    c = 0
    while c < 12:
        bit_dict[c].append(metric[c])
        c += 1

bit_count: dict = dict.fromkeys(bit_dict)

for i in range(0,12):
    ones = len([bit for bit in bit_dict[i] if bit == "1"])
    zeros = len([bit for bit in bit_dict[i] if bit == "0"])
    if ones > zeros:
        bigger = '1'
        smaller = '0'
        bit_count[i] = '1'
    elif zeros > ones:
        bigger = '0'
        smaller = '1'
        bit_count[i] = '0'
    else:
        bit_count[i] = '1'
        
    gamma.append(bigger)
    epsilon.append(smaller)
    
print(int("".join(gamma), 2) * int("".join(epsilon), 2))


## What is the life support rating of the submarine?
### Oxygen
def calculate_oxy(bits, index):
    _bits_dict  = dict.fromkeys(range(0,12))

    num_ones = len([x for x in bits if x[index] == '1'])
    num_zeros = len(bits) - num_ones
    if num_zeros > num_ones:
        _most_common = '0'
    else:
        _most_common = '1'
    bits = [x for x in bits if x[index] == _most_common]
    print(len(bits))
            
    if len(bits) == 1:
        return bits
    elif index == 12:
        return bits
    else:
        return calculate_oxy(bits, index+1)
        
        
oxy = calculate_oxy(bits_list, 0)


### CO2
def calculate_co2(bits, index):
    _bits_dict  = dict.fromkeys(range(0,12))

    num_ones = len([x for x in bits if x[index] == '1'])
    num_zeros = len(bits) - num_ones
    if num_zeros > num_ones:
        _least_common = '1'
    else:
        _least_common = '0'
    bits = [x for x in bits if x[index] == _least_common]
    print(len(bits))
            
    if len(bits) == 1:
        return bits
    elif index == 12:
        return bits
    else:
        return calculate_co2(bits, index+1)
        
        
co2 = calculate_co2(bits_list, 0)

## Result
print(int(oxy[0], 2) * int(co2[0], 2))