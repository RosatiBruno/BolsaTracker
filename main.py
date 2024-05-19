import yfinance as yf
import pandas as pd  #P/ poder converter a data

while True :

    acao = input("Digite qual Ação do Brasil deseja buscar (Ex: KLBN3, ITSA4, TAEE11): ")

    dataInicial = input("\nDigite a data inicial a partir da qual deseja verificar os dividendos (no formato DD/MM/AAAA). \nDeixe em branco para obter o máximo de informações disponíveis: ")
    print("")

    if dataInicial == "" :                  #Caso a data esteja em branco, atribui essa data p/ pegar todas as informações
        dataInicial = "01/01/1700"

    def converterDataParaPadraoBr(dataStr) :
        return pd.to_datetime(dataStr, format='%d/%m/%Y').strftime('%Y-%m-%d')


    dataInicial = converterDataParaPadraoBr(dataInicial)

    informacoes = yf.Ticker(acao + ".sa")
    informacoes = informacoes.dividends.loc[dataInicial:]

    for date, value in informacoes.items() :
        dataSemHoras = date.date()                                                #Obtém somente as datas, sem as horas
        print(f"Data: {dataSemHoras.strftime('%d/%m/%Y')}, Dividendo: {value}")   #Exibe a hora em padrão BR e os dividendos

    while True :
        try :
            respostaVerificarMais = input("\nDeseja verificar mais ações? (S/N): ")

            if (respostaVerificarMais.lower() == "n") :
                break

            elif (respostaVerificarMais.lower() == "s") :
                break

        except ValueError :
            print("Opção Inválida! Digite novamente!")

    if (respostaVerificarMais.lower() == "n") :
        break