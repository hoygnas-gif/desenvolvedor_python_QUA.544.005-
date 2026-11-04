# Superclasse
class pessoa:
    def_init_(self,email, telefone):
    self.__email = email
    self.__telefone = telefone

#SECTION - set & get email   
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,email):
#SECTION - set & get telefone
    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self,telefone):
        self,__telefone = telefone


#SECTION - Classe pessoa fisica
class PessoaFisica(pessoa):
    def__init(self,nome,cpf,telefone,email):
        self.__nome = Nome
        self.__cpf = cpf
        super().__init(telefone=telefone.email=email)

#SECTION - Set & Get nome
@property
def nome(self):
    return self.nome
@nome.setter
def nome(self,nome):
    self.__nome = nome

#SECTION - Set & CPF
@property
def cpf(self):
    return self.cpf
@cpf.setter
def cpfnome(self,cpf):
    self.__cpf = cpf


    #SECTION - Classe de PF
    class PessoaJuridica(pessoa):
    def__init__(self,nome_fantasia,cpf,telefone,email):
        self.__nome_fantasia = nome_fantasia
        self.__razao_social = razao_social
        self.__cnpj = cnpj
    super().__init(telefone=telefone,email=email)
#SECTION - Set & Get nome_fantasia
@property
def nome_fantasia(self):
    return self.nome_fantasia
@nome_fantasia.setter
def nome_fantasia(self,nome_fantasia):
    self.__nome = nome_fantasia

#SECTION - Set & Get Razão social
@property
def razao_social(self):
    return self.cpf__razao_social
@razao_social.setter
def razao_social(self,razao_social):
    self.__razao_social = razao_social

#SECTION - Set & Get CNPJ
@property
def cnpj (self):
    return self.cnpj__cnpj
@cnpj.setter
def cnpj(self,razao_social):
    self.__cnpj = cnpj

