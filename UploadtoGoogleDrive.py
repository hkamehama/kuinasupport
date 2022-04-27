from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import os
import csv
import time
from GoogleDrivefunc import getGoogleService, uploadFileToGoogleDrive

remotedirID = "1FMtBQwq_2vdzSQkxrVc08ratjUKWxSFs" #ファイルをアップロードするフォルダの末尾のID
keyFile = "client_secret.json" # ドライブに接続するためのjson設定ファイル
dirname = "RECdatas/"

#あとから値を代入する変数郡
fileID = ""
fileName = ""

try:
    while True:
        files = os.listdir(dirname)
        if len(files) > 0:
            files.sort()
            filepath = dirname + files[0]

            getGoogleService(keyFile)
            fileID = uploadFileToGoogleDrive(files[0], filepath, remotedirID, keyFile)
            with open('Logs/UploadLog.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([files[0], fileID])
            os.remove(filepath)
        else :
            time.sleep(100)
            print("wait")



except KeyboardInterrupt:
    print("Ctrl+C finished")