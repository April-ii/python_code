fi=open("卖火柴的小女孩.txt",'r')
fo=open("PY.txt",'w')
txt=fi.read()
d={}
for word in txt:
    d[word]=d.get(word,0)+1
del d["\n"]
del d[" "]
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
for i in range(len(ls)):
    ls[i]="{}:{}".format(ls[i][0],ls[i][1])
fo.write(",".join(ls))
fi.close()
fo.close()