import os
import speech_recognition as sr
import pyttsx3
import time
print("===================welcome_To_automation==================n")

pyttsx3.speak("welcome to hybrid automation")
print('say Partition to Create new partition')
print('say Hadoop to configure hadoop setup')
r = sr.Recognizer()
while True:
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		print("start say...")
		audio = r.listen(source)
		print("speech done..")
		p = r.recognize_google(audio)
		print("you said..  " + p) 
		if(("Partition" in p) or ("partition" in p)) or (("create Partition for me" in p) or ("Create Partition For Me" in p)) :
			print("Input your device name : i.e. /dev/sdb")
			pyttsx3.speak("tell your device name")
			os.system("fdisk -l")
			x = input()
			pyttsx3.speak("you enter : " + x)
			print("are you sure your divece name is correct if yes the press 1")
			pyttsx3.speak("are you sure your divece name is correct if yes the press 1")
			print("say.. create partition")
			with sr.Microphone() as source:
				r.adjust_for_ambient_noise(source)
				print("start say...")
				audio = r.listen(source)
				print("speech done..")
				p = r.recognize_google(audio)
				print("you said..  " + p)
				if(("create partition" in p) or ("Create Partition" in p)):
					os.system("fdisk %s"%x)
					os.system("n")
				else:
					print("Dont support.....")


		elif(("hadoop" in p) or ("Hadoop" in p)) or (("open hadoop" in p) or ("run hadoop" in p)):
			os.chdir('/etc/hadoop')
			os.system("ls")
			print("for cluster, what You want to Make... Namenode or Datanode")
			print("")
			print("")
			os.system("tput setaf 1")
			print("want to make namenode say...namenode")
			print("want to make datanode say...datanode")
			print("")
			t = 10
			for i in range(t):
				print(str(t - i) + "second remain" )
				time.sleep(1)
			with sr.Microphone() as source:
				r.adjust_for_ambient_noise(source)
				print("start say...")
				audio =  r.listen(source)
				print("speech done")
				p = r.recognize_google(audio)
				print("you said.." + p)
				if(("namenode" in p) or ("Namenode" in p)):
					if os.path.exists('nn'):
						os.rmdir('nn')
						os.mkdir('nn')
						pyttsx3.speak("wait a second directory is removing")
						time.sleep(2)
						print("older namenode directory is removed")
						os.system("tput setaf 6")
						pyttsx3.speak("wait a second new namenode directory is creating for you")
						time.sleep(2)
						pyttsx3.speak("directory is created for you")
						print("new namenode Directory is created")
						time.sleep(5)
						pyttsx3.speak("wait a second we are configuring hdfs-site for you..")
						
					elif not os.path.exists('nn'):
						pyttsx3.speak("wait a second for the first time namenode directory is creating for you")
						time.sleep(2)
						os.mkdir('nn')
						print("new Namenode Directory is Created")
					else:
						print("dont support")
						time.sleep(5)
				elif(("datanode" in p) or ("Datanode" in p)) or (("data node" in p) or ("Data Node" in p)):
					if os.path.exists('dn'):
						os.system("tput setaf 9")
						pyttsx3.speak("wait a second we removing previous datanode directory")
						os.rmdir('dn')
						time.sleep(2)
						pyttsx3.speak("directory is removed")
						print("directory is removed")
						pyttsx3.speak("new datanode directory is creating for you")
						print("directory is creating..wait a sec..")
						time.sleep(2)
						os.mkdir('dn')
						pyttsx3.speak("directory is created for you")
						print("directory is created")
					elif not os.path.exists('dn'):
						pyttsx3.speak("wait a second we creating new datanode directory for you")
						print("New datanode Directory is creating for you..")
						time.sleep(2)
						os.mkdir('dn')
						pyttsx3.speak("directroy is created")
						print("new datanode directory is created")
					
				else:
					print("dont support")
		else:
			print("dont support")
