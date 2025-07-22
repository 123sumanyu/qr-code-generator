#🎯 QR Code Generator GUI (WiFi & Form Link)

This is a beautifully designed desktop GUI application built with Python and Tkinter that allows users to generate custom QR codes for:

- 🌐 WiFi login (SSID + Password)
- 🔗 Form or website links

It supports custom artistic backgrounds, previews the QR in a popup window, and allows easy downloading with location selection.

---

🖼️ Demo

[Image Placeholder: Insert your image link here or replace this with a local preview]

---

✅ Features

- 📶 Generate WiFi QR codes (WPA2 encryption)
- 📋 Generate Form or URL QR codes with artistic backgrounds
- 🖼️ Artistic QR style using `segno` and background image
- 🪟 QR preview opens in a new popup window
- 💾 Save QR code to a custom file location
- 🎨 Beautiful user interface with a themed background (back.png)
- 🔐 Secure password entry for WiFi
- 🧼 Input validation and error handling

---

🔧 Setup Instructions

1. 📁 Prerequisites

Ensure you have Python 3.7+ installed.

Install the required libraries using pip:

pip install segno pillow qrcode-artistic

---

2. 📂 Files Needed

Make sure your project folder contains the following:

- main.py → Main application script
- back.png → Background image for the app window
- 2.png → Background used for form QR artistic style

---

3. ▶️ Run the App

python main.py

---

🖱️ How to Use

1. Launch the app.
2. Select "wifi qr code" or "form qr code" from the dropdown.
3. Fill in the appropriate fields (WiFi credentials or Form URL).
4. Click "Generate QR".
5. The QR preview will open in a new popup window with a "Download QR Code" button.

---

📦 Tech Stack

Component         | Description
------------------|-----------------------------------------
Tkinter           | GUI framework
Pillow            | Image loading & resizing
segno             | QR code generation
qrcode-artistic   | Artistic QR styling
shutil            | Copy QR to selected download path
filedialog        | Prompt user for save location

---

🧠 Behind the Scenes

- segno.make() is used to generate a basic QR code.
- For form QR codes, to_artistic() applies a background (2.png) behind the QR.
- A popup Toplevel() window is used to show the QR preview.
- filedialog.asksaveasfilename() allows the user to choose the save location.
- shutil.copy() copies the QR code to the selected path.

---

👤 Author

Sumanyu Singh

---

🪪 License

This project is open-source and licensed under the MIT License.
