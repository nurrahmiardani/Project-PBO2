from os import name
import wx
import Awalan
import home
import desain
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
        username = self.isi_user.GetValue()
        password = self.isi_psw.GetValue()
        conn = sqlite3.connect('pesananbaju.db')
        cursor = conn.cursor()
        cek_akun = ("SELECT * FROM akun_pelanggan WHERE username = ? AND password = ?")
        cursor.execute(cek_akun,(username,password))
        results = cursor.fetchall()
        if results :
            for i in results :
                wx.MessageBox("Berhasil Login")
                login = frame(parent=self)
                login.Show()
                # if(wx.OK):
                #     self.Destroy()

                    
        else :
            wx.MessageBox("username dan password belum terdaftar","Silahkan melakukan Registrasi!")

    def registrasiOnButtonClick(self, event):
        reg = Registrasi_Pelanggan(parent=self)
        reg.Show()

class Beranda_penjahit(Awalan.beranda_penjahit_frame):
    def __init__(self, parent):
        super().__init__(parent)
    
    def btn_pilihkan( self, event ):
        pil = Kain(parent=self)
        pil.Show()
        conn = sqlite3.connect('pesananbaju.db')
        cursor = conn.cursor()
        data = cursor.execute("SELECT * FROM kain").fetchall()
        conn.close()
        for baris in range (len(data)):
            self.tabelkain.AppendRows()
            for kolom in range(len(data[baris])) :
                self.tabelkain.SetCellValue(baris, kolom, str(data[baris][kolom]))


        # conn = sqlite3.connect('pesananbaju.db')
        # cursor = conn.cursor()
        # data = cursor.execute("select * from kain").fetchall()
        # conn.close()
        # for baris in range(len(data)):
        #     self..AppendRows()
        #     for kolom in range (len(data[baris])) :
        #         self.m_grid1.SetCellValue(baris, kolom, str(data[baris][kolom]))


    def btn_pesanan(self, event):
        pil1 = pesanan(parent=self)
        pil1.Show()

class pesanan (Awalan.pesanan_frame):
    def __init__(self, parent):
        super().__init__(parent)

    def bajuOnButtonClick ( self, event ):
        baju = Baju(parent=self)
        baju.Show()

    def celanaOnButtonClick ( self, event ):
        cln = Celana(parent=self)
        cln.Show()


class Baju (Awalan.baju_frame):
    def __init__(self, parent):
        super().__init__(parent)
        conn = sqlite3.connect('pesananbaju.db')
        cursor = conn.cursor()
        data = cursor.execute("select * from baju").fetchall()
        conn.close()
        for baris in range(len(data)):
            self.status_baju.AppendRows()
            for kolom in range (len(data[baris])) :
                self.status_baju.SetCellValue(baris, kolom, str(data[baris][kolom]))

    def editOnButtonClick ( self, event ):
        nama = self.isi_nama.GetValue()
        status = self.isi_status.GetValue()
        conn = sqlite3.connect('pesananbaju.db')
        cursor = conn.cursor()
        data = "UPDATE baju SET status = ? where nama =?"
        isian = (status,nama)
        cursor.execute(data,isian)
        data = cursor.execute("SELECT * FROM baju").fetchall()
        conn.commit()
        conn.close()
        for baris in range(len(data)):
            self.status_baju.AppendRows()
            for kolom in range (len(data[baris])):
                self.status_baju.SetCellValue(baris, kolom, str(data[baris][kolom]))
        print("Data berhasil diupdate")
        wx.MessageBox ("Data berhasil diupdate", "Information", wx.OK | wx.ICON_INFORMATION)

    def kembaliOnButtonClick ( self, event ):
        pil = Beranda_penjahit(parent=self)
        pil.Show()

class Celana (Awalan.celana_frame):
    def __init__(self, parent):
        super().__init__(parent)
        conn = sqlite3.connect('pesananbaju.db')
        cursor = conn.cursor()
        data = cursor.execute("select * from celana").fetchall()
        conn.close()
        for baris in range(len(data)):
            self.status_celana.AppendRows()
            for kolom in range (len(data[baris])) :
                self.status_celana.SetCellValue(baris, kolom, str(data[baris][kolom]))

    def editOnButtonClick ( self, event ):
        nama = self.isi_nama.GetValue()
        status = self.isi_status.GetValue()
        conn = sqlite3.connect('pesananbaju.db')
        cursor = conn.cursor()
        data = "UPDATE celana SET status = ? where nama =?"
        isian = (status,nama)
        cursor.execute(data,isian)
        data = cursor.execute("SELECT * FROM celana").fetchall()
        conn.commit()
        conn.close()
        for baris in range(len(data)):
            self.status_celana.AppendRows()
            for kolom in range (len(data[baris])):
                self.status_celana.SetCellValue(baris, kolom, str(data[baris][kolom]))
        print("Data berhasil diupdate")
        wx.MessageBox ("Data berhasil diupdate", "Information", wx.OK | wx.ICON_INFORMATION)
    
    def kembaliOnButtonClick ( self, event ):
        pil = Beranda_penjahit(parent=self)
        pil.Show()
        

