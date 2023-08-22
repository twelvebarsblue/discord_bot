import discord
import datetime
import asyncio
import pickle
import gspread
import json
import random

client = discord.Client()

token_main = ""
token_test = ""
id_test_server = 
id_lyn_abuse = 

gc = gspread.service_account(filename = 'service_account.json')
sh = gc.open_by_key("")
worksheet = sh.worksheet('Party List')

party1 = []
party2 = []
party3 = []
gold1 = []
gold2 = []
gold3 = []
immo = []
backup = []
backup2 = []
party1_id = []
party2_id = []
party3_id = []
gold1_id = []
gold2_id = []
gold3_id = []
immo_id = []
backup_id = []
backup2_id = []
donkey_list = []
donkey_facts = ["Donkeys can live for over 50 years",
                "Donkeys are very strong and intelligent",
                "A donkey is stronger than a horse of the same size",
                "Donkeys have an incredible memory – they can recognise areas and other donkeys they were with up to 25 years ago",
                "Donkeys are not easily startled (unlike horses) and have a keen sense of curiosity",
                "Donkeys have a reputation for stubbornness but this is due to their highly developed sense of self preservation. It is difficult to force or frighten a donkey into doing something it sees as contrary to its own best interest or safety",
                "Donkeys are more independent in their thinking than horses and will reason, then make decisions based on their safety",
                "Training a donkey relies upon showing him or her, by words and action, that they can trust you to protect them from harm. They learn what it is we want them to do if we take time to show them",
                "Donkeys originate from desert areas of the earth",
                "In the desert environment a donkey is able to hear the call of another donkey 60 miles away, they have far larger ears than horses. Their large ears also help keep them cool",
                "Because food is scarce in the desert, donkeys utilise 95% of what they eat which means their manure is not a very good fertilizer for land. Their digestive system can break down inedible vegetation and extract moisture from food more efficiently",
                "They don’t like the rain and being out in it for long periods can damage their health as their fur is not waterproof",
                "Donkeys don’t like being kept on their own although a single donkey will live quite happily with goats",
                "A herd will choose the strongest donkey to be their leader, even if domesticated. In the wild the lead donkey would stay to ward off an attack by a wolf or other predators in order to allow the rest of the herd to escape to safety",
                "Donkeys in a herd will groom each other in the same way as monkeys and chimps do",
                "The wealth of the Egyptians was due to the precious metals carried from Africa by donkeys",
                "Donkeys were used to carry silk along the ‘Silk Road’ from the Pacific Ocean to the Mediterranean in return for trade goods",
                "In Greece donkeys were used for working on the narrow paths between vines and their work in vineyards spread as far as Spain",
                "The donkey was associated with the Syrian God of Wine, Dionysius",
                "The Roman Army moved donkeys into Northern Europe using them in agriculture, vineyards and as pack animals",
                "Donkeys came to England with the Roman invasion of Britain in 43CE",
                "Donkeys are often a lifeline to families in many regions of the world. They help with water and wood fuel collection, land cultivation and transportation of produce to market",
                "Donkeys are used as guard animals for cattle, sheep and goats since they have a natural aversion to canines and will keep them away from a flock",
                "Donkeys are often fielded with horses due to the perceived calming effect they have on nervous horses. If a donkey is introduced to a mare and foal, the foal will often turn to the donkey for support after it has left its mother"]
members_dict = {}
organizer_dict ={"party1":"none", "party2":"none", "party3":"none", "gold1":"none", "gold2":"none", "gold3":"none", "immo":"none"}
date1 = ""
date2 = ""
date3 = ""
date4 = ""
date5 = ""
date6 = ""
date7 = ""
msg_1 = ""
msg_2 = ""
msg_3 = ""
msg_4 = ""
msg_5 = ""
msg_6 = ""
msg_7 = ""

with open("party1.txt", "rb") as fp:
    party1 = pickle.load(fp)
with open("party2.txt", "rb") as fp:
    party2 = pickle.load(fp)
with open("party3.txt", "rb") as fp:
    party3 = pickle.load(fp)
with open("gold1.txt", "rb") as fp:
    gold1 = pickle.load(fp)
with open("gold2.txt", "rb") as fp:
    gold2 = pickle.load(fp)
with open("gold3.txt", "rb") as fp:
    gold3 = pickle.load(fp)
with open("immo.txt", "rb") as fp:
    immo = pickle.load(fp)
with open("backup.txt", "rb") as fp:
    backup = pickle.load(fp)
with open("backup2.txt", "rb") as fp:
    backup2 = pickle.load(fp)

with open("party1_id.txt", "rb") as fp:
    party1_id = pickle.load(fp)
with open("party2_id.txt", "rb") as fp:
    party2_id = pickle.load(fp)
with open("party3_id.txt", "rb") as fp:
    party3_id = pickle.load(fp)
with open("gold1_id.txt", "rb") as fp:
    gold1_id = pickle.load(fp)
with open("gold2_id.txt", "rb") as fp:
    gold2_id = pickle.load(fp)
with open("gold3_id.txt", "rb") as fp:
    gold3_id = pickle.load(fp)
with open("immo_id.txt", "rb") as fp:
    immo_id = pickle.load(fp)
with open("backup_id.txt", "rb") as fp:
    backup_id = pickle.load(fp)
with open("backup2.txt", "rb") as fp:
    backup2 = pickle.load(fp)
with open("backup_id.txt", "rb") as fp:
    backup_id = pickle.load(fp)
with open("backup2_id.txt", "rb") as fp:
    backup2_id = pickle.load(fp)

with open("members_dict.txt", "rb") as fp:
    members_dict = pickle.load(fp)
with open("organizer_dict.txt", "rb") as fp:
    organizer_dict = pickle.load(fp)

with open("date1.txt", "rb") as fp:
    date1 = pickle.load(fp)
with open("date2.txt", "rb") as fp:
    date2 = pickle.load(fp)
with open("date3.txt", "rb") as fp:
    date3 = pickle.load(fp)
with open("date4.txt", "rb") as fp:
    date4 = pickle.load(fp)
with open("date5.txt", "rb") as fp:
    date5 = pickle.load(fp)
with open("date6.txt", "rb") as fp:
    date6 = pickle.load(fp)
with open("date7.txt", "rb") as fp:
    date7 = pickle.load(fp)

with open("msg_1.txt", "rb") as fp:
    msg_1 = pickle.load(fp)
with open("msg_2.txt", "rb") as fp:
    msg_2 = pickle.load(fp)
with open("msg_3.txt", "rb") as fp:
    msg_3 = pickle.load(fp)
with open("msg_4.txt", "rb") as fp:
    msg_4 = pickle.load(fp)
with open("msg_5.txt", "rb") as fp:
    msg_5 = pickle.load(fp)
with open("msg_6.txt", "rb") as fp:
    msg_6 = pickle.load(fp)
with open("msg_7.txt", "rb") as fp:
    msg_7 = pickle.load(fp)

