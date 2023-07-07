def if_more_five_char(stringg):
    if len(stringg)>5:
        return True
    else: return False
names = ["David", "John", "Annabelle", "Johnathan", "Veronica"]

#names=list(filter(if_more_five_char, names))#list(map(if_more_five_char,names)))
names=list(filter(lambda x:len(x)>5, names))
print(names)