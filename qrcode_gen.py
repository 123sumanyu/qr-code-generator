from segno import helpers
import segno
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import shutil
import os

current_qr_path = None  # Will hold current QR image path


def form_qr(link):
    try:
        qrcode = segno.make(link, error='h', mask=3)
        qrcode.to_artistic(background='2.png', target='form_qr.png', scale=10, kind='png')
        return 'form_qr.png'
    except Exception as e:
        messagebox.showerror("Error", f"Form QR Generation Failed:\n{e}")
        return None


def wifi_qr(id, passw):
    try:
        qrcode = helpers.make_wifi(ssid=id, password=passw, security='WPA2')
        qrcode.save('wifi.png')
        return 'wifi.png'
    except Exception as e:
        messagebox.showerror("Error", f"WiFi QR Generation Failed:\n{e}")
        return None


def generate_qr():
    global current_qr_path
    option = cb.get()
    if option == 'form qr code':
        link = entry_url.get()
        if not link:
            messagebox.showwarning("Input Required", "Please enter the form URL")
            return
        path = form_qr(link)
    elif option == 'wifi qr code':
        ssid = entry_ssid.get()
        password = entry_pass.get()
        if not ssid or not password:
            messagebox.showwarning("Input Required", "Please enter both SSID and Password")
            return
        path = wifi_qr(ssid, password)
    else:
        messagebox.showwarning("Selection Required", "Please select an option")
        return

    if path:
        current_qr_path = path
        show_qr(path)


def show_qr(path):
    new_win = Toplevel(window)
    new_win.title("QR Preview")
    new_win.geometry("400x450")
    new_win.resizable(False, False)

    img = Image.open(path)
    img = img.resize((350, 350), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)

    img_label = Label(new_win, image=img_tk)
    img_label.image = img_tk
    img_label.pack(pady=10)

    def download_qr():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")],
            title="Save QR Code",
            initialfile="qr_code.png"
        )
        if file_path:
            shutil.copy(current_qr_path, file_path)
            messagebox.showinfo("Saved", f"QR Code saved to:\n{file_path}")

    Button(new_win, text="Download QR Code", command=download_qr,
           font=("Arial", 11), bg="green", fg="white").pack(pady=10)


def update_form():
    for widget in form_widgets:
        canvas.delete(widget)
    form_widgets.clear()

    def draw_text_with_bg(x, y, text):
        rect = canvas.create_rectangle(x - 80, y - 15, x + 80, y + 15, fill="white", outline="")
        label = canvas.create_text(x, y, text=text, fill="black", font=("Arial", 12, "bold"))
        return [rect, label]

    if cb.get() == 'wifi qr code':
        ssid_items = draw_text_with_bg(400, 180, "WiFi SSID:")
        entry_ssid_window = canvas.create_window(400, 210, window=entry_ssid, width=250)

        pass_items = draw_text_with_bg(400, 250, "WiFi Password:")
        entry_pass_window = canvas.create_window(400, 280, window=entry_pass, width=250)

        form_widgets.extend(ssid_items + pass_items + [entry_ssid_window, entry_pass_window])

    elif cb.get() == 'form qr code':
        url_items = draw_text_with_bg(400, 200, "Form URL:")
        entry_url_window = canvas.create_window(400, 230, window=entry_url, width=300)

        form_widgets.extend(url_items + [entry_url_window])


# GUI Setup
window = Tk()
window.title("🎯 QR Code Generator")
window.geometry("800x600")
window.resizable(False, False)

canvas = Canvas(window, width=800, height=600, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Background
bg_img = Image.open('back.png').resize((800, 600), Image.LANCZOS)
bg_tk = ImageTk.PhotoImage(bg_img)
canvas.create_image(0, 0, image=bg_tk, anchor='nw')

# Dropdown
cb = ttk.Combobox(window, values=['wifi qr code', 'form qr code'], state="readonly", font=('Arial', 11))
cb.set("Select QR Type")
cb.bind("<<ComboboxSelected>>", lambda e: update_form())
cb_window = canvas.create_window(400, 130, window=cb, width=200)

# Inputs
entry_ssid = Entry(window, font=('Arial', 12))
entry_pass = Entry(window, font=('Arial', 12), show="*")
entry_url = Entry(window, font=('Arial', 12))
form_widgets = []

# Generate button
submit_btn = Button(window, text="Generate QR", command=generate_qr,
                    font=('Arial', 12, 'bold'), bg='navy', fg='white', cursor='hand2')
canvas.create_window(400, 330, window=submit_btn, width=150)

window.mainloop()
