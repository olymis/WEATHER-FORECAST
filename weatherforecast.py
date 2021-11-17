from os import scandir
from sqlite3.dbapi2 import Cursor
from PyQt5 import uic,QtWidgets

import sqlite3

global senha_db

def converte_celtofah():
    temp = int(telaconversao.lineEdit.text())
    temp = (temp * 9/5) + 32

    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Sucesso")
    msg.setText("Resultado: "+str(temp)+"°F")
    msg.exec()


def converte_fahtocel():
    temp2 = int(telaconversao.lineEdit_2.text())
    temp2 = (temp2 - 32) * 5/9

    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Sucesso")
    msg.setText("Resultado: "+str(temp2)+"°C")
    msg.exec()    

def sair_login():
    tela1login.close()
    primeiratela.show()

   
def conversao():
    primeiratela.close()
    telaconversao.show()   

def sair_conversao():
    telaconversao.close()
    primeiratela.show()

def cadastrar_db():
    nome = telacadastro.lineEdit_2.text()
    senha = telacadastro.lineEdit_3.text()
    c_senha = telacadastro.lineEdit_4.text()

    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco.db') 
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('"+nome+"','"+senha+"')")

            banco.commit() 
            banco.close()
            telacadastro.close()
            primeiratela.show()

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else:
        telacadastro.label.setText("As senhas digitadas estão diferentes")

def chama_primeiratela():
    tela1login.label_4.setText("")
    nome_user = tela1login.lineEdit.text()
    senha = tela1login.lineEdit_2.text()
    banco = sqlite3.connect('banco.db')
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT senha FROM cadastrar WHERE login = '{}'".format(nome_user))
        senha_db = cursor.fetchall()
        print(senha_db[0][0])
        banco.close
    except: 
        print("ERRO AO VALIDAR LOGIN")

    if senha == senha_db[0][0]:
        tela1login.close()
        primeiratela.show()

    else:
        tela1login.label_4.setText("Dados incorretos")


def cadastrar():
    tela1login.close()
    telacadastro.show()

def sair_cadastro():
    telacadastro.close()
    tela1login.show()

def voltar_login():
    primeiratela.close()
    tela1login.show()    

def abrir_temp():
    primeiratela.close()    
    telatempo.show()

def fechar_temp():
    telatempo.close()
    primeiratela.show()

def fechar_app():
    tela1login.close()

app=QtWidgets.QApplication([])
primeiratela = uic.loadUi("primeiratela.ui")
tela1login = uic.loadUi("tela1login.ui") 
telacadastro = uic.loadUi("telacadastro.ui")
telaconversao = uic.loadUi("telaconversao.ui")
telatempo = uic.loadUi("telatempo.ui")

primeiratela.pushButton_3.clicked.connect(conversao)
primeiratela.pushButton_4.clicked.connect(abrir_temp)
primeiratela.pushButton_2.clicked.connect(voltar_login)
telaconversao.pushButton_2.clicked.connect(sair_conversao)
telaconversao.pushButton_3.clicked.connect(converte_celtofah)
telaconversao.pushButton_4.clicked.connect(converte_fahtocel)
tela1login.pushButton.clicked.connect(chama_primeiratela)
tela1login.pushButton_2.clicked.connect(cadastrar)
telacadastro.pushButton.clicked.connect(cadastrar_db)
telacadastro.pushButton_2.clicked.connect(sair_cadastro)
tela1login.pushButton_3.clicked.connect(fechar_app)
telatempo.pushButton_3.clicked.connect(fechar_temp)


tela1login.show()
app.exec()