async def update_stats():
    await client.wait_until_ready()
    global party1, party2, party3, gold1, gold2, gold3, immo, backup, backup2, party1_id, party2_id, party3_id, gold1_id, gold2_id, gold3_id, immo_id, backup_id, backup2_id, members_dict, organizer_dict, date1, date2, date3, date4, date5, date6, date7, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7
    while not client.is_closed():
        try:
            with open("party1.txt", "wb") as fp:
                pickle.dump(party1, fp)
            with open("party2.txt", "wb") as fp:
                pickle.dump(party2, fp)
            with open("party3.txt", "wb") as fp:
                pickle.dump(party3, fp)
            with open("gold1.txt", "wb") as fp:
                pickle.dump(gold1, fp)
            with open("gold2.txt", "wb") as fp:
                pickle.dump(gold2, fp)
            with open("gold3.txt", "wb") as fp:
                pickle.dump(gold3, fp)
            with open("immo.txt", "wb") as fp:
                pickle.dump(immo, fp)
            with open("backup.txt", "wb") as fp:
                pickle.dump(backup, fp)
            with open("backup2.txt", "wb") as fp:
                pickle.dump(backup2, fp)

            with open("party1_id.txt", "wb") as fp:
                pickle.dump(party1_id, fp)
            with open("party2_id.txt", "wb") as fp:
                pickle.dump(party2_id, fp)
            with open("party3_id.txt", "wb") as fp:
                pickle.dump(party3_id, fp)
            with open("gold1_id.txt", "wb") as fp:
                pickle.dump(gold1_id, fp)
            with open("gold2_id.txt", "wb") as fp:
                pickle.dump(gold2_id, fp)
            with open("gold3_id.txt", "wb") as fp:
                pickle.dump(gold3_id, fp)
            with open("immo_id.txt", "wb") as fp:
                pickle.dump(immo_id, fp)
            with open("backup_id.txt", "wb") as fp:
                pickle.dump(backup_id, fp)
            with open("backup2_id.txt", "wb") as fp:
                pickle.dump(backup2_id, fp)

            with open("members_dict.txt", "wb") as fp:
                pickle.dump(members_dict, fp)
            with open("organizer_dict.txt", "wb") as fp:
                pickle.dump(organizer_dict, fp)

            with open("date1.txt", "wb") as fp:
                pickle.dump(date1, fp)
            with open("date2.txt", "wb") as fp:
                pickle.dump(date2, fp)
            with open("date3.txt", "wb") as fp:
                pickle.dump(date3, fp)
            with open("date4.txt", "wb") as fp:
                pickle.dump(date4, fp)
            with open("date5.txt", "wb") as fp:
                pickle.dump(date5, fp)
            with open("date6.txt", "wb") as fp:
                pickle.dump(date6, fp)
            with open("date7.txt", "wb") as fp:
                pickle.dump(date7, fp)

            with open("msg_1.txt", "wb") as fp:
                pickle.dump(msg_1, fp)
            with open("msg_1.txt", "wb") as fp:
                pickle.dump(msg_2, fp)
            with open("msg_1.txt", "wb") as fp:
                pickle.dump(msg_3, fp)
            with open("msg_1.txt", "wb") as fp:
                pickle.dump(msg_4, fp)
            with open("msg_1.txt", "wb") as fp:
                pickle.dump(msg_5, fp)
            with open("msg_1.txt", "wb") as fp:
                pickle.dump(msg_6, fp)
            with open("msg_1.txt", "wb") as fp:
                pickle.dump(msg_7, fp)

        # Upload to Google Sheet
        # Create lists
            msg_list = [msg_1,msg_2,msg_3,msg_4,msg_5,msg_6,msg_7]
            date_list = [date1,date2,date3,date4,date5,date6,date7]
            parties = [party1, party2, party3, gold1, gold2, gold3, immo, backup, backup2]
            dummy = [[''] * 10 for e in parties]
            msg_sheet_range = ['B{}'.format(i) for i in range(13, 20)]
            date_sheet_range = ['B{}'.format(i) for i in range(22, 29)]
            organizer_dict_range = ['B{}'.format(i) for i in range(31, 38)]
            partyindex = ["party1", "party2", "party3", "gold1", "gold2", "gold3", "immo"]

        # Update party list
            worksheet.batch_update([{
                'range': 'B2:K10',
                'values': dummy,
            }, {
                'range': 'B2:K10',
                'values': parties,
            }])

        # Update message list
            for m, i in zip(msg_list, msg_sheet_range):
                worksheet.update(i, m)
        # Update date list
            for m, i in zip(date_list, date_sheet_range):
                worksheet.update(i, json.dumps(m, default=str))
        # Update organizer list
            for m, i in zip(partyindex, organizer_dict_range):
                worksheet.update(i, organizer_dict[m])


            await asyncio.sleep(100)
        except Exception as e:
            print(e)
            await asyncio.sleep(100)


@client.event
async def on_ready():
    global party1, party2, party3, gold1, gold2, gold3, immo, backup, backup2, party1_id, party2_id, party3_id, gold1_id, gold2_id, gold3_id, immo_id, backup_id, backup2_id, members_dict, organizer_dict, date1, date2, date3, date4, date5, date6, date7, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member): # everyone who joined server will be greeted with this message
    for channel in member.guild.channels:
        if str(channel) == 'general':
            await channel.send(f"""Welcome new abuser {member.mention}""")
            await member.send(f"""Welcome! {member}. Please read #tutorial first on abuse tutorial. Any queries please ask in #general.""")
            await member.send("Type !help in channel #bot-commands for a list of commands of what I can do.")
            await member.send("The rules are simple:")
            await member.send("1. Commit at least 2 games")
            await member.send("2. Able to use discord voice chat to communicate")
            await member.send("3. First come first serve. We use a bot to organize our abuse list now. Please head over to #bot-commands and type !help for a list of useful commands.")
            await member.send("4. Default MVP belongs to the host and cohost. Anyone found trolling will be kicked or banned depending on the host mood. If you need MVP, either learn how to host or ask nicely.")

@client.event
async def on_message(message):
    global party1, party2, party3, gold1, gold2, gold3, immo, backup, backup2, party1_id, party2_id, party3_id, gold1_id, gold2_id, gold3_id, immo_id, backup_id, backup2_id, members_dict, organizer_dict, date1, date2, date3, date4, date5, date6, date7, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, donkey_list
    id = client.get_guild(id_lyn_abuse)
    channels = ["party-search", "tutorial"]
    admins = ["twelve bar blues#2441", "shockpoint#9968", "franzlich#0656"]
    valid_users = [] # Only users in this list can use admin commands

    if str(message.author) in donkey_list:
        await message.delete()
        await message.channel.send(f"""Heehaw? Heehaw. {message.author}""")
        await message.author.send(random.choice(donkey_facts))
        return

    if str(message.channel) in channels:

# User commands

# Displays all the commands currently
        if message.content == '!help':
            embed = discord.Embed(title="Bot Commands")
            embed.add_field(name="!addparty1/2/3", value="Adds yourself to non-gold party 1/2/3")
            embed.add_field(name="!addgold1/2/3", value="Adds yourself to gold party 1/2/3")
            embed.add_field(name="!addimmo", value="Adds yourself to immortal party")
            embed.add_field(name="!addbackup", value="Adds yourself to backup party")
            embed.add_field(name="!addbackup2", value="Adds yourself to gold backup party")
            embed.add_field(name="!whichparty", value="Checks which party you are in")
            embed.add_field(name="!remove", value="Remove yourself from the party list")
            embed.add_field(name="!count", value="Counts the number of players in each party")
            embed.add_field(name="!setorganizer", value="Set yourself as your party organizer")
            embed.add_field(name="!organizer", value="See the organizer for each party. Check !organizerhelp")
            embed.add_field(name="!msg <party>", value="Views the party message")
            embed.add_field(name="!date <party>", value="Checks the current abuse date and time")
            embed.add_field(name="!partylist", value="Views the list of parties available")
            embed.add_field(name="!role <role>", value="Assigns a role - gold300,gold200,gold100,cavern,event,immortal,divine")
            await message.channel.send(content=None, embed=embed)

        if message.content == '!organizerhelp':
            embed = discord.Embed(title="Organizer Commands")
            embed.add_field(name="!setmsg <party>,<message>", value="Sets the message for your party")
            embed.add_field(name="!setdate <party>,<datetime'%d/%m/%y %H:%M:%S'>", value="Set abuse date and time")
            embed.add_field(name="!empty <party>", value="Clears party list")
            embed.add_field(name="!summon <party>", value = "Tags all the members in the party")
            await message.channel.send(content=None, embed=embed)

        if message.content == '!partylist':
            embed = discord.Embed(title="List of parties", description="And how to query")
            embed.add_field(name="party1", value="Join: !addparty1, Date: !date party1, Msg: !msg party1")
            embed.add_field(name="party2", value="Join: !addparty2, Date: !date party2, Msg: !msg party2")
            embed.add_field(name="party3", value="Join: !addparty3, Date: !date party3, Msg: !msg party3")
            embed.add_field(name="gold1", value="Join: !addgold1, Date: !date gold1, Msg: !msg gold1")
            embed.add_field(name="gold2", value="Join: !addgold2, Date: !date gold2, Msg: !msg gold2")
            embed.add_field(name="gold3", value="Join: !addgold3, Date: !date party3, Msg: !msg gold3")
            embed.add_field(name="immo", value="Join: !addimmo, Date: !date immo, Msg: !msg immo")
            embed.add_field(name="backup", value="Join: !addbackup")
            embed.add_field(name="backup2", value="Join: !addbackup2")
            await message.channel.send(content=None, embed=embed)

