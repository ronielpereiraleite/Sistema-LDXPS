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


    if tela_criar_cliente.radioButtonJuridica.isChecked():
        print("Pessoa Juridica")
        tipo_pessoa = "Juridica"

    if tela_criar_cliente.radioButton_2.isChecked():
            print("Pessoa Fisica")
            tipo_pessoa = "Fisica"

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


def visualizar_clientes():
    cursor = banco.cursor()
    comando_sql = "SELECT * FROM cliente"
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()
    print(dados_lidos)


    print(len(dados_lidos))

    primeira_tela.tableWidget.setRowCount(len(dados_lidos))
    primeira_tela.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            primeira_tela.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))



def visualizar_vendedores():
    cursor = banco.cursor()
    comando_sql = "SELECT * FROM vendedor"
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()
    print(dados_lidos)

    print(len(dados_lidos))

    primeira_tela.tableWidget.setRowCount(len(dados_lidos))
    primeira_tela.tableWidget.setColumnCount(3)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
            primeira_tela.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def excluir_vendedor():
    linha = primeira_tela.tableWidget.currentRow()
    primeira_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM vendedor")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]

    cursor.execute("DELETE FROM vendedor WHERE id="+ str(valor_id))




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
# chama o arquivo para ser ezecutado pela fun????o
primeira_tela=uic.loadUi("interface.ui")
#tela_principal=uic.loadUi("interface.ui")
#  vendedor
tela_criar_vendedor=uic.loadUi("cadastroVendedores.ui")
tela_editar_vendedor=uic.loadUi("editarVendedor.ui")
tela_excluir_vendedor=uic.loadUi("excluirVendedor.ui")
# cliente
tela_criar_cliente=uic.loadUi("cadastroClientes.ui")
tela_editar_cliente=uic.loadUi("editarClientes.ui")
tela_excluir_cliente=uic.loadUi("excluirCliente.ui")
# a????o ao clicar no bot??o
# vendedor
primeira_tela.pushButtonVenCriar.clicked.connect(chama_tela_criar_vendedor)
primeira_tela.pushButtonVenEditar.clicked.connect(chama_tela_editar_vendedor)
# primeira_tela.pushButtonVenExcluir.clicked.connect(chama_excluir_vendedor)
# cliente
primeira_tela.pushButtonClienCriar.clicked.connect(chama_tela_criar_cliente)
primeira_tela.pushButtonClienEditar.clicked.connect(chama_tela_editar_cliente)
#primeira_tela.pushButtonClienExcluir.clicked.connect(chama_excluir_cliente)
primeira_tela.pushButtonSair.clicked.connect(exit)
# clik confirmar cadastro de vendedor
tela_criar_vendedor.pushButton.clicked.connect(funcao_principal_vendedor)
# clik cadastro de cliente
tela_criar_cliente.pushButtonCadastroCliente.clicked.connect(funcao_principal_cliente)
# bot??o visualizar vendedor
primeira_tela.pushButtonVenVisualizar.clicked.connect(visualizar_vendedores)
# bot??o visualizar cliente
primeira_tela.pushButtonClienVisualizar.clicked.connect(visualizar_clientes)
# excluir dados da tabela
primeira_tela.pushButtonClienExcluir.clicked.connect(excluir_vendedor)




"""cursor = banco.cursor()
comando_SQL = "SELECT * FROM vendedor"
cursor.execute(comando_SQL)
dados_lidos = cursor.fetchall()
print(dados_lidos)"""

primeira_tela.show()

app.exec()

