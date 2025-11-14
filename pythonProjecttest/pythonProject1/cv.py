from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

# ✅ Output PDF
pdf_path = "Kunal_Singh_Bisht_CV_Final.pdf"

# Create canvas
c = canvas.Canvas(pdf_path, pagesize=A4)
width, height = A4

# 🎨 Colors
red = colors.Color(0.6, 0, 0)   # Dark red
white = colors.white
black = colors.black

# 🟥 Draw Right Red Sidebar (slightly narrower)
sidebar_width = 6 * cm
c.setFillColor(red)
c.rect(width - sidebar_width, 0, sidebar_width, height, fill=1, stroke=0)

# ✅ Adjust content margin to avoid overlap
margin_left = 2 * cm
content_width = width - sidebar_width - 3 * cm

# 📝 Title
c.setFillColor(red)
c.setFont("Helvetica-Bold", 24)
c.drawString(margin_left, height - 2*cm, "KUNAL SINGH BISHT")

# 📄 Professional Summary
c.setFillColor(black)
c.setFont("Helvetica-Bold", 12)
c.drawString(margin_left, height - 3.5*cm, "PROFESSIONAL SUMMARY")

summary = """Dedicated administrative professional with comprehensive knowledge of medical standards,
compliance regulations, and operational workflows. Adept at problem-solving with a client-focused
approach and strong communication skills. Experienced in inventory management, customer service,
and office operations within healthcare and fitness environments."""
text = c.beginText(margin_left, height - 4.5*cm)
text.setFont("Helvetica", 9)
text.setLeading(12)
for line in summary.split("\n"):
    text.textLine(line)
c.drawText(text)

# 🎓 Certifications
y = height - 9*cm
c.setFont("Helvetica-Bold", 12)
c.drawString(margin_left, y, "CERTIFICATIONS & COURSES")
c.setFont("Helvetica", 10)
c.drawString(margin_left, y - 0.5*cm, "Ultimate Gym Solutions — Certified Personal Trainer")

# 💼 Professional Experience
y -= 2*cm
c.setFont("Helvetica-Bold", 12)
c.drawString(margin_left, y, "PROFESSIONAL EXPERIENCE")

exp1 = """Retail Assistant, 11/2023 - 12/2024
Satyam Medical Store, Mohali
• Managed daily store operations ensuring smooth functioning and customer satisfaction.
• Specialized in dispensing prescription and OTC medications, devices, and supplements.
• Implemented cross-selling opportunities to enhance product uptake."""
text = c.beginText(margin_left, y - 1*cm)
text.setFont("Helvetica", 9)
text.setLeading(12)
for line in exp1.split("\n"):
    text.textLine(line)
c.drawText(text)

exp2 = """Personal Trainer, 01/2023 - 10/2023
Coin Fitness Shivalik & Neo Fitness Gym, Kharar
• Designed and delivered personalized fitness programs based on client assessments.
• Conducted evaluations, tracked progress, and adjusted programs to optimize outcomes.
• Built strong client relationships through clear communication, motivation, and guidance."""
text = c.beginText(margin_left, y - 5*cm)
text.setFont("Helvetica", 9)
text.setLeading(12)
for line in exp2.split("\n"):
    text.textLine(line)
c.drawText(text)

# 🎓 Education Section
y -= 9*cm
c.setFont("Helvetica-Bold", 12)
c.drawString(margin_left, y, "EDUCATION")
edu = """Diploma, Pharmacy — Doaba Group of Colleges
Higher Secondary, 10+2 — Punjab School Education Board (P.S.E.B.)"""
text = c.beginText(margin_left, y - 1*cm)
text.setFont("Helvetica", 9)
text.setLeading(12)
for line in edu.split("\n"):
    text.textLine(line)
c.drawText(text)

# 🎯 Hobbies
c.setFont("Helvetica-Bold", 12)
c.drawString(margin_left, 5*cm, "HOBBIES AND INTERESTS")
c.setFont("Helvetica", 9)
c.drawString(margin_left, 4.5*cm, "Travelling, Reading Books")

# 🟩 Sidebar Content (Contact Info & Core Competencies)
c.setFillColor(white)
c.setFont("Helvetica", 9)
x_sidebar = width - sidebar_width + 0.5*cm
c.drawString(x_sidebar, height - 3*cm, "Kharar")
c.drawString(x_sidebar, height - 4*cm, "+91 79733 41998")
c.drawString(x_sidebar, height - 5*cm, "kunalbisht01@gmail.com")

# ⭐ Core Competencies Title
c.setFont("Helvetica-Bold", 12)
c.drawString(x_sidebar, height - 7*cm, "CORE COMPETENCIES")

# Draw Competency Bars (Evenly Spaced)
competencies = [
    ("Medical Product Sales & Inventory Management", 90),
    ("Client Relationship & Communication Skills", 85),
    ("Fitness Program Design & Personalized Training", 80),
    ("Exercise Physiology & Nutrition Guidance", 75),
    ("Cross-selling & Upselling Techniques", 70),
    ("Business Intelligence & Computer Literacy", 65)
]

y_bar = height - 8*cm
for name, percent in competencies:
    c.setFont("Helvetica", 7)
    c.drawString(x_sidebar, y_bar, name)
    # Bar background
    c.rect(x_sidebar, y_bar - 0.3*cm, 5*cm, 0.2*cm, fill=0, stroke=1)
    # Filled bar
    c.setFillColor(white)
    c.rect(x_sidebar, y_bar - 0.3*cm, (5*cm * percent) / 100, 0.2*cm, fill=1, stroke=0)
    y_bar -= 1*cm

# ✅ Save PDF
c.save()
print(f"✅ CV generated successfully → {pdf_path}")
