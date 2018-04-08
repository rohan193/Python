#Author : Rohan M. Nanaware
#Date C.: 13th Aug 2017
#Date M.: 13th Aug 2017
#Purpose: Python data structures code documentation

#6.1 Strings
fruit = 'banana'
print(fruit[0])
print(len(fruit))
for i in range(len(fruit)):
    print(i, fruit[i])
for letter in fruit:
    print(letter)
#Slicing strings - Upto but not including
string = 'Python is great!'
print(string[1:4])
print(string[7:])

#6.2 Manipulating strings
fruit = 'banana'
if 'nana' in fruit:
    print('Present')
if 'Rohan' < 'rohan':
    print('Capital first')
greet = 'Hello World!'
greet.lower()
print('Hello World!'.lower())
string = 'Hello World'
type(string)
dir(string)#Methods applicable on string
string.replace('Hello','Hi')
string = '  Yahallo!  '
string.lstrip()
string.rstrip()
string.strip()
line = 'The quick brown fox!'
line.startswith('T')
line.startswith('t')
#String slicing
string = 'Koreva teme#$! Makhinayo '
start = string.find('!')+2
end = string.find(' ',start)
print(string[start:end])

#7.1 Files
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line_strip = line.rstrip().upper()
    #line_strip_upper = line_strip.upper()
    print(line_strip)

# Use the file name mbox-short.txt as the file name 
#sample data - "X-DSPAM-Confidence:    0.8475"
fname = input("Enter file name: ")
fh = open(fname)
confidence = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print(line)
    confidence = float(line[line.find(":")+1:len(line)]) + confidence
    count = count + 1
avg_confidence = confidence/count    
print("Average spam confidence:",avg_confidence)

#8.4

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
#for line in fh:
#    for word in line.splitsplit():
#        if word in lst: 
#            print(word)
#            continue
#        lst.append(word)
#print(lst.sort())

for line in fh:
    line.rstrip()
    print(line.rstrip())

#9.1 Dictionaries
purse = dict()
purse['money'] = 10
purse['wallet'] = 1
print(purse['wallet'])
for w in purse:
    print(w)
    print(purse[w])
purse[1] = 15

dict_ = dict()
names = ['A','B','C','D','E','F','G','A','B','C']
for name in names:
    if name in  dict_:
        dict_[name] += 1
    else:
        dict_[name] = 1
print(dict_)

dict_ = dict()
names = ['A','B','C','D','E','F','G','A','B','C']
for name in names:
    dict_[name] = dict_.get(name, 0) + 1

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
word_dict = dict()
word_list = list()
for line in handle:
    if 'From:' not in line:
        continue
    else:
        words = line.split()
        word_list.append(words[1])
for word in word_list:
    word_dict[word] = word_dict.get(word, 0) + 1
max_count = max(word_dict.values())
#print(max_count)
for sender, count_ in word_dict.items():
    #print(sender)
    if count_ == max_count:
        print(sender, count_)
    