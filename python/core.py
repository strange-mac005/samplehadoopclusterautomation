def core_set(c):	
	x=open("/etc/hadoop/core-site.xml","r")	
	z=x.read()
	pos=z.find('<configuration>')
	pos+=15
	x.close()
	x=open("/etc/hadoop/core-site.xml","r+")
	x.read(pos)
	x.write("\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n</configuration>".format(c))



