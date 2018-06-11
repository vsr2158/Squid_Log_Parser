#import pdb; pdb.set_trace()
f = open('/var/log/squid/access.log', "r")
lines = f.readlines()
f.close()

uniqiplist = []
for l in lines:
    splitted = l.split()
    if splitted[2] not in uniqiplist:
        uniqiplist.append(splitted[2])

print uniqiplist
print "++++ DONE ++++"