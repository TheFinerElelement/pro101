import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BIFWmPcIs4QxbJvUTzRAkCC-8UqteJfOqyoBxwnTEVXJuyVg0X7y6m8tS-143CKJSrjQC3FNNziUrGi25PBAVM4i72Wpa52UD0NCYCXspPV_dwCZUVtXSZW2ImiMZTJ2aA2IdVpfuPAv'
    transferData = TransferData(access_token)

    file_from = 'testing.txt'
    file_to = '/test_dropbox/testing.txt'  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()