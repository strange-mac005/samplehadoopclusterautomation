import os
import sys
i=0
os.system("nmap 192.168.43.*>nmap.txt")
z=file("nmap.txt")
#y=z.read()
ip="192.168.43."
con=0#condition check
#y.split()
iptab=[]
for l in z:
	if ip in l:
		pos=l.find(ip)
		pos+=11
		sub=l[pos:pos+3]
		if sub<="224" and sub>="100":
			iz= sub
		elif sub[0:2]<="99" and sub[0:2]>="10":
			iz= sub[0:2]
		elif sub[0]<='9' and sub[0]>='0':
			iz= sub[0]
		i+=1
		iz=ip+iz
		if i>1:
			iptab.append(iz)

print iptab
print i
