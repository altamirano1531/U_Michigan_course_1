import re

################################################# Search and respond 
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.strip()
#     if re.search('From:', line):    # RegEx method
#     #if re.search('^From:', line):  # Caret forces to be at the beggining of the line
#         print(line)


# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.strip()
#     if line.find('From:') >= 0:     # Standard method
#     #if line.startwith('From:'):    # Reads from the beggining.
#         print(line)
    

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.strip()
#     if re.search('X-\S+:', line):       # Matches the line start, but shows the whole line.
#         print(line)

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.strip()
#     if re.search('X.*:', line):       # Matches the line start, but shows the whole line.
#         print(line)

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.strip()
#     if re.findall('^X-\S+:', line):       
#         print(line)

#################################################  Find and Extract
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.strip()
#     y = re.findall('F.+:', line)  
#     print(y)

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.strip()   
#     y = re.findall('^From (\\S+@\\S+)', line)     
#     print(y)

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.strip()
#     y = re.findall('^From.(\\S+@\\S)', line)
#     print(y)

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.strip()
#     y = re.findall('.*@([^ ]*)', line)
#     print(y)

# x = 'From: Using the : character'
# y = re.findall('^F.+:', x)
# print(y)

x = 'From stephen.marquar@uct.ac.za Sat Jan'
y = re.findall('\\S+?@\\S+', x)
print(y)