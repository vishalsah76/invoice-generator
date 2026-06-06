from flask import Flask, render_template, request, send_file
from docxtpl import DocxTemplate
from num2words import num2words
import os
import uuid
import json

app = Flask(__name__)

# ==========================================
# CONFIG
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_PATH = os.path.join(BASE_DIR, "template.docx")

OUTPUT_DIR = os.path.join(BASE_DIR, "output")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_json(filename):
    with open(
        os.path.join(BASE_DIR, "data", filename),
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)
# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
@app.route("/")
def home():

    company = load_json("company.json")
    buyers = load_json("buyers.json")
    items = load_json("items.json")

    return render_template(
        "form.html",
        company=company,
        buyers=buyers,
        items=items
    )

# ==========================================
# GENERATE INVOICE
# ==========================================

@app.route("/generate", methods=["POST"])
def generate_invoice():

    # ==========================================
    # UNIQUE FILE NAME
    # ==========================================

    file_id = str(uuid.uuid4())

    docx_output = os.path.join(
        OUTPUT_DIR,
        f"{file_id}.docx"
    )

    # ==========================================
    # BASIC DETAILS
    # ==========================================

    data = {

        "buyer_businessname": request.form.get(
            "buyer_businessname", ""
        ),

        "buyer_name": request.form.get(
            "buyer_name", ""
        ),

        "buyer_address1": request.form.get(
            "buyer_address1", ""
        ),

        "buyer_address2": request.form.get(
            "buyer_address2", ""
        ),

        "buyer_gst": request.form.get(
            "buyer_gst", ""
        ),

        "buyer_state": request.form.get(
            "buyer_state", ""
        ),

        "buyer_pincode": request.form.get(
            "buyer_pincode", ""
        ),

        "invoice_no": request.form.get(
            "invoice_no", ""
        ),

        "date": request.form.get(
            "date", ""
        )
    }

    # ==========================================
    # ITEM DATA
    # ==========================================

    sls = request.form.getlist("sl")

    descriptions = request.form.getlist("description")

    hsns = request.form.getlist("hsn")

    qtys = request.form.getlist("qty")

    rates = request.form.getlist("rate")

    pers = request.form.getlist("per")

    items = []

    total_amount = 0
    total_qty = 0

    for i in range(len(descriptions)):

        qty = float(qtys[i])

        rate = float(rates[i])

        amount = qty * rate

        total_amount += amount

        total_qty += qty

        items.append({

            "sl_no": sls[i],

            "description": descriptions[i],

            "hsn": hsns[i],

            "qty": f"{qty:,.2f}",

            "rate": f"{rate:,.2f}",

            "per": pers[i],

            "amount": f"{amount:,.2f}"
        })

    # ==========================================
    # TAX CALCULATION
    # ==========================================

    cgst = total_amount * 0.20

    sgst = total_amount * 0.20

    tax_amount = cgst + sgst

    grand_total = total_amount + tax_amount

    # ==========================================
    # AMOUNT IN WORDS
    # ==========================================

    total_in_words = num2words(
        int(round(grand_total)),
        lang='en_IN'
    ).title()

    total_in_words = (
        f"INR {total_in_words} Only"
    )

    tax_amount_words = num2words(
        int(round(tax_amount)),
        lang='en_IN'
    ).title()

    tax_amount_words = (
        f"INR {tax_amount_words} Only"
    )

    # ==========================================
    # FINAL TEMPLATE DATA
    # ==========================================

    data["items"] = items

    data["total_qty"] = (
        f"{total_qty:,.2f}"
    )
    
    data["total_amount"] = (
        f"{total_amount:,.2f}"
    )

    data["cgst"] = (
        f"{cgst:,.2f}"
    )

    data["sgst"] = (
        f"{sgst:,.2f}"
    )

    data["tax_amount"] = (
        f"{tax_amount:,.2f}"
    )

    data["grand_total"] = (
        f"{grand_total:,.2f}"
    )

    data["total_in_words"] = (
        total_in_words
    )

    data["tax_amount_words"] = (
        tax_amount_words
    )

    # ==========================================
    # GENERATE DOCX
    # ==========================================

    doc = DocxTemplate(TEMPLATE_PATH)

    doc.render(data)

    doc.save(docx_output)

    # ==========================================
    # CONVERT DOCX TO PDF
    # ==========================================

    # ==========================================
    # RETURN PDF
    # ==========================================

    return send_file(
        docx_output,
        as_attachment=True,
        download_name=f"Invoice-{file_id}.docx"
    )

# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)