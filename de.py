positions = [4, 8, 11]

with open('output.txt', 'w') as outfile:
    with open('a.txt', 'r') as infile:
        for line in infile:
            newline = line
            for l in positions:
                newline = newline[:l] + '|' + newline[l:]
            outfile.write(newline)
            
it=[4,8, 11]
with open('output.txt', 'w') as outfile:
    with open('a.txt', 'r') as infile:
        for line in infile:
            line = list(line)
            for i in lit:
                line.insert(i,'|')
            outfile.write("".join(line))
outfile.close() 
