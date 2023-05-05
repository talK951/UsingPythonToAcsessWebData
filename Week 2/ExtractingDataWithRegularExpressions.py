import re

data = open('ActualData')
num_found = []
for line in data:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    num_found.extend(numbers)
for i in range(len(num_found)):
    num_found[i] = int(num_found[i])
print(sum(num_found))
