""" DO NOT EDIT FILE UNLESS YOU KNOW WHAT YOU'RE DOING!!
This app has been made by Lapis Pheonix#2194
If you edit this project please put your name under Editors:

Editors:

"""


import config
import embed
from dhooks import Webhook

def main():
    try:
        hook = Webhook(config.webhook)
    except:
        print("[ERROR] Your webhook is invalid!\n Check your webhook in config.py")

    if config.ALERT is True:

        try:
            if config.directPing != "USER ID":
                hook.send(f"@everyone <@{config.directPing}>", embed=embed.Embed.embed)
                print("Webhook sent.")
            else:
                hook.send("@everyone", embed=embed.Embed.embed)
        except:
            print("[ERROR] Could not send webhook!")
            print("Check your webhook!")
        finally:
            print("Press ENTER to exit..")
            input()
            exit(0)

    elif config.ALERT is False:

        try:
            if config.directPing != "USER ID":
                hook.send(f"<@{config.directPing}>", embed=embed.Embed.embed)
                print("Webhook sent.")
            else:
                hook.send(embed=embed.Embed.embed)
                print("Webhook sent.")
        except:
            print("[ERROR] Could not send webhook!")
            print("Check your webhook!")
        finally:
            print("Press ENTER to exit..")
            input()
            exit(0)

if __name__ == "__main__":
    main()
