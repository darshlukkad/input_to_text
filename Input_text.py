import pyttsx3
import os
username='IIEC'
password='IIEC'
i=0
while (i==0):
	print("username : ")
	pyttsx3.speak("give username")
	u=input()
	print("password : ")
	pyttsx3.speak("give password")
	s=input()
	if username==u and  password==s :
		print("Logged in successfully!!!\n")
		while(True) :
			print("How can I help you : ")
			pyttsx3.speak("How can I help you?")
			p=input()
			if ( ("start" in p) or ("run" in p) or ("open" in p) or ("execute" in p) ) and ( ("google chrome" in p) or ("browser" in p) or ("chrome" in p) ) :
				if ("don't" in p) or ("not" in p) or ("dont" in p) :
					continue
				os.system("start chrome")
			elif ( ("start" in p) or ("run" in p) or ("open" in p) or ("execute" in p) ) and ( ("Notepad" in p) or ("text editor" in p) or("editor" in p)) :
				if ("don't" in p) or ("not" in p) or ("dont" in p) :
					continue
				os.system("notepad")
			elif ( ("start" in p) or ("run" in p) or ("open" in p) or ("execute" in p) ) and ( ("windows media player" in p) or ("media player" in p) or ("wmplayer" in p) ) :
				if ("don't" in p) or ("not" in p) or ("dont" in p) :
					continue
				os.system("start wmplayer")
			elif ( ("start" in p) or ("run" in p) or ("open" in p) or ("execute" in p) ) and ( ("file explorer" in p) or ("file manager" in p) or ("explorer" in p) ) :
				if ("don't" in p) or ("not" in p) or ("dont" in p) :
					continue
				os.system("explorer")
			elif ("exit"in p) or ("break" in p) or ("stop" in p) :
				if ("don't" in p) or ("not" in p) or ("dont" in p) :
					continue
				break
			elif ( ("start" in p) or ("run" in p) or ("open" in p) or ("execute" in p) ) and ( ("control panel" in p) or ("panel" in p) ) :
				if ("don't" in p) or ("not" in p) or ("dont" in p) :
					continue
				os.system("control panel")
			elif ( ("start" in p) or ("run" in p) or ("open" in p) or ("execute" in p) ) and ( ("jupyter notebook" in p) or ("jupyter" in p) or ("notebook" in p) ) :
				if ("don't" in p) or ("not" in p) or ("dont" in p) :
					continue
				os.system("jupyter notebook")
			elif ( ("start" in p) or ("run" in p) or ("open" in p) or ("execute" in p) ) and ( ("calculator" in p) or ("calc" in p) ) :
				if ("don't" in p) or ("not" in p) or ("dont" in p) :
					continue
				os.system("calc")
			elif ("date" in p) :
				if ("don't" in p) or ("not" in p) or ("dont" in p) :
					continue
				os.system("date")
				os.system("\n")
			elif (" current directory"in p) or (" dir " in p) or ("destination" in p) :
				os.system("dir")
			elif ("clear screen" in p) or ("clear" in p) :
				os.system("cls")
			elif ("time" in p) :
				if ("don't" in p) or ("not" in p) or ("dont" in p) :
					continue
				os.system("date")
				os.system("\n")
			elif ("display" in p) or ("computer address" in p) or ("mac address" in p) :
				os.system("getmac")
			elif ( ("start" in p) or ("run" in p) or ("open" in p) or ("execute" in p) ) and ("paint" in p) :
				if ("don't" in p) or ("not" in p) or ("dont" in p) :
					continue
				os.system("mspaint")
			elif ("display" in p) or ("network address" in p) or ("IP address" in p) or("IP" in p) :
				os.system("ipconfig")
			elif("putty" in p) :
				os.system("putty")

			elif ("create directory" in p) or ("create folder" in p) or ("new folder" in p) :
				pyttsx3.speak("provide name for the directory")
				print("provide name for the directory : ")
				x=input()
				x="mkdir "+x
				os.system(x)
				print("new directory created succesfully!!")
			elif ("remove directory" in p) or ("delete folder" in p) :
				pyttsx3.speak("provide name of the directory")
				print("provide name of the directory : ")
				x=input()
				x="rmdir "+x
				os.system(x)
				print("directory removed succesfully!!")
			else :
				pyttsx3.speak("try something else, sorry for inconvenience")
				print("don't support")

			

			
	else :
		print("wrong credentials \n")	
	print("do you want to go back to login or want to exit ?  :")
	s=input()
	if ("yes" in s) or ("okay" in s) or ("alright" in s) or ("done" in s) or ("login" in s) : 
		if ("don't" in s) or ("not" in s) or ("dont" in s) :
			i=1
			break
		else :
			i=0
	elif "no" in s :
		i=1
		pyttsx3.speak("Thank you!!")