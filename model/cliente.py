from sqlalchemy import Column,  Integer, String, DateTime
from datetime import datetime
from typing import Union

from  model import Base


class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column("pk_cliente", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    telefone = Column(Integer)
    bairro = Column(String(100))
    data_solicitacao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o Cliente e o comentário.
    # Essa relação é implicita, não está salva na tabela 'cliente',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.

    def __init__(self, nome:str, telefone:int, bairro:str,
                 data_solicitacao:Union[DateTime, None] = None):
        """
        Cria um Cliente

        Arguments:
            nome: nome do Cliente.
            telefone: telefone do cliente
            bairro: Bairro para entrega
            data_insercao: data de quando o cliente foi inserido à base
        """
        self.nome = nome
        self.telefone = telefone
        self.bairro = bairro

        # se não for informada, será o data exata da inserção no banco
        if data_solicitacao:
            self.data_solicitacao = data_solicitacao


