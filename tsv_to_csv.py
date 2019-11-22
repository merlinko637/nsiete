import csv
import glob

outFile = open('testLabels.csv', 'w', newline='')
writer = csv.writer(outFile, dialect=csv.excel)
header = ['filename', 'leftX', 'topY', 'width', 'height', 'plateNumber']
writer.writerow(header)
 
for file in glob.glob('data/test/*.txt'):
    with open(file, 'r') as fin:
        reader = csv.reader(fin)
        line = next(reader)
        splitLine = line[0].split()
        writer.writerow(splitLine)

