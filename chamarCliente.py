from PyQt5 import uic,QtWidgets

def chama_tela_criar_cliente():
    tela_criar_cliente.show()
    linha_nome = tela_criar_cliente.lineEditNome.text()
    print("teste")
    print('nome', linha_nome)


app2=QtWidgets.QApplication([])
primeira_tela=uic.loadUi("interface.ui")
tela_cadastrar_vendedor=uic.loadUi("cadastroVendedores.ui")

tela_criar_cliente=uic.loadUi("cadastroClientes.ui")

tela_cadastrar_vendedor.pushButtonClienCadastro.clicked.connect(chama_tela_criar_cliente)


#def funcao_principal():
 #   linha_nome = tela_criar_cliente.lineEditNome.text()
  #  print("teste")
   # print('nome', linha_nome)


tela_cadastrar_vendedor.show()
app2.exec_()