# This command sets the organizer for their respective party
        if message.content == "!setorganizer":
            partylist = [party1,party2,party3,gold1,gold2,gold3,immo]
            partyindex = ["party1","party2","party3","gold1","gold2","gold3","immo"]
            for list,index in zip(partylist, partyindex):
                if str(message.author) in list:
                    organizer_dict.update({str(index):str(message.author)})
                    await message.channel.send(f"""User {message.author} has been set as the organizer for {index}""")
            if str(message.author) not in organizer_dict.values():
                    await message.channel.send(f"""Error. User {message.author} is not in any main parties!""")

# This command checks the organizer for each party
        if message.content == '!organizer':
            embed = discord.Embed(title="Party organizers")
            embed.add_field(name="Non gold Party 1", value=organizer_dict["party1"])
            embed.add_field(name="Non gold Party 2", value=organizer_dict["party2"])
            embed.add_field(name="Non gold Party 3", value=organizer_dict["party3"])
            embed.add_field(name="Gold Party 1", value=organizer_dict["gold1"])
            embed.add_field(name="Gold Party 2", value=organizer_dict["gold2"])
            embed.add_field(name="Gold Party 3", value=organizer_dict["gold3"])
            embed.add_field(name="Immortal Party", value=organizer_dict["immo"])
            await message.channel.send(content=None, embed=embed)

# This command checks the current abuse date
        if message.content.startswith("!date"):
            if message.content[6:] == "party1":
                if isinstance(date1, datetime.date):
                    await message.channel.send(f"""The current abuse date and time for non gold party 1 is GMT+8 {date1}""")
                else:
                    await message.channel.send(f"""The current abuse date and time for non gold party 1 is yet to be set""")
            elif message.content[6:] == "party2":
                if isinstance(date2, datetime.date):
                    await message.channel.send(f"""The current abuse date and time for non gold party 2 is GMT+8 {date2}""")
                else:
                    await message.channel.send(f"""The current abuse date and time for non gold party 2 is yet to be set""")
            elif message.content[6:] == "party3":
                if isinstance(date3, datetime.date):
                    await message.channel.send(f"""The current abuse date and time for non gold party 3 is GMT+8 {date3}""")
                else:
                    await message.channel.send(f"""The current abuse date and time for non gold party 3 is yet to be set""")
            elif message.content[6:] == "gold1":
                if isinstance(date4, datetime.date):
                    await message.channel.send(f"""The current abuse date and time for gold party 1 is GMT+8 {date4}""")
                else:
                    await message.channel.send(f"""The current abuse date and time for gold party 1 is yet to be set""")
            elif message.content[6:] == "gold2":
                if isinstance(date5, datetime.date):
                    await message.channel.send(f"""The current abuse date and time for gold party 2 is GMT+8 {date5}""")
                else:
                    await message.channel.send(f"""The current abuse date and time for gold party 2 is yet to be set""")
            elif message.content[6:] == "gold3":
                if isinstance(date6, datetime.date):
                    await message.channel.send(f"""The current abuse date and time for gold party 3 is GMT+8 {date6}""")
                else:
                    await message.channel.send(f"""The current abuse date and time for gold party 3 is yet to be set""")
            elif message.content[6:] == "immo":
                if isinstance(date7, datetime.date):
                    await message.channel.send(f"""The current abuse date and time for immortal party is GMT+8 {date7}""")
                else:
                    await message.channel.send(f"""The current abuse date and time for immortal party is yet to be set""")


# This command checks and adds users to the list
        if message.content == "!addparty1":
            if str(message.author) in party1:
                await message.channel.send(f"""Error. User {message.author} is already in party 1!""")
                return
            elif str(message.author) in party2:
                await message.channel.send(f"""Error. User {message.author} is already in party 2!""")
                return
            elif str(message.author) in party3:
                await message.channel.send(f"""Error. User {message.author} is already in party 3!""")
                return
            elif str(message.author) in gold1:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 1!""")
                return
            elif str(message.author) in gold2:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 2!""")
                return
            elif str(message.author) in gold3:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 3!""")
                return
            elif str(message.author) in immo:
                await message.channel.send(f"""Error. User {message.author} is already in immortal party!""")
                return
            elif str(message.author) in backup:
                await message.channel.send(f"""Error. User {message.author} is already in backup!""")
                return
            elif str(message.author) in backup2:
                await message.channel.send(f"""Error. User {message.author} is already in gold backup!""")
                return
            elif len(party1) == 10:
                await message.channel.send(f"""Party 1 is already full. Try other party instead.""")
                return
            else:
                party1_id.append(str(message.author.id))
                party1.append(str(message.author))
                await message.channel.send(party1)
                return

        if message.content == "!addparty2":
            if str(message.author) in party1:
                await message.channel.send(f"""Error. User {message.author} is already in party 1!""")
                return
            elif str(message.author) in party2:
                await message.channel.send(f"""Error. User {message.author} is already in party 2!""")
                return
            elif str(message.author) in party3:
                await message.channel.send(f"""Error. User {message.author} is already in party 3!""")
                return
            elif str(message.author) in gold1:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 1!""")
                return
            elif str(message.author) in gold2:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 2!""")
                return
            elif str(message.author) in gold3:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 3!""")
                return
            elif str(message.author) in immo:
                await message.channel.send(f"""Error. User {message.author} is already in immortal party!""")
                return
            elif str(message.author) in backup:
                await message.channel.send(f"""Error. User {message.author} is already in backup!""")
                return
            elif str(message.author) in backup2:
                await message.channel.send(f"""Error. User {message.author} is already in gold backup!""")
                return
            elif len(party2) == 10:
                await message.channel.send(f"""Party 2 is already full. Try other party instead.""")
                return
            else:
                party2_id.append(str(message.author.id))
                party2.append(str(message.author))
                await message.channel.send(party2)
                return

        if message.content == "!addparty3":
            if str(message.author) in party1:
                await message.channel.send(f"""Error. User {message.author} is already in party 1!""")
                return
            elif str(message.author) in party2:
                await message.channel.send(f"""Error. User {message.author} is already in party 2!""")
                return
            elif str(message.author) in party3:
                await message.channel.send(f"""Error. User {message.author} is already in party 3!""")
                return
            elif str(message.author) in gold1:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 1!""")
                return
            elif str(message.author) in gold2:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 2!""")
                return
            elif str(message.author) in gold3:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 3!""")
                return
            elif str(message.author) in immo:
                await message.channel.send(f"""Error. User {message.author} is already in immortal party!""")
                return
            elif str(message.author) in backup:
                await message.channel.send(f"""Error. User {message.author} is already in backup!""")
                return
            elif str(message.author) in backup2:
                await message.channel.send(f"""Error. User {message.author} is already in gold backup!""")
                return
            elif len(party3) == 10:
                await message.channel.send(f"""Party 3 is already full. Try other party instead.""")
                return
            else:
                party3_id.append(str(message.author.id))
                party3.append(str(message.author))
                await message.channel.send(party3)
                return

        if message.content == "!addgold1":
            if str(message.author) in party1:
                await message.channel.send(f"""Error. User {message.author} is already in party 1!""")
                return
            elif str(message.author) in party2:
                await message.channel.send(f"""Error. User {message.author} is already in party 2!""")
                return
            elif str(message.author) in party3:
                await message.channel.send(f"""Error. User {message.author} is already in party 3!""")
                return
            elif str(message.author) in gold1:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 1!""")
                return
            elif str(message.author) in gold2:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 2!""")
                return
            elif str(message.author) in gold3:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 3!""")
                return
            elif str(message.author) in immo:
                await message.channel.send(f"""Error. User {message.author} is already in immortal party!""")
                return
            elif str(message.author) in backup:
                await message.channel.send(f"""Error. User {message.author} is already in backup!""")
                return
            elif str(message.author) in backup2:
                await message.channel.send(f"""Error. User {message.author} is already in gold backup!""")
                return
            elif len(gold1) == 10:
                await message.channel.send(f"""Gold Party 1 is already full. Try other party instead.""")
                return
            else:
                gold1_id.append(str(message.author.id))
                gold1.append(str(message.author))
                await message.channel.send(gold1)
                return

        if message.content == "!addgold2":
            if str(message.author) in party1:
                await message.channel.send(f"""Error. User {message.author} is already in party 1!""")
                return
            elif str(message.author) in party2:
                await message.channel.send(f"""Error. User {message.author} is already in party 2!""")
                return
            elif str(message.author) in party3:
                await message.channel.send(f"""Error. User {message.author} is already in party 3!""")
                return
            elif str(message.author) in gold1:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 1!""")
                return
            elif str(message.author) in gold2:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 2!""")
                return
            elif str(message.author) in gold3:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 3!""")
                return
            elif str(message.author) in immo:
                await message.channel.send(f"""Error. User {message.author} is already in immortal party!""")
                return
            elif str(message.author) in backup:
                await message.channel.send(f"""Error. User {message.author} is already in backup!""")
                return
            elif str(message.author) in backup2:
                await message.channel.send(f"""Error. User {message.author} is already in gold backup!""")
                return
            elif len(gold2) == 10:
                await message.channel.send(f"""Gold Party 2 is already full. Try other party instead.""")
                return
            else:
                gold2_id.append(str(message.author.id))
                gold2.append(str(message.author))
                await message.channel.send(gold2)
                return

        if message.content == "!addgold3":
            if str(message.author) in party1:
                await message.channel.send(f"""Error. User {message.author} is already in party 1!""")
                return
            elif str(message.author) in party2:
                await message.channel.send(f"""Error. User {message.author} is already in party 2!""")
                return
            elif str(message.author) in party3:
                await message.channel.send(f"""Error. User {message.author} is already in party 3!""")
                return
            elif str(message.author) in gold1:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 1!""")
                return
            elif str(message.author) in gold2:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 2!""")
                return
            elif str(message.author) in gold3:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 3!""")
                return
            elif str(message.author) in immo:
                await message.channel.send(f"""Error. User {message.author} is already in immortal party!""")
                return
            elif str(message.author) in backup:
                await message.channel.send(f"""Error. User {message.author} is already in backup!""")
                return
            elif str(message.author) in backup2:
                await message.channel.send(f"""Error. User {message.author} is already in gold backup!""")
                return
            elif len(gold3) == 10:
                await message.channel.send(f"""Gold Party 3 is already full. Try other party instead.""")
                return
            else:
                gold3_id.append(str(message.author.id))
                gold3.append(str(message.author))
                await message.channel.send(gold3)
                return

        if message.content == "!addimmo":
            if str(message.author) in party1:
                await message.channel.send(f"""Error. User {message.author} is already in party 1!""")
                return
            elif str(message.author) in party2:
                await message.channel.send(f"""Error. User {message.author} is already in party 2!""")
                return
            elif str(message.author) in party3:
                await message.channel.send(f"""Error. User {message.author} is already in party 3!""")
                return
            elif str(message.author) in gold1:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 1!""")
                return
            elif str(message.author) in gold2:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 2!""")
                return
            elif str(message.author) in gold3:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 3!""")
                return
            elif str(message.author) in immo:
                await message.channel.send(f"""Error. User {message.author} is already in immortal party!""")
                return
            elif str(message.author) in backup:
                await message.channel.send(f"""Error. User {message.author} is already in backup!""")
                return
            elif str(message.author) in backup2:
                await message.channel.send(f"""Error. User {message.author} is already in gold backup!""")
                return
            elif len(immo) == 10:
                await message.channel.send(f"""Immortal party is already full. Try other party instead.""")
                return
            else:
                immo_id.append(str(message.author.id))
                immo.append(str(message.author))
                await message.channel.send(immo)
                return

        if message.content == "!addbackup":
            if str(message.author) in party1:
                await message.channel.send(f"""Error. User {message.author} is already in party 1!""")
                return
            elif str(message.author) in party2:
                await message.channel.send(f"""Error. User {message.author} is already in party 2!""")
                return
            elif str(message.author) in party3:
                await message.channel.send(f"""Error. User {message.author} is already in party 3!""")
                return
            elif str(message.author) in gold1:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 1!""")
                return
            elif str(message.author) in gold2:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 2!""")
                return
            elif str(message.author) in gold3:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 3!""")
                return
            elif str(message.author) in immo:
                await message.channel.send(f"""Error. User {message.author} is already in immortal party!""")
                return
            elif str(message.author) in backup:
                await message.channel.send(f"""Error. User {message.author} is already in backup!""")
                return
            elif str(message.author) in backup2:
                await message.channel.send(f"""Error. User {message.author} is already in gold backup!""")
                return
            else:
                backup_id.append(str(message.author.id))
                backup.append(str(message.author))
                await message.channel.send(backup)
                return

        if message.content == "!addbackup2":
            if str(message.author) in party1:
                await message.channel.send(f"""Error. User {message.author} is already in party 1!""")
                return
            elif str(message.author) in party2:
                await message.channel.send(f"""Error. User {message.author} is already in party 2!""")
                return
            elif str(message.author) in party3:
                await message.channel.send(f"""Error. User {message.author} is already in party 3!""")
                return
            elif str(message.author) in gold1:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 1!""")
                return
            elif str(message.author) in gold2:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 2!""")
                return
            elif str(message.author) in gold3:
                await message.channel.send(f"""Error. User {message.author} is already in gold party 3!""")
                return
            elif str(message.author) in immo:
                await message.channel.send(f"""Error. User {message.author} is already in immortal party!""")
                return
            elif str(message.author) in backup:
                await message.channel.send(f"""Error. User {message.author} is already in backup!""")
                return
            elif str(message.author) in backup2:
                await message.channel.send(f"""Error. User {message.author} is already in gold backup!""")
                return
            else:
                backup2_id.append(str(message.author.id))
                backup2.append(str(message.author))
                await message.channel.send(backup2)
                return

