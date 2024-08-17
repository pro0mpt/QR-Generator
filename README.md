# QR Code Converter & Document Format Converter

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
   - [QR Code Converter](#qr-code-converter)
   - [Document Format Converter](#document-format-converter)
3. [Requirements](#requirements)
4. [Installation and Setup](#installation-and-setup)
5. [How to Use](#how-to-use)
6. [How to Run in VS Code](#how-to-run-in-vs-code)

## Overview
This repository contains two standalone Python-based software applications:
1. **QR Code Converter**: Converts documents, files, images, and links into QR codes.
2. **Document Format Converter**: Converts any document format (e.g., PDF, DOCX, XLSX) into another format.

Both projects have been built with a simple and clean UI using `Tkinter` and core Python libraries for functionality.

## Features

### QR Code Converter
- Convert **any file**, **image**, or **document** into a QR code.
- Input a **link** and generate a QR code from it.
- Display the generated QR code in the app.
- Save the generated QR code as a PNG image.

### Document Format Converter
- Convert documents between multiple formats (PDF, DOCX, XLSX, etc.).
- Easy-to-use interface to upload, convert, and download the converted file.
- Smooth and fast document conversion using a simple UI.

## Requirements
To run both the QR Code Converter and the Document Format Converter, you'll need the following Python libraries:
- `qrcode`
- `Pillow`
- `tkinter` (for UI)
- `pypandoc` (for document format conversion)

Install the dependencies via `pip`:
```bash
pip install qrcode[pil] Pillow pypandoc
```

## Installation and Setup

1. **Clone the Repository**:
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-repo-url.git
   ```
   
2. **Navigate to the Project Directory**:
   ```bash
   cd your-repo-directory
   ```

3. **Install the Dependencies**:
   Install the required Python packages listed above by running the following command:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure Python is Installed**:
   Make sure you have Python 3.x installed. You can verify by running:
   ```bash
   python --version
   ```

## How to Use

### QR Code Converter

1. **Launch the Application**:
   Run the QR Code Converter application by executing the Python file:
   ```bash
   python qr_code_converter.py
   ```

2. **Usage**:
   - **Upload a File**: Click the "Upload File" button to select a file (document, image, or other).
   - **Enter a Link**: Type any URL or text into the input field.
   - **Generate QR Code**: Click "Generate QR Code" to create a QR code from the file or link.
   - **Save the QR Code**: Click "Save QR Code" to download the generated QR code as a PNG file.

