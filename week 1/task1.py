l=list("abcdefghijklmnopqrstuvwxyz")
stri=input("enter your string: ")
string=' '
for i in stri:
    a=i.lower()
    if a in l:
        m=str(l.index(a)+1)
        string=string+m+' '
    else:
        continue
print("output: ",str(string))
    
