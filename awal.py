import wx
import Awalan
import sqlite3

class halaman(Awalan.halaman_awal):
    def __init__(self, parent):
        super().__init__(parent)

    def nextOnButtonClick(self, event):
        awal = Pilihan (parent=self)
        awal.Show()


class Pilihan(Awalan.pilihan_frame):
    def __init__(self, parent):
        super().__init__(parent)

    def penjahit_btnOnButtonClick(self, event):
        penjahit = Login_penjahit (parent=self)
        penjahit.Show()

    def pelanggan_btnOnButtonClick(self, event):
        pelanggan = Login_Pelanggan (parent=self)
        pelanggan.Show()


class Login_penjahit(Awalan.login_penjahit_frame):
    def __init__(self, parent):
        super().__init__(parent)

    def login_penjahitOnButtonClick(self,event):
        username = self.isi_user_penjahit.GetValue()
        password = self.isi_psw_penjahit.GetValue()
        conn = sqlite3.connect('pesananbaju.db')
        cursor = conn.cursor()
        cek_akun = ("SELECT * FROM akun_penjahit WHERE username = ? AND password = ?")
        cursor.execute(cek_akun,(username,password))
        results = cursor.fetchall()
        if results :
            for i in results :
                wx.MessageBox("Berhasil Login")
                login = Beranda_penjahit(parent=self)
                login.Show()
                # if(wx.OK):
                #     self.Destroy()
                    
        else :
            wx.MessageBox("username dan password belum terdaftar","Silahkan melakukan Registrasi!")
        

    def registrasi_penjahitOnButtonClick(self, event):
        self.usernm = self.isi_user_penjahit.GetValue()
        self.psw = self.isi_psw_penjahit.GetValue()
        reg = Registrasi_penjahit(parent=self)
        reg.Show()


class Registrasi_penjahit(Awalan.regis_penjahit_frame):
    def __init__(self, parent):
        super().__init__(parent)

    def regis_penjahitOnButtonClick(self, event):
        log = Login_penjahit(parent=self)
        log.Show()
        username = self.username_baru.GetValue()
        password = self.pass_baru.GetValue()
        if username == "" :
            wx.MessageBox("Username harus terisi!")
        elif password == "" :
            wx.MessageBox("Password harus terisi!")
        else :
            conn = sqlite3.connect('pesananbaju.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO akun_penjahit(username,password) VALUES(?,?)",(username,password))
            conn.commit()
            conn.close()
            wx.MessageBox("Data BERHASIL disimpan")
            if(wx.OK):
                self.Destroy()



class Login_Pelanggan(Awalan.login_pelanggan_frame):
    def __init__(self, parent):
        super().__init__(parent)

    def loginOnButtonClick(self,event):
        username = self.isi_user_penjahit.GetValue()
        password = self.isi_psw_penjahit.GetValue()
        conn = sqlite3.connect('pesananbaju.db')
        cursor = conn.cursor()
        cek_akun = ("SELECT * FROM akun_pelanggan WHERE username = ? AND password = ?")
        cursor.execute(cek_akun,(username,password))
        results = cursor.fetchall()
        if results :
            for i in results :
                wx.MessageBox("Berhasil Login")
                login = Beranda_penjahit(parent=self)
                login.Show()
                # if(wx.OK):
                #     self.Destroy()
                    
        else :
            wx.MessageBox("username dan password belum terdaftar","Silahkan melakukan Registrasi!")

    def registrasiOnButtonClick(self, event):
        reg = Registrasi_Pelanggan(parent=self)
        reg.Show()


class Registrasi_Pelanggan(Awalan.regis_pelanggan_frame):
    def __init__(self, parent):
        super().__init__(parent)

    def regisOnButtonClick(self, event):
        log = Login_Pelanggan(parent=self)
        log.Show()
        username = self.username_baru.GetValue()
        password = self.pass_baru.GetValue()
        if username == "" :
            wx.MessageBox("Username harus terisi!")
        elif password == "" :
            wx.MessageBox("Password harus terisi!")
        else :
            conn = sqlite3.connect('pesananbaju.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO akun_pelanggan(username,password) VALUES(?,?)",(username,password))
            conn.commit()
            conn.close()
            wx.MessageBox("Data BERHASIL disimpan")
            if(wx.OK):
                self.Destroy()
    

class Beranda_penjahit(Awalan.beranda_penjahit_frame):
    def __init__(self, parent):
        super().__init__(parent)




app = wx.App()
a = halaman(parent=None)
a.Show()   
app.MainLoop()   
