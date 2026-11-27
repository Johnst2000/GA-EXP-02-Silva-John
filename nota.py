import sys
# uso: python nota.py D1 D2 D3 D4 D5 D6   (niveles 0-4)
w=[10,20,15,20,25,10]; n=[int(x) for x in sys.argv[1:7]]
s=sum(a*b for a,b in zip(w,n))
print(" + ".join(f"{a}*{b}" for a,b in zip(w,n)),"=",s,"-> ",s,"/4*0.1 =",round(s/4*0.1,3),"~",round(s/4*0.1,1))
