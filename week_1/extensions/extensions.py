## ask for full name of the file --> tell the type of file it is

# Getting input
name = input("File name: ").lower()

# Cases
if ".gif" in name:
    print("image/gif")

elif ".jpeg" in name:
    print("image/jpeg")

elif ".jpg" in name:
    print("image/jpeg")

elif ".png" in name:
    print("image/png")

elif ".pdf" in name:
    print("application/pdf")

elif ".txt" in name:
    print("text/plain")

elif ".zip" in name:
    print("application/zip")

else:
    print("application/octet-stream")
