import os
from datetime import date

from arabic_reshaper import arabic_reshaper
from bidi.algorithm import get_display
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, PageBreak, Image, Table
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
import reportlab
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import dic as nan

pdfmetrics.registerFont(TTFont('Arabic', 'res\efonts\majalla.ttf'))
style=getSampleStyleSheet()


arabic_text ="اعمال ود الخليفة لاستيراد المستلزمات الطبية"
# reshape the text
rehaped_text = arabic_reshaper.reshape(arabic_text)
bidi_text = get_display(rehaped_text)
yourStyle = ParagraphStyle('yourtitle',
                           fontName="Arabic",
                           fontSize=18,
                           parent=None,
                           alignment=2,
                           spaceAfter=14)





def paper(name,sub,text):
    try:
          c = canvas.Canvas(name+'.pdf', A4, bottomup=1)
          c.setFont('Arabic', 18)
          # c.drawString(100,50,bidi_text)
          # c.drawRightString(200,100,bidi_text)
          c.setFont("Arabic", 27, leading=None)
          c.setFillColorRGB(0.2, 0.2, 0.2)
          c.drawRightString(170 * mm, 235 * mm, f"{get_display(arabic_reshaper.reshape(name))}")
          c.drawImage('res\pdf\Asset 3.png', 60, 733, width=540, preserveAspectRatio=True, mask='auto')
          c.drawImage('res\pdf\Asset 9.png', 128, 640, width=350, preserveAspectRatio=True, mask='auto')
          c.drawImage('res\pdf\Asset 20.png', 20, 250, width=80, preserveAspectRatio=True, mask='auto')
          c.drawImage('res\pdf\Asset 20.png', 505, 250, width=80, preserveAspectRatio=True, mask='auto')
          c.drawImage('res\pdf\Asset 4.png', 85, 540, width=450, preserveAspectRatio=True, mask='auto')
          c.drawImage('res\pdf\Asset 7.png', 30, 50, width=540, preserveAspectRatio=True, mask='auto')
          c.drawImage('res\pdf\Asset 6.png', 30, -165, width=200, preserveAspectRatio=True, mask='auto')
          c.drawImage('res\pdf\Asset 8.png', 300, -38, width=1.7, preserveAspectRatio=True, mask='auto')
          c.drawImage('res\pdf\Asset 5.png', 110, -400, width=400, preserveAspectRatio=True, mask='auto')
          c.drawCentredString(110*mm,210*mm,f"{get_display(arabic_reshaper.reshape(sub))}")

          arabic_text=get_display(arabic_reshaper.reshape(text))
          lines = ''
          d = '   '

          po = 180

          for x in range(len(text)):

              d = d + text[x]


              if stringWidth(d, fontName="Arabic", fontSize=18) > (A4[0]-40*mm) and text[x]==' ':

                  lines = d + '<br></br>'
                  d = ''
                  if po==180:
                      py=3
                  else:
                      py=10
                  pp=Paragraph(get_display(arabic_reshaper.reshape(lines)),yourStyle)
                  pp.wrapOn(c,180*mm,210*mm)
                  pp.drawOn(c,py*mm,po*mm,0)
                  po=po-8
          if len(d)>0:
                  lines = d + '<br></br>'
                  pp = Paragraph(get_display(arabic_reshaper.reshape(lines)), yourStyle)
                  pp.wrapOn(c,180*mm,210*mm)
                  pp.drawOn(c, 10 * mm, po * mm, 0)



          #par = Paragraph(arabic_text, yourStyle)
          #par.wrapOn(c,190*mm,210*mm)
          #par.drawOn(c,10*mm,180*mm,0)





          c.save()
          os.startfile(name+'.pdf')
    except Exception as e:
        pass


def text_resh(c,text):
    lines=''
    d = ''
    for x in range(len(text)):

        d = d + text[x]

        if stringWidth(d, fontName="Arabic", fontSize=16) >= (A4[0] - 40* mm):
            lines=lines+d+'<br></br>'
            d=''
            par=Paragraph(lines,yourStyle)
            par.wrapOn(c, 190 * mm, 210 * mm)
            par.drawOn(c, 10 * mm, 150 * mm, 0)

    if len(d)>0:
        lines=lines+d







