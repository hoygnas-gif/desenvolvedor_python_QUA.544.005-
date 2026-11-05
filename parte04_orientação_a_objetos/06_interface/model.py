#importa abstração
from abc import ABC,abstractclassmethod

# CRIANDO INTERFACE/ Classe abstrata
class IConta(ABC):
    @abstractclassmethod
    def consultar_conta(self):
        pass

    @abstractclassmethod
    def depositar(self,valor):
        pass

    @abstractclassmethod
    def sacar (self):
        pass


# Classe Conta
class Conta(IConta):
    def __init__(self,titular,cpf,agencia,n_conta,saldo):
        self._titular = titular
        self._cpf = cpf 
        self._agencia = agencia
        self._n_conta = n_conta
        self._saldo = saldo

        @property
        def titular(self):
             return.self_titular
    
        @titular.setter
        def titular(self,titular):
            self._titular = titular
     
        @property
        def cpf(self):
            return.self_cpf

        @cpf.setter
        def _cpf(self,cpf):
            self._cpf = cpf

    
        @property
        def agencia(self):
            return.self_agencia
        
        @agencia.setter
        def _agencia(self):
            self._agencia = agencia

        @property
          n_conta  def agencia(self):
            return.self_agencia
                
        @agencia.setter
        def _agencia(self):
            self._agencia = agencia
#TODO: terminar 06/11/2026
