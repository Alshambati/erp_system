import os
import threading
import time
import traceback


from PyQt5 import QtWidgets, uic
import sys

from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QSequentialAnimationGroup, QDate, QDateTime, QRect
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QDoubleValidator, QIcon, QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QMessageBox, QFileDialog

#first window class
from PyQt5.uic.properties import QtCore, QtGui

import PDF
from DataBase import DataBase
import dic as nan
from datetime import date, timedelta, datetime

stop_threads = False

class myy(QtWidgets.QMainWindow):



    #init first window
    def __init__(self):
        super(myy, self).__init__()
        uic.loadUi('app.ui', self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.show()
        self.controller()



    #first window controller
    def controller(self):
        self.setWindowIcon(QIcon("res\icon.png"))
        ptn = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.ln = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.ln2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        self.CB = self.findChild(QtWidgets.QCheckBox, 'checkBox')
        self.online = self.findChild(QtWidgets.QFrame, 'frame_4')
        self.exi=self.findChild(QtWidgets.QPushButton,'exit_b')
        self.min=self.findChild(QtWidgets.QPushButton,'Minimize_b')
        self.exi.clicked.connect(lambda :self.close())
        self.min.clicked.connect(lambda :self.showMinimized())
        self.CB.stateChanged.connect(self.show_pas)
        ptn.clicked.connect(self.log_in)
        self.ln2.textChanged.connect(self.reattemp)



    def reattemp(self):
        self.ln2.setStyleSheet("QLineEdit{border-color:rgb(189, 189, 189);border-style: solid;border-width: 1.5px;border-radius: 15px;padding-left: 10px;padding-right: 10px;padding-top: 4px;transition:border-color 2s;font-size: 16px;background: rgba(0,0,0,0.0);color: rgb(239, 239, 239);}QLineEdit:hover{border-color:rgb(103, 103, 103);}")




    #first window log_in functionality
    def log_in(self):
        global cloum_number, row_number
        try:
            self.user_name = self.ln.text()
            self.user_pass = self.ln2.text()
          #  self.mydb = MySQLdb.connect(host='localhost', user=self.user_name, passwd=self.user_pass, db='clients')
           # self.cur = self.mydb.cursor()
            #self.command = self.cur.execute('select * from client')

            self.Da=DataBase()
            self.Da.init(self.user_name,self.user_pass)
            self.cur=self.Da.query('select * from trans')



            self.we = AnotherWindow()


            #TERMINATE FIRST SCREEN
            self.hide()


        except Exception as e:

            self.ln2.setStyleSheet(" QLineEdit{ border-color:rgb(255, 0, 0);  border-style: solid; border-width: 1.5px; border-radius: 15px; padding-left: 10px; padding-right: 10px; padding-top: 4px; transition:border-color 2s; font-size: 16px; background: rgba(0,0,0,0.0); color: rgb(255,0,0); } QLineEdit:hover{ border-color:rgb(200,0,0);}")
            self.wiggle()






           #animation
    def wiggle(self):
            p=self.pos().x()
            yp=self.pos().y()

            self.anim = QPropertyAnimation(self, b"pos")
            self.anim.setEndValue(QPoint(p-30,yp))
            self.anim.setDuration(50)


            self.anim2 = QPropertyAnimation(self, b"pos")
            self.anim.setStartValue(QPoint(p - 30, yp))
            self.anim2.setEndValue(QPoint(p +30, yp))
            self.anim2.setDuration(50)


            self.anim3 = QPropertyAnimation(self, b"pos")
            self.anim.setStartValue(QPoint(p + 30, yp))
            self.anim3.setEndValue(QPoint(p - 25, yp))
            self.anim3.setDuration(50)


            self.anim4 = QPropertyAnimation(self, b"pos")
            self.anim.setStartValue(QPoint(p - 25, yp))
            self.anim4.setEndValue(QPoint(p + 25, yp))
            self.anim4.setDuration(50)


            self.ani = QPropertyAnimation(self, b"pos")
            self.ani.setEndValue(QPoint(p, yp))
            self.ani.setDuration(50)


            self.anim_group = QSequentialAnimationGroup()
            self.anim_group.addAnimation(self.anim)
            self.anim_group.addAnimation(self.anim2)
            self.anim_group.addAnimation(self.anim3)
            self.anim_group.addAnimation(self.anim4)
            self.anim_group.addAnimation(self.ani)
            self.anim_group.start()






    #show password function
    def show_pas(self):
        if self.CB.checkState() !=0:
            self.ln2.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ln2.setEchoMode(QtWidgets.QLineEdit.Password)




class reciept_config(QtWidgets.QMainWindow):
        def __init__(self):
            super(reciept_config, self).__init__()
            uic.loadUi('reciept_conf.ui', self)
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.show()
            self.controller()

        def controller(self):
            self.ok=self.findChild(QtWidgets.QPushButton,'OK')
            self.ok.clicked.connect(self.confirm)


        def confirm(self):
            self.close()
            window.we.pages.setCurrentIndex(2)



class deleter(QtWidgets.QMainWindow):

        def __init__(self):
            super(deleter, self).__init__()
            uic.loadUi('delete.ui', self)
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.show()
            self.controller()

        def controller(self):
            #self.setWindowIcon(QIcon("icons\warning.png"))

            self.delp = self.findChild(QtWidgets.QPushButton, 'DELETE')
            self.canc = self.findChild(QtWidgets.QPushButton, 'cancel')
            self.l1=self.findChild(QtWidgets.QLabel,'label_2')
            self.l2=self.findChild(QtWidgets.QLabel,'label_3')
            self.delpass=self.findChild(QtWidgets.QLineEdit,'delpass')
            self.delpass.setEchoMode(QtWidgets.QLineEdit.Password)
            self.l1.setText(window.we.table2.selectedItems()[1].text())
            self.l2.setText(window.we.table2.selectedItems()[9].text())



            self.delp.clicked.connect(self.delll)
            self.canc.clicked.connect(self.close)


        def delll(self):
           if self.delpass.text() == window.user_pass:
             try:
               tem = window.we.table2.selectedItems()[0].text()
               window.Da.query(f"DELETE FROM trans WHERE id= {tem};")
               window.Da.query(window.we.invbacksql)
             except:
                 pass

             window.we.SV(2)
             self.close()
           else:
               self.delpass.setStyleSheet("QLineEdit{ border-style:solid; border-width:2; border-radius:15px; border-color: rgb(255, 0, 4); padding-right:10px;}")


class adder(deleter):

    def __init__(self,u,v,x,e):
        super(deleter, self).__init__()
        uic.loadUi('adder.ui', self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.show()
        print(u,v,x,e)
        self.controller(u,v,x,e)
        print(u,v,x,e)

    def controller(self,u,v,x,e):
        self.delp = self.findChild(QtWidgets.QPushButton, 'ADD')

        self.canc = self.findChild(QtWidgets.QPushButton, 'cancel')
        self.canc.setText("إلغاء")
        self.inf=self.findChild(QtWidgets.QLabel,'label')
        if e==1 or e==3:
            self.inf.setText("تأكيد تعديل السجل")
            self.delp.setText("تعديل")


        self.delp.clicked.connect(lambda :self.delll(u,v,x,e))
        self.canc.clicked.connect(self.close)

    def delll(self,u,v,w,e):
     try:
      if e==1:
          try:
            window.Da.query(u)
            print(v)
            window.Da.query(w)
            self.UQsql = ""
          
            for x in range(window.we.fProduct.count()):
                qttem = window.Da.query(f"select count from inventory where name ='{nan.custom_encode(window.we.fProduct.item(x).text())}'")
                if qttem[0][0] < int(window.we.cartlist[x]):
                    window.we.statusBar().showMessage(f" كمبة المنتج غير كافية {window.we.fProduct.item(x).text()}")
                    return
                self.UQsql = self.UQsql + f"update inventory set count= {qttem[0][0] - int(window.we.cartlist[x])} where (name='{nan.custom_encode(window.we.fProduct.item(x).text())}');"
            window.Da.query(self.UQsql)
          except:
              pass
            
          self.close()
          window.we.sclear()
          window.we.Fclear()
            
          return

           
      if e==2:
            window.Da.query(w)
            window.we.sclear()
            self.close()
            return
      if e==3:
            print(w)
            window.Da.query(w)
            
            self.close()
            window.we.sclear()
            window.we.Fclear()
            return
      if e==0:
          self.UQsql = ""
          try:
            for x in range(window.we.fProduct.count()):
                qttem = window.Da.query(f"select count from inventory where name ='{nan.custom_encode(window.we.fProduct.item(x).text())}'")
                if qttem[0][0] < int(window.we.cartlist[x]):
                    window.we.statusBar().showMessage(f" كمبة المنتج غير كافية {window.we.fProduct.item(x).text()}")
                    self.close()
                    return
                self.UQsql = self.UQsql + f"update inventory set count= {qttem[0][0] - int(window.we.cartlist[x])} where (name='{nan.custom_encode(window.we.fProduct.item(x).text())}');"
            window.Da.query(self.UQsql)
          except:
              pass
          try:
               window.Da.query(w)
          except:
              pass
            

          self.close()
          window.we.fadd.setText('إضافة')
          window.we.Fclear()
     except Exception as e:
           print(e)


class Log_out(QtWidgets.QMainWindow):

        def __init__(self):
            super(Log_out, self).__init__()
            uic.loadUi('log_out.ui', self)
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.show()
            self.cl = self.findChild(QtWidgets.QPushButton, 'OK')
            self.ca = self.findChild(QtWidgets.QPushButton, 'cancel')
            self.cl.clicked.connect(self.clo)
            self.ca.clicked.connect(lambda: self.close())

        def clo(self):
            global stop_threads
            stop_threads=True
            window.we.close()
            app.closeAllWindows()








class AnotherWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(AnotherWindow, self).__init__()
        uic.loadUi('dashboard.ui', self)
        self.show()
        self.controller()

    def closeEvent(self, event):
         global stop_threads
         if stop_threads==False:
            event.ignore()
         self.log_ou=Log_out()




    def controller(self):
        self.PB1 = self.findChild(QtWidgets.QPushButton, 'PB1')
        self.PB1.clicked.connect(lambda x: self.SV(0))
        self.PB2 = self.findChild(QtWidgets.QPushButton, 'PB2')
        self.PB2.clicked.connect(lambda x: self.SV(1))
        self.PB3 = self.findChild(QtWidgets.QPushButton, 'PB3')
        self.PB3.clicked.connect(lambda x: self.SV(2))
        self.PB4 = self.findChild(QtWidgets.QPushButton, 'PB4')
        self.PB4.clicked.connect(lambda x: self.SV(3))
        self.PB5 = self.findChild(QtWidgets.QPushButton, 'PB5')
        self.PB5.clicked.connect(lambda x: self.SV(4))
        self.PB6 = self.findChild(QtWidgets.QPushButton, 'PB6')
        self.PB6.clicked.connect(lambda x: self.SV(6))
        self.PB7=self.findChild(QtWidgets.QPushButton,'paper_b')
        self.PB7.clicked.connect(lambda x:self.SV(5))
        self.PR= self.findChild(QtWidgets.QPushButton, 'bill_b')
        self.PR.clicked.connect(self.reci)
        self.print_paper=self.findChild(QtWidgets.QPushButton,'print_paper')
        self.plain_paper=self.findChild(QtWidgets.QPlainTextEdit,'plain_paper')
        self.name_paper=self.findChild(QtWidgets.QLineEdit,'name_paper')
        self.sub_paper=self.findChild(QtWidgets.QLineEdit,'subject')

        self.print_paper.clicked.connect(lambda : PDF.paper(self.name_paper.text(),"الموضوع: "+self.sub_paper.text(),self.plain_paper.toPlainText()))
        self.table2 = self.findChild(QtWidgets.QTableWidget, 'tableWidget2')
        self.table3 = self.findChild(QtWidgets.QTableWidget, 'tableWidget3')
        self.pages=self.findChild(QtWidgets.QStackedWidget,"stackedWidget")
        self.table2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.settings=self.findChild(QtWidgets.QPlainTextEdit,'settingstext')
        self.settingspass=self.findChild(QtWidgets.QLineEdit,'settingspass')
        self.settingspass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.settingspass.textChanged.connect( lambda :self.settingspass.setStyleSheet("QLineEdit{border-style:solid;border-width:2;border-radius:15px;border-color: rgb(58, 153, 101);background-color: rgba(0, 0, 0, 0);padding-left:10px;padding-right:10px;}"))


        self.settingsb=self.findChild(QtWidgets.QPushButton,'settingsbutton')
        self.settingsb.clicked.connect(self.setting)
        self.tables_cont()
        self.mainscreeninit()
        self.forum()
        self.inve()


    def reci(self):
        self.rr=reciept_config()

    def setting(self):
        temtext=self.settings.toPlainText()
        tempass=self.settingspass.text()

        if tempass==window.user_pass:
            try:
                window.Da.query(temtext)
                self.settings.setPlainText(" ــــــــ تم ـــــــ ")
                self.settingspass.setText("")
                self.settingspass.setStyleSheet("QLineEdit{border-style:solid;border-width:2;border-radius:15px;border-color: rgb(58, 153, 101);background-color: rgba(0, 0, 0, 0);padding-left:10px;padding-right:10px;}")
            except:
                self.statusBar().showMessage("مشكلة اثناء تنفيذ الامر")
        else:
            self.settingspass.setStyleSheet("QLineEdit{ border-color:rgb(255, 0, 0);  border-style: solid; border-width: 1.5px; border-radius: 15px; padding-left: 10px; padding-right: 10px; padding-top: 4px; transition:border-color 2s; font-size: 16px; background: rgba(0,0,0,0.0); color: rgb(255,0,0); } QLineEdit:hover{ border-color:rgb(200,0,0);}")

    def mainscreeninit(self):

        self.setWindowIcon(QIcon("res\icon.png"))
        self.alabel = self.findChild(QtWidgets.QLabel, "ALLlabel")
        self.tlabel = self.findChild(QtWidgets.QLabel, "THISMONTHlabel")
        self.GEDlabel = self.findChild(QtWidgets.QLabel, "GAINED")
        self.NGEDlabel = self.findChild(QtWidgets.QLabel, "NOTGAINED")
        tot=window.Da.query("SELECT SUM(total)  FROM trans")
        mt = window.Da.query(f"SELECT SUM(total)  FROM trans where date>{date.today() - timedelta(days=30)}")
        GED = window.Da.query("SELECT SUM(total)  FROM trans  where gained=1")
        NGED = window.Da.query("SELECT SUM(total)  FROM trans  where gained=0")
        pali=window.Da.query("select payschedule from trans ORDER BY date ")
        te=[]
        for j in range(len(pali)):
            e=str(nan.custom_decode(pali[j][0])).split(";")
            e.pop(len(e)-1)


            for f in range(len(e)):
                te.append(e[f])





        self.alabel.setText(str(tot[0][0]))
        self.tlabel.setText(str(mt[0][0]))
        self.GEDlabel.setText(str(GED[0][0]))
        self.NGEDlabel.setText(str(NGED[0][0]))
        if str(GED[0][0])=='None':
            self.GEDlabel.setText(str(1))
        if str(NGED[0][0])=='None':
            self.NGEDlabel.setText(str(1))


        self.pa_li=self.findChild(QtWidgets.QListWidget,'payment_list')
        self.pages.setCurrentIndex(0)
        self.inventpages.setCurrentIndex(0)
        self.pages_2=self.findChild(QtWidgets.QStackedWidget,'stackedWidget_2')


        for s in te:
            self.pa_li.addItem(str(s))


        self.th2=threading.Thread(target=self.lp,name="th2",args=())
        self.th2.start()





    def lp(self):
        
        i=1
        global stop_threads
        while i !=0:
            if i%2 == 0 :
                self.pages_2.setCurrentIndex(1)
            else:
                self.pages_2.setCurrentIndex(0)
            i=i+1
            time.sleep(5)

            if stop_threads:
                break








    def tables_cont(self):
        self.VIEW = self.findChild(QtWidgets.QPushButton, "VIEW")
        self.EDIT = self.findChild(QtWidgets.QPushButton, "EDIT")
        self.DELETE = self.findChild(QtWidgets.QPushButton, "DELETE")
        self.all_t = self.findChild(QtWidgets.QPushButton, 'ALL')
        self.week_t = self.findChild(QtWidgets.QPushButton, 'THISWEEK')
        self.month_t = self.findChild(QtWidgets.QPushButton, 'THISMONTH')
        self.price_t = self.findChild(QtWidgets.QPushButton, 'PRICING')
        self.search_t = self.findChild(QtWidgets.QPushButton, 'SEARCH')
        self.sline_t = self.findChild(QtWidgets.QLineEdit, 'SEARCHLINE')
        self.all_t_2 = self.findChild(QtWidgets.QPushButton, 'ALL_2')
        self.week_t_2 = self.findChild(QtWidgets.QPushButton, 'THISWEEK_2')
        self.month_t_2 = self.findChild(QtWidgets.QPushButton, 'THISMONTH_2')
        self.price_t_2 = self.findChild(QtWidgets.QPushButton, 'PRICING_2')
        self.search_t_2 = self.findChild(QtWidgets.QPushButton, 'SEARCH_2')
        self.sline_t_2 = self.findChild(QtWidgets.QLineEdit, 'SEARCHLINE_2')
        self.VIEW.clicked.connect(self.view)
        self.EDIT.clicked.connect(self.edit)
        self.DELETE.clicked.connect(self.delete)
        self.all_t.clicked.connect(lambda : self.tab_filler(window.Da.query("select * from trans")))
        self.week_t.clicked.connect(lambda: self.tab_filler(window.Da.query(f"select * from trans where date>{date.today()-timedelta(days=7)}")))
        self.month_t.clicked.connect(lambda: self.tab_filler( window.Da.query(f"select * from trans where date>{date.today() - timedelta(days=30)}")))
        self.price_t.clicked.connect(lambda: self.tab_filler( window.Da.query(f"select * from trans ORDER BY total DESC;")))
        self.search_t.clicked.connect(lambda: self.tab_filler(window.Da.query(f"select * from trans WHERE name LIKE '%{str(nan.custom_encode(self.sline_t.text()))}%'")))
        self.all_t_2.clicked.connect(lambda: self.tab_filler(window.Da.query("select * from inventory")))
        self.week_t_2.clicked.connect(lambda: self.tab_filler( window.Da.query(f"select * from inventory where date>{date.today() - timedelta(days=7)}")))
        self.month_t_2.clicked.connect(lambda: self.tab_filler( window.Da.query(f"select * from inventory where date>{date.today() - timedelta(days=30)}")))
        self.price_t_2.clicked.connect( lambda: self.tab_filler(window.Da.query(f"select * from inventory ORDER BY price DESC;")))
        self.search_t_2.clicked.connect(lambda: self.tab_filler( window.Da.query(f"select * from inventory WHERE name LIKE '%{str(nan.custom_encode(self.sline_t_2.text()))}%'")))

        #SECOND table
        self.sVIEW = self.findChild(QtWidgets.QPushButton, "secVIEW")
        self.sEDIT = self.findChild(QtWidgets.QPushButton, "secEDIT")
        self.sADD = self.findChild(QtWidgets.QPushButton, "secADD")
        self.sVIEW.clicked.connect(self.sview)
        self.inventpages=self.findChild(QtWidgets.QStackedWidget,'stackedWidget_3')
        self.finvname=self.findChild(QtWidgets.QLineEdit,'invname_2')
        self.finvserial = self.findChild(QtWidgets.QLineEdit, 'invserial')

        self.finvcountry= self.findChild(QtWidgets.QLineEdit, 'invcountry')
        self.finvvendor = self.findChild(QtWidgets.QLineEdit, 'invvendor')
        self.finvprice = self.findChild(QtWidgets.QLineEdit, 'invprice_2')
        self.finvprice.setValidator(QDoubleValidator(0,9999999999,4))
        self.finvadate=self.findChild(QtWidgets.QDateTimeEdit,'invadate')
        self.finvvdate = self.findChild(QtWidgets.QDateTimeEdit, 'invvdate')
        self.finvqty = self.findChild(QtWidgets.QSpinBox, 'invqty')
        self.finvqty.setMaximum(9999999)
        self.finvbb = self.findChild(QtWidgets.QPushButton, 'invbbutton')
        self.finvipath = self.findChild(QtWidgets.QLineEdit, 'invimagepath')
        self.invento=self.findChild(QtWidgets.QLineEdit,'invento')
        self.finvbb.clicked.connect(self.getfile)





        self.sEDIT.clicked.connect(self.sedit)
        self.sADD.clicked.connect(self.add)

    def getfile(self):
        try:
             fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.gif *png)")
             print(fname[0])
             self.finvipath.setText(fname[0])
        except Exception as e:
            pass

    def sedit(self):
            try:
                cur = self.table3.selectedItems()[0].data(0)
                if self.inventpages.currentIndex() == 0:
                      self.inventpages.setCurrentIndex(1)

                      re=window.Da.query(f"select * from inventory where id={cur}")
                      self.finvname.setText(nan.custom_decode(re[0][2]))
                      self.finvserial.setText(re[0][1])
                      self.finvprice.setText(str(re[0][3]))
                      self.finvqty.setValue(re[0][4])
                      self.finvadate.setDateTime(re[0][5])
                      self.finvvdate.setDateTime(re[0][6])
                      self.finvvendor.setText(nan.custom_decode(re[0][7]))
                      self.finvcountry.setText(nan.custom_decode(re[0][8]))
                      self.finvipath.setText(re[0][9])
                      self.invento.setText(nan.custom_decode(re[0][10]))
                      self.sEDIT.setText("حفظ")
                      return
                if self.sEDIT.text()=="تعديل":
                    self.sEDIT.setText("حفظ")
                    return
                else:

                    sqliu=f"update inventory set count= {self.finvqty.text()},serial={self.finvserial.text()},name='{nan.custom_encode(self.finvname.text())}',price={self.finvprice.text()},date='{self.finvadate.dateTime().toString('yyyy-MM-dd hh:mm:ss')}',validation='{self.finvvdate.dateTime().toString('yyyy-MM-dd hh:mm:ss')}',vendor='{nan.custom_encode(self.finvvendor.text())}',country='{nan.custom_encode(self.finvcountry.text())}',image='{self.finvipath.text()}',inventory='{nan.custom_encode(self.invento.text())}' where (id={cur})"
                    self.invadd = adder("", "", sqliu, 3)
                    

            except Exception as e:
                pass








            # print(self.table2.selectedItems(self))

    def add(self):
        try:
            if self.inventpages.currentIndex() == 0:
                self.inventpages.setCurrentIndex(1)
                return
            else:

                if self.finvname.text()=="" or self.finvserial.text()=="" or self.finvqty.text()=="" or self.finvprice.text()=="":
                    self.statusBar().showMessage("رجاءا اكمل المعلومات الاساسية لاضافة منتج (الاسم,الرفم,السعر,الكمية)")
                    return
                sql=f"insert into inventory (serial,name,price,count,date,validation,vendor,country,image,inventory) values('{nan.custom_encode(self.finvserial.text())}','{nan.custom_encode(self.finvname.text())}',{float(self.finvprice.text())},{self.finvqty.value()},'{self.finvadate.dateTime().toString('yyyy-MM-dd hh:mm:ss')}','{self.finvvdate.dateTime().toString('yyyy-MM-dd hh:mm:ss')}','{nan.custom_encode(self.finvvendor.text())}','{nan.custom_encode(self.finvcountry.text())}','{self.finvipath.text()}','{nan.custom_encode(self.invento.text())}')"
                sqli=sql.encode('utf-8')
                self.invadd=adder("","",sqli,2)
                
        except Exception as e:
            pass



    def sclear(self):
         try:

                      self.finvname.setText('')
                      self.finvserial.setText('')
                      self.finvprice.setText('')
                      self.finvqty.setValue(0)
                      self.finvvendor.setText('')
                      self.finvcountry.setText('')
                      self.finvipath.setText('')
                      self.invento.setText('')
         except:
              pass
    def sview(self):
        try:

              tem = window.Da.query("select * from inventory")
              PDF.inv_info(tem)
        except:
            pass






    def edit(self):
      try:
          self.Fclear()
          self.curr=self.table2.selectedItems()[0].data(0)
          tem=window.Da.query(f"select * from trans where id={self.curr}")
          self.fname.setText(str(nan.custom_decode(tem[0][1])))
          self.flocate.setText(str(nan.custom_decode(tem[0][2])))
          self.faddress.setText(str(nan.custom_decode(tem[0][4])))
          self.fcontact.setText(str(nan.custom_decode(tem[0][3])))
          self.ftotal.setText(str(tem[0][8]))
          self.fdate.setDateTime(tem[0][9])
          self.fpaydate.setDateTime(tem[0][9])

          tem2=tem[0][5].split(",")
          tem2.pop(len(tem2) - 1)
          tem22=[]
          for c in tem2:
              tem22.append(nan.custom_decode(c))


          for x in tem22:
            self.fProduct.addItem(str(x))

          tem3=window.Da.query("select name from inventory")


          for y in range(len(tem3)):
             if nan.custom_decode(tem3[y][0]) not in tem22:
                self.fProducts.addItem(str(nan.custom_decode(tem3[y][0])))


          temprice=str(tem[0][7]).split(",")
          temprice.pop(len(temprice) - 1)
          self.cartprices=temprice
          temQTY=str(tem[0][6]).split(",")
          temQTY.pop(len(temQTY) - 1)

          for d in temQTY:
              self.cartlist.append(int(d))







          self.cartlist=temQTY
          try:
             temsch=str(nan.custom_decode(tem[0][10])).split(";")
             for u in temsch:
                self.paylist.addItem(u)

          except:
              self.paylist.addItem('None')
          self.total=0
          self.SV(1)
          self.fadd.setText("تعديل")


          #self.Fclear()
          #self.filllist()
      except Exception as e:
          pass









    def delete(self):
        try:
             self.curr=self.table2.selectedItems()[0].data(0)
             if self.table2.selectedItems()[11].text() == '1':
                 self.statusBar().showMessage("لا يمكن حذف السجلات المتحصلة",5000)
                 return
             try:
                 pp = window.Da.query(f"select product from trans where id={self.curr}")
                 pq = window.Da.query(f"select QTY from trans where id={self.curr}")
                 pp = str(pp[0][0]).split(",")
                 pq = str(pq[0][0]).split(",")
                 pp.pop(len(pp) - 1)
                 pq.pop(len(pq) - 1)
                 self.invbacksql = ""
             except:
                 pass
             try:
                 for w in range(len(pp)):
                     teb = window.Da.query(f"select count from inventory where name ='{pp[w]}'")
                     self.invbacksql = self.invbacksql + f"update inventory set count={teb[0][0] + int(pq[w])}  where (name='{pp[w]}');"
             except:
                 pass
             self.dell = deleter()
              


        except Exception as e:
              print(e)
    def view(self):
       try:
          self.t_it=self.table2.selectedItems()[0].data(0)
          tem=window.Da.query(f"select * from trans where id={self.t_it}")
          prices=str(tem[0][7]).split(",")
          QTY=str(tem[0][6]).split(",")
          total=[]
          prod=[]
          pro=str(tem[0][5]).split(",")
          for r in pro:
              prod.append(nan.custom_decode(r))
          tu=[]
          for x in range(len(QTY)-1):
              total.append(float(prices[x]) * int(QTY[x]))
              tu.append([total[x],QTY[x],prices[x],prod[x]])



          PDF.bill(nan.custom_decode(tem[0][1]),nan.custom_decode(tem[0][2]),tem[0][9],tem[0][8],nan.custom_decode(tem[0][10]).split(";"),tem[0][11],tu)

       except Exception as e:
           pass


#END OF TQ ........ def
    def inve(self):
        #INSERT INTO `clients`.`inventory` (`id`, `serial`, `name`, `price`, `count`, `date`, `validation`, `vendor`, `country`, `image`) VALUES ('1', '239847284', 'مناديل مبللة', '3400.2', '98', '2021/3/1', '2024/4/5', 'hultar', 'turkie', 'res\\product image\\robot-style-car-with-joystick.jpg');

        self.invname=self.findChild(QtWidgets.QLabel ,'invname')
        self.invno = self.findChild(QtWidgets.QLabel, 'invno')
        self.invcon = self.findChild(QtWidgets.QLabel, 'invcon')
        self.invman = self.findChild(QtWidgets.QLabel, 'invman')
        self.invad = self.findChild(QtWidgets.QLabel, 'invarivedate')
        self.invprice = self.findChild(QtWidgets.QLabel, 'invprice')
        self.invexpire = self.findChild(QtWidgets.QLabel, 'invexpire')
        self.invv = self.findChild(QtWidgets.QLabel, 'inv')
        self.invcount = self.findChild(QtWidgets.QLabel, 'invcount')
        self.invimg = self.findChild(QtWidgets.QLabel, 'invpreview')
        self.inventt=self.findChild(QtWidgets.QLabel,'inv')
        self.table3.itemSelectionChanged.connect(lambda : self.get_inv())



    def get_inv(self):
        try:
            self.inventpages.setCurrentIndex(0)
            x=self.table3.selectedItems()[0].text()
            tem=window.Da.query(f"select * from inventory where id={x}")
            self.invname.setText("الاسم:"+nan.custom_decode(str(tem[0][2])))
            self.invno.setText("الرقم المتسلسل:" + str(tem[0][1]))
            self.invprice.setText("السعر:" + str(tem[0][3]))
            self.invcon.setText("المنشأ:" + nan.custom_decode(str(tem[0][8])))
            self.invman.setText("المصنع:" + nan.custom_decode(str(tem[0][7])))
            self.invad.setText("تاريخ الوصول:" + str(tem[0][5]))
            self.invcount.setText("الكمية:" + str(tem[0][4]))
            self.invexpire.setText("الصلاحية:" + str(tem[0][6]))
            self.inventt.setText("المخزن:"+nan.custom_decode(str(tem[0][10])))
            try:
               self.invimg.setPixmap(QPixmap(str(tem[0][9])))
            except:
                self.invimg.setPixmap(QPixmap("icons\warning.png"))




        except Exception as e:
            self.invname.setText("الاسم:" )
            self.invno.setText("الرقم:" )
            self.invprice.setText("السعر:" )
            self.invcon.setText("المنشأ:" )
            self.invman.setText("المصنع:" )
            self.invad.setText("تاريخ الوصول:" )
            self.invcount.setText("الكمية:" )
            self.invexpire.setText("الصلاحية:" )
            self.invimg.setPixmap(QPixmap("icons\warning.png"))




















    def forum(self):
        self.fname=self.findChild(QtWidgets.QLineEdit,'fNAME')
        self.flocate = self.findChild(QtWidgets.QLineEdit, 'fLOCATE')
        self.faddress = self.findChild(QtWidgets.QLineEdit, 'fADDRESS')
        self.fcontact = self.findChild(QtWidgets.QLineEdit, 'fCONTACT')
        self.fspin = self.findChild(QtWidgets.QSpinBox, 'fSPIN')
        self.fprice = self.findChild(QtWidgets.QLineEdit, 'fPRICE')
        self.ftotal = self.findChild(QtWidgets.QLineEdit, 'fTOTAL')
        self.fdate = self.findChild(QtWidgets.QDateTimeEdit, 'fDATE')
        self.fpaied = self.findChild(QtWidgets.QLineEdit, 'fPAIED')
        self.fpaydate = self.findChild(QtWidgets.QDateTimeEdit, 'fPAYDATE')
        self.fadd = self.findChild(QtWidgets.QPushButton, 'fADD')
        self.fclear = self.findChild(QtWidgets.QPushButton, 'fCLEAR')
        self.fview = self.findChild(QtWidgets.QPushButton, 'fVIEW')
        self.fProducts=self.findChild(QtWidgets.QListWidget,'fProductlist')
        self.fProduct=self.findChild(QtWidgets.QListWidget,'fCartlist')
        self.fcartadd=self.findChild(QtWidgets.QPushButton,'fCartadd')
        self.fcartdel=self.findChild(QtWidgets.QPushButton,'fCartdel')
        self.fcartclear=self.findChild(QtWidgets.QPushButton,'fCartclear')
        self.fpayadd=self.findChild(QtWidgets.QPushButton,'fPayadd')
        self.paylist=self.findChild(QtWidgets.QListWidget,'fPaymentlist')
        self.payclear=self.findChild(QtWidgets.QPushButton,'fPaymentclear')
        self.fGcheck=self.findChild(QtWidgets.QCheckBox,'Gcheck')


    #simple inti
        self.cartlist=[]
        self.cartprices=[]
        self.total=0
        self.filllist()
        self.fprice.setText('0')
        self.fdate.setDateTime(QDateTime.currentDateTime())
        self.fpaydate.setDateTime(QDateTime.currentDateTime())
        self.ftotal.setValidator(QDoubleValidator(0,9999999999,4))
        self.fprice.setValidator(QDoubleValidator(0,9999999999,4))
        self.fpaied.setValidator(QDoubleValidator(0,999999999,4))
        self.fspin.setMaximum(9999999)


    #buttons actions
        self.fadd.clicked.connect(self.Fadd)
        self.fclear.clicked.connect(self.Fclear)
        self.fview.clicked.connect(self.Fview)
        self.fcartadd.clicked.connect(self.addlist)
        self.fcartclear.clicked.connect(self.clearlist)
        self.fcartdel.clicked.connect(self.dellist)
        self.fspin.valueChanged.connect(self.spined)
        self.fProduct.currentItemChanged.connect(self.order_det)
        self.ftotal.textChanged.connect(self.total_ch)
        self.fpayadd.clicked.connect(self.pay)
        self.payclear.clicked.connect(self.total_ch)
        self.SV(0)







    #basic functions _______________________

    def filllist(self):
        try:
           self.fProducts.clear()
           tem=window.Da.query('select name from inventory where count>0')
           for x in tem:
                self.fProducts.addItem(str(nan.custom_decode(x[0])))
        except Exception as e:
            pass


    def addlist(self):
        try:
           tem=self.fProducts.currentItem()
           self.fProduct.addItem(tem.text())
           self.cartprices.append(0)
           self.cartlist.append(0)
           self.fProducts.takeItem(self.fProducts.row(self.fProducts.currentItem()))

        except:
            pass


    def clearlist(self):
      try:
        self.fProduct.clear()
        self.filllist()
        self.ftotal.setText("")
        self.cartlist.clear()
        self.cartprices.clear()
      except:
          pass


    def dellist(self):
        try:
           tem=self.fProduct.currentItem()
           self.fProducts.addItem(tem.text())
           self.cartlist.pop(self.fProduct.currentIndex().row())
           self.cartprices.pop(self.fProduct.currentIndex().row())
           self.fProduct.takeItem(self.fProduct.row(tem))
           self.fspin.setValue(0)


        except:
            pass

    def pay(self):
      try:

        if float(self.fpaied.text()) > float(self.total) or float(self.fpaied.text())==0:
            return
        tem=self.fpaied.text()

        self.paylist.addItem(f"{tem}               {self.fpaydate.dateTime().toString('yyyy-MM-dd hh:mm:ss')}")
        self.total=self.total-float(tem)
        self.fpaied.setText(str(self.total))
      except:
          pass




    def total_ch(self):
        try:
           self.fpaied.setText(str(self.ftotal.text()))
           self.total=float(self.ftotal.text())
           self.paylist.clear()
        except:
            pass





    def order_det(self):
        try:
            temp=window.Da.query(f"select price from inventory where name='{nan.custom_encode(self.fProduct.currentItem().text())}'")
            t=temp[0][0]
            self.fprice.setText(str(t))
            self.cartprices[self.fProduct.currentIndex().row()]=float(t)

            self.fspin.setValue(int(self.cartlist[self.fProduct.currentIndex().row()]))



        except:
            pass


    def spined(self):
      try:
        self.cartlist[self.fProduct.currentIndex().row()]=self.fspin.value()
        self.total=0
        u=0


        for x in self.cartlist:
            self.total=self.total+float(x)*float(self.cartprices[u])
            u=u+1

        self.ftotal.setText(str(self.total))
        self.paylist.clear()
        self.fpaied.setText(str(self.total))
        #str(float(self.fprice.text()) * self.fspin.value()
      except:
          pass


    def Fadd(self):


        if len(self.fname.text())<4 or len(self.flocate.text())<4 :
            self.statusBar().showMessage("رجاءا الكمل المعلومات الاساسية",5000)
            return
        if self.fProduct.count()==0:
            self.statusBar().showMessage("الرجاء ادخال منتج واحد كحد ادنى")
            return
        if self.ftotal.text()=="":
            self.statusBar().showMessage("القيمة الكلية للمعاملة يجب الا تكون 0",5000)
            return
        if self.total != 0:
            self.statusBar().showMessage("اكمل جدول المدفوعات",5000)
            return









        try:
            self.nn = str(nan.custom_encode(self.fname.text()))
            self.pl = str(nan.custom_encode(self.flocate.text()))
            self.cc = str(nan.custom_encode(self.fcontact.text()))
            self.aa = str(nan.custom_encode(self.faddress.text()))


            temp=""
            te=""
            tt=""
            for x in  range(self.fProduct.count()):
                temp=temp+nan.custom_encode(self.fProduct.item(x).text())+","
                te=te+str(self.cartlist[x])+","
                tt=tt+str(self.cartprices[x])+","

            print(temp)





            listtem=""
            for y in range(self.paylist.count()):
                v=self.paylist.item(y).text()
                listtem=listtem+v+" ;"





            if self.fGcheck.checkState() !=0:
                gained=1
            else:
                gained=0










            sqt=f"insert into trans(name,place,contact,address,product,QTY,price,total,date,payschedule,gained) values('{self.nn}','{self.pl}','{self.cc}','{self.aa}','{temp}','{te}','{tt}',{float(self.ftotal.text())},'{self.fdate.dateTime().toString('yyyy-MM-dd hh:mm:ss')}','{listtem}',{gained})"


            self.se=sqt
            
            ee=''
            ew=''
            print(self.fadd.text())            
            

            if self.fadd.text()=='إضافة':
                 print('h')
                 self.addq=adder("","",self.se,0)
                

            else:
                try:
                     pp=window.Da.query(f"select product from trans where id={self.curr}")
                     pq = window.Da.query(f"select QTY from trans where id={self.curr}")
                     pp=str(pp[0][0]).split(",")
                     pq=str(pq[0][0]).split(",")
                     pp.pop(len(pp) - 1)
                     pq.pop(len(pq) - 1)

                     self.invbacksql=""
                     for w in range(len(pp)):
                          teb= window.Da.query( f"select count from inventory where name ='{pp[w]}'")
                          self.invbacksql=self.invbacksql+f"update inventory set count={teb[0][0]+int(pq[w])}  where (name='{pp[w]}');"


                except Exception as e:
                    pass

               # for x in range(self.fProduct.count()):
                #    qttem = window.Da.query(
                 #       f"select count from inventory where name ='{nan.custom_encode(self.fProduct.item(x).text())}'")

                  #  self.UQsql = self.UQsql + f"update inventory(count) values({qttem[0][0] - self.cartlist[x]}) where name='{nan.custom_encode(self.fProduct.item(x).text())}';"

                usqt = f"UPDATE trans SET name='{str(nan.custom_encode(self.fname.text()))}',place='{nan.custom_encode(self.flocate.text())}',contact='{nan.custom_encode(self.fcontact.text())}',address='{nan.custom_encode(self.faddress.text())}',product='{temp}',QTY='{te}',price='{tt}',total='{self.ftotal.text()}',date='{self.fdate.dateTime().toString('yyyy-MM-dd hh:mm:ss')}',payschedule='{listtem}',gained={gained} WHERE id={self.curr};"

                self.use = usqt.encode('utf-8')
                self.ubse=self.invbacksql.encode('utf-8')
                self.addq=adder(self.invbacksql,"",self.use,1)













        except Exception as e:
            print(e)






    def Fclear(self):
        self.fname.setText("")
        self.flocate.setText("")
        self.faddress.setText("")
        self.fcontact.setText("")
        self.fProduct.clear()
        self.fProducts.clear()
        self.fspin.setValue(0)
        self.cartlist.clear()
        self.cartprices.clear()

        self.fprice.setText("")
        self.ftotal.setText("")
        self.fpaied.setText("")
        self.paylist.clear()
        self.total=0
        self.filllist()





    def Fview(self):
        pass



    def tab_filler(self,x):
        try:

            self.table2.clearSelection()
            self.table2.setRowCount(0)



            for row_number, row_data in enumerate(x):
                self.table2.insertRow(row_number)
                for cloum_number, data in enumerate(row_data):
                    self.table2.setItem(row_number, cloum_number,
                                        QTableWidgetItem(str(nan.custom_decode(str(data)))))


            self.table3.clearSelection()
            self.table3.setRowCount(0)

            for row_number, row_data in enumerate(x):
                self.table3.insertRow(row_number)
                for cloum_number, data in enumerate(row_data):
                    self.table3.setItem(row_number, cloum_number, QTableWidgetItem(nan.custom_decode(str(data))))
        except Exception as e:
            pass





    def anim_label(self):
            self.pages_2.setCurrentIndex(0)
            self.anim = QPropertyAnimation(self.GEDlabel, b"geometry")
            self.anim.setDuration(500)
            self.anim.setStartValue(QRect(60, 80, 0,31))
            self.anim.setEndValue(QRect(60, 80,int(10+(float(self.GEDlabel.text())/(float(self.GEDlabel.text())+float(self.NGEDlabel.text())))*400), 31))
            self.animee = QPropertyAnimation(self.NGEDlabel, b"geometry")
            self.animee.setDuration(500)
            self.animee.setStartValue(QRect(60, 130, 0, 31))
            self.animee.setEndValue(QRect(60, 130,int(10+(float(self.NGEDlabel.text())/(float(self.GEDlabel.text())+float(self.NGEDlabel.text())))*400), 31))
            self.anim.start()
            self.animee.start()
    def SV(self,x):
        try:
           self.fadd.setText('إضافة')
           self.sEDIT.setText('تعديل')
           self.pages.setCurrentIndex(x)
           self.anim_label()

           self.table2.setRowCount(0)

           for row_number, row_data in enumerate(window.Da.query("select * from trans")):
               self.table2.insertRow(row_number)
               for cloum_number, data in enumerate(row_data):
                    self.table2.setItem(row_number, cloum_number, QTableWidgetItem(str(nan.custom_decode(str(data)))))




           self.table3.setRowCount(0)

           for row_number, row_data in enumerate(window.Da.query("select * from inventory")):
                   self.table3.insertRow(row_number)
                   for cloum_number, data in enumerate(row_data):
                      self.table3.setItem(row_number, cloum_number, QTableWidgetItem(str(nan.custom_decode(str(data)))))
        except Exception as e:
            print(e)



app = QtWidgets.QApplication(sys.argv)
window = myy()
app.exec_()
