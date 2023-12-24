import requests
import wx
import wx.xrc


# La liste des skills par ID
skills_name = ["Attack","Defence","Strength","Constitution","Ranged","Prayer","Magic","Cooking",
               "Woodcutting","Fletching","Fishing","Firemaking","Crafting","Smithing","Mining",
               "Herblore","Agility","Thieving","Slayer","Farming","Runecrafting","Hunter","Construction",
               "Summoning","Dungeoneering","Divination","Invention","Archaeology","Necromancy"]

name = input("Enter name: ")

# La classe des skills
class Skills:
    def __init__(self, lvl, xp, rank, name):
        self.lvl = lvl
        self.xp = xp
        self.rank = rank
        self.name = name

#sans ça, ça fait une erreur je ne sais pas pourquoi


# La function pour pogner les skills
def get_skills(input_name):	

	# Requests va prendre le fichier .json selon le joueur choisi
	profile_url = "https://apps.runescape.com/runemetrics/profile/profile?user="+input_name+"&activities=20"
	response = requests.get(profile_url)


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

	return s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29

# Lancer la function et mettre ca dans skills
skills = get_skills(name)

# Le GUI ( merci maxou )
class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 300,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, name, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_PROCESS_ENTER )
		bSizer1.Add( self.m_textCtrl2, 0, wx.ALL|wx.EXPAND, 5 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )
		
		skillstomatch = "Attack"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button23 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button23.SetBitmap( wx.Bitmap( u"icons/Attack-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button23, 0, wx.ALL, 5 )

		skillstomatch = "Constitution"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button24 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button24.SetBitmap( wx.Bitmap( u"icons/Constitution-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button24, 0, wx.ALL, 5 )

		skillstomatch = "Mining"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button25 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button25.SetBitmap( wx.Bitmap( u"icons/Mining-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button25, 0, wx.ALL, 5 )

		skillstomatch = "Strength"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button26 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button26.SetBitmap( wx.Bitmap( u"icons/Strength-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button26, 0, wx.ALL, 5 )

		skillstomatch = "Agility"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button27 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button27.SetBitmap( wx.Bitmap( u"icons/Agility-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button27, 0, wx.ALL, 5 )
		
		skillstomatch = "Smithing"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button28 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button28.SetBitmap( wx.Bitmap( u"icons/Smithing-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button28, 0, wx.ALL, 5 )

		skillstomatch = "Defence"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button29 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button29.SetBitmap( wx.Bitmap( u"icons/Defence-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button29, 0, wx.ALL, 5 )
		
		skillstomatch = "Herblore"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button30 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button30.SetBitmap( wx.Bitmap( u"icons/Herblore-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button30, 0, wx.ALL, 5 )
		
		skillstomatch = "Fishing"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button31 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button31.SetBitmap( wx.Bitmap( u"icons/Fishing-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button31, 0, wx.ALL, 5 )

		skillstomatch = "Ranged"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button32 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button32.SetBitmap( wx.Bitmap( u"icons/Ranged-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button32, 0, wx.ALL, 5 )

		skillstomatch = "Thieving"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button33 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button33.SetBitmap( wx.Bitmap( u"icons/Thieving-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button33, 0, wx.ALL, 5 )

		skillstomatch = "Cooking"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button34 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button34.SetBitmap( wx.Bitmap( u"icons/Cooking-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button34, 0, wx.ALL, 5 )

		skillstomatch = "Prayer"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button35 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button35.SetBitmap( wx.Bitmap( u"icons/Prayer-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button35, 0, wx.ALL, 5 )

		skillstomatch = "Crafting"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button36 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button36.SetBitmap( wx.Bitmap( u"icons/Crafting-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button36, 0, wx.ALL, 5 )

		skillstomatch = "Firemaking"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button37 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button37.SetBitmap( wx.Bitmap( u"icons/Firemaking-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button37, 0, wx.ALL, 5 )

		skillstomatch = "Magic"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button38 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button38.SetBitmap( wx.Bitmap( u"icons/Magic-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button38, 0, wx.ALL, 5 )

		skillstomatch = "Fletching"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button39 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button39.SetBitmap( wx.Bitmap( u"icons/Fletching-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button39, 0, wx.ALL, 5 )

		skillstomatch = "Woodcutting"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button40 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button40.SetBitmap( wx.Bitmap( u"icons/Woodcutting-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button40, 0, wx.ALL, 5 )

		skillstomatch = "Runecrafting"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button41 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button41.SetBitmap( wx.Bitmap( u"icons/Runecrafting-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button41, 0, wx.ALL, 5 )

		skillstomatch = "Slayer"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button42 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button42.SetBitmap( wx.Bitmap( u"icons/Slayer-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button42, 0, wx.ALL, 5 )

		skillstomatch = "Farming"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button43 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button43.SetBitmap( wx.Bitmap( u"icons/Farming-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button43, 0, wx.ALL, 5 )

		skillstomatch = "Construction"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button44 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button44.SetBitmap( wx.Bitmap( u"icons/Construction-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button44, 0, wx.ALL, 5 )

		skillstomatch = "Hunter"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button45 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button45.SetBitmap( wx.Bitmap( u"icons/Hunter-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button45, 0, wx.ALL, 5 )
		
		skillstomatch = "Summoning"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button46 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button46.SetBitmap( wx.Bitmap( u"icons/Summoning-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button46, 0, wx.ALL, 5 )

		skillstomatch = "Dungeoneering"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button47 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button47.SetBitmap( wx.Bitmap( u"icons/Dungeoneering-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button47, 0, wx.ALL, 5 )

		skillstomatch = "Divination"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button48 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button48.SetBitmap( wx.Bitmap( u"icons/Divination-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button48, 0, wx.ALL, 5 )

		skillstomatch = "Invention"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button49 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button49.SetBitmap( wx.Bitmap( u"icons/Invention-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button49, 0, wx.ALL, 5 )

		skillstomatch = "Archaeology"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button50 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button50.SetBitmap( wx.Bitmap( u"icons/Archaeology-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button50, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )

		skillstomatch = "Necromancy"
		for item in skills:
			if item.name == skillstomatch:
				self.m_button51 = wx.Button( self, wx.ID_ANY, str(item.lvl), wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_button51.SetBitmap( wx.Bitmap( u"icons/Necromancy-icon.png", wx.BITMAP_TYPE_ANY ) )
				wSizer1.Add( self.m_button51, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )


		bSizer1.Add( wSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrl2.Bind( wx.EVT_TEXT_ENTER, self.search_player )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def search_player( self, event ):
		event.Skip()



	

# old main
class CalcFrame(MyFrame1):
    def __init__(self,parent):
        MyFrame1.__init__(self,parent)

    def search_player(self,event):
        user_input = event.GetValue()
        get_skills(user_input)
        MyFrame1.Refresh(self)
		


app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)

app.MainLoop()
