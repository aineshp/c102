import dropbox 
import cv2 
import time
import random
startTime = time.time()
print(startTime)


def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObj = cv2.VideoCapture(0)
    result=True 
    while(result):
        ret,frame = videoCaptureObj.read()
        img_name = 'img'+str(number)+'.png'
        cv2.imwrite(img_name,frame)
        startTime = time.time()
        result = False 
    return(img_name) 
    print('Snapshot taken')   
    print(num)
    videoCaptureObj.release()
    cv2.destroyAllWindows()
def UploadAllFiles(img_name): 
    accesstoken='pZgBk9L6JTwAAAAAAAAAxAS49MoVDGj8uivrBAI0RmaKAB4Z6oRurLKwhXfJyUrE9'
    file1=(img_name)
    file_from=file1
    file_to='Python/'+(img_name)
    dbx = dropbox.Dropbox(accesstoken)     
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print('File Uploaded')

     
def main():
    while(True):
        if((time.time()-startTime)>=3):
            name = take_snapshot()       
            UploadAllFiles(name)
main()