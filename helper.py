import random
import string
import os





def getrefID():
    characters =  string.digits + string.ascii_uppercase
    return ''.join(random.choice(characters) for _ in range(15))
 
def getphone():
    sb = []

    sb.append('9')
    
    for i in range(9):
         
         digit = str(random.randint(0, 9))
         sb.append(digit)

    return ''.join(sb) 

def getIp():
    ip = []
    for i in range(4):

        digit = str(random.randint(100, 233))
        ip.append(digit)
    return ".".join(ip)

def getpan():
    pans = ["ABCTY1234D", "AAJCT3251A", "IIJPS4226k", "AALCA0171E"]
    return random.choice(pans)

def getgst():
    gsts = ["33AAJCT3251A1ZU", "33AADCF9175D1ZP", "33AABCT0422H2ZW", "33AAHCP1178L1Z7", "33AAEFD7067L1Z8", "33AAAGM0289C1ZQ", "33AEUPA7288L2ZU", "33AALCA0171E1Z6"]
    return random.choice(gsts)       
        

def getaadhar():
    sb = []

    for i in range(16):
         digit = str(random.randint(0, 9))
         sb.append(digit)

    return ''.join(sb)

   
def getTrade():
   
    department_names = ["Microsoft Corp", "IBM Corp", "Cisco Systems Inc", "Oracle Corp", "Squidex", "meat and eat", "well done"]
    domain = random.choice(department_names)
    
    return domain

def getname():
    names = [
    "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hank", "Ivy", "Jack",
    "Kate", "Leo", "Mia", "Nick", "Olivia", "Paul", "Quinn", "Rose", "Sam", "Tina",
    "Ulysses", "Vera", "Walter", "Xander", "Yvonne", "Zane", "Abigail", "Benjamin", "Chloe", "Daniel",
    "Eleanor", "Finn", "Gemma", "Henry", "Isabella", "James", "Katherine", "Liam", "Mila", "Nathan",
    "Oscar", "Penelope", "Quentin", "Rachel", "Seth", "Sophie", "Tristan", "Uma", "Victor", "Willa",
    "Xavier", "Yasmine", "Zachary", "Aria", "Brady", "Cora", "Dylan", "Eliza", "Felix", "Gianna",
    "Hudson", "Isabel", "Jacob", "Kaia", "Luna", "Max", "Nora", "Owen", "Poppy", "Quincy", "Rebecca",
    "Sebastian", "Thea", "Usher", "Violet", "Wyatt", "Ximena", "Yara", "Zara", "Aaron", "Bella",
    "Caleb", "Daisy", "Elijah", "Fiona", "Gabriel", "Hazel", "Isaac", "Julia", "Kai", "Lily"
]

    return random.choice(names)



def getweburl():
    urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.amazon.com",
    "https://www.nytimes.com",
    "https://www.wikipedia.org",
    "https://www.cnn.com",
    "https://www.apple.com",
    "https://www.microsoft.com",
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://www.instagram.com",
    "https://www.twitter.com",
    "https://www.linkedin.com",
    "https://www.reddit.com",
    "https://www.stackoverflow.com",
    "https://www.netflix.com",
    "https://www.spotify.com",
    "https://www.pinterest.com",
    "https://www.tumblr.com",
    "https://www.yahoo.com",
    "https://www.bing.com",
    "https://www.wikipedia.com",
    "https://www.nasa.gov",
    "https://www.bbc.com",
    "https://www.duckduckgo.com",
    "https://www.quora.com",
    "https://www.dropbox.com",
    "https://www.medium.com",
    "https://www.twitch.tv",
    "https://www.wikipedia.org",
    "https://www.ebay.com",
    "https://www.aliexpress.com",
    "https://www.walmart.com",
    "https://www.target.com",
    "https://www.bestbuy.com",
    "https://www.homedepot.com",
    "https://www.lowes.com",
    "https://www.costco.com",
    "https://www.alibaba.com",
    "https://www.booking.com",
    "https://www.expedia.com",
    "https://www.airbnb.com",
    "https://www.zillow.com",
    "https://www.trulia.com",
    "https://www.realtor.com",
    "https://www.reuters.com",
    "https://www.bloomberg.com",
    "https://www.wsj.com",
    "https://www.ft.com",
    "https://www.economist.com",
    "https://www.forbes.com",
    "https://www.businessinsider.com",
    "https://www.cnbc.com",
    "https://www.buzzfeed.com",
    "https://www.techcrunch.com",
    "https://www.engadget.com",
    "https://www.arstechnica.com",
    "https://www.wired.com",
    "https://www.theverge.com",
    "https://www.mashable.com",
    "https://www.cnet.com",
    "https://www.pcworld.com",
    "https://www.tomsguide.com",
    "https://www.gamespot.com",
    "https://www.ign.com",
    "https://www.polygon.com",
    "https://www.kotaku.com",
    "https://www.eurogamer.net",
    "https://www.bbcgoodfood.com",
    "https://www.allrecipes.com",
    "https://www.foodnetwork.com",
    "https://www.epicurious.com",
    "https://www.bonappetit.com",
    "https://www.delish.com",
    "https://www.seriouseats.com",
    "https://www.foodandwine.com",
    "https://www.cooksillustrated.com",
    "https://www.myrecipes.com",
    "https://www.simplyrecipes.com",
    "https://www.thekitchn.com",
    "https://www.recipe.com",
    "https://www.skinnytaste.com",
    "https://www.bettycrocker.com",
    "https://www.kingarthurflour.com",
    "https://www.bbcgoodfood.com",
    "https://www.bbc.co.uk",
    "https://www.guardian.co.uk",
    "https://www.telegraph.co.uk",
    "https://www.independent.co.uk",
    "https://www.mirror.co.uk",
    "https://www.thesun.co.uk",
    "https://www.dailymail.co.uk",
    "https://www.nhs.uk",
    "https://www.gov.uk",
    "https://www.parliament.uk",
    "https://www.bbc.com",
    "https://www.news.sky.com",
    "https://www.itv.com",
    "https://www.channel4.com",
    "https://www.channel5.com",
    "https://www.bbc.co.uk",
    "https://www.nationalgeographic.com",
    "https://www.discovery.com",
    "https://www.smithsonianmag.com",
    "https://www.popsci.com",
    "https://www.scientificamerican.com",
    "https://www.nature.com",
    "https://www.newscientist.com",
    "https://www.nasa.gov",
    "https://www.space.com",
    "https://www.un.org",
    "https://www.worldbank.org",
    # Add more URLs as needed
]
    
    return random.choices(urls)
    

