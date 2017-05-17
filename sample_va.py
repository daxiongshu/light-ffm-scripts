import sys

f = open()
fo = open(,'w')
count = 0
for c,line in enumerate(f):
    if line[0] == 'x':
	count +=1

    if count%10 == 0:
	start = True
    else:
	start = False
    if start:
	fo.write(line)
f.close()
fo.close()

