from time import sleep
from threading import Thread
import subprocess
import re
import filecmp
import sys

#Receive the cmd line arguments in string variable
string=str(sys.argv[1])    
            	
status=-1
#Split String to get Language,question number,username
language=string[0:1]
event=string[1:3]
qnum=string[3:5]
username=string[5:]
snooziness = 5

def loop_detect():
    while True:
        pass

f=open('user_data/out_'+username,'w') #output file
os.chmod('user_data/out_'+username, 0777);	
    


#Run C code
def compileC():
    t = Thread(target=loop_detect)  # run the some_task function in another
                              # thread
    t.daemon = True               # Python will exit when the main thread
                              # exits, even if this thread is still
                              # running
    t.start()
    sleep(snooziness)
    
    #global language,qnum,username,statuspython compiler.py 10115ankush.26.11@gmail.com
    compile = 'gcc -std=gnu99 -w -O2 -fomit-frame-pointer -lm files/event_'+event +'/ques_'+qnum+'/'+ username + '.c -o user_data/' + username + ' 2>' + ' user_data/err_' + username
    execute = "./user_data/" + username + " < in_files/in_" +event+'_'+ qnum+" > user_data/out_" + username+"_" + event+'_'+ qnum
    
    #File for dumping errors
    
    f1 = open('user_data/err_'+username,'w+')
    #Compile code and check for compile time errors
    subprocess.call([compile],shell=True)	
    
    #If there is no compile error then run binary 
    if (f1.read() != ""):
        status=3 #ce
    else:
        subprocess.call([execute],shell=True)
        #Check for run time errors
        if(f1.read() == ""): 
        
            #If no Errors then compare files 
            if(filecmp.cmp('user_data/out_'+username+'_'+event+'_'+ qnum, 'out_files/out_'+event+'_'+ qnum)==True):
                status=1
            else:
                status=2 #wa
        else:
            #If run time error
            status=4	#re 
        subprocess.call(['rm user_data/out_'+username+"_"+event+'_'+qnum],shell=True)
    print status
    
    
def compilePY():
    t = Thread(target=loop_detect)  # run the some_task function in another
                                    # thread
    t.daemon = True               # Python will exit when the main thread
                              # exits, even if this thread is still
                              # running
    t.start()
    sleep(snooziness)
    #open error file
    f1 = open('user_data/err_'+username,'w')
    cmd='python files/event_'+event +'/ques_'+qnum+'/'+ username +'.py ' + '< in_files/in_'+event+'_'+ qnum+' >user_data/out_'+username+'_'+event+'_'+ qnum+' 2>user_data/err_'+username
    #run the code
    subprocess.call([cmd],shell=True)
    #close file
    f1.close()
    #open error file for read
    f1 = open('user_data/err_'+username,'r')
    #if there is an error put it in pyError
    if(f1.read()!=""):
        status=3	#error
    #else compare files````
    else:	
        if(filecmp.cmp('user_data/out_'+username+"_"+event+'_'+ qnum, 'out_files/out_'+event+'_'+ qnum)==True):
            status=1 #ca
        else:    status=2 #wa
        subprocess.call(['rm user_data/out_'+username+"_"+event+'_'+qnum],shell=True)
    print status
    



def compileCPP():
    t = Thread(target=loop_detect)  # run the some_task function in another
                              # thread
    t.daemon = True               # Python will exit when the main thread
                              # exits, even if this thread is still
                              # running
    t.start()
    sleep(snooziness)
    #global language,qnum,username,status
    compile = 'g++ files/event_'+event +'/ques_'+qnum+'/' + username + '.cpp -o user_data/' + username + ' 2>' + ' user_data/err_' + username
    execute = "./user_data/" + username + " < in_files/in_" +event+'_'+ qnum +" > user_data/out_" + username+"_" + event+'_'+ qnum
    
    #File for dumping errors
    f1 = open('user_data/err_'+username,'w+')   

    #Compile code and check for compile time errors
    subprocess.call([compile],shell=True)   
    #If there is no compile error then run binary 
    if (f1.read() != ""):				
    	status=3 #ce
    else:
        subprocess.call([execute],shell=True)
    
        #Check for run time errors
        if(f1.read() == ""): 
            #If no Errors then compare files 
            if(filecmp.cmp('user_data/out_'+username+'_'+event+'_'+ qnum, 'out_files/out_'+event+'_'+ qnum)==True):
                status=1 #ca
        
            else:
                status=2 #wa
        else:
            #If run time error
            status=4	#re 
        subprocess.call(['rm user_data/out_'+username+"_"+event+'_'+qnum],shell=True)
    print status
    
        
        

'''
def compileJAVA():
    t = Thread(target=loop_detect)  # run the some_task function in another
                              # thread
    t.daemon = True               # Python will exit when the main thread
                              # exits, even if this thread is still
                              # running
    t.start()
    sleep(snooziness)
    #global language,qnum,username,status
    compile = 'javac files/' + username + '.java' + ' 2>' + ' user_data/err_' + username
    execute = "java /user_data/" + username + " < in_files/in_" + qnum +" > user_data/out_" + username+"_" + qnum
    
    #File for dumping errors
    f1 = open('user_data/err_'+username,'w+')   
    f2= open('user_data/garari','r')
    
    #Compile code and check for compile time errors
    subprocess.call([compile],shell=True)   
    
    #If there is no compile error then run binary 
   
    subprocess.call([execute],shell=True)
    
    #Check for run time errors
    if(f1.read() == ""): 
        #If no Errors then compare files 
        if(filecmp.cmp('user_data/out_'+username+'_'+qnum, 'out_files/out_'+qnum)==True):
            status=1 #ca
        
        else:
            status=2 #wa
    else:
        #If run time error
        status=4	#re 
    subprocess.call(['rm user_data/out_'+username+"_"+qnum],shell=True)
    print status
''' 
        

#If language is C==01
if(language=="1"):
    compileC()
    
#If language is PY==03
if(language=="3"):
    compilePY()
#If language is C++==02
if(language=="2"):
    compileCPP()
    





subprocess.call(['rm user_data/out_'+username],shell=True)
subprocess.call(['rm user_data/err_'+username],shell=True)
'''
if(filecmp.cmp('user_data/out_'+username+"_"+qnum, 'out_files/out_'+qnum)==True):
	status=1 #ca
else:
	status=2 #wa


subprocess.call(['rm user_data/out_'+username+"_"+qnum],shell=True)
subprocess.call(['rm user_data/out_'+username],shell=True)

echo status
'''
