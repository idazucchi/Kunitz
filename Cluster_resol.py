import sys   
 
def get_dic(filename):
	d = {}
	with open(filename) as f:
		for line in f:
			 #~ print(line)
			 v = line.rstrip().split()
			 #~ print(v[0],v[-1])
			 d[v[0]] = float(v[-1])
			 
	return d
	
def sort_cluster(clist,d):
	tlist = []
	for pID in  clist:
		v = d.get(pID,float('inf')) # keeps the script from crushing if the id is not found in file1
		tlist.append([v,pID])
		tlist.sort()
	return tlist
	
if __name__ == '__main__':
	file1 = sys.argv[1]  # all ids list with resolution :) not the general table! Aha! Now I see!
	file2 = sys.argv[2]  # cluster file
	d = get_dic(file1)
	with open(file2) as f:
		for line in f:
			l_id = line.rstrip().split()
			sl_id = sort_cluster(l_id,d)
			print(len(sl_id),'  '.join([i[1]+':'+str(i[0]) for i in sl_id]))
			