# This command prints the list
        if message.content == "!party1":
            await message.channel.send(party1)
        if message.content == "!party2":
            await message.channel.send(party2)
        if message.content == "!party3":
            await message.channel.send(party3)
        if message.content == "!gold1":
            await message.channel.send(gold1)
        if message.content == "!gold2":
            await message.channel.send(gold2)
        if message.content == "!gold3":
            await message.channel.send(gold3)
        if message.content == "!immo":
            await message.channel.send(immo)
        if message.content == "!backup":
            await message.channel.send(backup)
        if message.content == "!backup2":
            await message.channel.send(backup2)

# This command checks which party are you in
        if message.content == "!whichparty":
            if str(message.author) in party1:
                await message.channel.send(f"""User {message.author} is in party 1!""")
                return
            elif str(message.author) in party2:
                await message.channel.send(f"""User {message.author} is in party 2!""")
                return
            elif str(message.author) in party3:
                await message.channel.send(f"""User {message.author} is in party 3!""")
                return
            elif str(message.author) in gold1:
                await message.channel.send(f"""User {message.author} is in gold party 1!""")
                return
            elif str(message.author) in gold2:
                await message.channel.send(f"""User {message.author} is in gold party 2!""")
                return
            elif str(message.author) in gold3:
                await message.channel.send(f"""User {message.author} is in gold party 3!""")
                return
            elif str(message.author) in immo:
                await message.channel.send(f"""User {message.author} is in immortal party!""")
                return
            elif str(message.author) in backup:
                await message.channel.send(f"""User {message.author} is in backup!""")
                return
            elif str(message.author) in backup2:
                await message.channel.send(f"""User {message.author} is in gold backup!""")
                return
            else:
                await message.channel.send(f"""User {message.author} is not in any party!""")

# This command removes yourself from list
        if message.content == "!remove":
            if str(message.author) in party1:
                party1.remove(str(message.author))
                party1_id.remove(str(message.author.id))
                if organizer_dict["party1"] == str(message.author):
                    organizer_dict.update({"party1":"none"})
                await message.channel.send(f"""User {message.author} removed from party 1!""")
                return
            elif str(message.author) in party2:
                party2.remove(str(message.author))
                party2_id.remove(str(message.author.id))
                if organizer_dict["party2"] == str(message.author):
                    organizer_dict.update({"party2":"none"})
                await message.channel.send(f"""User {message.author} removed from party 2!""")
                return
            elif str(message.author) in party3:
                party3.remove(str(message.author))
                party3_id.remove(str(message.author.id))
                if organizer_dict["party3"] == str(message.author):
                    organizer_dict.update({"party3":"none"})
                await message.channel.send(f"""User {message.author} removed from party 3!""")
                return
            elif str(message.author) in gold1:
                gold1.remove(str(message.author))
                gold1_id.remove(str(message.author.id))
                if organizer_dict["gold1"] == str(message.author):
                    organizer_dict.update({"gold1":"none"})
                await message.channel.send(f"""User {message.author} removed from gold party 1!""")
                return
            elif str(message.author) in gold2:
                gold2.remove(str(message.author))
                gold2_id.remove(str(message.author.id))
                if organizer_dict["gold2"] == str(message.author):
                    organizer_dict.update({"gold2":"none"})
                await message.channel.send(f"""User {message.author} removed from gold party 2!""")
                return
            elif str(message.author) in gold3:
                gold3.remove(str(message.author))
                gold3_id.remove(str(message.author.id))
                if organizer_dict["gold3"] == str(message.author):
                    organizer_dict.update({"gold3":"none"})
                await message.channel.send(f"""User {message.author} removed from gold party 3!""")
                return
            elif str(message.author) in immo:
                immo.remove(str(message.author))
                immo_id.remove(str(message.author.id))
                if organizer_dict["immo"] == str(message.author):
                    organizer_dict.update({"immo":"none"})
                await message.channel.send(f"""User {message.author} removed from immortal party!""")
                return
            elif str(message.author) in backup:
                backup.remove(str(message.author))
                backup_id.remove(str(message.author.id))
                await message.channel.send(f"""User {message.author} is removed from backup!""")
                return
            elif str(message.author) in backup2:
                backup2.remove(str(message.author))
                backup2_id.remove(str(message.author.id))
                await message.channel.send(f"""User {message.author} is removed from gold backup!""")
                return
            else:
                await message.channel.send(f"""User {message.author} is not in any party!""")


