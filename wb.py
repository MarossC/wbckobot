import discord, re, time, os

client = discord.Client()

config = {
    "meteorit"      :   str(1234567891234567891),                       #Zde nahradit id role pro Meteorit, atp. dale                       
    "draciCisar"    :   str(1234567891234567891),
    "lavovyDrak"    :   str(1234567891234567891), 
    "magTemnoty"    :   str(1234567891234567891),
    
    "kralWubba"     :   str(1234567891234567891), 
    "zelenyDrak"    :   str(1234567891234567891),                   
    "prirodniKral"  :   str(1234567891234567891), 
    "kingKong"      :   str(1234567891234567891),
    "obriHumr"      :   str(1234567891234567891),
    "vzdTygra"      :   str(1234567891234567891),
    "kralPlamenu"   :   str(1234567891234567891),
    "devitiocas"    :   str(1234567891234567891),
    "tmavyVudce"    :   str(1234567891234567891),
    "ork"           :   str(1234567891234567891),
    "zelva"         :   str(1234567891234567891),
    "pavouk"        :   str(1234567891234567891),
    
    "eventBoss"     :   str(1234567891234567891),
}

zaslatZde = client.get_channel(1286079174720749621)                   #Zde nahradit id kanalu kam posilat upozorneni


@client.event
async def on_ready():
    print(f'Ready: {client.user}')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.embeds:
        
        if message.embeds[0].description == None:
            return

        if message.channel.id != 1005580890010816522:               #Zde popripade nahradit ID kanalu odkud se ctou upozorneni
            return

        currTime = str(int(time.time()))

########### Event boss
        
        if re.search("Dýňový smrťák.. se", message.embeds[0].description):
            print("----- Eventový boss - Spawn -----")
            await zaslatZde.send('<@&'+ config['eventBoss'] + '> Dýňový smrťák se prave spawnul. <t:'+ currTime +':R>')
            return   
        
########### High tier boss

        if re.search("Meteorit.. se", message.embeds[0].description):
            print("----- Meteorit - Spawn -----")
            await zaslatZde.send('<@&'+ config['meteorit'] + '> se prave spawnul. <t:'+ currTime +':R>')
            return
        
        if re.search("Dračí císař.. se", message.embeds[0].description):
            print("----- Draci cisar - Spawn -----")
            await zaslatZde.send('<@&'+ config['draciCisar'] + '> se prave spawnul. <t:'+ currTime +':R>')  
            return
        
        if re.search("Lávový drak.. se", message.embeds[0].description):
            print("----- Lavovy drak - Spawn -----")
            await zaslatZde.send('<@&'+ config['lavovyDrak'] + '> se prave spawnul. <t:'+ currTime +':R>') 
            return
        
        if re.search("Mág temnoty.. se", message.embeds[0].description):
            print("----- Mag temnoty - Spawn -----")
            await zaslatZde.send('<@&'+ config['magTemnoty'] + '> se prave spawnul. <t:'+ currTime +':R>')
            return    
        
############ low tier boss
        
        if re.search("Císař Wubba.. se", message.embeds[0].description):
            print("----- Císař Wubba - Spawn -----")
            await zaslatZde.send('<@&'+ config['kralWubba'] + '> se prave spawnul. <t:'+ currTime +':R>')
            return   
        
        if re.search("Zelený drak.. se", message.embeds[0].description):
            print("----- Zelený drak - Spawn -----")
            await zaslatZde.send('<@&'+ config['zelenyDrak'] + '> se prave spawnul. <t:'+ currTime +':R>')
            return
        
        if re.search("Přírodní král.. se", message.embeds[0].description):
            print("----- Přírodní král - Spawn -----")
            await zaslatZde.send('<@&'+ config['prirodniKral'] + '> se prave spawnul. <t:'+ currTime +':R>')
            return
        
        if re.search("King Kong.. se", message.embeds[0].description):
            print("----- King Kong - Spawn -----")
            await zaslatZde.send('<@&'+ config['kingKong'] + '> se prave spawnul. <t:'+ currTime +':R>')
            return
        
        if re.search("Obří Humr.. se", message.embeds[0].description):
            print("----- Obří Humr - Spawn -----")
            await zaslatZde.send('<@&'+ config['obriHumr'] + '> se prave spawnul. <t:'+ currTime +':R>')
            return  

        if re.search("Velký žlutý duch tygra.. se", message.embeds[0].description):
            print("----- Velký žlutý duch tygra - Spawn -----")
            await zaslatZde.send('<@&'+ config['vzdTygra'] + '> se prave spawnul. <t:'+ currTime +':R>')            
            return
        
        if re.search("Tmavý král plamenů.. se", message.embeds[0].description):
            print("----- Král plamenů - Spawn -----")
            await zaslatZde.send('<@&'+ config['kralPlamenu'] + '> se prave spawnul. <t:'+ currTime +':R>')
            return
        
        if re.search("Devítiocas.. se", message.embeds[0].description):
            print("----- Devítiocas - Spawn -----")
            await zaslatZde.send('<@&'+ config['devitiocas'] + '> se prave spawnul. <t:'+ currTime +':R>')
            return    

        if re.search("Tmavý vůdce.. se", message.embeds[0].description):
            print("----- Tmavý vůdce - Spawn -----")
            await zaslatZde.send('<@&'+ config['tmavyVudce'] + '> se prave spawnul. <t:'+ currTime +':R>')
            return  

        if re.search("Ork.. se", message.embeds[0].description):
            print("----- Ork - Spawn -----")
            await zaslatZde.send('<@&'+ config['ork'] + '> se prave spawnul. <t:'+ currTime +':R>')
            return  

        if re.search("Želva.. se", message.embeds[0].description):
            print("----- Želva - Spawn -----")
            await zaslatZde.send('<@&'+ config['zelva'] + '> se prave spawnul. <t:'+ currTime +':R>')
            return 

        if re.search("Pavouk.. se", message.embeds[0].description):
            print("----- Pavouk - Spawn -----")
            await zaslatZde.send('<@&'+ config['pavouk'] + '> se prave spawnul. <t:'+ currTime +':R>')
            return   
        

        

        

