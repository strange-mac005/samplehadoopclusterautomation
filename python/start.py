import os
import show_ip
#os.system("python /root/project/python/proj.py")
z=[]
x=0#z is list of active nodes
c=0

nnC=3
jtC=3#to check if the nodes are already up
r=open("/root/project/python/usedip","r")
u=r.read()
r.close();
uIP=u.split(';')
show_ip.active_ip()
if u!="":
	print "Used IP"
for v in uIP:
	if v[0:5]=='ip_NN':
		print "IP for Name Node Is {}".format(v[5:])
		nnC=0
	elif v[0:5]=='ip_JT':
		print "IP for Job Tracker Is {}".format(v[5:])
		jtC=0
	elif v[0:5]=='ip_DN':
		print "IP for Data Ndoe Task Tracker Is {}".format(v[5:])
inp=0
while inp!=5:
	print "\t\t\t1 to Setup Name Node"
	print "\t\t\t2 to Setup JobTracker"
	print "\t\t\t3 to Setup Data Node and TaskTracker"
	print "\t\t\t4 to Check Status"
	print "\t\t\t 5 to Exit"
	inp=int(raw_input())
	if inp==1:
		if nnC!=0:
			nnC=0
			os.system("python /root/project/python/nameNode.py")
		else:
			print "Name Node Already Set up"
	if inp==2:
		if jtC!=0 and nnC==0:
			jtC=0
			os.system("python /root/project/python/jobtracker.py ")
		elif nnC!=0:
			print "Set Name Node First"
		else:
			print "Jobtracker Already Setup"
	if inp==3:
		if jtC!=0 and nnC!=0:
			os.system("python /root/project/python/datanode.py")
		else:
			print"Job Tracker or Name Node not set"
	if inp==4:
		show_ip.active_ip();
		show_ip.status_ip()
	if inp==5:
		exit

