import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)

def main():
    access_token="aWNp8inDBVgAAAAAAAAAAXSWTROYHYEycGgboAngCnlMHiQ7iyTYbx6hbwbxtq-0"
    transferData=TransferData(access_token)
    file_from="xyz.txt"
    file_to="/test_dropbox/xyz.txt"
    transferData.upload_file(file_from,file_to)
    print("File Moved!")

main()