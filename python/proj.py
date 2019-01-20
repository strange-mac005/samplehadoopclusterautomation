#!/usr/bin/python
import subprocess
import sys
import os
i=0
os.system("nmap -sn 192.168.43.*>nmap.txt")
z=file("nmap.txt")
fil=file("activeip","w")
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
		#if i>1:
		iptab.append(iz)
print iptab
for x in iptab:
	print x
	s= os.system("sshpass -p redhat scp /root/hadoop-1.2.1-1.x86_64.rpm {}:/root/Desktop ".format(x))
	p=os.system("sshpass -p redhat scp /root/jdk-7u79-linux-x64.rpm {}:/root/ ".format(x))
	print os.system("sshpass -p redhat ssh root@{} 'rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --replacefiles'".format(x))
	print os.system("sshpass -p redhat ssh root@{} 'rpm -ivh /root/jdk-7u79-linux-x64.rpm'".format(x))
	print os.system("sshpass -p redhat scp /root/.bashrc {}:/root/ ".format(x))
	print os.system("sshpass -p redhat ssh root@{} 'export JAVA_HOME=/usr/java/jdk1.7.0_79'".format(x))
	print os.system("sshpass -p redhat ssh root@{} 'export PATH=/usr/java/jdk1.7.0_79/bin/:$PATH'".format(x))
	if s==0 and p==0:
		fil.write("{};".format(x))		
