import sys

file = open("info_inputs.txt", 'r')

user_list = []
total = 0

for i in file:
	txt = i.strip()
	new_txt = txt.split("\t")
	# converts new list into ints
	new_txt = list(map(int, new_txt))
	user_list.append(new_txt)

for k in user_list:
	highest = max(k)
	lowest = min(k)
	subtracted = highest - lowest
	total += subtracted

print(total)
