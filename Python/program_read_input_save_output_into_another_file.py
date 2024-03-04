# A program that reads input from an external file
# Performs some processing and then 
# Writes output to another file
# It uses a few Python methods that are specific to input and output
# The code in the first couple lines uses the open method,this opens files with specific names that are located in the same folder as the program file
# The values.txt file in the files list. When opening this file, it contains a list of numbers, notice that the file list doesn't contain a values-total.txt file. 



infile = open('values.txt', 'rt')  # 'rt' read text mode
outfile = open('values-totaled.txt', 'wt') # 'wt' write mode
print('Processing input')
sum = 0 # creating a counter 
for line in infile:    # Taking one line at a time, a number at a time
    sum += int(line) # converting it to integer, adding them up with + operastor and assigning it to Sum variable  
    print(line.rstrip(), file=outfile) # Printing current line with right space strip character, and specifying to save data to a file, output to outfile variable, which is a file that will be created
print('\nTotal: ' + str(sum), file=outfile) # convert to string to concatenate strings, store in outfile
outfile.close()  # close the outfile
print('Output complete')
