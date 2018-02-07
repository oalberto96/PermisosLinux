import os

groups = ["zeppelin", "spiritbox", "korn"]

users = {"page": groups[0], "plant": [0],
 "laplante": groups[1], "davis": groups[2]}


for user in users:
	os.system("rm -r " + user )
	os.system("sudo userdel " + user)

for group in groups:
	os.system("sudo groupdel " + group)
