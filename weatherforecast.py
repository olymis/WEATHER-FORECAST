from os import scandir
from PyQt5 import uic,QtWidgets
import sqlite3

def login():
    primeiratela.close()
    tela1login.show()

def sair_login():
    tela1login.close()
    primeiratela.show()

def conversao():
    primeiratela.close()
    telaconversao.show()

def sair_conversao():
    telaconversao.close()
    primeiratela.show()


def chama_tela2login():
    tela1login.label_4.setText("")
    nome_user = tela1login.lineEdit.text()
    senha = tela1login.lineEdit_2.text()
    if nome_user == "rafael" and senha == "123":
        tela1login.close()
        tela2login.show()
    else:
        tela1login.label_4.setText("Dados incorretos!")

def sair():
        tela2login.close()
        tela1login.show()

def cadastrar():
    tela1login.close()
    telacadastro.show()

def sair_cadastro():
    telacadastro.close()
    tela1login.show()


def fechar_app():
    primeiratela.close()



app=QtWidgets.QApplication([])
primeiratela = uic.loadUi("primeiratela.ui")
tela1login = uic.loadUi("tela1login.ui")
tela2login = uic.loadUi("tela2login.ui") 
telacadastro = uic.loadUi("telacadastro.ui")
telaconversao = uic.loadUi("telaconversao.ui")


primeiratela.pushButton.clicked.connect(login)
tela1login.pushButton_3.clicked.connect(sair_login)
primeiratela.pushButton_3.clicked.connect(conversao)
telaconversao.pushButton_2.clicked.connect(sair_conversao)
tela1login.pushButton.clicked.connect(chama_tela2login)
tela2login.pushButton_2.clicked.connect(sair)
tela1login.pushButton_2.clicked.connect(cadastrar)
telacadastro.pushButton_2.clicked.connect(sair_cadastro)
primeiratela.pushButton_2.clicked.connect(fechar_app)

primeiratela.show()
app.exec()