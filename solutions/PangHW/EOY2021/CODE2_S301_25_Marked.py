vals = []

val = input("Input signal fragment: ")
vals.append(val)
while val != "!END":
    val = input("Input signal fragment (or end with '!END'): ")
    vals.append(val)
vals = vals[:-1]

lodd = len(vals)//2

om = []

for i in range(lodd):
    om.append(vals[lodd+i])
    om.append(vals[i])

if len(vals)%2!=0:
    om.append(vals[-1])

print("OM is: {}".format(' '.join(om)))
print("The length of OM is: {}".format( len(vals)+len(vals[0])-1 ))

omg = om[0]+"".join([x[-1] for x in om[1:]])    #Q13 1/4, 2/4, 3/4

print("OM full string is: {}".format(omg))      #Q13 4/4

#Q13 4/4
