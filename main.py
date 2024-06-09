
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\nawaw\OneDrive\Desktop\RektrafApp\build\assets")


def relative_to_assets(path: str) -> Path:return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("700x550")
window.configure(bg = "#FFFFFF")
window.title("Rektraf App")

canvas = Canvas(window,bg = "#FFFFFF",height = 550,width = 700,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

#------------ ASSETS BACKGROUND ------------#
bg_1 = PhotoImage(file=relative_to_assets("bg1.png"))
bg_2 = PhotoImage(file=relative_to_assets("bg2.png"))
bg_3 = PhotoImage(file=relative_to_assets("bg3.png"))
bg_4 = PhotoImage(file=relative_to_assets("bg4.png"))
bg_5 = PhotoImage(file=relative_to_assets("bg5.png"))
bg_6 = PhotoImage(file=relative_to_assets("bg6.png"))
bg_7 = PhotoImage(file=relative_to_assets("bg7.png"))

#------------ ASSETS ALL PAGE ------------#
home_utilisasi = PhotoImage(file=relative_to_assets("utilisasi.png"))
home_ws = PhotoImage(file=relative_to_assets("ws.png"))
home_ls = PhotoImage(file=relative_to_assets("ls.png"))
home_lq = PhotoImage(file=relative_to_assets("lq.png"))
home_wq = PhotoImage(file=relative_to_assets("wq.png"))
home_info = PhotoImage(file=relative_to_assets("info.png"))

utilitas_entry_image_1 = PhotoImage(file=relative_to_assets("utilitas_entry_1.png"))
utilitas_entry_image_2 = PhotoImage(file=relative_to_assets("utilitas_entry_2.png"))
utilitas_hitung = PhotoImage(file=relative_to_assets("utilitas_hitung.png"))
utilitas_back = PhotoImage(file=relative_to_assets("utilitas_back.png"))

ws_entry_image_1 = PhotoImage(file=relative_to_assets("ws_entry_1.png"))
ws_entry_image_2 = PhotoImage(file=relative_to_assets("ws_entry_2.png"))
ws_hitung = PhotoImage(file=relative_to_assets("ws_hitung.png"))
ws_back = PhotoImage(file=relative_to_assets("ws_back.png"))

ls_entry_image_1 = PhotoImage(file=relative_to_assets("ls_entry_1.png"))
ls_entry_image_2 = PhotoImage(file=relative_to_assets("ls_entry_2.png"))
ls_hitung = PhotoImage(file=relative_to_assets("ls_hitung.png"))
ls_back = PhotoImage(file=relative_to_assets("ls_back.png"))

lq_entry_image_1 = PhotoImage(file=relative_to_assets("lq_entry_1.png"))
lq_entry_image_2 = PhotoImage(file=relative_to_assets("lq_entry_2.png"))
lq_entry_image_3 = PhotoImage(file=relative_to_assets("lq_entry_2.png"))
lq_hitung = PhotoImage(file=relative_to_assets("lq_hitung.png"))
lq_back = PhotoImage(file=relative_to_assets("lq_back.png"))

wq_entry_image_1 = PhotoImage(file=relative_to_assets("wq_entry_1.png"))
wq_entry_image_2 = PhotoImage(file=relative_to_assets("wq_entry_2.png"))
wq_hitung = PhotoImage(file=relative_to_assets("wq_hitung.png"))
wq_back = PhotoImage(file=relative_to_assets("wq_back.png"))

info_back = PhotoImage(file=relative_to_assets("info_back.png"))

#------------ ALL PAGE ------------#
def buka_utilitas():

    def kembali():
        canvas.delete(bg,utilitas_entry1_image,utilitas_entry2_image, hasil)
        utilitas_btn_back.destroy()
        utilitas_btn_hitung.destroy()
        utilitas_entry1.destroy()
        utilitas_entry2.destroy()
        home()

    def hitung():
        try:
            x = float(utilitas_entry1.get())
            y = float(utilitas_entry2.get())
            
            if y == 0:
                messagebox.showerror("Error", "Entry tidak boleh 0.")
            else:
                z = x / y
                canvas.itemconfig(tagOrId=hasil, text=z)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid.")
        except tk.TclError: # type: ignore
            messagebox.showerror("Error", "Entry tidak boleh kosong.")

    bg = canvas.create_image(350.0,275.0,image=bg_2)

    hasil = canvas.create_text(270.0,428.0,anchor="nw",text="",fill="#000000",font=("RobotoRoman Regular", 13 * -1, "bold"))

    utilitas_entry1_image = canvas.create_image(349.5,329.5,image=utilitas_entry_image_1)
    utilitas_entry1 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    utilitas_entry1.place(x=156.0,y=312.0,width=387.0,height=29.0)

    utilitas_entry2_image = canvas.create_image(349.5,397.5,image=utilitas_entry_image_2)
    utilitas_entry2 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    utilitas_entry2.place(x=156.0,y=380.0,width=387.0,height=29.0)

    utilitas_btn_hitung = Button(image=utilitas_hitung,borderwidth=0,highlightthickness=0,command=hitung,relief="flat")
    utilitas_btn_hitung.place(x=252.0,y=459.0,width=196.0,height=31.0)

    utilitas_btn_back = Button(image=utilitas_back,borderwidth=0,highlightthickness=0,command=kembali,relief="flat")
    utilitas_btn_back.place(x=13.0,y=9.0,width=31.0,height=31.0)

def buka_ws():

    def kembali():
        canvas.delete(bg,ws_entry1_image,ws_entry2_image, hasil)
        ws_btn_back.destroy()
        ws_btn_hitung.destroy()
        ws_entry1.destroy()
        ws_entry2.destroy()
        home()

    def hitung():
        try:
            x = float(ws_entry1.get())
            y = float(ws_entry2.get())
            
            if y == 0:
                messagebox.showerror("Error", "Entry tidak boleh 0.")
            else:
                z = x + (1/y)
                canvas.itemconfig(tagOrId=hasil, text=z)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid.")
        except tk.TclError: # type: ignore
            messagebox.showerror("Error", "Entry tidak boleh kosong.")
    bg = canvas.create_image(350.0,275.0,image=bg_3)

    hasil = canvas.create_text(374.0,428.0,anchor="nw",text="",fill="#000000",font=("RobotoRoman Regular", 13 * -1, 'bold'))

    ws_entry1_image = canvas.create_image(349.5,329.5,image=ws_entry_image_1)
    ws_entry1 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    ws_entry1.place(x=156.0,y=312.0,width=387.0,height=29.0)
    
    ws_entry2_image = canvas.create_image(349.5,397.5,image=ws_entry_image_2)
    ws_entry2 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    ws_entry2.place(x=156.0,y=380.0,width=387.0,height=29.0)
    
    ws_btn_hitung = Button(image=ws_hitung,borderwidth=0,highlightthickness=0,command=hitung,relief="flat")
    ws_btn_hitung.place(x=252.0,y=459.0,width=196.0,height=31.0)

    ws_btn_back = Button(image=ws_back,borderwidth=0,highlightthickness=0,command=kembali,relief="flat")
    ws_btn_back.place(x=13.0,y=9.0,width=31.0,height=31.0)

def buka_ls():

    def kembali():
        canvas.delete(bg,ls_entry_1_image,ls_entry_2_image,hasil)
        ls_btn_back.destroy()
        ls_btn_hitung.destroy()
        ls_entry_1.destroy()
        ls_entry_2.destroy()
        home()

    def hitung():
        try:
            x = float(ls_entry_1.get())
            y = float(ls_entry_2.get())
            
            z = x + y
            canvas.itemconfig(tagOrId=hasil, text=z)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid.")
        except tk.TclError: # type: ignore
            messagebox.showerror("Error", "Entry tidak boleh kosong.")

    bg = canvas.create_image(350.0,275.0,image=bg_4)

    hasil = canvas.create_text(430.0,428.0,anchor="nw",text="",fill="#000000",font=("RobotoRoman Regular", 13 * -1, 'bold'))

    ls_entry_1_image = canvas.create_image(349.5,329.5,image=ls_entry_image_1)
    ls_entry_1 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    ls_entry_1.place(x=156.0,y=312.0,width=387.0,height=29.0)

    ls_entry_2_image = canvas.create_image(349.5,397.5,image=ls_entry_image_2)
    ls_entry_2 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    ls_entry_2.place(x=156.0,y=380.0,width=387.0,height=29.0)

    
    ls_btn_hitung = Button(image=ls_hitung,borderwidth=0,highlightthickness=0,command=hitung,relief="flat")
    ls_btn_hitung.place(x=252.0,y=459.0,width=196.0,height=31.0)

    ls_btn_back = Button(image=ls_back,borderwidth=0,highlightthickness=0,command=kembali,relief="flat")
    ls_btn_back.place(x=13.0,y=9.0,width=31.0,height=31.0)

def buka_lq():

    def kembali():
        canvas.delete(bg,lq_entry_1_image,lq_entry_2_image,lq_entry_3_image,hasil)
        lq_btn_back.destroy()
        lq_btn_hitung.destroy()
        lq_entry_1.destroy()
        lq_entry_2.destroy()
        lq_entry_3.destroy()
        home()

    def hitung():
        try:
            x = float(lq_entry_1.get())
            y = float(lq_entry_2.get())
            z = float(lq_entry_3.get())
            
            if z == 1:
                messagebox.showerror("Error", "Utilitas tidak boleh 1.")
            else:
                w = (((x**2)*y)+(z**2))/(2*(1-z)) 
                canvas.itemconfig(tagOrId=hasil, text=w)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid.")
        except tk.TclError: # type: ignore
            messagebox.showerror("Error", "Entry tidak boleh kosong.")

    bg = canvas.create_image(350.0,275.0,image=bg_5)

    hasil = canvas.create_text(380.0,428.0,anchor="nw",text="",fill="#000000",font=("RobotoRoman Regular", 13 * -1, 'bold'))

    lq_entry_1_image = canvas.create_image(212.5,329.5,image=lq_entry_image_1)
    lq_entry_1 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    lq_entry_1.place(x=97.0,y=312.0,width=231.0,height=29.0)

    lq_entry_2_image = canvas.create_image(488.5,329.5,image=lq_entry_image_2)
    lq_entry_2 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    lq_entry_2.place(x=373.0,y=312.0,width=231.0,height=29.0)

    lq_entry_3_image = canvas.create_image(212.5,397.5,image=lq_entry_image_3)
    lq_entry_3 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    lq_entry_3.place(x=97.0,y=380.0,width=231.0,height=29.0)

    lq_btn_hitung = Button(image=lq_hitung,borderwidth=0,highlightthickness=0,command=hitung,relief="flat")
    lq_btn_hitung.place(x=252.0,y=459.0,width=196.0,height=31.0)

    lq_btn_back = Button(image=lq_back,borderwidth=0,highlightthickness=0,command=kembali,relief="flat")
    lq_btn_back.place(x=13.0,y=9.0,width=31.0,height=31.0)

def buka_wq():

    def kembali():
        canvas.delete(bg,wq_entry_1_image,wq_entry_2_image,hasil)
        wq_btn_back.destroy()
        wq_btn_hitung.destroy()
        wq_entry_1.destroy()
        wq_entry_2.destroy()
        home()

    def hitung():
        try:
            x = float(wq_entry_1.get())
            y = float(wq_entry_2.get())
            
            if y == 0:
                messagebox.showerror("Error", "Kedatangan tidak boleh 0.")
            else:
                z = x / y
                canvas.itemconfig(tagOrId=hasil, text=z)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid.")
        except tk.TclError: # type: ignore
            messagebox.showerror("Error", "Entry tidak boleh kosong.")

    bg = canvas.create_image(350.0,275.0,image=bg_6)

    hasil = canvas.create_text(438.0,427.0,anchor="nw",text="",fill="#000000",font=("RobotoRoman Regular", 13 * -1, 'bold'))

    wq_entry_1_image = canvas.create_image(350.0,329.5,image=wq_entry_image_1)
    wq_entry_1 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    wq_entry_1.place(x=156.0,y=312.0,width=388.0,height=29.0)

    wq_entry_2_image = canvas.create_image(350.0,397.5,image=wq_entry_image_2)
    wq_entry_2 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    wq_entry_2.place(x=156.0,y=380.0,width=388.0,height=29.0)

    wq_btn_hitung = Button(image=wq_hitung,borderwidth=0,highlightthickness=0,command=hitung,relief="flat")
    wq_btn_hitung.place(x=252.0,y=459.0,width=196.0,height=31.0)

    wq_btn_back = Button(image=wq_back,borderwidth=0,highlightthickness=0,command=kembali,relief="flat")
    wq_btn_back.place(x=13.0,y=9.0,width=31.0,height=31.0)

def buka_info():

    def kembali():
        canvas.delete(bg)
        info_btn_back.destroy()
        home()

    bg = canvas.create_image(350.0,275.0,image=bg_7)

    info_btn_back = Button(image=info_back,borderwidth=0,highlightthickness=0,command=kembali,relief="flat")
    info_btn_back.place(x=13.0,y=9.0,width=31.0,height=31.0)

def home():
    def pindah_utilisasi():
        btn_utilisasi.destroy()
        btn_ws.destroy()
        btn_ls.destroy()
        btn_lq.destroy()
        btn_wq.destroy()
        btn_info.destroy()
        canvas.delete(bg)
        buka_utilitas()
    
    def pindah_ws():
        btn_utilisasi.destroy()
        btn_ws.destroy()
        btn_ls.destroy()
        btn_lq.destroy()
        btn_wq.destroy()
        btn_info.destroy()
        canvas.delete(bg)
        buka_ws()

    def pindah_ls():
        btn_utilisasi.destroy()
        btn_ws.destroy()
        btn_ls.destroy()
        btn_lq.destroy()
        btn_wq.destroy()
        btn_info.destroy()
        canvas.delete(bg)
        buka_ls()

    def pindah_lq():
        btn_utilisasi.destroy()
        btn_ws.destroy()
        btn_ls.destroy()
        btn_lq.destroy()
        btn_wq.destroy()
        btn_info.destroy()
        canvas.delete(bg)
        buka_lq()

    def pindah_wq():
        btn_utilisasi.destroy()
        btn_ws.destroy()
        btn_ls.destroy()
        btn_lq.destroy()
        btn_wq.destroy()
        btn_info.destroy()
        canvas.delete(bg)
        buka_wq()

    def pindah_info():
        btn_utilisasi.destroy()
        btn_ws.destroy()
        btn_ls.destroy()
        btn_lq.destroy()
        btn_wq.destroy()
        btn_info.destroy()
        canvas.delete(bg)
        buka_info()

    bg = canvas.create_image(350.0,275.0,image=bg_1)

    btn_utilisasi = Button(image=home_utilisasi,borderwidth=0,highlightthickness=0,command=pindah_utilisasi,relief="flat")
    btn_utilisasi.place(x=73.0,y=271.0,width=264.0,height=45.0)

    btn_ws = Button(image=home_ws,borderwidth=0,highlightthickness=0,command=pindah_ws,relief="flat")
    btn_ws.place(x=362.0,y=271.0,width=264.0,height=45.0)

    btn_ls = Button(image=home_ls,borderwidth=0,highlightthickness=0,command=pindah_ls,relief="flat")
    btn_ls.place(x=73.0,y=328.0,width=264.0,height=45.0)

    btn_lq = Button(image=home_lq,borderwidth=0,highlightthickness=0,command=pindah_lq,relief="flat")
    btn_lq.place(x=362.0,y=328.0,width=264.0,height=45.0)

    btn_wq = Button(image=home_wq,borderwidth=0,highlightthickness=0,command=pindah_wq,relief="flat")
    btn_wq.place(x=173.0,y=385.0,width=352.0,height=45.0)

    btn_info = Button(image=home_info,borderwidth=0,highlightthickness=0,command=pindah_info,relief="flat")
    btn_info.place(x=246.0,y=452.0,width=208.0,height=45.0)
        
home()
window.resizable(False, False)
window.mainloop()