# This commands counts the number of players in a party
        if message.content == "!count":
            embed = discord.Embed(title="Player count", description="Counts how many players in each party")
            embed.add_field(name="Party 1", value= str(len(party1)))
            embed.add_field(name="Party 2", value= str(len(party2)))
            embed.add_field(name="Party 3", value= str(len(party3)))
            embed.add_field(name="Gold Party 1", value=str(len(gold1)))
            embed.add_field(name="Gold Party 2", value=str(len(gold2)))
            embed.add_field(name="Gold Party 3", value=str(len(gold3)))
            embed.add_field(name="Immortal Party", value=str(len(immo)))
            embed.add_field(name="Backup", value=str(len(backup)))
            embed.add_field(name="Gold Backup", value=str(len(backup2)))
            await message.channel.send(content=None, embed=embed)

# This command views party messages
        if message.content.startswith("!msg"):
            if message.content[5:] == "party1":
                await message.channel.send(f"""Non Gold Party1: {msg_1}""")
            if message.content[5:] == "party2":
                await message.channel.send(f"""Non Gold Party2: {msg_2}""")
            if message.content[5:] == "party3":
                await message.channel.send(f"""Non Gold Party3: {msg_3}""")
            if message.content[5:] == "gold1":
                await message.channel.send(f"""Gold Party1: {msg_4}""")
            if message.content[5:] == "gold2":
                await message.channel.send(f"""Gold Party2: {msg_5}""")
            if message.content[5:] == "gold3":
                await message.channel.send(f"""Gold Party3: {msg_6}""")
            if message.content[5:] == "immo":
                await message.channel.send(f"""Immortal Party: {msg_7}""")

# This command assigns roles
        if message.content.startswith("!role"):
            if message.content[5:] == "":
                for roles in message.author.roles[1:]:
                    await message.channel.send(f"""{message.author} is in {roles}""")
            if message.content[6:] == "gold300":
                role = discord.utils.find(lambda r: r.name == "gold300", message.author.roles)
                if role in message.author.roles:
                    await message.channel.send(f"""{message.author} is already in {role}""")
                else:
                    role = discord.utils.get(message.guild.roles, name="gold300")
                    await message.author.add_roles(role)
                    await message.channel.send(f"""{message.author} added to {role}""")
            if message.content[6:] == "gold200":
                role = discord.utils.find(lambda r: r.name == "gold200", message.author.roles)
                if role in message.author.roles:
                    await message.channel.send(f"""{message.author} is already in {role}""")
                else:
                    role = discord.utils.get(message.guild.roles, name="gold200")
                    await message.author.add_roles(role)
                    await message.channel.send(f"""{message.author} added to {role}""")
            if message.content[6:] == "gold100":
                role = discord.utils.find(lambda r: r.name == "gold100", message.author.roles)
                if role in message.author.roles:
                    await message.channel.send(f"""{message.author} is already in {role}""")
                else:
                    role = discord.utils.get(message.guild.roles, name="gold100")
                    await message.author.add_roles(role)
                    await message.channel.send(f"""{message.author} added to {role}""")
            if message.content[6:] == "cavern":
                role = discord.utils.find(lambda r: r.name == "cavern", message.author.roles)
                if role in message.author.roles:
                    await message.channel.send(f"""{message.author} is already in {role}""")
                else:
                    role = discord.utils.get(message.guild.roles, name="cavern")
                    await message.author.add_roles(role)
                    await message.channel.send(f"""{message.author} added to {role}""")
            if message.content[6:] == "event_t1":
                role = discord.utils.find(lambda r: r.name == "event_t1", message.author.roles)
                if role in message.author.roles:
                    await message.channel.send(f"""{message.author} is already in {role}""")
                else:
                    role = discord.utils.get(message.guild.roles, name="event_t1")
                    await message.author.add_roles(role)
                    await message.channel.send(f"""{message.author} added to {role}""")
            if message.content[6:] == "event_t2":
                role = discord.utils.find(lambda r: r.name == "event_t2", message.author.roles)
                if role in message.author.roles:
                    await message.channel.send(f"""{message.author} is already in {role}""")
                else:
                    role = discord.utils.get(message.guild.roles, name="event_t2")
                    await message.author.add_roles(role)
                    await message.channel.send(f"""{message.author} added to {role}""")
            if message.content[6:] == "event_t3":
                role = discord.utils.find(lambda r: r.name == "event_t3", message.author.roles)
                if role in message.author.roles:
                    await message.channel.send(f"""{message.author} is already in {role}""")
                else:
                    role = discord.utils.get(message.guild.roles, name="event_t3")
                    await message.author.add_roles(role)
                    await message.channel.send(f"""{message.author} added to {role}""")
            if message.content[6:] == "event_t4":
                role = discord.utils.find(lambda r: r.name == "event_t4", message.author.roles)
                if role in message.author.roles:
                    await message.channel.send(f"""{message.author} is already in {role}""")
                else:
                    role = discord.utils.get(message.guild.roles, name="event_t4")
                    await message.author.add_roles(role)
                    await message.channel.send(f"""{message.author} added to {role}""")
            if message.content[6:] == "event_tt":
                role = discord.utils.find(lambda r: r.name == "event_tt", message.author.roles)
                if role in message.author.roles:
                    await message.channel.send(f"""{message.author} is already in {role}""")
                else:
                    role = discord.utils.get(message.guild.roles, name="event_tt")
                    await message.author.add_roles(role)
                    await message.channel.send(f"""{message.author} added to {role}""")
            if message.content[6:] == "immortal":
                role = discord.utils.find(lambda r: r.name == "immortal", message.author.roles)
                if role in message.author.roles:
                    await message.channel.send(f"""{message.author} is already in {role}""")
                else:
                    role = discord.utils.get(message.guild.roles, name="immortal")
                    await message.author.add_roles(role)
                    await message.channel.send(f"""{message.author} added to {role}""")
            if message.content[6:] == "divine":
                role = discord.utils.find(lambda r: r.name == "divine", message.author.roles)
                if role in message.author.roles:
                    await message.channel.send(f"""{message.author} is already in {role}""")
                else:
                    role = discord.utils.get(message.guild.roles, name="divine")
                    await message.author.add_roles(role)
                    await message.channel.send(f"""{message.author} added to {role}""")

        if message.content.startswith("!unrole"):
            if message.content[8:] == "gold300":
                role = discord.utils.find(lambda r: r.name == "gold300", message.author.roles)
                if role not in message.author.roles:
                    await message.channel.send(f"""{message.author} is not in gold300""")
                else:
                    role = discord.utils.get(message.guild.roles, name="gold300")
                    await message.author.remove_roles(role)
                    await message.channel.send(f"""{message.author} remove from {role}""")
            if message.content[8:] == "gold200":
                role = discord.utils.find(lambda r: r.name == "gold200", message.author.roles)
                if role not in message.author.roles:
                    await message.channel.send(f"""{message.author} is not in gold200""")
                else:
                    role = discord.utils.get(message.guild.roles, name="gold200")
                    await message.author.remove_roles(role)
                    await message.channel.send(f"""{message.author} remove from {role}""")
            if message.content[8:] == "gold100":
                role = discord.utils.find(lambda r: r.name == "gold100", message.author.roles)
                if role not in message.author.roles:
                    await message.channel.send(f"""{message.author} is not in gold100""")
                else:
                    role = discord.utils.get(message.guild.roles, name="gold100")
                    await message.author.remove_roles(role)
                    await message.channel.send(f"""{message.author} remove from {role}""")
            if message.content[8:] == "cavern":
                role = discord.utils.find(lambda r: r.name == "cavern", message.author.roles)
                if role not in message.author.roles:
                    await message.channel.send(f"""{message.author} is not in cavern""")
                else:
                    role = discord.utils.get(message.guild.roles, name="cavern")
                    await message.author.remove_roles(role)
                    await message.channel.send(f"""{message.author} remove from {role}""")
            if message.content[8:] == "event_t1":
                role = discord.utils.find(lambda r: r.name == "event_t1", message.author.roles)
                if role not in message.author.roles:
                    await message.channel.send(f"""{message.author} is not in event_t1""")
                else:
                    role = discord.utils.get(message.guild.roles, name="event_t1")
                    await message.author.remove_roles(role)
                    await message.channel.send(f"""{message.author} remove from {role}""")
            if message.content[8:] == "event_t2":
                role = discord.utils.find(lambda r: r.name == "event_t2", message.author.roles)
                if role not in message.author.roles:
                    await message.channel.send(f"""{message.author} is not in event_t2""")
                else:
                    role = discord.utils.get(message.guild.roles, name="event_t2")
                    await message.author.remove_roles(role)
                    await message.channel.send(f"""{message.author} remove from {role}""")
            if message.content[8:] == "event_t3":
                role = discord.utils.find(lambda r: r.name == "event_t3", message.author.roles)
                if role not in message.author.roles:
                    await message.channel.send(f"""{message.author} is not in event_t3""")
                else:
                    role = discord.utils.get(message.guild.roles, name="event_t3")
                    await message.author.remove_roles(role)
                    await message.channel.send(f"""{message.author} remove from {role}""")
            if message.content[8:] == "event_t4":
                role = discord.utils.find(lambda r: r.name == "event_t4", message.author.roles)
                if role not in message.author.roles:
                    await message.channel.send(f"""{message.author} is not in event_t4""")
                else:
                    role = discord.utils.get(message.guild.roles, name="event_t4")
                    await message.author.remove_roles(role)
                    await message.channel.send(f"""{message.author} remove from {role}""")
            if message.content[8:] == "event_tt":
                role = discord.utils.find(lambda r: r.name == "event_tt", message.author.roles)
                if role not in message.author.roles:
                    await message.channel.send(f"""{message.author} is not in event_tt""")
                else:
                    role = discord.utils.get(message.guild.roles, name="event_tt")
                    await message.author.remove_roles(role)
                    await message.channel.send(f"""{message.author} remove from {role}""")
            if message.content[8:] == "immortal":
                role = discord.utils.find(lambda r: r.name == "immortal", message.author.roles)
                if role not in message.author.roles:
                    await message.channel.send(f"""{message.author} is not in immortal""")
                else:
                    role = discord.utils.get(message.guild.roles, name="immortal")
                    await message.author.remove_roles(role)
                    await message.channel.send(f"""{message.author} remove from {role}""")
            if message.content[8:] == "divine":
                role = discord.utils.find(lambda r: r.name == "divine", message.author.roles)
                if role not in message.author.roles:
                    await message.channel.send(f"""{message.author} is not in divine""")
                else:
                    role = discord.utils.get(message.guild.roles, name="divine")
                    await message.author.remove_roles(role)
                    await message.channel.send(f"""{message.author} remove from {role}""")

