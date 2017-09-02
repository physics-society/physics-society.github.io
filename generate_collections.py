import csv
import hashlib

def generate_person(row):
	outfile = open(f"_people/{row[1]}.md", 'w')
	outfile.write("---" + "\n")
	outfile.write("key : \"" + row[1] + "\"\n")
	outfile.write("name : \"" + row[0] + "\"\n")
	outfile.write("batch : \"" + row[3] + "\"\n")
	outfile.write("email : \"" + row[2] + "\"\n")
	outfile.write("---" + "\n")
	outfile.close()


def generate_project(row):
	content = '-'.join(row)
	md5sum = hashlib.md5(bytes(content, 'utf-8')).hexdigest()
	outfile = open(f"_projects/{md5sum}.md", 'w')
	outfile.write("---" + "\n")
	outfile.write("title : \"" + row[4] + "\"\n")
	outfile.write("description : \"" + row[6] + "\"\n")
	outfile.write("people : \"" + row[1] + "\"\n")
	outfile.write("field : \"" + row[5] + "\"\n")
	outfile.write("---" + "\n")
	outfile.close()


data = open('data.csv', 'r')
csvreader = csv.reader(data)
flag = 0
for row in csvreader:
	if not flag:
		print(row)
		flag = 1
		continue
	generate_person(row)
	generate_project(row)
