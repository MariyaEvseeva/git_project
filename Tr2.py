from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber
from PyQt5.QtGui import QPixmap
import sys
 

class Say_Hello(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(600, 600, 1000, 1000)
        self.setWindowTitle('������������')

app = QApplication(sys.argv)
ex2 = Say_Hello()
ex2.show()
sys.exit(app.exec())
         
         
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setGeometry(100, 100, 500, 350)
        self.setWindowTitle('��������������')
        
        self.table = QLCDNumber(self)
        self.table.display('')
        self.setStyleSheet("background-color: #EEE8AA; color: #191970; font-family: Times;")
        self.table.move(20, 20)
        self.table.resize(460, 50)            
        
        self.btn = QPushButton('�������, ����� ������ �����', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(217, 120)
        self.btn.clicked.connect(self.coding)
 
        self.label = QLabel(self)
        self.label.setText("����� ����������� ������� �����")
        self.label.move(40, 30)
 
        self.word_label = QLabel(self)
        self.word_label.setText("������� �����: ")
        self.word_label.move(40, 90)
 
        self.word_input = QLineEdit(self)
        self.word_input.move(130, 90)
        self.word_input.resize(330, 20)      
        
        ## ������ 2
        self.table2 = QLabel(self)
        self.table2.move(20, 200)
        self.table2.resize(480, 20)        
        
        self.table3 = QLabel(self)
        self.table3.move(20, 230)
        self.table3.resize(480, 20)
        
        self.table4 = QLabel(self)
        self.table4.move(20, 260)
        self.table4.resize(480, 20)
 
        self.table5 = QLabel(self)
        self.table5.move(20, 290)
        self.table5.resize(480, 20)
        
        ## ������
        self.ad_area = QLabel(self)
        self.ad_area.setText("����� �� ������ ������� �������� ���������� � �����:")
        self.ad_area.move(20, 180)   
        
        ## ������ � ������
        self.btn_to_add = QPushButton('�������, ����� ������� ������ �� ���� �����', self)
        self.btn_to_add.resize(self.btn_to_add.sizeHint())
        self.btn_to_add.move(132, 145)
        self.btn_to_add.clicked.connect(self.information)    
    
    
    def coding(self):
        self.d = {'�':'A', '�':'B', '�':'V', '�':'G', '�':'D', '�':'E', '�':'E', '�':'Zh', '�':'Z', '�':'I','�':'I','�':'K','�':'L', '�':'M', '�':'N', '�':'O', '�':'P','�':'R','�':'S','�':'T','�':'U','�':'F','�':'Kh','�':'Tc', '�':'Ch','�':'Sh','�':'Shch', '�':'Y','�':'E','�':'Iu', '�':'Ia', '�':'a', '�':'b', '�':'v', '�':'g', '�':'d', '�':'e', '�':'e', '�':'zh', '�':'z', '�':'i','�':'i','�':'k','�':'l', '�':'m', '�':'n', '�':'o', '�':'p','�':'r','�':'s','�':'t','�':'u','�':'f','�':'kh','�':'tc', '�':'ch','�':'sh','�':'shch', '�':'y','�':'e','�':'iu', '�':'ia' }
        answ = self.word_input.text()
        ans = ''
        for i in answ:
            if i in self.d:
                ans += self.d[i]
            elif i != '�' and i != '�' and i != '�' and i != '�':
                ans += i
        self.label.setText("{}".format(ans))
        self.WORD = ans
    
    def information(self):
        word_to_ad = self.WORD 
        word_in_Russian = self.word_input.text()
        self.table2.setText("��������: {};  ��������������: {}".format(word_in_Russian, word_to_ad))
        self.table3.setText("����� ����� � ������� ��������: {};  � �������������������: {}".format(len(word_in_Russian), len(word_to_ad)))
        g = ['a', 'u', 'e', 'o', 'y', 'i']
        gg = ['�', '�', '�', '�', '�', '�', '�', '�', '�', '�']
        kk = 0
        for i in word_to_ad:
            if i.lower() in g:
                kk += 1
                
        kkk = 0
        for i in word_in_Russian:
            if i.lower() in gg:
                kkk += 1
                
        self.table4.setText("���������� ������� ������ � ������� ������: {};  � ������������������� ������: {}".format(kkk, kk))
        self.table5.setText("���������� ��������� ������ � ������� ������: {};  � ������������������� ������: {}".format(len(word_in_Russian) - kkk, len(word_to_ad) - kk))
        
        
app = QApplication(sys.argv)
ex = Example()
ex2.close()
ex.show()
sys.exit(app.exec())