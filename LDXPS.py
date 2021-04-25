from PyQt5 import uic,QtWidgets


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
primeira_tela=uic.loadUi("interface.ui")
#  vendedor
tela_criar_vendedor=uic.loadUi("cadastroVendedores.ui")
tela_editar_vendedor=uic.loadUi("editarVendedor.ui")
tela_excluir_vendedor=uic.loadUi("editarVendedor.ui")
# cliente
tela_criar_cliente=uic.loadUi("cadastroClientes.ui")
tela_editar_cliente=uic.loadUi("editarClientes.ui")
tela_excluir_cliente=uic.loadUi("editarClientes.ui")

# vendedor
primeira_tela.pushButtonVenCriar.clicked.connect(chama_tela_criar_vendedor)
primeira_tela.pushButtonVenEditar.clicked.connect(chama_tela_editar_vendedor)
primeira_tela.pushButtonVenExcluir.clicked.connect(chama_excluir_vendedor)
# cliente
primeira_tela.pushButtonClienCriar.clicked.connect(chama_tela_criar_cliente)
primeira_tela.pushButtonClienEditar.clicked.connect(chama_tela_editar_cliente)
primeira_tela.pushButtonClienExcluir.clicked.connect(chama_excluir_cliente)
primeira_tela.pushButtonSair.clicked.connect(exit)


primeira_tela.pushButtonVenEditar.clicked.connect(chama_tela_editar_vendedor)



primeira_tela.show()
app.exec_()