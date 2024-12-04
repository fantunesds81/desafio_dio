# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input("Digite a area de atuação ('saúde','segurança pública','transporte','educação')")

# Função responsável por receber uma área de aplicação e retornar sua respectiva descrição.
def descrever_aplicacao(area):
    if area == "saúde":
        return "diagnóstico precoce e tratamento personalizado"
    elif area == "segurança pública":
        return "monitoramento e prevenção de crimes"
    elif area == "transporte":
        return "veículos autônomos e otimização de rotas"
    elif area == "educação":
        return "personalização do aprendizado e tutoria inteligente"
        
# Imprime a descrição da aplicação na área recebido na "entrada" através da função "descrever_aplicacao". 
print(descrever_aplicacao(entrada))

