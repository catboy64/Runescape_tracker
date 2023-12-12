import requests

# Tu demandes au user le nom du joueur

name = input("Player's name: ")

# Requests va prendre le fichier .json selon le joueur choisi

profile_url = "https://apps.runescape.com/runemetrics/profile/profile?user="+name+"&activities=20"
response = requests.get(profile_url)

# La liste des skills par ID

skills_name = ["Attack","Defence","Strength","Constitution","Ranged","Prayer","Magic","Cooking",
               "Woodcutting","Fletching","Fishing","Firemaking","Crafting","Smithing","Mining",
               "Herblore","Agility","Thieving","Slayer","Farming","Runecrafting","Hunter","Construction",
               "Summoning","Dungeoneering","Divination","Invention","Archaeology","Necromancy"]

# La classe des skills

class Skills:
    def __init__(self, lvl, xp, rank, name):
        self.lvl = lvl
        self.xp = xp
        self.rank = rank
        self.name = name

# Parse le fichier .json (ignore ce tas de marde)

s1 = Skills(response.json()['skillvalues'][0]['level'],
                response.json()['skillvalues'][0]['xp'],
                response.json()['skillvalues'][0]['rank'],
                skills_name[response.json()['skillvalues'][0]['id']])

s2 = Skills(response.json()['skillvalues'][1]['level'],
                 response.json()['skillvalues'][1]['xp'],
                 response.json()['skillvalues'][1]['rank'],
                 skills_name[response.json()['skillvalues'][1]['id']])

s3 = Skills(response.json()['skillvalues'][2]['level'],
                  response.json()['skillvalues'][2]['xp'],
                  response.json()['skillvalues'][2]['rank'],
                  skills_name[response.json()['skillvalues'][2]['id']])

s4 = Skills(response.json()['skillvalues'][3]['level'],
                  response.json()['skillvalues'][3]['xp'],
                  response.json()['skillvalues'][3]['rank'],
                  skills_name[response.json()['skillvalues'][3]['id']])

s5 = Skills(response.json()['skillvalues'][4]['level'],
                 response.json()['skillvalues'][4]['xp'],
                 response.json()['skillvalues'][4]['rank'],
                 skills_name[response.json()['skillvalues'][4]['id']])

s6 = Skills(response.json()['skillvalues'][5]['level'],
                 response.json()['skillvalues'][5]['xp'],
                 response.json()['skillvalues'][5]['rank'],
	  	 skills_name[response.json()['skillvalues'][5]['id']])

s7 = Skills(response.json()['skillvalues'][6]['level'],
                 response.json()['skillvalues'][6]['xp'],
                 response.json()['skillvalues'][6]['rank'],
		 skills_name[response.json()['skillvalues'][6]['id']])

s8 = Skills(response.json()['skillvalues'][7]['level'],
                 response.json()['skillvalues'][7]['xp'],
                 response.json()['skillvalues'][7]['rank'],
		 skills_name[response.json()['skillvalues'][7]['id']])

s9 = Skills(response.json()['skillvalues'][8]['level'],
                 response.json()['skillvalues'][8]['xp'],
                 response.json()['skillvalues'][8]['rank'],
		 skills_name[response.json()['skillvalues'][8]['id']])

s10 = Skills(response.json()['skillvalues'][9]['level'],
                 response.json()['skillvalues'][9]['xp'],
                 response.json()['skillvalues'][9]['rank'],
		 skills_name[response.json()['skillvalues'][9]['id']])

s11 = Skills(response.json()['skillvalues'][10]['level'],
                 response.json()['skillvalues'][10]['xp'],
                 response.json()['skillvalues'][10]['rank'],
		 skills_name[response.json()['skillvalues'][10]['id']])

s12 = Skills(response.json()['skillvalues'][11]['level'],
                 response.json()['skillvalues'][11]['xp'],
                 response.json()['skillvalues'][11]['rank'],
		 skills_name[response.json()['skillvalues'][11]['id']])

