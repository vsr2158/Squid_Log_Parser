#import pdb; pdb.set_trace()
#f = open('/var/log/squid/access.log', "r")
f = open('squid-access.log', "r")
lines = f.readlines()
f.close()
cluster_ip = raw_input("Enter Cluster IPAddr : ")
print ("Compiling Unique URLs for cluster : " + cluster_ip)
uniqurllist = []
for l in lines:
    splitted = l.split()
#    print splitted
    if splitted[2] == cluster_ip:
        if splitted[6] not in uniqurllist:
            uniqurllist.append(splitted[6])

for item in uniqurllist:
    print item

print "++++ DONE ++++"
