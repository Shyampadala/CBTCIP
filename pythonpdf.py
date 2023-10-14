from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

w,h = A4
c = canvas.Canvas('Tranction bill.pdf',pagesize=A4)
text1 = c.beginText(50,h-50)
text1.setFont("Times-Roman",16)
text1.textLines("hello shyam\n here is your transaction bill")
c.drawText(text1)
x = 50
y = h-100
c.line(x,y,x+500,y)
text2 = c.beginText(50,h-150)
text2.setFont("Helvetica", 12)
text2.textLines("Reference number                                                    IHM264XXX\n Amount                                                                     2500\n Status                                                                       Paid\n Debit A/c                                                                  53427689xxxx\n Date                                                                         28-9-2023\n Debit A/c                                                                  56746289xxxx")
c.drawText(text2)
c.save()
