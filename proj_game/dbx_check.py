import dropbox
import os
import base64


def main():
    try:
        dbx = dropbox.Dropbox("o1EsRhw7NlYAAAAAAAAAAVDOBRwtghtZjR3u0ni7WRNxcQy-lnW81V5DK0ekpjmv")
        file_location = "/letgetcodewars/Fix me.JPG"
        _, f = dbx.files_download(file_location)
        print(base64.b64encode(f.content))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
