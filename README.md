# kubernetes-webapp
Feature - 
👉 It can launch pods with specific name given by user.  
👉 Run deployment using image and name given by user.  
👉 Expose services on given user input port number.  
👉 Scale the replica according to user need.  
👉 Delete complete environment created.  
👉 Delete specific resources given by user. 
👉 Extra features related to k8s ( Optional)  Note - There should be webUI based menu display so that user can get to know what your webapp can do. 

# Idea 
As we know managing the kubernetes with the help of commands is very boaring and time consuming task 
so I came with the idea that we can manage the kubernetes with the help of website that will created very easily and easy to manage without the commands

# Tools and Technologies
1.AWS
2.Kubernetes multinode cluster
3.HTML, CSS and Javascript with python at the backend


### steps

##### Step1 : 
first of all we have to launch three ec2 instances on AWS cloud so that we can run our kubernetes cluster there.
I am going to privode a file which contains how to setup the kubernetes cluster

![alt txt](https://github.com/abhikesare9/kubernetes-webapp/blob/e7911edd994e2f1efffa880081bbe1bb36c2b3eb/images/1.png)


After setting the master your controle plane will look like below

![alt txt](https://github.com/abhikesare9/kubernetes-webapp/blob/e7911edd994e2f1efffa880081bbe1bb36c2b3eb/images/2.png)

Similarly, according to the script setup the node and configure the cluster


#### Step2 : 
You have to install the httpd server into your system and copy html,css and js code to /var/www/html

![alt txt](https://github.com/abhikesare9/kubernetes-webapp/blob/main/images/httpd%20install.png)
![alt txt](https://github.com/abhikesare9/kubernetes-webapp/blob/main/images/copy%20files.png)

#### step 3 :
you have to copy python files to /var/www/cgi-bin folder of master
![alt txt](https://github.com/abh6ikesare9/kubernetes-webapp/blob/main/images/backend.png)


#### step 4:
In the final step start the httpd server using command systemctl start httpd your website will be ready at port number 80
![alt_txt](https://github.com/abhikesare9/kubernetes-webapp/blob/main/images/webapp.png)