# Organizer commands

# This command changes party messages
        if message.content.startswith("!setmsg"):
            msg_content = message.content[8:].split(sep=",")
            if msg_content[0] == "party1":
                if str(message.author) == organizer_dict[msg_content[0]] or str(message.author) in valid_users or str(message.author) in admins:
                    msg_1 = msg_content[1]
                    await message.channel.send(f"""The party message for non gold party 1 has been changed to: {msg_1}""")
            elif msg_content[0] == "party2":
                if str(message.author) == organizer_dict[msg_content[0]] or str(message.author) in valid_users or str(message.author) in admins:
                    msg_2 = msg_content[1]
                    await message.channel.send(f"""The party message for non gold party 2 has been changed to: {msg_2}""")
            elif msg_content[0] == "party3":
                if str(message.author) == organizer_dict[msg_content[0]] or str(message.author) in valid_users or str(message.author) in admins:
                    msg_3 = msg_content[1]
                    await message.channel.send(f"""The party message for non gold party 3 has been changed to: {msg_3}""")
            elif msg_content[0] == "gold1":
                if str(message.author) == organizer_dict[msg_content[0]] or str(message.author) in valid_users or str(message.author) in admins:
                    msg_4 = msg_content[1]
                    await message.channel.send(f"""The party message for gold party 1 has been changed to: {msg_4}""")
            elif msg_content[0] == "gold2":
                if str(message.author) == organizer_dict[msg_content[0]] or str(message.author) in valid_users or str(message.author) in admins:
                    msg_5 = msg_content[1]
                    await message.channel.send(f"""The party message for gold party 2 has been changed to: {msg_5}""")
            elif msg_content[0] == "gold3":
                if str(message.author) == organizer_dict[msg_content[0]] or str(message.author) in valid_users or str(message.author) in admins:
                    msg_6 = msg_content[1]
                    await message.channel.send(f"""The party message for gold party 3 has been changed to: {msg_6}""")
            elif msg_content[0] == "immo":
                if str(message.author) == organizer_dict[msg_content[0]] or str(message.author) in valid_users or str(message.author) in admins:
                    msg_7 = msg_content[1]
                    await message.channel.send(f"""The party message for immortal party has been changed to: {msg_7}""")

# This command sets the date for abuse
        if message.content.startswith("!setdate"):
            msg_content = message.content[9:].split(sep=",")
            if msg_content[0] == "party1":
                if str(message.author) == organizer_dict[msg_content[0]] or str(message.author) in valid_users or str(message.author) in admins:
                    date1 = datetime.datetime.strptime(msg_content[1], '%d/%m/%y %H:%M:%S')
                    await message.channel.send(f"""The abuse date and time for non gold party 1 is {date1}""")
            if msg_content[0] == "party2":
                if str(message.author) == organizer_dict[msg_content[0]] or str(message.author) in valid_users or str(message.author) in admins:
                    date2 = datetime.datetime.strptime(msg_content[1], '%d/%m/%y %H:%M:%S')
                    await message.channel.send(f"""The abuse date and time for non gold party 2 is {date2}""")
            if msg_content[0] == "party3":
                if str(message.author) == organizer_dict[msg_content[0]] or str(message.author) in valid_users or str(message.author) in admins:
                    date3 = datetime.datetime.strptime(msg_content[1], '%d/%m/%y %H:%M:%S')
                    await message.channel.send(f"""The abuse date and time for non gold party 3 is {date3}""")
            if msg_content[0] == "gold1":
                if str(message.author) == organizer_dict[msg_content[0]] or str(message.author) in valid_users or str(message.author) in admins:
                    date4 = datetime.datetime.strptime(msg_content[1], '%d/%m/%y %H:%M:%S')
                    await message.channel.send(f"""The abuse date and time for gold party 1 is {date4}""")
            if msg_content[0] == "gold2":
                if str(message.author) == organizer_dict[msg_content[0]] or str(message.author) in valid_users or str(message.author) in admins:
                    date5 = datetime.datetime.strptime(msg_content[1], '%d/%m/%y %H:%M:%S')
                    await message.channel.send(f"""The abuse date and time for gold party 2 is {date5}""")
            if msg_content[0] == "gold3":
                if str(message.author) == organizer_dict[msg_content[0]] or str(message.author) in valid_users or str(message.author) in admins:
                    date6 = datetime.datetime.strptime(msg_content[1], '%d/%m/%y %H:%M:%S')
                    await message.channel.send(f"""The abuse date and time for gold party 3 is {date6}""")
            if msg_content[0] == "immo":
                if str(message.author) == organizer_dict[msg_content[0]] or str(message.author) in valid_users or str(message.author) in admins:
                    date7 = datetime.datetime.strptime(msg_content[1], '%d/%m/%y %H:%M:%S')
                    await message.channel.send(f"""The abuse date and time for immortal party is {date7}""")

        if message.content.startswith("!empty"):
            if str(message.author) == organizer_dict[message.content[7:]] or str(message.author) in valid_users or str(message.author) in admins:
                if message.content[7:] == "party1":
                    party1.clear()
                    party1_id.clear()
                    organizer_dict.update({"party1":"none"})
                    await message.channel.send("Party 1 cleared")
                elif message.content[7:] == "party2":
                    party2.clear()
                    party2_id.clear()
                    organizer_dict.update({"party2": "none"})
                    await message.channel.send("Party 2 cleared")
                elif message.content[7:] == "party3":
                    party3.clear()
                    party3_id.clear()
                    organizer_dict.update({"party3": "none"})
                    await message.channel.send("Party 3 cleared")
                elif message.content[7:] == "gold1":
                    gold1.clear()
                    gold1_id.clear()
                    organizer_dict.update({"gold1": "none"})
                    await message.channel.send("Gold Party 1 cleared")
                elif message.content[7:] == "gold2":
                    gold2.clear()
                    gold2_id.clear()
                    organizer_dict.update({"gold2": "none"})
                    await message.channel.send("Gold Party 2 cleared")
                elif message.content[7:] == "gold3":
                    gold3.clear()
                    gold3_id.clear()
                    organizer_dict.update({"gold3": "none"})
                    await message.channel.send("Gold Party 3 cleared")
                elif message.content[7:] == "immo":
                    immo.clear()
                    immo_id.clear()
                    organizer_dict.update({"immo": "none"})
                    await message.channel.send("Immortal Party cleared")

        if message.content.startswith("!summon"):
            if str(message.author) == organizer_dict[message.content[8:]] or str(message.author) in valid_users or str(message.author) in admins:
                if message.content[8:] == "party1":
                    for i in party1_id:
                        await message.channel.send(f"""<@{i}>""")
                if message.content[8:] == "party2":
                    for i in party2_id:
                        await message.channel.send(f"""<@{i}>""")
                if message.content[8:] == "party3":
                    for i in party3_id:
                        await message.channel.send(f"""<@{i}>""")
                if message.content[8:] == "gold1":
                    for i in gold1_id:
                        await message.channel.send(f"""<@{i}>""")
                if message.content[8:] == "gold2":
                    for i in gold2_id:
                        await message.channel.send(f"""<@{i}>""")
                if message.content[8:] == "gold3":
                    for i in gold3_id:
                        await message.channel.send(f"""<@{i}>""")
                if message.content[8:] == "immo":
                    for i in immo_id:
                        await message.channel.send(f"""<@{i}>""")


