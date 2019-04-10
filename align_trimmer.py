#!/usr/local/bin/python3
import sys 

def trim(infile, outfile):
	# Open db file and output file 
	out = open(outfile,'w')
	in_file = open(infile)

	flag = 0

	# Select the sequence
	seq = []
	for line in in_file:
		if line[0] == '>':
			out.write(line)
			line = in_file.readline()
			out.write(line[8:-4].upper()+'\n')
		elif len(line)==2:
			continue
		else:
			#~ print(len(line),line)
			out.write(line)
	
	
	
	out.close()
	in_file.close()

if __name__ == "__main__":
	infile = sys.argv[1]
	outfile = sys.argv[2]
	trim(infile, outfile)




