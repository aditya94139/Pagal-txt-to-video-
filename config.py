import os

API_ID = API_ID = 22946135

API_HASH = os.environ.get("API_HASH", "93e1b0c387cabe34a3ccfa1724ae8527")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7313088857:AAFTKLis7R15rOsxgKuzVHNAZjzbNRCqUlc")

PASS_DB = int(os.environ.get("PASS_DB", "mongodb+srv://mehoca2283:q9unKKrK4gAZvf7U@cluster0.imuhxkw.mongodb.net/?retryWrites=true&w=majority"))

OWNER = int(os.environ.get("OWNER", 7062964338))

LOG = -1002231302276,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7062964338").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


