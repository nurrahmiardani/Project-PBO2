import wx
import desain
import sqlite3

class Kain(desain.MyFrame1):
    def __init__(self, parent):
        super().__init__(parent)

    def add(self, event):
        # self.isitabel()
        id = self.inputID.GetValue()
        jenis = self.inputJenis.GetValue()
        warna = self.inputWarna.GetValue()
        harga = self.inputHarga.GetValue()
        stok = self.inputStok.GetValue()

        if id == '' or jenis == '' or warna == '' or harga == '' or stok == '' :
            wx.MessageBox ('Harap mengisi data yang kosong!')
        elif not id.isdecimal() or not harga.isdecimal() or not stok.isdecimal():
            wx.MessageBox ('Nomor ID, harga, dan Stok harus berupa angka, mohon isi dengan kembali dengan benar')
        elif not (wx.OK):
            self.inputID.SetValue("")
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
            data = cursor.execute("INSERT INTO kain (ID, jenis, warna, harga, stok) VALUES (?,?,?,?,?)", (id, jenis, warna, harga, stok))
            data = cursor.execute("SELECT * FROM kain").fetchall()
            conn.commit()
            conn.close()
            for baris in range(len(data)):
                self.m_grid1.AppendRows()
                for kolom in range (len(data[baris])):
                    self.m_grid1.SetCellValue(baris, kolom, str(data[baris][kolom]))
            print("Data berhasil disimpan")
            wx.MessageBox ("Data berhasil disimpan", "Information", wx.OK | wx.ICON_INFORMATION)

    def edit( self, event ):
        id = self.inputID.GetValue()
        jenis = self.inputJenis.GetValue()
        warna = self.inputWarna.GetValue()
        harga = self.inputHarga.GetValue()
        stok = self.inputStok.GetValue()

        if jenis == '' or warna == '' or harga == '' or stok == '' :
            wx.MessageBox ('Harap mengisi data yang kosong!')
        elif not harga.isdecimal() or not stok.isdecimal():
            wx.MessageBox ('Harga dan Stok harus berupa angka, mohon isi dengan kembali dengan benar')
        elif not (wx.OK):
            self.inputID.SetValue("")
            self.inputJenis.SetValue("")
            self.inputWarna.SetValue("") 
            self.inputHarga.SetValue("") 
            self.inputStok.SetValue("") 

        else : 
            conn = sqlite3.connect('pesananbaju.db')
            cursor = conn.cursor()
            # self.data = "update kain set jenis = ?,warna = ?, harga = ?, stok = ? where ID = ? "
            # self.isian = (self.jenis, self.warna, self.harga, self.stok, self.ID)
            data = "UPDATE kain SET jenis = ?, warna = ?, harga = ?, stok = ? where ID=?"
            isian = (jenis, warna, harga, stok, id)
            cursor.execute(data, isian)
            data = cursor.execute("SELECT * FROM kain").fetchall()
            conn.commit()
            conn.close()
            for baris in range(len(data)):
                self.m_grid1.AppendRows()
                for kolom in range (len(data[baris])):
                    self.m_grid1.SetCellValue(baris, kolom, str(data[baris][kolom]))
            print("Data berhasil diupdate")
            wx.MessageBox ("Data berhasil diupdate", "Information", wx.OK | wx.ICON_INFORMATION)

    def delete( self, event ):
        id = self.inputID.GetValue()
        # jenis = self.inputJenis.GetValue()
        # warna = self.inputWarna.GetValue()
        # harga = self.inputHarga.GetValue()
        # stok = self.inputStok.GetValue()

        if (wx.OK):
            self.inputID.SetValue("")
            # self.inputJenis.SetValue("")
            # self.inputWarna.SetValue("") 
            # self.inputHarga.SetValue("") 
            # self.inputStok.SetValue("")
            conn = sqlite3.connect('pesananbaju.db')
            cursor = conn.cursor()
            data = "DELETE from kain where ID=?"
            isian = (id)
            cursor.execute(data, isian)
            conn.commit()
            conn.close()
            print("Data berhasil dihapus")
            wx.MessageBox ("Data berhasil dihapus", "Information", wx.OK | wx.ICON_INFORMATION)

        else : 
            print("Data gagal ")
            wx.MessageBox ("Data berhasil dihapus", "Information", wx.OK | wx.ICON_INFORMATION)

app = wx.App()
tampilan = Kain(parent=None).Show()
app.MainLoop()