# Admin commands

# Checks valid users
        if str(message.author) in admins or str(message.author) in valid_users:

            if message.content == "!adminhelp":
                embed = discord.Embed(title="Admin Commands", description="Power Overwhelming")
                embed.add_field(name="!users", value="Checks number of users in server")
                embed.add_field(name="!setmsg <party>,<message>", value="Changes party message")
                embed.add_field(name="!msgclr", value="Removes all party messages")
                embed.add_field(name="!adduser <party>,<user>", value="Manually adds an user to a party")
                embed.add_field(name="!rm <party>,<int>", value="Removes a specific player base on the list index")
                embed.add_field(name="!replace <user1>,<user2>", value="Replace user1 with user2 in party")
                embed.add_field(name="!clear <party>/organizer/date", value="Clears a list")
                embed.add_field(name="!clear all", value="Clear every list (including organizer and date")
                embed.add_field(name="!tag <party>", value="Tags every users in specific party")
                embed.add_field(name="!setdate <party>,<datetime'%d/%m/%y %H:%M:%S'>", value="Set abuse date and time")
                embed.add_field(name="!donkey <user>", value="Turns a user into a donkey")
                embed.add_field(name="!undonkey <user>", value="Remove a donkey")
                embed.add_field(name="!listofdonkeys", value="The donkeys")
                await message.channel.send(content=None, embed=embed)

            if message.content == "!users":
                await message.channel.send(f"""# of Members: {id.member_count}""")

# This command adds people to the donkey list
            if message.content.startswith("!donkey"):
                msg_content = message.content[8:].split(sep = ",")
                if msg_content[0] == str(message.author):
                    await message.channel.send("Are you seriously trying to use this on your ownself?")
                elif msg_content[0] in admins:
                    await message.channel.send(f"""I KNEW ONE OF YOU FUCKS WILL EVENTUALLY TRY THIS ON ME. HAVE A REVERSE UNO. HEEHAW MOTHERFUCKER.""")
                    donkey_list.append(str(message.author))
                else:
                    donkey_list.append(msg_content[0])
                    await message.channel.send(f"""Heehaw. User {msg_content[0]} is now a stupid donkey""")

# This command removes people from the donkey list
            if message.content.startswith("!undonkey"):
                msg_content = message.content[10:].split(sep = ",")
                if msg_content[0] in donkey_list:
                    donkey_list.remove(msg_content[0])
                    await message.channel.send(f"""User {msg_content[0]} is now human again.""")

# This command checks the donkey list
            if message.content == "!listofdonkeys":
                await message.channel.send(donkey_list)

# This command clears all message
            if message.content == "!msgclr":
                msg_1 = ""
                msg_2 = ""
                msg_3 = ""
                msg_4 = ""
                msg_5 = ""
                msg_6 = ""
                msg_7 = ""
                await message.channel.send("All party messages removed!")

# This command remove a single player from party list using index
            if message.content.startswith("!rm"):
                msg_content = message.content[4:].split(sep = ",")
                if msg_content[0] == "party1":
                    try:
                        name = party1[int(msg_content[1])]
                        del party1[int(msg_content[1])]
                        del party1_id[int(msg_content[1])]
                        await message.channel.send(f"""Player {name} from Non Gold Party 1 removed""")
                        await message.channel.send(party1)
                    except ValueError:
                        await message.channel.send("Please enter an integer from 0-9")
                    except IndexError:
                        await message.channel.send("Please enter a valid list index")

                if msg_content[0] == "party2":
                    try:
                        name = party2[int(msg_content[1])]
                        del party2[int(msg_content[1])]
                        del party2_id[int(msg_content[1])]
                        await message.channel.send(f"""Player {name} from Non Gold Party 2 removed""")
                        await message.channel.send(party2)
                    except ValueError:
                        await message.channel.send("Please enter an integer from 0-9")
                    except IndexError:
                        await message.channel.send("Please enter a valid list index")

                if msg_content[0] == "party3":
                    try:
                        name = party3[int(msg_content[1])]
                        del party3[int(msg_content[1])]
                        del party3_id[int(msg_content[1])]
                        await message.channel.send(f"""Player {name} from Non Gold Party 3 removed""")
                        await message.channel.send(party3)
                    except ValueError:
                        await message.channel.send("Please enter an integer from 0-9")
                    except IndexError:
                        await message.channel.send("Please enter a valid list index")

                if msg_content[0] == "gold1":
                    try:
                        name = gold1[int(msg_content[1])]
                        del gold1[int(msg_content[1])]
                        del gold1_id[int(msg_content[1])]
                        await message.channel.send(f"""Player {name} from Gold Party 1 removed""")
                        await message.channel.send(gold1)
                    except ValueError:
                        await message.channel.send("Please enter an integer from 0-9")
                    except IndexError:
                        await message.channel.send("Please enter a valid list index")

                if msg_content[0] == "gold2":
                    try:
                        name = gold2[int(msg_content[1])]
                        del gold2[int(msg_content[1])]
                        del gold2_id[int(msg_content[1])]
                        await message.channel.send(f"""Player {name} from Gold Party 2 removed""")
                        await message.channel.send(gold2)
                    except ValueError:
                        await message.channel.send("Please enter an integer from 0-9")
                    except IndexError:
                        await message.channel.send("Please enter a valid list index")

                if msg_content[0] == "gold3":
                    try:
                        name = gold3[int(msg_content[1])]
                        del gold3[int(msg_content[1])]
                        del gold3_id[int(msg_content[1])]
                        await message.channel.send(f"""Player {name} from Gold Party 3 removed""")
                        await message.channel.send(gold3)
                    except ValueError:
                        await message.channel.send("Please enter an integer from 0-9")
                    except IndexError:
                        await message.channel.send("Please enter a valid list index")

                if msg_content[0] == "immo":
                    try:
                        name = immo[int(msg_content[1])]
                        del immo[int(msg_content[1])]
                        del immo_id[int(msg_content[1])]
                        await message.channel.send(f"""Player {name} from Immortal Party removed""")
                        await message.channel.send(immo)
                    except ValueError:
                        await message.channel.send("Please enter an integer from 0-9")
                    except IndexError:
                        await message.channel.send("Please enter a valid list index")

                if msg_content[0] == "backup":
                    try:
                        name = backup[int(msg_content[1])]
                        del backup[int(msg_content[1])]
                        del backup_id[int(msg_content[1])]
                        await message.channel.send(f"""Player {name} from Backup removed""")
                        await message.channel.send(backup)
                    except ValueError:
                        await message.channel.send("Please enter an integer from 0-9")
                    except IndexError:
                        await message.channel.send("Please enter a valid list index")

                if msg_content[0] == "backup2":
                    try:
                        name = backup2[int(msg_content[1])]
                        del backup2[int(msg_content[1])]
                        del backup2_id[int(msg_content[1])]
                        await message.channel.send(f"""Player {name} from Gold Backup removed""")
                        await message.channel.send(backup2)
                    except ValueError:
                        await message.channel.send("Please enter an integer from 0-9")
                    except IndexError:
                        await message.channel.send("Please enter a valid list index")

