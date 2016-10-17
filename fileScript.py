import os
import glob
import shutil
import time

def fileDirectory(path):
    filesDir = os.listdir(path)
    return filesDir

def listSpecificFile (path, fileType):
    pdfFilesDir = [name for name in os.listdir(path) if name.endswith(fileType)]
    return pdfFilesDir

def removeFiles (path):
    ##path must end with "/*" to work##
    files = glob.glob(path)
    for f in files:
        os.remove(f)

def moveFiles (file_name, destination_path):
    shutil.move(file_name, destination_path)

def main_controller ():
	gDrive_path ='/usr/local/google/home/gilaguilar/AppEngineDevelopment/app-engine-bootcamp'
	temp_file_path = '/usr/local/google/home/gilaguilar/AppEngineDevelopment/app-engine-bootcamp/temp'
	pdf_files_dir = listSpecificFile(gDrive_path,'.pdf')
	counter = 0
	while counter < len(pdf_files_dir):
		moveFiles(pdf_files_dir[counter], temp_file_path)
		counter = counter + 1

	removeFiles(temp_file_path+'/*')
