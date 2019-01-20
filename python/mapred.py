def mapred_setup(c):	
	ma=open("/root/project/trackers/mapred-site.xml","r")	
	r=ma.read()
	pos=r.find("<configuration>")
	pos+=15
	x=open("/root/project/trackers/mapred-site.xml","r+")	
	x.read(pos)
	x.write("\n<property>\n<name>mapred.job.tracker</name>\n<value>{}:9002</value>\n</property>\n</configuration>".format(c))


