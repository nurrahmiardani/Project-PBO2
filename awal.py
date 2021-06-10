import wx
import Awalan

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
        self.usernm = self.isi_user_penjahit.GetValue()
        self.psw = self.isi_psw_penjahit.GetValue()
        login = Beranda_penjahit(parent=self)
        login.Show()

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


class Login_Pelanggan(Awalan.login_pelanggan_frame):
    def __init__(self, parent):
        super().__init__(parent)

    def loginOnButtonClick(self,event):
        self.usernm = self.isi_user.GetValue()
        self.psw = self.isi_psw.GetValue()
        login = Beranda_Pelanggan(parent=self)
        login.Show()

    def registrasiOnButtonClick(self, event):
        self.usernm = self.isi_user.GetValue()
        self.psw = self.isi_psw.GetValue()
        reg = Registrasi_Pelanggan(parent=self)
        reg.Show()


class Registrasi_Pelanggan(Awalan.regis_pelanggan_frame):
    def __init__(self, parent):
        super().__init__(parent)

    def regisOnButtonClick(self, event):
        log = Login_Pelanggan(parent=self)
        log.Show()
    

class Beranda_penjahit(Awalan.beranda_penjahit_frame):
    def __init__(self, parent):
        super().__init__(parent)




app = wx.App()
a = Pilihan(parent=None)
a.Show()   
app.MainLoop()   
