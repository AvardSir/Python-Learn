txt = input()

def words(txt):
    s=''
    for i in range(len(txt)):
        if txt[i]==' ':
            
            yield s
            s=''
        elif i!=len(txt)-1:
            s+=txt[i]
            yield s
        else:

            s+=txt[i]
        
    #yield txt.split()
    #your code goes here

print(list(words(txt)))
