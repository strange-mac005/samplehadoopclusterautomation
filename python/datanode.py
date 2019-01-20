import os
import core
import show_ip
#show_ip.active_ip()
#show_ip.status_ip()

os.system("clear")


u=open("usedip","r")
check=u.read();
uIP=check.split(";")
u.close()
c=0
x=len(uIP)
while c<x:
	if uIP[c][0:6]=="ip_NN:":
		print "Name Node IP:",
	elif uIP[c][0:6]=="ip_JT:":
		print "Job Tracker IP:",
	elif uIP[c][0:6]=="ip_DN:":
		print "Data Node Task Tracker IP:",
	uIP[c]=uIP[c][6:]
	print uIP[c]
	c+=1



ac=open("activeip","r")
z=ac.read()
z=z.split(';')
x=len(z)#z is list of active nodes
c=0
print "usable IP"
while c<x-1:
 	if z[c] not in uIP:
		print z[c]
	c+=1

con=0
while con!=2:
	ip_DN=raw_input("Enter IP For data node")
	if ip_DN in z and ip_DN not in uIP:
		con=2
	else:
		print "Enter Valid IP"

core.core_set(ip_DN)
c=0
print "Setup Done"


raw_input("Press Enter To start data node")
os.system("sshpass -p redhat ssh root@{} 'iptables -F'".format(ip_DN))
os.system("sshpass -p redhat scp /root/project/datatask/hdfs-site.xml root@{}:/etc/hadoop".format(ip_DN))
os.system("sshpass -p redhat ssh root@{} 'hadoop-daemon.sh start datanode'".format(ip_DN))
os.system("sshpass -p redhat ssh root@{} 'hadoop-daemon.sh start tasktracker'".format(ip_DN))
raw_input("Data Node Task Tracker Set Press Enter")

fil=open("usedip","r+")
z=fil.read()
fil.write(";ip_DN:{}".format(ip_DN))
fil.close()
os.system("clear");
