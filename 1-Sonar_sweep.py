### depths = input_file as a huge multiline string.

depths_list = depths.split("\n")

# The number of times a depth measurement increases
num_of_increase = 0
c = 1
while c < (len(depths_list) -1) :
    if int(depths_list[c-1]) < int(depths_list[c]):
        num_of_increase += 1
    c += 1
print(num_of_increase)


# Three-measurement sliding window
# Ugly, but was too easy to import anything
num_of_increase = 0
c = 3
while c < (len(depths_list) -1) :
    if (int(depths_list[c-3]) + int(depths_list[c-2]) + int(depths_list[c-1])) < (int(depths_list[c-2]) + int(depths_list[c-1]) + int(depths_list[c])):
        num_of_increase += 1
    c += 1
print(num_of_increase)