#!/usr/bin/python3 
print("content-type:text/plain")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()
expose_deployname = form.getvalue("expose_deployname")
command="kubectl expose deployment  {} --type=NodePort --port=80".format(expose_deployname)	
output=sp.getoutput(command+"  --kubeconfig /home/kruparaju/admin.conf")
print(output)
