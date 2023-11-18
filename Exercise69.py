souocluong=15
i=1
while i<=souocluong:
    pi=3
    add=1
    for j in range(1,i+1):
        mauso=(2*j)*(2*j+1)*(2*j+2)
        phanso=4/mauso
        pi=pi+add*phanso
        add=add*-1
    print('Estimate ',i,': ',pi,sep='')
    i=i+1
