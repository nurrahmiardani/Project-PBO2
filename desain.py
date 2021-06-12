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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 650,498 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 181 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"DATA KAIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer5.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel7 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_panel8 = wx.Panel( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer9.Add( self.m_staticText6, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticText31 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Jenis", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer9.Add( self.m_staticText31, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticText32 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Warna", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer9.Add( self.m_staticText32, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticText33 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer9.Add( self.m_staticText33, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticText34 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Stok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer9.Add( self.m_staticText34, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.m_panel8.SetSizer( bSizer9 )
		self.m_panel8.Layout()
		bSizer9.Fit( self.m_panel8 )
		gSizer3.Add( self.m_panel8, 1, wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT, 5 )

		self.m_panel11 = wx.Panel( self.m_panel7, wx.ID_ANY, wx.Point( -1,-1 ), wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.inputID = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer10.Add( self.inputID, 0, wx.ALL, 5 )

		self.inputJenis = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 200,-1 ), 0 )
		bSizer10.Add( self.inputJenis, 0, wx.ALL, 5 )

		self.inputWarna = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer10.Add( self.inputWarna, 0, wx.ALL, 5 )

		self.inputHarga = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer10.Add( self.inputHarga, 0, wx.ALL, 5 )

		self.inputStok = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer10.Add( self.inputStok, 0, wx.ALL, 5 )


		self.m_panel11.SetSizer( bSizer10 )
		self.m_panel11.Layout()
		bSizer10.Fit( self.m_panel11 )
		gSizer3.Add( self.m_panel11, 0, wx.ALL, 5 )

		self.m_panel12 = wx.Panel( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_button7 = wx.Button( self.m_panel12, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button7.SetBackgroundColour( wx.Colour( 85, 255, 170 ) )

		bSizer11.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_button8 = wx.Button( self.m_panel12, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button8.SetBackgroundColour( wx.Colour( 255, 128, 64 ) )

		bSizer11.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_button9 = wx.Button( self.m_panel12, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button9.SetBackgroundColour( wx.Colour( 255, 72, 72 ) )

		bSizer11.Add( self.m_button9, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.m_panel12.SetSizer( bSizer11 )
		self.m_panel12.Layout()
		bSizer11.Fit( self.m_panel12 )
		gSizer3.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel7.SetSizer( gSizer3 )
		self.m_panel7.Layout()
		gSizer3.Fit( self.m_panel7 )
		bSizer5.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer5 )
		self.m_panel2.Layout()
		bSizer5.Fit( self.m_panel2 )
		bSizer4.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.tabelsemwakain = wx.grid.Grid( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabelsemwakain.CreateGrid( 5, 5 )
		self.tabelsemwakain.EnableEditing( True )
		self.tabelsemwakain.EnableGridLines( True )
		self.tabelsemwakain.EnableDragGridSize( False )
		self.tabelsemwakain.SetMargins( 0, 0 )

		# Columns
		self.tabelsemwakain.EnableDragColMove( False )
		self.tabelsemwakain.EnableDragColSize( True )
		self.tabelsemwakain.SetColLabelSize( 30 )
		self.tabelsemwakain.SetColLabelValue( 0, u"ID" )
		self.tabelsemwakain.SetColLabelValue( 1, u"Jenis" )
		self.tabelsemwakain.SetColLabelValue( 2, u"Warna" )
		self.tabelsemwakain.SetColLabelValue( 3, u"Harga" )
		self.tabelsemwakain.SetColLabelValue( 4, u"Stok" )
		self.tabelsemwakain.SetColLabelValue( 5, u"warna" )
		self.tabelsemwakain.SetColLabelValue( 6, u"warna" )
		self.tabelsemwakain.SetColLabelValue( 7, u"warna" )
		self.tabelsemwakain.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelsemwakain.EnableDragRowSize( True )
		self.tabelsemwakain.SetRowLabelSize( 80 )
		self.tabelsemwakain.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.tabelsemwakain.SetLabelBackgroundColour( wx.Colour( 80, 80, 80 ) )
		self.tabelsemwakain.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		# Cell Defaults
		self.tabelsemwakain.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.tabelsemwakain.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer6.Add( self.tabelsemwakain, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel6.SetSizer( bSizer6 )
		self.m_panel6.Layout()
		bSizer6.Fit( self.m_panel6 )
		bSizer4.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.DataKain )
		self.m_button7.Bind( wx.EVT_BUTTON, self.add )
		self.m_button8.Bind( wx.EVT_BUTTON, self.edit )
		self.m_button9.Bind( wx.EVT_BUTTON, self.delete )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def DataKain( self, event ):
		event.Skip()

	def add( self, event ):
		event.Skip()

	def edit( self, event ):
		event.Skip()

	def delete( self, event ):
		event.Skip()


