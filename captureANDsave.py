import cv2
import dropbox
import time
import random

start_time=time.time()

def snapTaker():

    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        imageName = "img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        
        start_time = time.time

        result=False
    return imageName
    #print("snapshot taken!!")

    #videoCaptureObject.release()
    #cv2.destroyAllWindows()

def uploadFile(imageName):
    passcode = "sl.A0ZRxtuBzAoY4K-o36qu3EihCRIBMmHxR36R2QSFIMgEw8NkMx2fIMzqpXRvLgefnwL5S-LxjCMiOeQFjOqk5TzFqCWqF_iX701Sg4M3fIaoiziPFrp5HCpNWZf110vvaT6uajs"
    file=imageName
    file_from = file
    file_to = "/newFolder1/"+(imageName)
    dbx=dropbox.Dropbox(passcode)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File has been uploaded!!")

def main():
    while (True):
        if((time.time()-start_time)>= 300):
            name=snapTaker()
            uploadFile(name)        
   

    

snapTaker() 