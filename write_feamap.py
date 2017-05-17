import sys
at = int(sys.argv[1])
num = 29 
fo = open('feamap.txt','w')
for i in range(num):
    if i== at:
	line = ' '.join(['-1' for j in range(num)])
    elif i<13:
   	line = ' '.join(['-1' for j in range(13)]+[str(j-13) for j in range(13,25)]+['12' for j in range(25,num)])
    else:
	line = ' '.join([str(j) for j in range(13)]+['-1' for j in range(13,num)])
    fo.write('%d: %s\n'%(i,line))
fo.close()
	
