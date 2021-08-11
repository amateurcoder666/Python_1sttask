str = input("Please enter a string : ")
str = str.lower()

def freqsort(freq):
    sortedfreq = sorted(freq.items(), key = lambda kv: kv[1],reverse=True)
    freqdict = dict(sortedfreq)
    for i,j in freqdict.items():
        print(i,'=',j,end =" ")        

def dictinsert(lst):
    freq = {}
    for i in range(0,len(str)):
        if(lst[ord(str[i])-ord("a")]!= 0):
            freq[str[i]] = lst[ord(str[i])-ord("a")]
            lst[ord(str[i]) - ord('a')] = 0           
    freqsort(freq)

def frequency(str):
    lst = []
    for i in range(0,26):
        lst.append(0)
    for i in range (0,len(str)): 
        lst[ord(str[i])-ord("a")] += 1
    dictinsert(lst) 
frequency(str)   


        
    
