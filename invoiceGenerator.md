# Invoice Generator - Setup & Installation Guide

## Overview

This project is a Flask-based Invoice Generator system that:

* Accepts invoice details from UI
* Generates DOCX invoice using placeholders
* Converts DOCX to PDF
* Downloads final PDF invoice
* Supports dynamic item rows
* Supports prefilled buyers/items
* Calculates GST automatically
* Converts amount into words

---

# Project Structure

```text
invoiceGenerator/
│
├── invoice.py
├── template.docx
├── requirements.txt
├── output/
│
├── templates/
│   └── form.html
│
└── static/
```

---

# Software Required

## 1. Python

Install Python 3.10 or above.

Recommended:

* Python 3.11
* Python 3.12
* Python 3.13

Download:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

IMPORTANT:
During installation:

✔ Check:

```text
Add Python to PATH
```

---

# 2. LibreOffice

LibreOffice is required for converting DOCX → PDF.

Download:

[https://www.libreoffice.org/download/download-libreoffice/](https://www.libreoffice.org/download/download-libreoffice/)

Install with default settings.

Default Windows path:

```text
C:\Program Files\LibreOffice\program\soffice.exe
```

---

# Python Packages Required

Open CMD inside project folder and run:

```bash
pip install flask
pip install docxtpl
pip install num2words
```

OR use requirements.txt

---

# requirements.txt

Create a file named:

```text
requirements.txt
```

Add:

```text
flask
python-docx
DocxTemplate
num2words
```

Install all:

```bash
pip install -r requirements.txt
```

# Running The Project

Open CMD inside project folder:

```bash
python invoice.py
```

Server starts:

```text
http://127.0.0.1:5000
```

Open in browser.

---

# Features Included

## Buyer Master

* Pre-filled buyer dropdown
* Auto fill GST/details

## Item Master

* Predefined item selection
* Auto fill HSN/rate/per

## Automatic Calculation

* Amount = Qty × Rate
* CGST = 20%
* SGST = 20%
* Grand Total calculation
* Amount in words

## PDF Generation

* DOCX generated dynamically
* LibreOffice converts DOCX → PDF

---

# Common Errors & Fixes

---

## Error: soffice.exe not found

Fix:

Update path in invoice.py:

```python
LIBRE_OFFICE_PATH = r"C:\Program Files\LibreOffice\program\soffice.exe"
```

---

## Error: Placeholder not replaced

Fix:

* Re-type placeholders manually in Word
* Avoid copy-paste from WhatsApp
* Keep placeholders plain text

Correct:

```text
{{buyer_name}}
```

Wrong:

```text
{{ buyer_name }}
```

---

## Error: Items appear in single row

Fix:

* Use proper table row loop
* Keep placeholders in separate cells
* Do not merge item row cells

---

## Error: KeyError in Flask

Fix:

Use:

```python
request.form.get("field", "")
```

instead of:

```python
request.form["field"]
```

---

# Recommended Improvements

Future upgrades possible:

* Database support
* Invoice history
* Login system
* Company logo upload
* Multi-user support
* Auto invoice numbering
* Excel export
* Email invoice
* Multi-page invoices
* GST percentage selection
* Docker deployment

---

# Deployment Options

Possible deployment methods:

* Windows Server
* Linux Server
* Docker
* AWS EC2
* Azure VM
* Render
* Railway
* Local office system

---

# Recommended Production Stack

Frontend:

* HTML
* CSS
* JavaScript

Backend:

* Flask

Template Engine:

* docxtpl

PDF Conversion:

* LibreOffice

Database (future):

* SQLite
* MySQL
* PostgreSQL

---

# Final Notes

This project is suitable for:

* Distributor invoices
* Tally-like billing
* GST invoice generation
* Retail billing
* Office invoice automation

The system currently works fully offline and generates professional PDF invoices dynamically.
