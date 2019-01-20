import os
import core
ac=open("activeip","r")
z=ac.read()
os.system("clear")
z=z.split(';')
x=len(z)#z is list of active nodes
c=0
ac.close()
while c<x-1:
	print z[c]
	c+=1

con=0
while con!=2:
	ip_NN=raw_input("Enter IP For Name Node")
	if ip_NN in z:
		con=2
	else:
		print "Enter Valid IP"

core.core_set(ip_NN)#setup core-site.xml
c=0
while c<x-1:
	os.system("sshpass -p redhat scp /etc/hadoop/core-site.xml {}:/etc/hadoop/ ".format(z[c]))#core site Setup
	c+=1
os.system("sshpass -p redhat scp /root/project/namenode/hdfs-site.xml {}:/etc/hadoop/ ".format(ip_NN))#hdfs-site Setup
print "Setup Done"
raw_input("Press Enter To start name node")
os.system("sshpass -p redhat ssh root@{} 'iptables -F'".format(ip_NN))
os.system("sshpass -p redhat ssh root@{} 'hadoop-daemon.sh start namenode'".format(ip_NN))
os.system("sshpass -p redhat ssh root@{} 'hadoop namenode -format'".format(ip_NN))
raw_input("Name Node Set Press Enter ")
os.system("clear")
fil=open("usedip","w")
fil.write("ip_NN:{}".format(ip_NN))
fil.close()
