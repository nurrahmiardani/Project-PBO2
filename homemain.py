import wx
import home
import sqlite3

class frame (home.MyFrame1):
    def __init__(self,parent):
        super().__init__(parent)
    def btn_pesan(self,event):
        b = frame2(parent=self)
        b.Show()
    def btn_daftar(self, event):
        c = frame3(parent=self)
        c.Show()
  
        

class frame2(home.MyFrame2):
    def __init__(self, parent):
        super().__init__(parent)
    def btn_baju(self, event):
        baju = framebaju(parent=self)
        baju.Show()
    def btn_celana(self, event):
        celana = framecelana(parent=self)
        celana.Show()

class frame3(home.MyFrame9):
    def __init__(self, parent):
        super().__init__(parent)


class framebaju (home.MyFrame3):
    def __init__(self, parent):
        super().__init__(parent)
    def btn_pesanbaju(self, event):
        jenis = self.isikain.GetValue()
        warna = self.isiwarna.GetValue()
        lebar = self.isilebar.GetValue()
        panjang = self.isipanjang.GetValue()

        if jenis == '' or lebar =='' or panjang =='' or warna =='':
            wx.MessageBox ('Isian harus lengkap', 'Peringatan data kosong')
        elif not lebar.isdecimal() or not panjang.isdecimal() :
            wx.MessageBox ("Lebar Dada atau Panjang Baju harus berupa angka","peringatan kesalahan angka") 
        else :
            conn = sqlite3.connect('pesananbaju.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO baju (jenis,warna,lingkar_dada,panjang_baju) VALUES (?,?,?,?)",(jenis,warna,lebar,panjang))
            conn.commit()
            conn.close()
            wx.MessageBox ('Data berhasil disimpan', 'Data berhasil disimpan')
            if (wx.OK):
                self.Destroy()
class framecelana (home.MyFrame4):
    def __init__(self, parent):
        super().__init__(parent)
    def btn_pesancelana(self, event):
        jeniscel = self.isijeniscelana.GetValue()
        warnacel = self.isiwarnacelana.GetValue()
        pinggang = self.isilingkar.GetValue()
        panjangcel = self.isipanjangcelana.GetValue()
        if jeniscel == '' or pinggang =='' or panjangcel =='' or warnacel=='':
            wx.MessageBox ('Isian harus lengkap', 'Peringatan data kosong')
        elif not pinggang.isdecimal() or not panjangcel.isdecimal() :
            wx.MessageBox ("Lingkar Pinggang atau Panjang Celana harus berupa angka","peringatan kesalahan angka") 
        else :
            conn = sqlite3.connect('pesananbaju.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO celana (jenis,warna,lingkar_pinggang,panjang_celana) VALUES (?,?,?,?)",(jeniscel,warnacel,pinggang,panjangcel))
            conn.commit()
            conn.close()
            wx.MessageBox ('Data berhasil disimpan', 'Data berhasil disimpan')
            if (wx.OK):
                self.Destroy()
            

app = wx.App()
tampil = frame(parent=None)
tampil.Show()
app.MainLoop()