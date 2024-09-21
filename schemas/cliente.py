from pydantic import BaseModel
from typing import Optional, List
from model.cliente import Cliente


class ClienteSchema(BaseModel):
    """ Define como um novo cliente a ser inserido deve ser representado
    """
    nome: str = "José"
    telefone: int = 2199999994
    bairro: str = "Cidade de Deus"


class ClienteBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do cliente.
    """
    nome: str = "Teste"


class ListagemClientesSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    clientes:List[ClienteSchema]


def apresenta_clientes(clientes: List[Cliente]):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    result = []
    for cliente in clientes:
        result.append({
            "nome": cliente.nome,
            "telefone": cliente.telefone,
            "bairro": cliente.bairro,
        })

    return {"clientes": result}


class ClienteViewSchema(BaseModel):
    """ Define como um cliente será retornado: Cliente + comentários.
    """
    id: int = 1
    nome: str = "josé"
    telefone: int = 9
    bairro: str = "Cidade de Deus"


class ClienteDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_cliente(cliente: Cliente):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    return {
        "id": cliente.id,
        "nome": cliente.nome,
        "telefone": cliente.telefone,
        "bairro": cliente.bairro,      
    }
