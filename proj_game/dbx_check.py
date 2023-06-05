import dropbox
import os
import base64


def main():
    try:
        dbx = dropbox.Dropbox("{API_KEY}")
        file_location = "/letgetcodewars/Fix me.JPG"
        _, f = dbx.files_download(file_location)
        print(base64.b64encode(f.content))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
