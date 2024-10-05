import re

out = list()
total = 0

hand = open('regex_sum_588166.txt')
for line in hand:
    line = line.strip()
    out = re.findall('[0-9]+', line)  
    if (len(out) == 0):
        continue 
    for num in out:
        total = total + int(num)
print(total)