data = []

def count_line(filename):
    count= 0

    with open(filename,'r') as fname:
        lines = fname.readlines()
        for line in lines:
            data.append(line.strip('\n'))
            count = count + 1
    return count    
    
def count_words():
    countword=0
    for word in data:
        
            countword = count_words + len (word)
            print(countword)  
