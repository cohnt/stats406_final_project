import csv
from hurricane import Hurricane, DataLine

def read_file(fname):
	hurricane_list = []
	with open(fname) as csvfile:
		reader = csv.reader(csvfile, delimiter=",")

		for row in reader:
			if row[0][0:2] == "AL":
				atcf_number = int(row[0][2:4])
				year = int(row[0][4:8])
				hurricane_name = row[1].strip()
				hurricane_list.append(Hurricane(hurricane_name, atcf_number, year))
			else:
				hurricane_list[-1].add_data_line(DataLine(row))

	return hurricane_list