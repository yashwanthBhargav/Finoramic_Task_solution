import json
import os

with open ('f1.json') as f:
	data= json.load(f)

error=[]

for i in range(len(data["Dependencies"])):
	if os.system("pip install "+data["Dependencies"][i])==0:
		pass
	else:
		error.append(data["Dependencies"][i])
		continue

print "-----------------------------------------------------"
print "--RESULT--"
if error==[]:
	print "          success"
else:
	print "Followig modules didn't install:"
	for j in error:
		print "          "+ str(j)+"\n"
