import sys 

def extract_seq (db, ID_list, out_file):
    # Extract set of IDs from file
    ID_set = []
    with open(ID_list) as ID:
	    for line_id in ID:
	        ID_set.append((line_id.rstrip(),True))
	# Using the dictionary makes matching the line id with our list faster
    ID_d = dict(ID_set)
	
	# Open db file and output file 
    out = open(out_file,'w')
    db_in = open(db)

    flag = 0

    # Match IDs in list and write sequences to output file
    for line in db_in:    
        if line[0] == '>':
            # Memory efficient option using Bool
            #~ if ID_d.get(line.split(' ')[0][1:],False):
            if ID_d.get(line.split('|')[1],False):
            #~ if (ID_d.get(line.split(' ')[0][1:],0)==1):
            
                out.write(line)

                flag = 1

            else:
                flag = 0

        elif flag == 1:
                out.write(line)

        

    out.close()
    db_in.close()

if __name__ == "__main__":
    ID_list = sys.argv[1]
    db = sys.argv[2]
    out = sys.argv[3]
    extract_seq(db, ID_list, out)

    


