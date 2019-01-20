x=open("/etc/hadoop/mapred-site.xml","r")
z=x.read()
pos=z.find('<configuration>')
pos+=15
x.close()
x=open("/etc/hadoop/mapred-site.xml","r+")
x.read(pos)
x.write("<property>\n<name>.job.tracker</name>\n<value>hdfs://{}:9002</value>\n</property>\n</configuration>".format(x))

