import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk

# Function to handle file upload
def upload_file():
    file_path = filedialog.askopenfilename(title="Select File")
    if file_path:
        entry_data.delete(0, tk.END)
        entry_data.insert(0, file_path)

# Function to generate QR code from file path or link
def generate_qr():
    input_data = entry_data.get()
    if not input_data:
        messagebox.showwarning("Input Error", "Please upload a file or enter a link")
        return
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input_data)  # Adds the file path or link to the QR code
    qr.make(fit=True)
    
    # Create an image of the QR code
    img = qr.make_image(fill="black", back_color="white")
    img.save("qr_code.png")

    # Display the QR code in the application
    img = Image.open("qr_code.png")
    img = img.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    qr_code_label.config(image=img)
    qr_code_label.image = img

# Function to save the generated QR code
def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        img = Image.open("qr_code.png")
        img.save(file_path)
        messagebox.showinfo("Success", f"QR Code saved at {file_path}")

# Main application window
app = tk.Tk()
app.title("Document/File/Image/Link to QR Code Converter")
app.geometry("400x500")
app.resizable(False, False)

# Input Section
label_data = tk.Label(app, text="Upload a file or enter a link:")
label_data.pack(pady=10)

entry_data = tk.Entry(app, width=40)
entry_data.pack(pady=5)

# Buttons for file upload and QR code generation
btn_upload = tk.Button(app, text="Upload File or Link", command=upload_file)
btn_upload.pack(pady=5)

btn_generate = tk.Button(app, text="Generate QR Code", command=generate_qr)
btn_generate.pack(pady=20)

# Display area for QR code
qr_code_label = tk.Label(app)
qr_code_label.pack(pady=10)

# Save QR code button
btn_save = tk.Button(app, text="Save QR Code", command=save_qr)
btn_save.pack(pady=20)

# Run the application
app.mainloop()
