import os
import mapred
use=file("usedip","r")
uIP=use.read(6)
uIP=use.read()
use.close()
ac=open("activeip","r")
z=ac.read()
os.system("clear")
ac.close()
z=z.split(';')
x=len(z)#z is list of active nodes
c=0
while c<x-1:
	if z[c]!=uIP:
		print z[c]
	c+=1
con=0
while con!=2:
	ip_JT=raw_input("Enter IP for Job Tracker")
	if ip_JT in z and ip_JT!=uIP:
		con=2
	elif ip_JT==uIP:
		print "IP already used for Name Node"
	else:
		print "Enter a valid IP"
mapred.mapred_setup(ip_JT)#setup mapred-site.xml
c=0
while c<x-1:
	if z[c]!=uIP:
		os.system("sshpass -p redhat scp /root/project/trackers/mapred-site.xml {}:/etc/hadoop/ ".format(z[c]))#core site Setup
	c+=1
print "Basic Setup Done"
raw_input("Press Enter To start JobTracker")
os.system("sshpass -p redhat ssh root@{} 'hadoop-daemon.sh start jobtracker'".format(ip_JT))
os.system("sshpass -p redhat ssh root@{} 'iptables -F'".format(ip_JT))
raw_input("Job Tracker Started Press Enter ")
fil=open("usedip","r+")
z=fil.read()
fil.write(";ip_JT:{}".format(ip_JT))
fil.close()
os.system("clear");
