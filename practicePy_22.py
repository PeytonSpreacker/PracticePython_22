# open file to read
fhand = open("./SUN.txt")

# print line count to check integrity of the file handle
# count = 0
# for line in fhand:
#     count = count +1
# print("Line Count:", count)

counter_dict = {}

line = fhand.readline()
while line:
    words = line.split("/")
    if words[2] in counter_dict:
        counter_dict[words[2]] += 1
    else:
        counter_dict[words[2]] = 1
    line = fhand.readline()

print(counter_dict)