def generate(text):
    p1 = Paragraph(f'''
              <para align=center spaceb=3><b>{get_display(arabic_reshaper.reshape(text))}</b></para>''', yourStyle)
    return p1
def bill(name,place,Date,total,payments,Gained,*args):
    try:
         c = canvas.Canvas(str(name)+'.pdf', A4, bottomup=1)
         c.setFont('Arabic', 18)

         c.drawImage('res\pdf\Asset 3.png', 60, 733, width=540, preserveAspectRatio=True, mask='auto')
         c.drawImage('res\pdf\Asset 9.png', 128, 640, width=350, preserveAspectRatio=True, mask='auto')
         c.drawImage('res\pdf\Asset 20.png', 20, 250, width=80, preserveAspectRatio=True, mask='auto')
         c.drawImage('res\pdf\Asset 20.png', 505, 250, width=80, preserveAspectRatio=True, mask='auto')
         c.drawImage('res\pdf\Asset 7.png', 30, 50, width=540, preserveAspectRatio=True, mask='auto')
         c.drawImage('res\pdf\Asset 6.png', 30, -165, width=200, preserveAspectRatio=True, mask='auto')
         c.drawImage('res\pdf\Asset 8.png', 300, -38, width=1.7, preserveAspectRatio=True, mask='auto')
         c.drawImage('res\pdf\Asset 5.png', 110, -400, width=400, preserveAspectRatio=True, mask='auto')
         p0=[[generate("الكلي"),generate("الكمية"),generate("السعر"),generate("المنتج")]]
         p1=[]

         for x in args[0]:

             for y in x:
                  v=get_display(arabic_reshaper.reshape(str(y)))
                  p1.append(Paragraph(f'''<para align=center spaceb=3><b>{v}</b></para>''',
                        yourStyle))

             p0.append(p1)
             p1=[]





         data = p0
         #print(data)
         t = Table(data, style=[
                                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                ('BOX', (0, 0), (-1, -1), 2, colors.black),
                                ('LINEABOVE', (0, 1), (len(p0), 1), 2, colors.red),
                                ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                ])



         for i in range(len(p0)):
             t._argH[i] = .7 * inch


         t._argW[0] = .9 * inch
         t.wrapOn(c, 176.7 * mm, 200 * mm)
         t.drawOn(c, 18 * mm, 110.6 * mm)

         c.setFont("Arabic",27,leading=None)
         c.setFillColorRGB(.1, .4, .2,alpha=1)
         c.rect(0*mm,240*mm,210*mm,10*mm,stroke=0,fill=1)
         c.setFillColorRGB(1, 1, 1, alpha=1)
         c.drawCentredString(105 * mm, 243 * mm, get_display(arabic_reshaper.reshape("فاتورة نهائية")))
         c.setFont("Arabic", 23, leading=None)
         c.setFillColorRGB(.3, .3, .3)
         c.drawRightString(180*mm,8*mm,f"{get_display(arabic_reshaper.reshape('التاريخ: '))} " )
         c.drawRightString(160 * mm, 8 * mm, f"{date.today()} ")
         c.setFont("Arabic", 27, leading=None)
         c.setFillColorRGB(0, 0,0)
         c.drawRightString(200 * mm, 210 * mm, f"{get_display(arabic_reshaper.reshape(name))}")
         c.drawRightString(200 * mm, 200 * mm, f"{get_display(arabic_reshaper.reshape(place))} ")
         c.setFont("Arabic", 18, leading=None)
         c.drawRightString(190 * mm, 90 * mm, f"{get_display(arabic_reshaper.reshape('القيمة الكلية:'))} ")
         c.drawRightString(100*mm,90*mm,get_display(arabic_reshaper.reshape("جدول المدفوعات:")))
         c.drawRightString(160 * mm, 90 * mm, f"{total} ")
         c.drawRightString(190 * mm, 80 * mm, f"{get_display(arabic_reshaper.reshape('تاريخ الشراء:'))} ")
         c.drawRightString(160 * mm, 80 * mm, f"{Date} ")
         for x in range(len(payments)):
              c.drawRightString(80 * mm, 80 * mm-x*10*mm, f"{payments[x]}")
         if(Gained==1):
             print('painted')
             c.drawImage("res\pdf\PAID.png",30*mm,-15*mm, width=200, preserveAspectRatio=True, mask='auto')

         c.save()
         os.startfile(str(name)+'.pdf')
    except Exception as e:
        pass


