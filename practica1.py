import os

groups = ["zeppelin", "spiritbox", "korn"]

users = {"page": groups[0], "plant": groups[0],
 "laplante": groups[1], "davis": groups[2]}

cpath = os.popen("pwd").read()

for grup in groups:
	os.system("sudo groupadd " + grup)

for user in users:
	os.system("mkdir " + user)
	os.system("sudo useradd " + " -d " + cpath.strip() + "/" + user + " " + user + " -g " + users.get(user) + " -p password" )