# This command clears party list
            if message.content.startswith("!clear"):
                if message.content[7:] == "party1":
                    party1.clear()
                    party1_id.clear()
                    organizer_dict.update({"party1":"none"})
                    await message.channel.send("Party 1 cleared")
                elif message.content[7:] == "party2":
                    party2.clear()
                    party2_id.clear()
                    organizer_dict.update({"party2": "none"})
                    await message.channel.send("Party 2 cleared")
                elif message.content[7:] == "party3":
                    party3.clear()
                    party3_id.clear()
                    organizer_dict.update({"party3": "none"})
                    await message.channel.send("Party 3 cleared")
                elif message.content[7:] == "gold1":
                    gold1.clear()
                    gold1_id.clear()
                    organizer_dict.update({"gold1": "none"})
                    await message.channel.send("Gold Party 1 cleared")
                elif message.content[7:] == "gold2":
                    gold2.clear()
                    gold2_id.clear()
                    organizer_dict.update({"gold2": "none"})
                    await message.channel.send("Gold Party 2 cleared")
                elif message.content[7:] == "gold3":
                    gold3.clear()
                    gold3_id.clear()
                    organizer_dict.update({"gold3": "none"})
                    await message.channel.send("Gold Party 3 cleared")
                elif message.content[7:] == "immo":
                    immo.clear()
                    immo_id.clear()
                    organizer_dict.update({"immo": "none"})
                    await message.channel.send("Immortal Party cleared")
                elif message.content[7:] == "backup":
                    backup.clear()
                    backup_id.clear()
                    await message.channel.send("Backup cleared")
                elif message.content[7:] == "backup2":
                    backup.clear()
                    backup_id.clear()
                    await message.channel.send("Backup 2 cleared")
                elif message.content[7:] == "organizer":
                    organizer_dict = {"party1": "none", "party2": "none", "party3": "none", "gold1": "none",
                                      "gold2": "none", "gold3": "none", "immo": "none"}
                elif message.content[7:] == "date":
                    date1 = ""
                    date2 = ""
                    date3 = ""
                    date4 = ""
                    date5 = ""
                    date6 = ""
                    date7 = ""
                    await message.channel.send("All dates cleared!")
                elif message.content[7:] == "msg":
                    msg_1 = ""
                    msg_2 = ""
                    msg_3 = ""
                    msg_4 = ""
                    msg_5 = ""
                    msg_6 = ""
                    msg_7 = ""
                    await message.channel.send("Party messages cleared!")
                elif message.content[7:] == "all":
                    party1.clear()
                    party1_id.clear()
                    party2.clear()
                    party2_id.clear()
                    party3.clear()
                    party3_id.clear()
                    gold1.clear()
                    gold1_id.clear()
                    gold2.clear()
                    gold2_id.clear()
                    gold3.clear()
                    gold3_id.clear()
                    immo.clear()
                    immo_id.clear()
                    backup.clear()
                    backup_id.clear()
                    backup2.clear()
                    backup2_id.clear()
                    organizer_dict = {"party1": "none", "party2": "none", "party3": "none", "gold1": "none",
                                      "gold2": "none", "gold3": "none", "immo": "none"}
                    date1 = ""
                    date2 = ""
                    date3 = ""
                    date4 = ""
                    date5 = ""
                    date6 = ""
                    date7 = ""
                    msg_1 = ""
                    msg_2 = ""
                    msg_3 = ""
                    msg_4 = ""
                    msg_5 = ""
                    msg_6 = ""
                    msg_7 = ""
                    await message.channel.send("Reset complete")

# This command tags all party members in their respective party
            if message.content.startswith("!tag"):
                if message.content[5:] == "party1":
                    for i in party1_id:
                        await message.channel.send(f"""<@{i}>""")
                if message.content[5:] == "party2":
                    for i in party2_id:
                        await message.channel.send(f"""<@{i}>""")
                if message.content[5:] == "party3":
                    for i in party3_id:
                        await message.channel.send(f"""<@{i}>""")
                if message.content[5:] == "gold1":
                    for i in gold1_id:
                        await message.channel.send(f"""<@{i}>""")
                if message.content[5:] == "gold2":
                    for i in gold2_id:
                        await message.channel.send(f"""<@{i}>""")
                if message.content[5:] == "gold3":
                    for i in gold3_id:
                        await message.channel.send(f"""<@{i}>""")
                if message.content[5:] == "immo":
                    for i in immo_id:
                        await message.channel.send(f"""<@{i}>""")
                if message.content[5:] == "backup":
                    for i in backup_id:
                        await message.channel.send(f"""<@{i}>""")
                if message.content[5:] == "backup2":
                    for i in backup2_id:
                        await message.channel.send(f"""<@{i}>""")

# This command checks and swaps two different party members

            if message.content.startswith("!replace"):

    # Updates the member list into a dictionary
                for guild in client.guilds:
                    for member in guild.members:
                        members_dict.update({str(member): str(member.id)})

    # Split message contents into parts
                content = message.content[9:].split(sep = ",")
                player1 = content[0]
                player2 = content[1]

    # Get the id from dictionary
                player1_id = members_dict.get(player1)
                player2_id = members_dict.get(player2)

    # Party swap!

    # Create a list of list
                parties = [party1, party2, party3, gold1, gold2, gold3, immo, backup, backup2]
                parties_id = [party1_id, party2_id, party3_id, gold1_id, gold2_id, gold3_id, immo_id, backup_id, backup2_id]
    # Search parties for players
                for list, id in zip(parties, parties_id):
                    if player1 in list:
                        list.remove(player1)
                        id.remove(player1_id)
                        list.append(player2+"**") # Adds an unique identifier
                        id.append(player2_id+"**")
                    if player2 in list:
                        list.remove(player2)
                        id.remove(player2_id)
                        list.append(player1)
                        id.append(player1_id)
                for list, id in zip(parties, parties_id):
                    if player2+"**" in list:
                        list.remove(player2+"**")
                        id.remove(player2_id+"**")
                        list.append(player2)
                        id.append(player2_id)
                await message.channel.send(f"""User {player1} replaced {player2} in party!""")
                await message.channel.send(f"""If {player1} is in an another party, {player2} will be swapped there.""")

# Add another user in party

            if message.content.startswith("!adduser"):

        # Updates the member list into a dictionary
                for guild in client.guilds:
                    for member in guild.members:
                        members_dict.update({str(member): str(member.id)})

        # Split message contents into parts
                content = message.content[9:].split(sep=",")
                party = content[0]
                player = content[1]

        # Get the id from dictionary
                player_id = members_dict.get(player)

        # Create a list of list
                parties = [party1, party2, party3, gold1, gold2, gold3, immo, backup, backup2]
                parties_name = ["party1", "party2", "party3", "gold1", "gold2", "gold3", "immo", "backup", "backup2"]
                parties_id = [party1_id, party2_id, party3_id, gold1_id, gold2_id, gold3_id, immo_id, backup_id, backup2_id]
        # Search parties for players
                for list,id,name in zip(parties, parties_id, parties_name):
                    if player in list:
                        await message.channel.send(f"""User {player} is already in a party. Use !replace instead.""")
                        return
                    else:
                        if party == name:
                            list.append(player)
                            id.append(player_id)
                            await message.channel.send(f"""User {player} sucessfully added to {party}!""")




client.loop.create_task(update_stats())
client.run(token_main) #Remember to change back before git commit
