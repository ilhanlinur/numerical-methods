 dizi=[1.0,-7.0,-3.0,79.0,-46.0,-120.0]
    yeni=[]
    kokler=[]
def kok(x):
 	x1=0.0
for i in range(len(dizi)):
 	x1=x1+dizi[i]*(x**(len(dizi)-(i+1)))
 	return(x1)
  def yenidenklem(x):
  	yeni.append(dizi[0])
 	for i in range(1,len(dizi)):
 	yeni.append(x*yeni[i-1]+dizi[i])
 	dizi.clear()
 	for i in range(0,len(yeni)-1):
    dizi.append(yeni[i])
 	return(1)
 
while len(dizi)>2:
 	t1=float(input("t1 için değer girin: "))
 	t2=float(input("t2 için değer girin: "))
 	t3=0.0
 	n=-1.0
    for i in range(0,100):
 	
 	if kok(t1)*kok(t2)>0:
 		t1=float(input("t1 için yeni değer girin: "))
 		t2=float(input("t2 için yeni değer girin: "))
  	elif kok(t1)*kok(t2)<0:
		t3=(t1+t2)/2
 	if kok(t3)*kok(t1)<0:
 		t2=t3
 	elif kok(t3)*kok(t1)==0:
 			kokler.append(t3)
 			n=t3
 		break
 	else:
 		t1=t3
    else:
 	if kok(t1)==0:
 		kokler.append(t1)
 		n=t1
 		break
 	else:
 	kokler.append(t2)
 	n=t2
 	break
    n=(t1+t2)/2
    if n==0:
    print("denklemin koklerinden biri 0 ,0 olmayan bir aralik seçin ")
    continue
    yeni.clear()
 	yenidenklem(n)
    print(dizi)
    kokler.append(-dizi[1])
    print("kokler")
    print(kokler)	
