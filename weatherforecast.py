from os import scandir
from sqlite3.dbapi2 import Cursor
from PyQt5 import uic,QtWidgets

import sqlite3

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
    try:
        Cursor.execute("SELECT senha FROM cadastrar_db WHERE login ='{}").format(nome_user)
        senha_db = Cursor.fetchall()
        print(senha_db[0][0])
        banco.close
    except:
        print("Erro ao validar login")
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
tela1login.pushButton.clicked.connect(chama_primeiratela)
tela1login.pushButton_2.clicked.connect(cadastrar)
telacadastro.pushButton.clicked.connect(cadastrar_db)
telacadastro.pushButton_2.clicked.connect(sair_cadastro)
tela1login.pushButton_3.clicked.connect(fechar_app)
telatempo.pushButton_3.clicked.connect(fechar_temp)

tela1login.show()
app.exec()