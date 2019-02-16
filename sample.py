import sqlite3
from fpdf import FPDF
print("content-type=text/html \r\n\r\n")
con=sqlite3.connect("student.db")
cur=con.cursor()
sql="select * from certifData"
cur.execute(sql)

pdf = FPDF()
for row in cur.fetchall():
    #print(row[0],row[1],row[2])
    pdf.add_page("a4")
    pdf.image('certificate.jpg', 10, 8, 280)
    pdf.set_font('Arial', 'B', 16)
    pdf.ln(70)
    pdf.cell(90, 10, '',0,0,"C")
    pdf.cell(100, 10, row[0],0,0,"C")
    pdf.ln(40)
    pdf.cell(90, 10, '',0,0,"C")
    pdf.cell(100, 10, row[1],0,0,"C")
    pdf.ln(20)
    pdf.cell(60, 10, '',0,0,"C")
    pdf.cell(40, 10, row[2],0,0,"C")
    pdf.image('mysign.png', 193, 135, 40)

pdf.output('a.pdf', 'F')

