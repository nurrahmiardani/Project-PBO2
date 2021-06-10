import wx
import desain
import sqlite3

class Kain(desain.MyFrame1):
    def __init__(self, parent):
        super().__init__(parent)

    def add(self, event):
        # self.isitabel()
        jenis = self.inputJenis.GetValue()
        warna = self.inputWarna.GetValue()
        harga = self.inputHarga.GetValue()
        stok = self.inputStok.GetValue()

        if jenis == '' or warna == '' or harga == '' or stok == '' :
            wx.MessageBox ('Harap mengisi data yang kosong!')
        elif not harga.isdecimal() or not stok.isdecimal():
            wx.MessageBox ('Harga dan Stok harus berupa angka, mohon isi dengan kembali dengan benar')
        elif not (wx.OK):
            self.inputJenis.SetValue("")
            self.inputWarna.SetValue("") 
            self.inputHarga.SetValue("") 
            self.inputStok.SetValue("") 
            # conn = sqlite3.connect('pesananbaju.db') 
            # cursor = conn.cursor()
            # data = cursor.execute("SELECT * FROM kain").fetchall()
            # conn.close()
            # for baris in range(len(data)):
            #     self.m_grid1.AppendRows()
            #     for kolom in range (len(data[baris])):
            #         self.m_grid1.SetCellValue(baris, kolom, str(data[baris][kolom]))
        else :
            conn = sqlite3.connect('pesananbaju.db') 
            cursor = conn.cursor()
            # for baris in range(len(data)):
            #     self.m_grid1.AppendRows()
            #     for kolom in range (len(data[baris])):
            #         self.m_grid1.SetCellValue(baris, kolom, str(data[baris][kolom]))
            data = cursor.execute("INSERT INTO kain (jenis, warna, harga, stok) VALUES (?,?,?,?)", (jenis, warna, harga, stok))
            data = cursor.execute("SELECT * FROM kain").fetchall()
            conn.commit()
            conn.close()
            for baris in range(len(data)):
                self.m_grid1.AppendRows()
                for kolom in range (len(data[baris])):
                    self.m_grid1.SetCellValue(baris, kolom, str(data[baris][kolom]))
            print("Data berhasil disimpan")
            wx.MessageBox ("Data berhasil disimpan", "Information", wx.OK | wx.ICON_INFORMATION)
    
    # def isitabel(self):
    #     conn = sqlite3.connect('pesananbaju.db') 
    #     cursor = conn.cursor()
    #     data = cursor.execute("INSERT INTO kain (jenis, warna, harga, stok) VALUES (?,?,?,?)", (jenis, warna, harga, stok))
    #     data = cursor.execute("SELECT * FROM kain").fetchall()
    #     conn.commit()
    #     conn.close()
    #     self.data = "select * from kain"
    #     for baris in range(len(data)):
    #         self.m_grid1.AppendRows()
    #         for kolom in range (len(data[baris])):
    #             self.m_grid1.SetCellValue(baris, kolom, str(data[baris][kolom]))

    def edit( self, event ):
        jenis = self.inputJenis.GetValue()
        warna = self.inputWarna.GetValue()
        harga = self.inputHarga.GetValue()
        stok = self.inputStok.GetValue()

        if jenis == '' or warna == '' or harga == '' or stok == '' :
            wx.MessageBox ('Harap mengisi data yang kosong!')
        elif not harga.isdecimal() or not stok.isdecimal():
            wx.MessageBox ('Harga dan Stok harus berupa angka, mohon isi dengan kembali dengan benar')
        elif not (wx.OK):
            self.inputJenis.SetValue("")
            self.inputWarna.SetValue("") 
            self.inputHarga.SetValue("") 
            self.inputStok.SetValue("") 

        else : 
            conn = sqlite3.connect('pesananbaju.db')
            cursor = conn.cursor()
            data = cursor.execute("update kain set jenis = ? ,warna = ?, harga = ?, stok = ?, where ID = ? ", (self.jenis, self.warna, self.harga, self.stok, self.__ID))
            data = cursor.execute("SELECT * FROM kain").fetchall()
            conn.commit()
            conn.close()
            for baris in range(len(data)):
                self.m_grid1.AppendRows()
                for kolom in range (len(data[baris])):
                    self.m_grid1.SetCellValue(baris, kolom, str(data[baris][kolom]))
            print("Data berhasil disimpan")
            wx.MessageBox ("Data berhasil disimpan", "Information", wx.OK | wx.ICON_INFORMATION)


		

	

app = wx.App()
tampilan = Kain(parent=None).Show()
app.MainLoop()