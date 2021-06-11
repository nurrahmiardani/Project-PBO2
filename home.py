# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 300,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 181 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer1.Add( self.m_staticText1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Silahkan pilih menu berikut ini", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer1.Add( self.m_staticText2, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.pesanklik = wx.Button( self, wx.ID_ANY, u"Pesan Sekarang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pesanklik.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.pesanklik.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer1.Add( self.pesanklik, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.EXPAND, 5 )

		self.cekklik = wx.Button( self, wx.ID_ANY, u"Cek Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cekklik.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.cekklik.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer1.Add( self.cekklik, 1, wx.ALL|wx.EXPAND, 5 )

		self.kainklik = wx.Button( self, wx.ID_ANY, u"Lihat Daftar Kain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kainklik.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.kainklik.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer1.Add( self.kainklik, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.logoutklik = wx.Button( self, wx.ID_ANY, u"LogOut", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.logoutklik.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.logoutklik.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer1.Add( self.logoutklik, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.pesanklik.Bind( wx.EVT_BUTTON, self.btn_pesan )
		self.cekklik.Bind( wx.EVT_BUTTON, self.btn_cek )
		self.kainklik.Bind( wx.EVT_BUTTON, self.btn_daftar )
		self.logoutklik.Bind( wx.EVT_BUTTON, self.btn_logout )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_pesan( self, event ):
		event.Skip()

	def btn_cek( self, event ):
		event.Skip()

	def btn_daftar( self, event ):
		event.Skip()

	def btn_logout( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 300,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 181 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Segera Pesan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Book Antiqua" ) )

		bSizer2.Add( self.m_staticText3, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Keinginanmu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		self.m_staticText27.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Book Antiqua" ) )

		bSizer2.Add( self.m_staticText27, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.bajuklik = wx.Button( self, wx.ID_ANY, u"Baju", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bajuklik.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.bajuklik.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer3.Add( self.bajuklik, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.celanaklik = wx.Button( self, wx.ID_ANY, u"Celana", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.celanaklik.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.celanaklik.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer3.Add( self.celanaklik, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.bajuklik.Bind( wx.EVT_BUTTON, self.btn_baju )
		self.celanaklik.Bind( wx.EVT_BUTTON, self.btn_celana )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_baju( self, event ):
		event.Skip()

	def btn_celana( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 181 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Sesuaikan Ukuran Bajumu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer4.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.isinama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.isinama, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Jenis Kain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.isikain = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.isikain, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Warna", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.isiwarna = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.isiwarna, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Lebar Dada", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.isilebar = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.isilebar, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Panjang Baju", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.isipanjang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.isipanjang, 0, wx.ALL, 5 )


		bSizer4.Add( gSizer2, 1, wx.EXPAND, 5 )

		self.pesanklik = wx.Button( self, wx.ID_ANY, u"Pesan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pesanklik.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.pesanklik.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer4.Add( self.pesanklik, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.pesanklik.Bind( wx.EVT_BUTTON, self.btn_pesanbaju )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_pesanbaju( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 181 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Sesuaikan Ukuran Celanamu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer4.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.isinamaa = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.isinamaa, 0, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Jenis Celana", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.isijeniscelana = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.isijeniscelana, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Warna", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.isiwarnacelana = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.isiwarnacelana, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Lingkar Pinggang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.isilingkar = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.isilingkar, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Panjang Celana", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.isipanjangcelana = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.isipanjangcelana, 0, wx.ALL, 5 )


		bSizer4.Add( gSizer2, 1, wx.EXPAND, 5 )

		self.pesancelanaklik = wx.Button( self, wx.ID_ANY, u"Pesan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pesancelanaklik.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.pesancelanaklik.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer4.Add( self.pesancelanaklik, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.pesancelanaklik.Bind( wx.EVT_BUTTON, self.btn_pesancelana )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_pesancelana( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame9
###########################################################################

class MyFrame9 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 181 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Daftar Kain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		self.m_staticText28.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText28.SetBackgroundColour( wx.Colour( 255, 255, 181 ) )

		bSizer9.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tabelkain = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabelkain.CreateGrid( 0, 5 )
		self.tabelkain.EnableEditing( True )
		self.tabelkain.EnableGridLines( True )
		self.tabelkain.EnableDragGridSize( False )
		self.tabelkain.SetMargins( 0, 0 )

		# Columns
		self.tabelkain.EnableDragColMove( False )
		self.tabelkain.EnableDragColSize( True )
		self.tabelkain.SetColLabelSize( 30 )
		self.tabelkain.SetColLabelValue( 0, u"ID" )
		self.tabelkain.SetColLabelValue( 1, u"Jenis" )
		self.tabelkain.SetColLabelValue( 2, u"Warna" )
		self.tabelkain.SetColLabelValue( 3, u"Harga" )
		self.tabelkain.SetColLabelValue( 4, u"Stok" )
		self.tabelkain.SetColLabelValue( 5, u"Stok" )
		self.tabelkain.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelkain.EnableDragRowSize( True )
		self.tabelkain.SetRowLabelSize( 80 )
		self.tabelkain.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.tabelkain.SetLabelBackgroundColour( wx.Colour( 80, 80, 80 ) )
		self.tabelkain.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		# Cell Defaults
		self.tabelkain.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.tabelkain.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.tabelkain.SetBackgroundColour( wx.Colour( 16, 16, 16 ) )

		bSizer9.Add( self.tabelkain, 0, wx.ALL, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame7
###########################################################################

class MyFrame7 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 554,345 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 181 ) )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.inputnama = wx.StaticText( self, wx.ID_ANY, u"Masukkan Namamu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputnama.Wrap( -1 )

		self.inputnama.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer8.Add( self.inputnama, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.namacari = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.namacari, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.klikcari = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.klikcari.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer8.Add( self.klikcari, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Baju", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Narrow" ) )

		bSizer8.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tabelcari = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabelcari.CreateGrid( 0, 5 )
		self.tabelcari.EnableEditing( True )
		self.tabelcari.EnableGridLines( True )
		self.tabelcari.EnableDragGridSize( False )
		self.tabelcari.SetMargins( 0, 0 )

		# Columns
		self.tabelcari.EnableDragColMove( False )
		self.tabelcari.EnableDragColSize( True )
		self.tabelcari.SetColLabelSize( 30 )
		self.tabelcari.SetColLabelValue( 0, u"Jenis" )
		self.tabelcari.SetColLabelValue( 1, u"Warna" )
		self.tabelcari.SetColLabelValue( 2, u"Lingkar Dada" )
		self.tabelcari.SetColLabelValue( 3, u"Panjang Baju" )
		self.tabelcari.SetColLabelValue( 4, u"Nama" )
		self.tabelcari.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelcari.EnableDragRowSize( True )
		self.tabelcari.SetRowLabelSize( 80 )
		self.tabelcari.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelcari.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer8.Add( self.tabelcari, 0, wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Celana", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		self.m_staticText20.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Narrow" ) )

		bSizer8.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tabelcelana = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabelcelana.CreateGrid( 0, 5 )
		self.tabelcelana.EnableEditing( True )
		self.tabelcelana.EnableGridLines( True )
		self.tabelcelana.EnableDragGridSize( False )
		self.tabelcelana.SetMargins( 0, 0 )

		# Columns
		self.tabelcelana.EnableDragColMove( False )
		self.tabelcelana.EnableDragColSize( True )
		self.tabelcelana.SetColLabelSize( 30 )
		self.tabelcelana.SetColLabelValue( 0, u"Jenis" )
		self.tabelcelana.SetColLabelValue( 1, u"Warna" )
		self.tabelcelana.SetColLabelValue( 2, u"Lingkar Pinggang" )
		self.tabelcelana.SetColLabelValue( 3, u"Panjang Celana" )
		self.tabelcelana.SetColLabelValue( 4, u"Nama" )
		self.tabelcelana.SetColLabelValue( 5, u"Jenis" )
		self.tabelcelana.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelcelana.EnableDragRowSize( True )
		self.tabelcelana.SetRowLabelSize( 80 )
		self.tabelcelana.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelcelana.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer8.Add( self.tabelcelana, 0, wx.ALL, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.klikcari.Bind( wx.EVT_BUTTON, self.btn_cari )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_cari( self, event ):
		event.Skip()


