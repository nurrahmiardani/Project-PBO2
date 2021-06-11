# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class halaman_awal
###########################################################################

class halaman_awal ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 255, 255, 181 ) )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel16 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self.m_panel16, wx.ID_ANY, u"Selamat Datang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )
		self.m_staticText11.SetForegroundColour( wx.Colour( 230, 230, 0 ) )
		self.m_staticText11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer14.Add( self.m_staticText11, 0, wx.ALIGN_CENTER|wx.ALL, 15 )

		self.m_staticText12 = wx.StaticText( self.m_panel16, wx.ID_ANY, u"Di SMARTWING", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )
		self.m_staticText12.SetForegroundColour( wx.Colour( 221, 221, 0 ) )
		self.m_staticText12.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer14.Add( self.m_staticText12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self.m_panel16, wx.ID_ANY, u"^_^", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )
		self.m_staticText13.SetForegroundColour( wx.Colour( 235, 122, 20 ) )
		self.m_staticText13.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer14.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.ALL, 15 )

		self.next = wx.Button( self.m_panel16, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.Size( 150,35 ), 0 )
		self.next.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.next.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )

		bSizer14.Add( self.next, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel16.SetSizer( bSizer14 )
		self.m_panel16.Layout()
		bSizer14.Fit( self.m_panel16 )
		bSizer13.Add( self.m_panel16, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.next.Bind( wx.EVT_BUTTON, self.nextOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def nextOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class pilihan_frame
###########################################################################

class pilihan_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 181 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel15 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText12 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Silahkan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )

		bSizer11.Add( self.m_staticText12, 0, wx.ALIGN_CENTER|wx.ALL, 10 )

		self.m_staticText13 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Pilih Salah Satu ^_^", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )

		bSizer11.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.ALL, 10 )


		self.m_panel15.SetSizer( bSizer11 )
		self.m_panel15.Layout()
		bSizer11.Fit( self.m_panel15 )
		bSizer9.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel14 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		self.penjahit_btn = wx.Button( self.m_panel14, wx.ID_ANY, u"Penjahit", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.penjahit_btn.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.penjahit_btn.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		gSizer6.Add( self.penjahit_btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.pelanggan_btn = wx.Button( self.m_panel14, wx.ID_ANY, u"Pelanggan", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.pelanggan_btn.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.pelanggan_btn.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.pelanggan_btn.SetBackgroundColour( wx.Colour( 145, 160, 217 ) )

		gSizer6.Add( self.pelanggan_btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.m_panel14.SetSizer( gSizer6 )
		self.m_panel14.Layout()
		gSizer6.Fit( self.m_panel14 )
		bSizer9.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.penjahit_btn.Bind( wx.EVT_BUTTON, self.penjahit_btnOnButtonClick )
		self.pelanggan_btn.Bind( wx.EVT_BUTTON, self.pelanggan_btnOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def penjahit_btnOnButtonClick( self, event ):
		event.Skip()

	def pelanggan_btnOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class login_penjahit_frame
###########################################################################

class login_penjahit_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"LOGIN PENJAHIT", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.SetBackgroundColour( wx.Colour( 255, 255, 181 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.judul_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1.Add( self.judul_panel, 0, wx.EXPAND |wx.ALL, 5 )

		self.atas_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.user_label_penjahit = wx.StaticText( self.atas_panel, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.user_label_penjahit.Wrap( -1 )

		self.user_label_penjahit.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.user_label_penjahit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.isi_user_penjahit = wx.TextCtrl( self.atas_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.isi_user_penjahit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.psw_label_penjahit = wx.StaticText( self.atas_panel, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.psw_label_penjahit.Wrap( -1 )

		self.psw_label_penjahit.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.psw_label_penjahit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.isi_psw_penjahit = wx.TextCtrl( self.atas_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.isi_psw_penjahit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.atas_panel.SetSizer( gSizer2 )
		self.atas_panel.Layout()
		gSizer2.Fit( self.atas_panel )
		bSizer1.Add( self.atas_panel, 1, wx.EXPAND |wx.ALL, 5 )

		self.bawah_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.login_penjahit = wx.Button( self.bawah_panel, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.Size( 165,-1 ), 0 )
		self.login_penjahit.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer2.Add( self.login_penjahit, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.registrasi_penjahit = wx.Button( self.bawah_panel, wx.ID_ANY, u"Registrasi", wx.DefaultPosition, wx.Size( 165,-1 ), 0 )
		self.registrasi_penjahit.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.registrasi_penjahit.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.registrasi_penjahit.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer2.Add( self.registrasi_penjahit, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.bawah_panel.SetSizer( bSizer2 )
		self.bawah_panel.Layout()
		bSizer2.Fit( self.bawah_panel )
		bSizer1.Add( self.bawah_panel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.login_penjahit.Bind( wx.EVT_BUTTON, self.login_penjahitOnButtonClick )
		self.registrasi_penjahit.Bind( wx.EVT_BUTTON, self.registrasi_penjahitOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def login_penjahitOnButtonClick( self, event ):
		event.Skip()

	def registrasi_penjahitOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class regis_penjahit_frame
###########################################################################

class regis_penjahit_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"REGISTRASI PENJAHIT", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 181 ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7.Add( self.m_panel10, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.username_label = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username_label.Wrap( -1 )

		self.username_label.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer4.Add( self.username_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.username_baru = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.username_baru, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.pass_label = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pass_label.Wrap( -1 )

		self.pass_label.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer4.Add( self.pass_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.pass_baru = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.pass_baru, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel11.SetSizer( gSizer4 )
		self.m_panel11.Layout()
		gSizer4.Fit( self.m_panel11 )
		bSizer7.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel12 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.regis_penjahit = wx.Button( self.m_panel12, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.regis_penjahit.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.regis_penjahit.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.regis_penjahit.SetBackgroundColour( wx.Colour( 24, 219, 19 ) )

		bSizer8.Add( self.regis_penjahit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel12.SetSizer( bSizer8 )
		self.m_panel12.Layout()
		bSizer8.Fit( self.m_panel12 )
		bSizer7.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.regis_penjahit.Bind( wx.EVT_BUTTON, self.regis_penjahitOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def regis_penjahitOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class login_pelanggan_frame
###########################################################################

class login_pelanggan_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"LOGIN PELANGGAN", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.SetBackgroundColour( wx.Colour( 255, 255, 181 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.judul_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1.Add( self.judul_panel, 0, wx.EXPAND |wx.ALL, 5 )

		self.atas_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.user_label = wx.StaticText( self.atas_panel, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.user_label.Wrap( -1 )

		gSizer2.Add( self.user_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.isi_user = wx.TextCtrl( self.atas_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.isi_user, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.psw_label = wx.StaticText( self.atas_panel, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.psw_label.Wrap( -1 )

		gSizer2.Add( self.psw_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.isi_psw = wx.TextCtrl( self.atas_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.isi_psw, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.atas_panel.SetSizer( gSizer2 )
		self.atas_panel.Layout()
		gSizer2.Fit( self.atas_panel )
		bSizer1.Add( self.atas_panel, 1, wx.EXPAND |wx.ALL, 5 )

		self.bawah_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.login = wx.Button( self.bawah_panel, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.login, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.registrasi = wx.Button( self.bawah_panel, wx.ID_ANY, u"Registrasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.registrasi.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.registrasi.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer2.Add( self.registrasi, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.bawah_panel.SetSizer( bSizer2 )
		self.bawah_panel.Layout()
		bSizer2.Fit( self.bawah_panel )
		bSizer1.Add( self.bawah_panel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.login.Bind( wx.EVT_BUTTON, self.loginOnButtonClick )
		self.registrasi.Bind( wx.EVT_BUTTON, self.registrasiOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def loginOnButtonClick( self, event ):
		event.Skip()

	def registrasiOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class regis_pelanggan_frame
###########################################################################

class regis_pelanggan_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"REGISTRASI PELANGGAN", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 181 ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7.Add( self.m_panel10, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.username_label = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username_label.Wrap( -1 )

		gSizer4.Add( self.username_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.username_baru = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.username_baru, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.pass_label = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pass_label.Wrap( -1 )

		gSizer4.Add( self.pass_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.pass_baru = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.pass_baru, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel11.SetSizer( gSizer4 )
		self.m_panel11.Layout()
		gSizer4.Fit( self.m_panel11 )
		bSizer7.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel12 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.regis = wx.Button( self.m_panel12, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.regis.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.regis.SetBackgroundColour( wx.Colour( 26, 210, 26 ) )

		bSizer8.Add( self.regis, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel12.SetSizer( bSizer8 )
		self.m_panel12.Layout()
		bSizer8.Fit( self.m_panel12 )
		bSizer7.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.regis.Bind( wx.EVT_BUTTON, self.regisOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def regisOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class beranda_penjahit_frame
###########################################################################

class beranda_penjahit_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,384 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 181 ) )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText14 = wx.StaticText( self.m_panel17, wx.ID_ANY, u"SMARTWING", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )
		self.m_staticText14.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer15.Add( self.m_staticText14, 0, wx.ALIGN_CENTER|wx.ALL, 15 )


		self.m_panel17.SetSizer( bSizer15 )
		self.m_panel17.Layout()
		bSizer15.Fit( self.m_panel17 )
		bSizer11.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel15 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.pilih_kain = wx.Button( self.m_panel15, wx.ID_ANY, u"Pilihan Kain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pilih_kain.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.pilih_kain.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.pilih_kain.SetBackgroundColour( wx.Colour( 176, 176, 176 ) )

		bSizer12.Add( self.pilih_kain, 0, wx.ALIGN_CENTER|wx.ALL|wx.SHAPED, 10 )

		self.pesanan = wx.Button( self.m_panel15, wx.ID_ANY, u"Pesanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pesanan.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.pesanan.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer12.Add( self.pesanan, 0, wx.ALIGN_CENTER|wx.ALL|wx.SHAPED, 10 )

		self.logout = wx.Button( self.m_panel15, wx.ID_ANY, u"Log out", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.logout.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.logout.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.logout.SetBackgroundColour( wx.Colour( 206, 0, 0 ) )

		bSizer12.Add( self.logout, 0, wx.ALIGN_CENTER|wx.ALL|wx.SHAPED, 10 )


		self.m_panel15.SetSizer( bSizer12 )
		self.m_panel15.Layout()
		bSizer12.Fit( self.m_panel15 )
		bSizer11.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.pilih_kain.Bind( wx.EVT_BUTTON, self.btn_pilihkan )
		self.pesanan.Bind( wx.EVT_BUTTON, self.btn_pesanan )
		self.logout.Bind( wx.EVT_BUTTON, self.btn_keluar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_pilihkan( self, event ):
		event.Skip()

	def btn_pesanan( self, event ):
		event.Skip()

	def btn_keluar( self, event ):
		event.Skip()


