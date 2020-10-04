# coding: utf-8

class Loja:

  def __init__(self, nome_loja, logradouro, numero, complemento, bairro, 
               municipio, estado, cep, telefone, observacao, cnpj,
               inscricao_estadual):
    self.nome_loja = nome_loja
    self.logradouro = logradouro
    self.numero = numero
    self.complemento = complemento
    self.bairro = bairro
    self.municipio = municipio
    self.estado = estado
    self.cep = cep
    self.telefone = telefone
    self.observacao = observacao
    self.cnpj = cnpj
    self.inscricao_estadual = inscricao_estadual

def isEmpty(value: str) -> bool:
    return (value == None) or (len(value) == value.count(" "))

def dados_loja_objeto(loja):
    if (isEmpty(loja.nome_loja)):
        raise Exception("O campo nome da loja é obrigatório")

    if (isEmpty(loja.logradouro)):
        raise Exception("O campo logradouro do endereço é obrigatório")

    numero = int ()
    try:
      numero = int(loja.numero)
    except Exception:
      numero = 0

    if numero <= 0:
      numero = "s/n"

    if (isEmpty(loja.municipio)):
        raise Exception("O campo município do endereço é obrigatório")

    if (isEmpty(loja.estado)):
        raise Exception("O campo estado do endereço é obrigatório")

    if (isEmpty(loja.cnpj)):
        raise Exception("O campo CNPJ da loja é obrigatório")
  
    if (isEmpty(loja.inscricao_estadual)):
        raise Exception("O campo inscrição estadual da loja é obrigatório")

    linha2 = f"{loja.logradouro}, {numero}"
    if not isEmpty(loja.complemento):
        linha2 += f" {loja.complemento}"

    linha3 = str()
    if not isEmpty(loja.bairro):
        linha3 += f"{loja.bairro} - "
    linha3 += f"{loja.municipio} - {loja.estado}"

    linha4 = str()
    if not isEmpty(loja.cep):
        linha4 = f"CEP:{loja.cep}"
    if not isEmpty(loja.telefone):
        if not isEmpty(linha4):
            linha4 += " "
        linha4 += f"Tel {loja.telefone}"
    if not isEmpty(linha4):
        linha4 += "\n"

    linha5 = str()
    if not isEmpty(loja.observacao):
        linha5 += f"{loja.observacao}"

    output = f"{loja.nome_loja}\n"
    output += f"{linha2}\n"
    output += f"{linha3}\n"
    output += f"{linha4}"
    output += f"{linha5}\n"
    output += f"CNPJ: {loja.cnpj}\n"
    output += f"IE: {loja.inscricao_estadual}"

    return output
