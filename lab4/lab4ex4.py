import json
def fill(n, c):
    s=""
    for i in range(n):
        s+=c
    return s

with open("jfile.json","r") as json_file:
    a=json_file.read()
b=json.loads(a)
print("Status")
print("===========================================================================================================")
print("DN____________________________________________________________    Description__________    Speed__    MTU__")
#       2     60                                                       4     11          10     4    5  2  4   3 2
for bi in b["imdata"]:
    #s=bi["l1PhysIf"]["attributes"]["dn"].ljust(71-len(bi["l1PhysIf"]["attributes"]["dn"]))
   # s.ljust(46-len(bi["l1PhysIf"]["attributes"]["dn"])," ")
    #s.ljust(25)
   # s=s+bi["l1PhysIf"]["attributes"]["speed"]
    #s.ljust(11-len(bi["l1PhysIf"]["attributes"]["speed"])," ")
    #s=s+bi["l1PhysIf"]["attributes"]["mtu"]

    s=bi["l1PhysIf"]["attributes"]["dn"]+fill(91-len(bi["l1PhysIf"]["attributes"]["dn"])," ")+bi["l1PhysIf"]["attributes"]["speed"]+fill(11-len(bi["l1PhysIf"]["attributes"]["speed"])," ")+bi["l1PhysIf"]["attributes"]["mtu"]
    '''
    s+=fill(s,91-len(bi["l1PhysIf"]["attributes"]["dn"])," ")
    s+=bi["l1PhysIf"]["attributes"]["speed"]
    s+=fill(s,11-len(bi["l1PhysIf"]["attributes"]["speed"])," ")
    s+=bi["l1PhysIf"]["attributes"]["mtu"]'''
    print(s)