def getbusiness():
    names = [
    "TechCraft Solutions", "EcoGreen Innovations", "AlphaMatrix Enterprises", "Infinite Insights Co.",
    "SwiftSync Technologies", "Pinnacle Ventures", "Global Fusion Solutions", "BlueWave Innovations",
    "Stratosphere Solutions", "NexGen Dynamics", "SummitSpark Innovations", "Catalyst Creations",
    "Zenith Innovators", "Quantum Leap Ventures", "InnovateHub Solutions", "Vertex Visions Co.",
    "AccelerateX Enterprises", "ProActive Dynamics", "AgileMinds Innovations", "ElevateTech Solutions",
    "Skyline Synergy Ventures", "InnoSphere Technologies", "Nimbus Nexus Co.", "Apex Fusion Innovations",
    "TechPulse Dynamics", "FutureForge Enterprises", "OptiCore Innovations", "Synergetic Solutions",
    "InsightCraft Ventures", "StriveSync Technologies", "EvolveElite Innovations", "VivaVox Dynamics",
    "MindSpark Innovations", "InfinitiQuest Solutions", "SynthWave Enterprises", "EcoScape Innovations",
    "PentaPulse Technologies", "QuantumQuotient Ventures", "TechTraverse Dynamics", "Nexify Innovations",
    "VistaVortex Solutions", "InnovateIQ Ventures", "CatalystCraft Innovations", "FusionFlare Dynamics",
    "ZenithQuest Enterprises", "SummitShift Technologies", "AgileWave Innovations", "ElevateTech Dynamics",
    "StriveSphere Ventures", "ApexCraft Innovations", "InnoVista Technologies", "NimbusNest Dynamics",
    "ProActiveHub Ventures", "TechNucleus Innovations", "FutureFlare Solutions", "SynergeticSpark Co.",
    "VivaVista Innovations", "MindMatrix Dynamics", "InfinitiShift Ventures", "SynthCraft Innovations",
    "EcoVortex Technologies", "PentaQuest Solutions", "QuantumForge Enterprises", "TechTraverse Innovations",
    "NexGen Nexus Dynamics", "VistaForge Solutions", "InnovateElite Innovations", "CatalystSynergy Ventures",
    "FusionPulse Dynamics", "ZenithVortex Innovations", "SummitCraft Enterprises", "AgileFlare Innovations",
    "ElevateSphere Ventures", "Stratosphere Innovations", "NexifyCraft Technologies", "ProActiveQuotient Dynamics",
    "InsightPulse Innovations", "EvolveElite Solutions", "VivaCraft Ventures", "MindSphere Innovations",
    "InfinitiCraft Technologies", "SynthSync Dynamics", "EcoForge Ventures", "PentaShift Innovations",
    "QuantumElite Technologies", "TechNest Dynamics", "FutureFlare Innovations", "SynergeticSpark Ventures"
]

    return random.choice(names)

def getemail():
    names = [
    "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hank", "Ivy", "Jack",
    "Kate", "Leo", "Mia", "Nick", "Olivia", "Paul", "Quinn", "Rose", "Sam", "Tina",
    "Ulysses", "Vera", "Walter", "Xander", "Yvonne", "Zane", "Abigail", "Benjamin", "Chloe", "Daniel",
    "Eleanor", "Finn", "Gemma", "Henry", "Isabella", "James", "Katherine", "Liam", "Mila", "Nathan",
    "Oscar", "Penelope", "Quentin", "Rachel", "Seth", "Sophie", "Tristan", "Uma", "Victor", "Willa",
    "Xavier", "Yasmine", "Zachary", "Aria", "Brady", "Cora", "Dylan", "Eliza", "Felix", "Gianna",
    "Hudson", "Isabel", "Jacob", "Kaia", "Luna", "Max", "Nora", "Owen", "Poppy", "Quincy", "Rebecca",
    "Sebastian", "Thea", "Usher", "Violet", "Wyatt", "Ximena", "Yara", "Zara", "Aaron", "Bella",
    "Caleb", "Daisy", "Elijah", "Fiona", "Gabriel", "Hazel", "Isaac", "Julia", "Kai", "Lily"
]   
    random_name = random.choice(names)
    random_Num = random.randint(0,123456)
    gmail = "@gmail.com"
    email = f"{random_name}{random_Num}{gmail}"
    return email

def getApproveMsg():

    approvemessage ="Approved the data"
    return approvemessage


def getRejectMsg():

    rejectmessage ="Rejected the data"
    return rejectmessage

def getDelMsg():

    delmessage ="Deleted the 'Approved' data"
    return delmessage

def getInvestigateMsg():

    investigatemessage ="Investigate the data"
    return investigatemessage

def getLine():

    line = "                                                                        "

    #line = "•·······························•·······························•"
    return line

def getDotLine():


    dotline = "•·······························•·······························•"
    return dotline


def getDir():
    dir = os.getcwd()
    return dir
print(getDir())

