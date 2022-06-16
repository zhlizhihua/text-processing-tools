'''
This script randomly samples a percentage of a csv file using two naive methods.
Takes in the file and the percentage number. Output the result sample.
'''

import csv, random

# traverse file only once, but build list object of entire file
def sampling1(filename, k):
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = '\t')
        linecount = 0
        line_list = list()
        for line in csvreader:
            linecount += 1
            line_list.append(line)
        result = random.sample(line_list, int(k*100))
        print(result)

# traverse file twice, but does not build list object of entire file
def sampling2(filename, k):
    with open(filename) as f:
        linecount = sum(1 for line in f)
        linenum = sorted(random.sample(range(int(linecount)), int(linecount*k)), reverse=True)
        cur_line = linenum.pop()
        result = []
        f.seek(0)
        for n,line in enumerate(f):
            if n == cur_line:
                result.append(line)
                if len(linenum) > 0:
                    cur_line = linenum.pop()
                else:
                    break
        print(result)
        

if __name__ == "__main__":
    fname = input("File name: ")
    percent = float(input("Percentage: "))
    sampling1(fname, percent)
    sampling2(fname, percent)