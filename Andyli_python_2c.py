#Andy li
import os
def C_tran(a): #translate number to Chinese Number
    x=a
    z=[]
    countN=0
    output_ch_n=""
    while x != 0 :#put input number into array
        z.insert(0,x%10)
        x=int(x/10) #force x been an integer
        countN=countN+1
    z.append(-1)
    if countN >= 2 :#check if bigger than ten
        if z[0] == 1 :#10~19
            output_ch_n = changeN(10)+put_num(1,z)
        else : #>20
                z.insert(1,10) #insert 'ten' between two ch_numbers
                output_ch_n=put_num(0,z)
    else: #just 0~9
        output_ch_n=output_ch_n+put_num(0,z)
    
    return output_ch_n
        
def changeN(a): #change 0~10 to Chinese
    stringC=['　','一','二','三','四','五','六','七','八','九','十']
    return str(stringC[a])
def put_num(start_point,array_list): #change array list to string
        b=array_list
        output_ch_n=""
        while b[start_point] != -1:
                output_ch_n=output_ch_n+changeN(b[start_point])
                start_point=start_point+1
        return str(output_ch_n)

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
            print("%s乘以%s等於%-5s\t" %(C_tran(y+z*3),C_tran(x),C_tran(x*(y+z*3))),end="")
        print()

print("***********************************************************************")
#for windows system running
os.system("pause")