s13 = Skills(response.json()['skillvalues'][12]['level'],
                 response.json()['skillvalues'][12]['xp'],
                 response.json()['skillvalues'][12]['rank'],
		 skills_name[response.json()['skillvalues'][12]['id']])

s14 = Skills(response.json()['skillvalues'][13]['level'],
                 response.json()['skillvalues'][13]['xp'],
                 response.json()['skillvalues'][13]['rank'],
		 skills_name[response.json()['skillvalues'][13]['id']])

s15 = Skills(response.json()['skillvalues'][14]['level'],
                 response.json()['skillvalues'][14]['xp'],
                 response.json()['skillvalues'][14]['rank'],
		 skills_name[response.json()['skillvalues'][14]['id']])

s16 = Skills(response.json()['skillvalues'][15]['level'],
                 response.json()['skillvalues'][15]['xp'],
                 response.json()['skillvalues'][15]['rank'],
	  	 skills_name[response.json()['skillvalues'][15]['id']])

s17 = Skills(response.json()['skillvalues'][16]['level'],
                 response.json()['skillvalues'][16]['xp'],
                 response.json()['skillvalues'][16]['rank'],
		 skills_name[response.json()['skillvalues'][16]['id']])

s18 = Skills(response.json()['skillvalues'][17]['level'],
                 response.json()['skillvalues'][17]['xp'],
                 response.json()['skillvalues'][17]['rank'],
		 skills_name[response.json()['skillvalues'][17]['id']])

s19 = Skills(response.json()['skillvalues'][18]['level'],
                 response.json()['skillvalues'][18]['xp'],
                 response.json()['skillvalues'][18]['rank'],
		 skills_name[response.json()['skillvalues'][18]['id']])

s20 = Skills(response.json()['skillvalues'][19]['level'],
                 response.json()['skillvalues'][19]['xp'],
                 response.json()['skillvalues'][19]['rank'],
		 skills_name[response.json()['skillvalues'][19]['id']])

s21 = Skills(response.json()['skillvalues'][20]['level'],
                 response.json()['skillvalues'][20]['xp'],
                 response.json()['skillvalues'][20]['rank'],
		 skills_name[response.json()['skillvalues'][20]['id']])

s22 = Skills(response.json()['skillvalues'][21]['level'],
                 response.json()['skillvalues'][21]['xp'],
                 response.json()['skillvalues'][21]['rank'],
		 skills_name[response.json()['skillvalues'][21]['id']])

s23 = Skills(response.json()['skillvalues'][22]['level'],
                 response.json()['skillvalues'][22]['xp'],
                 response.json()['skillvalues'][22]['rank'],
		 skills_name[response.json()['skillvalues'][22]['id']])

s24 = Skills(response.json()['skillvalues'][23]['level'],
                 response.json()['skillvalues'][23]['xp'],
                 response.json()['skillvalues'][23]['rank'],
		 skills_name[response.json()['skillvalues'][23]['id']])

s25 = Skills(response.json()['skillvalues'][24]['level'],
                 response.json()['skillvalues'][24]['xp'],
                 response.json()['skillvalues'][24]['rank'],
	 	 skills_name[response.json()['skillvalues'][24]['id']])

s26 = Skills(response.json()['skillvalues'][25]['level'],
                 response.json()['skillvalues'][25]['xp'],
                 response.json()['skillvalues'][25]['rank'],
		 skills_name[response.json()['skillvalues'][25]['id']])

s27 = Skills(response.json()['skillvalues'][26]['level'],
                 response.json()['skillvalues'][26]['xp'],
                 response.json()['skillvalues'][26]['rank'],
		 skills_name[response.json()['skillvalues'][26]['id']])

s28 = Skills(response.json()['skillvalues'][27]['level'],
                 response.json()['skillvalues'][27]['xp'],
                 response.json()['skillvalues'][27]['rank'],
		 skills_name[response.json()['skillvalues'][27]['id']])

s29 = Skills(response.json()['skillvalues'][28]['level'],
                 response.json()['skillvalues'][28]['xp'],
                 response.json()['skillvalues'][28]['rank'],
		 skills_name[response.json()['skillvalues'][28]['id']])