def inv_info(*args):
    try:
         c = canvas.Canvas("inv_info_"+str(date.today())+'.pdf', A4, bottomup=1)
         c.setFont('Arabic', 18)

         c.drawImage('res\pdf\Asset 3.png', 60, 733, width=540, preserveAspectRatio=True, mask='auto')
         c.drawImage('res\pdf\Asset 9.png', 128, 640, width=350, preserveAspectRatio=True, mask='auto')
         c.drawImage('res\pdf\Asset 20.png', 20, 250, width=80, preserveAspectRatio=True, mask='auto')
         c.drawImage('res\pdf\Asset 20.png', 505, 250, width=80, preserveAspectRatio=True, mask='auto')
         c.drawImage('res\pdf\Asset 7.png', 30, 50, width=540, preserveAspectRatio=True, mask='auto')
         c.drawImage('res\pdf\Asset 6.png', 30, -165, width=200, preserveAspectRatio=True, mask='auto')
         c.drawImage('res\pdf\Asset 8.png', 300, -38, width=1.7, preserveAspectRatio=True, mask='auto')
         c.drawImage('res\pdf\Asset 5.png', 110, -400, width=400, preserveAspectRatio=True, mask='auto')
         p0=[[generate("المخزن"),generate("البلد"),generate("المزود"),generate("الصلاحية"),generate("تاريخ الوصول"),generate("الكمية"),generate("السعر"),generate("الاسم"),generate("المتسلسل"),generate("No.")]]
         p1=[]

         for x in args:

             for y in x:


                 for u in range(len(y)):
                    if(len(y)-u-1)==9:
                        pass
                    else:
                         v=get_display(arabic_reshaper.reshape((nan.custom_decode(str(y[len(y)-u-1])))))
                         p1.append(Paragraph(f'''<para align=center spaceb=3><b>{v}</b></para>''',
                               yourStyle))

                 p0.append(p1)
                 p1=[]





         data = p0
         #print(data)
         t = Table(data, style=[
                                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                ('BOX', (0, 0), (-1, -1), 2, colors.black),
                                ('LINEABOVE', (0, 1), (-1, 1), 2, colors.red),
                                ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                ])



         for i in range(len(p0)):
             t._argH[i] = .7 * inch


         t._argW[0] = .9 * inch
         t.wrapOn(c, 176.7 * mm, 200 * mm)
         t.drawOn(c, 5 * mm, 110.6 * mm)

         c.setFont("Arabic",27,leading=None)
         c.setFillColorRGB(.1, .4, .2,alpha=1)
         c.rect(0*mm,240*mm,210*mm,10*mm,stroke=0,fill=1)
         c.setFillColorRGB(1, 1, 1, alpha=1)
         c.drawCentredString(105 * mm, 243 * mm, get_display(arabic_reshaper.reshape("معلومات المخزن")))
         c.setFont("Arabic", 23, leading=None)
         c.setFillColorRGB(.3, .3, .3)
         c.drawRightString(180*mm,8*mm,f"{get_display(arabic_reshaper.reshape('التاريخ: '))} " )
         c.drawRightString(160 * mm, 8 * mm, f"{date.today()} ")
         c.setFont("Arabic", 27, leading=None)
         c.setFillColorRGB(0, 0,0)

         c.setFont("Arabic", 18, leading=None)





         c.save()
         os.startfile("inv_info_"+str(date.today())+'.pdf')
    except Exception as e:
        print(e)