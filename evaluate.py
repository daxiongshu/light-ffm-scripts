from metric import apk
import sys
def sort_value(dic):
    return sorted(dic, key=dic.get, reverse=True)

def get_apk(inputx,group):
    with open(inputx) as f:
        with open(group) as g:
	    last = ''
	    pred,act = {},[]
	    count = 0
	    apks = 0
	    groups = 0
	    for c,line in enumerate(f):
		gg = g.readline().strip()
		gg,y = gg.split(',')
		if last!='' and last!=gg:
		    pred = sort_value(pred)
		    print apk(act,pred,12)
		    apks += apk(act,pred,12)
         	    act = []
        	    pred = {}
		    count = 0
		    groups += 1
		if y == '1':
		    act.append(count)	        		   
	        pred[count] = float(line.strip())
		count+=1
		last = gg
 		if c%100000 == 0:
		    print("%s %d lines processed, apk: %.4f"%(inputx,c,apks/(groups+1)))
	    pred = sort_value(pred)
            apks += apk(act,pred,12)
    print("final apk: %.4f"%(apks/(groups+1)))

def get_apk_lffm(inputx,group):
    with open(inputx) as f:
        with open(group) as g:
            last = ''
            pred,act = {},[]
            count = 0
            apks = 0
            groups = 0
            for c,line in enumerate(f):
                gg = g.readline().strip()
                if gg[0]=='x':
		    if last!='':
                        pred = sort_value(pred)
                        #print act,pred#apk(act,pred,12)
                        apks += apk(act,pred,12)
                        act = []
                        pred = {}
                        count = 0
                        groups += 1
		    gg = g.readline()
		y = gg[0]
		print gg,line
                if y == '1':
                    act.append(count)
                pred[count] = float(line.strip())
                count+=1
                last = gg
                if c%100000 == 0:
                    print("%s %d lines processed, apk: %.4f"%(inputx,c,apks/(groups+1)))
            pred = sort_value(pred)
            apks += apk(act,pred,12)
    print("final apk: %.4f"%(apks/(groups+1)))


if __name__ == "__main__" :
    if 'group' not in sys.argv[2]:
	get_apk_lffm(sys.argv[1],sys.argv[2])
    else:
        get_apk(sys.argv[1],sys.argv[2])       
