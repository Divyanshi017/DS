f=open("C:\\Users\\hp\\Desktop\\DS\\fun.txt","r")
f_out=open("C:\\Users\\hp\\Desktop\\DS\\fun_wc.txt","w")
for line in f:
    tokens=line.split(' ')
    f_out.write(" Wordcount:"+str(len(tokens))+" " +line)

f.close()
f_out.close()