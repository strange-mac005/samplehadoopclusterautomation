import os
#os.system("python proj.py")
def active_ip():
	ac=open("/root/project/python/activeip","r")
	z=ac.read()
	os.system("clear")
	z=z.split(';')
	x=len(z)#z is list of active ip
	c=0
	print "Active IP"
	while c<x-1:
		print z[c]
		c+=1
def status_ip():	
	r=open("/root/project/python/usedip","r")
	u=r.read()
	r.close();
	uIP=u.split(';')
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
		

