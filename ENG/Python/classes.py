class Pedido:
    def __init__(self, idPedido, idCLiente, idMesa):
        self.__idPedido = int;
        self.__idCliente = int;
        self.__idMesa = int;
    
class Pagamento:
    def __init__(self, valor, idPedido, tipoPagamento):
        self.__valor__ = decimal;
        self.__idPedido__ = int;
        self.__tipoPagamento__= int;

class itemPedido:
    def __init__(self, idPedido, quantidade, valor, idPedido):
        self.__idPedido__= int;
        self.__quantidade__= decimal;
        self.__valor__= decimal;
        self.__idPedido__= int;

class Prato:
    def __init__(self, idIngredientes, situaçãoPrato):
        self.__idIngredientes__ = int;
        self.__situaçãoPrato__= string;

class Ingredientes:
    def __init__(self, idIngredientes, quantidade):
        self.__idIngredientes__= int;
        self.__quantidade__= decimal;

class Estoque:
    def __init__(self, idIngredientes, quatidadeMinima, quantidadeAtual, quantidadeMaxima):
        self.__idIngredientes__= int;
        self.__quantidadeMinima__= decimal;
        self.__quantidadeAtual__= decimal;
        self.__quantidadeMaxima__= decimal;

class ListaCompras:
    def __init__(self, idLista, idCompra, quantidade):
        self.__idLista__= int;
        self.__idCompra__= int;
        self.__quantidade__= decimal;

class Entrega:
    def __init__(self, idEntrega, situação):
        self.__idEntrega__ = int;
        self.__situação__= string;
