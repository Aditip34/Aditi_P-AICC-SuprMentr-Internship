import hashlib
import re

users = {}

def hash_password(p):
    return hashlib.sha256(p.encode()).hexdigest()

def valid(p):
    return (len(p)>=8 and re.search("[A-Z]",p) and re.search("[a-z]",p)
            and re.search("[0-9]",p) and re.search("[!@#$%^&*]",p))

u = input("Username: ")
p = input("Password: ")

if valid(p):
    users[u] = hash_password(p)
    print("Registered")

if users.get(u) == hash_password(input("Login Password: ")):
    print("Login Success")