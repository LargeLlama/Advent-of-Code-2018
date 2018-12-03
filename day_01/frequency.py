def convert_to_list(filename):
    list = []
    file = open(filename, 'r')
    for line in file:
        list.append(int(line))

    return list

#print(sum(convert_to_list('input.txt')))

def find_duplicates(nums):
    frequencies = []
    current_frequency = 0
    for num in nums:
        current_frequency += num
        frequencies.append(current_frequency)
    #print(frequencies)

    dictionary = {}
    for num in frequencies:
        if num in dictionary:
            dictionary[num] += 1
        else:
            dictionary[num] = 1
    
    for key in dictionary.keys():
        if dictionary[key] > 1:
            return dictionary[key]
    return "nothing found!"

#print(find_duplicates(convert_to_list('input.txt')))
print(find_duplicates(convert_to_list('input.txt')))
