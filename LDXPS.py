from PyQt5 import uic,QtWidgets
import mysql.connector


banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="LDXPS"
)

def funcao_principal_cliente():
    linhaNomeCliente = tela_criar_cliente.lineEdit.text()
    linhaCodVendedor = tela_criar_cliente.lineEdit_2.text()
    linhaLimiteCred = tela_criar_cliente.lineEdit_3.text()

    print("nome cliente", linhaNomeCliente)
    print("cod vendedor", linhaCodVendedor)
    print("limite de credito", linhaLimiteCred)

    tipo_pessoa = ""

    if tela_criar_cliente.radioButton_2.isChecked():
        print("Pessoa Fisica")
        tipo_pessoa = "Pessoa Fisica"
    else:
        print("Pessoa Juridica")
        tipo_pessoa = "Pessoa Juridica"

        # cadastrar cliente no banco
        cursor = banco.cursor()
        comando_sql = "INSERT INTO cliente(NOME,id_clien_vende,limite_credito,tipo_pessoa) VALUES (%s,%s,%s,%s)"
        dados = (str(linhaNomeCliente), str(linhaCodVendedor), str(linhaLimiteCred), tipo_pessoa)
        cursor.execute(comando_sql, dados)
        banco.commit()

        tela_criar_cliente.lineEdit.setText("")
        tela_criar_cliente.lineEdit_2.setText("")
        tela_criar_cliente.lineEdit_3.setText("")


def funcao_principal_vendedor():
    linhaNomeVendedor = tela_criar_vendedor.lineEditNome.text()
    linhaDataVendedor = tela_criar_vendedor.dateEditData.text()

    print("nome", linhaNomeVendedor)
    print("data", linhaDataVendedor)

# cadastrar vendedor no banco
    cursor = banco.cursor()
    comando_sql = "INSERT INTO vendedor(NOME,data) VALUES (%s,%s)"
    dados = (str(linhaNomeVendedor), str(linhaDataVendedor))
    cursor.execute(comando_sql, dados)
    banco.commit()
    # limpar campo
    tela_criar_vendedor.lineEditNome.setText("")




def chama_tela_criar_vendedor():
    tela_criar_vendedor.show()

def chama_tela_editar_vendedor():
    tela_editar_vendedor.show()

def chama_excluir_vendedor():
    tela_excluir_vendedor.show()

def chama_tela_criar_cliente():
    tela_criar_cliente.show()

def chama_tela_editar_cliente():
    tela_editar_cliente.show()

def chama_excluir_cliente():
    tela_excluir_cliente.show()




app=QtWidgets.QApplication([])

# chama o arquivo para ser ezecutado pela função
primeira_tela=uic.loadUi("interface.ui")
#  vendedor
tela_criar_vendedor=uic.loadUi("cadastroVendedores.ui")
tela_editar_vendedor=uic.loadUi("editarVendedor.ui")
tela_excluir_vendedor=uic.loadUi("excluirVendedor.ui")
# cliente
tela_criar_cliente=uic.loadUi("cadastroClientes.ui")
tela_editar_cliente=uic.loadUi("editarClientes.ui")
tela_excluir_cliente=uic.loadUi("excluirCliente.ui")
# ação ao clicar no botão
# vendedor
primeira_tela.pushButtonVenCriar.clicked.connect(chama_tela_criar_vendedor)
primeira_tela.pushButtonVenEditar.clicked.connect(chama_tela_editar_vendedor)
primeira_tela.pushButtonVenExcluir.clicked.connect(chama_excluir_vendedor)
# cliente
primeira_tela.pushButtonClienCriar.clicked.connect(chama_tela_criar_cliente)
primeira_tela.pushButtonClienEditar.clicked.connect(chama_tela_editar_cliente)
primeira_tela.pushButtonClienExcluir.clicked.connect(chama_excluir_cliente)
primeira_tela.pushButtonSair.clicked.connect(exit)
# clik confirmar cadastro de vendedor
tela_criar_vendedor.pushButton.clicked.connect(funcao_principal_vendedor)
# clik cadastro de cliente
tela_criar_cliente.pushButtonCadastroCliente.clicked.connect(funcao_principal_cliente)



primeira_tela.show()
#tela_criar_vendedor.show()

app.exec_()

