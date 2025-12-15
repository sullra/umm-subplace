import time

cookie = ""
PlaceID = False
isPrivateServer = False
privateserverID = ""

def do_Inputs():
    PlaceId = str(input("Please input the place id of the game!"))

    cookie = str(input("Please input your roblox cookie (leave blank to auto-detect)"))

    checkForPrivate = str(input("Is there a private server? (Y/N)"))

    while checkForPrivate.lower() != "y" or checkForPrivate.lower() != "n":
        print(checkForPrivate.lower(), checkForPrivate.lower() != "n")
        time.sleep(0.01)
        checkForPrivate = str(input("It appears you did a typo, please type 'Y' or 'N' to indicate if there is a private server?"))
    
    if checkForPrivate.lower == "y":
        isPrivateServer = True
        privateserverID = "?privateServerLinkCode=" + str(input("Please input the bit after the '?privateServerLinkCode=' e.g: '8236306244555044u7280d0238655898' Note: if this is wrong this could break the script"))


do_Inputs()