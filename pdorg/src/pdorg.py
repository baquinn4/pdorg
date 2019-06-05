
import os
import queue
import subprocess
import shutil

os.chdir("../../")
#file = open("temp_data.txt","r")


nameQueue = queue.Queue(0)


#print(linedata[34:])
#print(linedata[34:87])
#print(linedata.find("\n"))
#testrr = linedata[34:87]
cwd = os.getcwd()
#print(cwd)

#shutil.move(cwd + "/" + testrr, cwd + "/test")

#colon is at index 32
#linedata = file.readline()
counter = 0


with open("temp_data.txt") as f:
	for linedata in f:
		if "File Name" in linedata:
			nameQueue.put(linedata[34:len(linedata)-1])
			counter = counter + 1
		if "Date/" in linedata:
			if counter != 1:
				while counter > 1:
					nameQueue.get()
					counter = counter - 1
			try:		
				os.mkdir(linedata[34:38])
			except FileExistsError:
				pass

			filename = nameQueue.get()
			counter = counter - 1
			try:
				shutil.move(cwd + "/" + filename, cwd + "/" + linedata[34:38])
			except shutil.Error:
				pass
		print("moved")

	
	
	#if "Date" in data:


