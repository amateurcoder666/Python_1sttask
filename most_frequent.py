str = input("Please enter a string : ")
str = str.lower()

def freqsort(freq):
    sortedfreq = sorted(freq.items(),key = lambda kv: kv[1], reverse=True)
    freqdict = dict(sortedfreq)
    for i,j in freqdict.items():
        print(i,'=',j,end =" ")        

def frequency(str):
 freq = {}
 for i in range(0,len(str)):
     freq[str[i]] = 0
 for i in range(0,len(str)):
     freq[str[i]] = freq.get(str[i]) + 1
 
 freqsort(freq)
 
frequency(str)
