#!/usr/bin/python3 
print("content-type:text/plain")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()
podname = form.getvalue("podname")
imgname = form.getvalue("podimage")
command="kubectl run {} --image={}".format(podname,imgname)
output=sp.getoutput(command+"  --kubeconfig /home/kruparaju/admin.conf")
print(output)
