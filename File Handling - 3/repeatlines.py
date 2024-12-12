# repeat the lines

inputfile=open("calculator.txt","r")
outputfile=open("repeat.txt","x")
linesofar=set()
for lines in inputfile:
    if lines not in linesofar:
        outputfile.write(lines)
        linesofar.add(lines)

inputfile.close()
outputfile.close()