################################################## Death notification

        if re.search(".*právě zabil \*\*Meteorit\*\*", message.embeds[0].description):
            print("----- Meteorit - Kill -----")
            await zaslatZde.send(str(message.embeds[0].description) + ' <t:'+ currTime +':R>')
            return
        
        if re.search(".*právě zabil \*\*Dračího císaře\*\*", message.embeds[0].description):
            print("----- Draci cisar - Kill -----")
            await zaslatZde.send(str(message.embeds[0].description) + ' <t:'+ currTime +':R>')
            return
        
        if re.search(".*právě zabil \*\*Lávového draka\*\*", message.embeds[0].description):
            print("----- Lavovy drak - Kill -----")
            await zaslatZde.send(str(message.embeds[0].description) + ' <t:'+ currTime +':R>')
            return
        
        if re.search(".*právě zabil \*\*Mága temnoty\*\*", message.embeds[0].description):
            print("----- Mag temnoty - Kill -----")
            await zaslatZde.send(str(message.embeds[0].description) + ' <t:'+ currTime +':R>')
            return 

########### Event boss

        if re.search(".*právě zabil \*\*Dýňového smrťáka\*\*", message.embeds[0].description):
            print("----- Dýňového smrťáka - Kill -----")
            await zaslatZde.send(str(message.embeds[0].description) + ' <t:'+ currTime +':R>')
            return 

########### Low bosses

        if re.search(".*právě zabil \*\*Císaře Wubbu\*\*", message.embeds[0].description):
            print("----- Císař Wubba - Kill -----")
            await zaslatZde.send(str(message.embeds[0].description) + ' <t:'+ currTime +':R>')
            return 
        
        if re.search(".*právě zabil \*\*Přírodního krále\*\*", message.embeds[0].description):
            print("----- Přírodního krále - Kill -----")
            await zaslatZde.send(str(message.embeds[0].description) + ' <t:'+ currTime +':R>')
            return 

        if re.search(".*právě zabil \*\*Pavouka\*\*", message.embeds[0].description):
            print("----- Pavouk - Kill -----")
            await zaslatZde.send(str(message.embeds[0].description) + ' <t:'+ currTime +':R>')
            return 

        if re.search(".*právě zabil \*\*Želvu\*\*", message.embeds[0].description):
            print("----- Želva - Kill -----")
            await zaslatZde.send(str(message.embeds[0].description) + ' <t:'+ currTime +':R>')
            return 
        
        if re.search(".*právě zabil \*\*Orka\*\*", message.embeds[0].description):
            print("----- Ork - Kill -----")
            await zaslatZde.send(str(message.embeds[0].description) + ' <t:'+ currTime +':R>')
            return 
        
        if re.search(".*právě zabil \*\*Tmavého vůdce\*\*", message.embeds[0].description):
            print("----- Tmavý vůdce - Kill -----")
            await zaslatZde.send(str(message.embeds[0].description) + ' <t:'+ currTime +':R>')
            return 
        
        if re.search(".*právě zabil \*\*Devítiocase\*\*", message.embeds[0].description):
            print("----- Devítiocas - Kill -----")
            await zaslatZde.send(str(message.embeds[0].description) + ' <t:'+ currTime +':R>')
            return 

        if re.search(".*právě zabil \*\*Tmavého krále plamenů\*\*", message.embeds[0].description):
            print("----- Král Plamenů - Kill -----")
            await zaslatZde.send(str(message.embeds[0].description) + ' <t:'+ currTime +':R>')
            return 

        if re.search(".*právě zabil \*\*Velkého žlutého ducha tygra\*\*", message.embeds[0].description):
            print("----- Velký žlutý duch tygr - Kill -----")
            await zaslatZde.send(str(message.embeds[0].description) + ' <t:'+ currTime +':R>')
            return 

        if re.search(".*právě zabil \*\*Obřího Humra\*\*", message.embeds[0].description):
            print("----- Obří Humr - Kill -----")
            await zaslatZde.send(str(message.embeds[0].description) + ' <t:'+ currTime +':R>')
            return 

        if re.search(".*právě zabil \*\*King Konga\*\*", message.embeds[0].description):
            print("----- King Kong - Kill -----")
            await zaslatZde.send(str(message.embeds[0].description) + ' <t:'+ currTime +':R>')
            return 

        if re.search(".*právě zabil \*\*Zeleného draka\*\*", message.embeds[0].description):
            print("----- Zelený drak - Kill -----")
            await zaslatZde.send(str(message.embeds[0].description) + ' <t:'+ currTime +':R>')
            return 

if os.path.exists("token.txt"):
    fToken = open("token.txt", "r").readline()
    client.run(fToken)
else:
    print("token doesnt exist cya later")

