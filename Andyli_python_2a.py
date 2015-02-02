#Andy li
import string

def C_tran(a): #translate number to Chinese Number
	x=int(a)
	out_str=""
	while x != 0 :#put input number into sequence string
		out_str= changeN(x%10)+out_str
		x=int(x/10) #force x been an integer
	return out_str
		
def changeN(a): #change 1~10 to Chinese
	stringC=['十','一','二','三','四','五','六','七','八','九']
	return str(stringC[a])

print("***********************************************************************")
for x in range(1, 10):
        for y in range(1, 10):
                print("%d*%d=%2d  " % (y, x, x*y), end="")
        print()
print()
print("************************以下中文陳述***********************************")

for z in range(0,3):
    print()
    for x in range(1, 10):
        for y in range(1,4):
            print("%s%s%s%s%-5s\t" %(C_tran(y+z*3),"乘以",C_tran(x),"等於",C_tran(x*(y+z*3))),end="")
        print()

print("***********************************************************************")

#for windows system pause
print("Press any buttom to exit",end='')
input()
