import requests

name = input("Player's name: ")

profile_url = "https://apps.runescape.com/runemetrics/profile/profile?user="+name+"&activities=20"
response = requests.get(profile_url)

class Skills:
    def __init__(self, lvl, xp, rank, ID):
        self.lvl = lvl
        self.xp = xp
        self.rank = rank

s1 = Skills(response.json()['skillvalues'][0]['level'],
                response.json()['skillvalues'][0]['xp'],
                response.json()['skillvalues'][0]['rank'],
		response.json()['skillvalues'][0]['id'])

s2 = Skills(response.json()['skillvalues'][1]['level'],
                 response.json()['skillvalues'][1]['xp'],
                 response.json()['skillvalues'][1]['rank'],
		response.json()['skillvalues'][1]['id'])

s3 = Skills(response.json()['skillvalues'][2]['level'],
                  response.json()['skillvalues'][2]['xp'],
                  response.json()['skillvalues'][2]['rank'],
		  response.json()['skillvalues'][2]['id'])

s4 = Skills(response.json()['skillvalues'][3]['level'],
                  response.json()['skillvalues'][3]['xp'],
                  response.json()['skillvalues'][3]['rank'],
		  response.json()['skillvalues'][3]['id'])

s5 = Skills(response.json()['skillvalues'][4]['level'],
                 response.json()['skillvalues'][4]['xp'],
                 response.json()['skillvalues'][4]['rank'],
		 response.json()['skillvalues'][4]['id'])

s6 = Skills(response.json()['skillvalues'][5]['level'],
                 response.json()['skillvalues'][5]['xp'],
                 response.json()['skillvalues'][5]['rank'],
		 response.json()['skillvalues'][5]['id'])

s7 = Skills(response.json()['skillvalues'][6]['level'],
                 response.json()['skillvalues'][6]['xp'],
                 response.json()['skillvalues'][6]['rank'],
		 response.json()['skillvalues'][6]['id'])

s8 = Skills(response.json()['skillvalues'][7]['level'],
                 response.json()['skillvalues'][7]['xp'],
                 response.json()['skillvalues'][7]['rank'],
		 response.json()['skillvalues'][7]['id'])

s9 = Skills(response.json()['skillvalues'][8]['level'],
                 response.json()['skillvalues'][8]['xp'],
                 response.json()['skillvalues'][8]['rank'],
		 response.json()['skillvalues'][8]['id'])

s10 = Skills(response.json()['skillvalues'][9]['level'],
                 response.json()['skillvalues'][9]['xp'],
                 response.json()['skillvalues'][9]['rank'],
		 response.json()['skillvalues'][9]['id'])

s11 = Skills(response.json()['skillvalues'][10]['level'],
                 response.json()['skillvalues'][10]['xp'],
                 response.json()['skillvalues'][10]['rank'],
		 response.json()['skillvalues'][10]['id'])

s12 = Skills(response.json()['skillvalues'][11]['level'],
                 response.json()['skillvalues'][11]['xp'],
                 response.json()['skillvalues'][11]['rank'],
		 response.json()['skillvalues'][11]['id'])

s13 = Skills(response.json()['skillvalues'][12]['level'],
                 response.json()['skillvalues'][12]['xp'],
                 response.json()['skillvalues'][12]['rank'],
	 	 response.json()['skillvalues'][12]['id'])

s14 = Skills(response.json()['skillvalues'][13]['level'],
                 response.json()['skillvalues'][13]['xp'],
                 response.json()['skillvalues'][13]['rank'],
		 response.json()['skillvalues'][13]['id'])

s15 = Skills(response.json()['skillvalues'][14]['level'],
                 response.json()['skillvalues'][14]['xp'],
                 response.json()['skillvalues'][14]['rank'],
		 response.json()['skillvalues'][14]['id'])

s16 = Skills(response.json()['skillvalues'][15]['level'],
                 response.json()['skillvalues'][15]['xp'],
                 response.json()['skillvalues'][15]['rank'],
		 response.json()['skillvalues'][15]['id'])

s17 = Skills(response.json()['skillvalues'][16]['level'],
                 response.json()['skillvalues'][16]['xp'],
                 response.json()['skillvalues'][16]['rank'],
		 response.json()['skillvalues'][16]['id'])

s18 = Skills(response.json()['skillvalues'][17]['level'],
                 response.json()['skillvalues'][17]['xp'],
                 response.json()['skillvalues'][17]['rank'],
 		 response.json()['skillvalues'][17]['id'])

s19 = Skills(response.json()['skillvalues'][18]['level'],
                 response.json()['skillvalues'][18]['xp'],
                 response.json()['skillvalues'][18]['rank'],
    		 response.json()['skillvalues'][18]['id'])

s20 = Skills(response.json()['skillvalues'][19]['level'],
                 response.json()['skillvalues'][19]['xp'],
                 response.json()['skillvalues'][19]['rank'],
		 response.json()['skillvalues'][19]['id'])

s21 = Skills(response.json()['skillvalues'][20]['level'],
                 response.json()['skillvalues'][20]['xp'],
                 response.json()['skillvalues'][20]['rank'],
		 response.json()['skillvalues'][20]['id'])

s22 = Skills(response.json()['skillvalues'][21]['level'],
                 response.json()['skillvalues'][21]['xp'],
                 response.json()['skillvalues'][21]['rank'],
		 response.json()['skillvalues'][21]['id'])

s23 = Skills(response.json()['skillvalues'][22]['level'],
                 response.json()['skillvalues'][22]['xp'],
                 response.json()['skillvalues'][22]['rank'],
		 response.json()['skillvalues'][22]['id'])

s24 = Skills(response.json()['skillvalues'][23]['level'],
                 response.json()['skillvalues'][23]['xp'],
                 response.json()['skillvalues'][23]['rank'],
		 response.json()['skillvalues'][23]['id'])

s25 = Skills(response.json()['skillvalues'][24]['level'],
                 response.json()['skillvalues'][24]['xp'],
                 response.json()['skillvalues'][24]['rank'],
		 response.json()['skillvalues'][24]['id'])

s26 = Skills(response.json()['skillvalues'][25]['level'],
                 response.json()['skillvalues'][25]['xp'],
                 response.json()['skillvalues'][25]['rank'],
	 	 response.json()['skillvalues'][25]['id'])

s27 = Skills(response.json()['skillvalues'][26]['level'],
                 response.json()['skillvalues'][26]['xp'],
                 response.json()['skillvalues'][26]['rank'],
		 response.json()['skillvalues'][26]['id'])

s28 = Skills(response.json()['skillvalues'][27]['level'],
                 response.json()['skillvalues'][27]['xp'],
                 response.json()['skillvalues'][27]['rank'],
	       	 response.json()['skillvalues'][27]['id'])

s29 = Skills(response.json()['skillvalues'][28]['level'],
                 response.json()['skillvalues'][28]['xp'],
                 response.json()['skillvalues'][28]['rank'],
		 response.json()['skillvalues'][28]['id'])