class frame (home.MyFrame1):
    def __init__(self,parent):
        super().__init__(parent)
    def btn_pesan(self,event):
        b = frame2(parent=self)
        b.Show()
    def btn_daftar(self, event):
        c = DaftarPesan(parent=self)
        c.Show()
    def btn_cek (self,event) :
        d = CariNama(parent=self)
        d.Show()
    def btn_logout(self, event):
        e = halaman(parent=self)
        e.Show()
        

class frame2(home.MyFrame2):
    def __init__(self, parent):
        super().__init__(parent)
    def btn_baju(self, event):
        baju = framebaju(parent=self)
        baju.Show()
        
    def btn_celana(self, event):
        celana = framecelana(parent=self)
        celana.Show()

class DaftarPesan(home.MyFrame9):
    def __init__(self, parent):
        super().__init__(parent)
        conn = sqlite3.connect('pesananbaju.db')
        cursor = conn.cursor()
        data = cursor.execute("select * from kain").fetchall()
        conn.close()
        for baris in range(len(data)):
            self.tabelkain.AppendRows()
            for kolom in range (len(data[baris])) :
                self.tabelkain.SetCellValue(baris, kolom, str(data[baris][kolom]))

class CariNama(home.MyFrame7):
    def __init__(self, parent):
        super().__init__(parent)
    def btn_cari(self, event):
        namaa = self.namacari.GetValue()
        conn = sqlite3.connect('pesananbaju.db')
        cursor = conn.cursor()
        data = cursor.execute("select * from baju WHERE nama = ?", (namaa,)).fetchall()
        datacelana = cursor.execute("select * from celana WHERE nama = ?", (namaa,)).fetchall()
        for baris in range(len(data)):
            self.tabelcari.AppendRows()
            for kolom in range (len(data[baris])) :
                self.tabelcari.SetCellValue(baris, kolom, str(data[baris][kolom]))
        for baris in range(len(datacelana)):
            self.tabelcelana.AppendRows()
            for kolom in range (len(datacelana[baris])) :
                self.tabelcelana.SetCellValue(baris, kolom, str(datacelana[baris][kolom]))
        self.namacari.SetValue("")
        
class framebaju (home.MyFrame3):
    def __init__(self, parent):
        super().__init__(parent)
    def btn_pesanbaju(self, event):
        jenis = self.isikain.GetValue()
        warna = self.isiwarna.GetValue()
        lebar = self.isilebar.GetValue()
        panjang = self.isipanjang.GetValue()
        nama = self.isinama.GetValue()

        if jenis == '' or lebar =='' or panjang =='' or warna =='':
            wx.MessageBox ('Isian harus lengkap', 'Peringatan data kosong')
        elif not lebar.isdecimal() or not panjang.isdecimal() :
            wx.MessageBox ("Lebar Dada atau Panjang Baju harus berupa angka","peringatan kesalahan angka") 
        else :
            conn = sqlite3.connect('pesananbaju.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO baju (jenis,warna,lingkar_dada,panjang_baju,nama) VALUES (?,?,?,?,?)",(jenis,warna,lebar,panjang,nama))
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
        nama = self.isinamaa.GetValue()
        if jeniscel == '' or pinggang =='' or panjangcel =='' or warnacel=='':
            wx.MessageBox ('Isian harus lengkap', 'Peringatan data kosong')
        elif not pinggang.isdecimal() or not panjangcel.isdecimal() :
            wx.MessageBox ("Lingkar Pinggang atau Panjang Celana harus berupa angka","peringatan kesalahan angka") 
        else :
            conn = sqlite3.connect('pesananbaju.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO celana (jenis,warna,lingkar_pinggang,panjang_celana,nama) VALUES (?,?,?,?,?)",(jeniscel,warnacel,pinggang,panjangcel,nama))
            conn.commit()
            conn.close()
            wx.MessageBox ('Data berhasil disimpan', 'Data berhasil disimpan')
            if (wx.OK):
                self.Destroy()

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

class Kain(desain.MyFrame1):
    def __init__(self, parent):
        super().__init__(parent)

    def add(self, event):
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
            conn = sqlite3.connect('myDB.db')
            cursor = conn.cursor()
            data = cursor.execute("SELECT * FROM kain").fetchall()
            conn.commit()
            conn.close()
            for baris in range(len(data)):
                self.m_grid1.DeleteRows(id)
                for kolom in range (len(data[baris])):
                    self.m_grid1.SetCellValue(baris, kolom, str(data[baris][kolom]))
            print("Data berhasil dihapus")
            wx.MessageBox ("Data berhasil dihapus", "Information", wx.OK | wx.ICON_INFORMATION)

        else : 
            print("Data gagal ")
            wx.MessageBox ("Data gagal dihapus", "Information", wx.OK | wx.ICON_INFORMATION)



app = wx.App()
a = halaman(parent=None)
a.Show()   
app.MainLoop()   
