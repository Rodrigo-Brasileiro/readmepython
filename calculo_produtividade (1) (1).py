#cadastrar uma planta; dar um numero de identificacao para a planta; salvar numeros em uma lista; input verificar planta; fornece informacoes para a planta como: quando estara pronta para a colheita umidade, luz, etc...
#Fazer as listas como histórico de ações do usuário, então toda vez que o usuário quiser ver tudo que ele fez no programa, retorna-se a lista

listaplanta = []

# Calcula quantidade total de plantas na área produtiva:
def populacao_plantas(plantas_metro_linear, area_produtiva, espacamento):
    comprimento_area = area_produtiva / (espacamento/100) #Transformar área em metros lineares: como pegar toda a área e transformar em uma só linha reta de plantação
    total_plantas = plantas_metro_linear * comprimento_area
    return total_plantas

# FUNÇÕES PARA SOJA:

# Calcula media de grãos por planta:
def media_graos(quantidade_graos, plantas_amostragem):
    numero_graos_por_planta = quantidade_graos / plantas_amostragem
    return numero_graos_por_planta

# Calcula media da quantidade de grãos por planta em gramas:
def peso_graos(numero_graos_por_planta, pmg):
    peso_graos_por_planta = numero_graos_por_planta * pmg / 1000
    return peso_graos_por_planta

# Calcula quantidade estimada de sacas de 60 kg de soja:
def estimativa_soja(peso_graos_por_planta, total_plantas):
    estimativa_sacas_soja = peso_graos_por_planta * total_plantas / 60000
    return estimativa_sacas_soja

# Função menu soja:
def soja():
    menu_soja = True

    # Dicas iniciais: 
    print('Vale lembrar que é importante que o cálculo seja feito após o enchimento dos grãos por completo (O enchimento dos grãos da cultura se dá no estágio fenológico R5).')
    print('Para realizar o cálculo com mais precisão, é necessário que: ')
    print('1 - Com o auxílio de uma trena, medir 1 metro linear no talhão, contando o número total de plantas nessa linha.')
    print('2 - Colete entre 5 e 10 plantas para amostragem, lembre-se que quanto maior a quantidade de plantas colhidas, mais precisa é a estimativa.')
    print('3 - Você precisara também de uma balança durante a última etapa da estimativa para obter o PMG (Peso de Mil Grãos)')

    # Coleta informações necessárias:
    while menu_soja == True:
        try:
            iniciar_calculo_soja = int(input('Caso esteja pronto, digite 1 para iniciar o cálculo ou 0 para voltar: '))
            if iniciar_calculo_soja == 1:
                while True:
                    try:
                        plantas_metro_linear = float(input('Digite a quantidade de plantas existente em 1 metro linear da lavoura: '))
                        if plantas_metro_linear <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print('Insira somente números acima de 0')
                        continue
                    except:
                        print('Digite apenas números positivos.')
                        continue
                while True:
                    try:
                        area_produtiva = float(input('Digite a quantidade em METROS QUADRADOS de área produtiva de sua lavoura vertical de soja: '))
                        if area_produtiva <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print('Insira somente números acima de 0')
                        continue
                    except:
                        print('Digite apenas números positivos.')
                        continue
                while True:
                    try:
                        espacamento = float(input('Digite o espaçamento entre linhas em CENTÍMETROS na área indicada anteriormente: '))
                        if espacamento <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print('Insira somente números acima de 0')
                        continue
                    except:
                        print('Digite apenas números positivos.')
                        continue
                while True:
                    try:
                        plantas_amostragem = int(input('Digite quantas plantas foram colhidas para amostragem: '))
                        if plantas_amostragem <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print('Insira somente números acima de 0')
                        continue
                    except:
                        print('Digite apenas números inteiros positivos.')
                        continue
                while True:
                    try:
                        quantidade_graos = float(input(f'Digite a quantidade de grãos produzidos por essas {plantas_amostragem} plantas colhidas para amostragem: '))
                        if quantidade_graos <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print('Insira somente números acima de 0')
                        continue
                    except:
                        print('Digite apenas números positivos.')
                        continue
                while True:
                    try:
                        pmg = float(input('Por fim, digite o PMG (Peso de Mil Grãos), utilize uma balança (é esperado que o valor obtido esteja entre 140 e 220 gramas): '))
                        if pmg <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print('Insira somente números acima de 0')
                        continue
                    except:
                        print('Digite apenas números positivos.') 
                        continue

            elif iniciar_calculo_soja == 0:
                menu_soja == False
                break

            else:
                print('Digite somente 0 ou 1!')
                continue

        except: 
            print('Digite somente 0 ou 1!')
            continue

        # Chama funções/Realiza cálculos:
        total_plantas = populacao_plantas(plantas_metro_linear, area_produtiva, espacamento)
        numero_graos_por_planta = media_graos(quantidade_graos, plantas_amostragem)
        peso_graos_por_planta = peso_graos(numero_graos_por_planta, pmg)
        estimativa_sacas_soja = estimativa_soja(peso_graos_por_planta, total_plantas)   

        # Printa resultados na tela:
        print(f'Área produtiva: {area_produtiva} metros quadrados \nPopulação total de plantas: {total_plantas} plantas \nPlantas por metro linear: {plantas_metro_linear} plantas \nQuantidade aproximada de grãos por planta: {numero_graos_por_planta} grãos \nPeso aproximado de grãos por planta: {peso_graos_por_planta} gramas \nQuantidade aproximada de soja em sacas de 60 kg: {round(estimativa_sacas_soja, 2)} sacas')


    return iniciar_calculo_soja  




# FUNÇÕES PARA FRUTÍFEROS:



# Calcula media de frutos por planta:
def media_frutos(quantidade_frutos, frutiferos_contagem):
    numero_frutos_por_planta = quantidade_frutos / frutiferos_contagem
    return numero_frutos_por_planta

# Calcula media da quantidade de frutos por planta em gramas:
def peso_frutos(numero_frutos_por_planta, pmf, numero_frutos_colhidos):
    peso_frutos_por_planta = numero_frutos_por_planta * pmf / numero_frutos_colhidos
    return peso_frutos_por_planta

# Calcula PMF (Peso Medio de Fruto)
def peso_medio_frutos(quantidade_frutos_pesagem):
    lista_pesos = [] # Cria lista para armazenar pesos dos diferentes tomates
    c = 0
    while True:
        try:
            for c in range(quantidade_frutos_pesagem):
                pesos = float(input(f'{c + 1}º fruto - Insira o peso EM GRAMAS: '))
                if pesos <= 0:
                    raise ValueError
                lista_pesos.append(pesos)
        except ValueError:
            print('Insira somente números acima de 0')
            continue
        except:
            print('Digite somente números positivos!')
            continue

        pmf = sum(lista_pesos) / len(lista_pesos) # Calcula media

        return pmf 




# Calcula quantidade estimada de caixas de 25 kg de frutos:
def estimativa_frutos(peso_frutos_por_planta, total_plantas):
    estimativa_caixas_frutos = peso_frutos_por_planta * total_plantas / 25000
    return estimativa_caixas_frutos



# Função menu tomate:

def tomate():
    menu_tomate = True

    # Dicas iniciais: 
    print('Vale lembrar que é importante que o cálculo seja feito após ou durante a fase de frutificação e desenvolvimento, quando já é possível contar quantos frutos serão gerados por cada planta.')
    print('Para realizar o cálculo com mais precisão, é necessário que: ')
    print('1 - Com o auxílio de uma trena, medir 1 metro linear na plantação, contando o número total de plantas nessa linha.')
    print('2 - Colete entre 5 e 10 tomates para pesagem, lembre-se que quanto maior a quantidade de tomates colhidos, mais precisa é a estimativa.')
    print('3 - Voce precisara tambem de uma balanca durante a ultima etapa da estimativa para obter o PMF (Peso Médio de Fruto)')

    # Coleta informações necessárias:
    while menu_tomate == True:
        try:
            iniciar_calculo_tomate = int(input('Caso esteja pronto, digite 1 para iniciar o cálculo ou 0 para voltar: '))
            if iniciar_calculo_tomate == 1:
                while True:
                    try:
                        plantas_metro_linear = float(input('Digite a quantidade de tomateiros existente em 1 metro linear da lavoura: '))
                        if plantas_metro_linear <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print('Insira somente números acima de 0')
                        continue
                    except:
                        print('Digite apenas números positivos.')
                        continue
                while True:
                    try:
                        area_produtiva = float(input('Digite a quantidade em METROS QUADRADOS de área produtiva do seu cultivo de tomates: '))
                        if area_produtiva <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print('Insira somente números acima de 0')
                        continue
                    except:
                        print('Digite apenas números positivos.')
                        continue
                while True:
                    try:
                        espacamento = float(input('Digite o espaçamento entre fileiras em CENTÍMETROS na área indicada anteriormente: '))
                        if espacamento <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print('Insira somente números acima de 0')
                        continue
                    except:
                        print('Digite apenas números positivos.')
                        continue
                while True:
                    try:
                        frutiferos_contagem = int(input('Digite quantos tomateiros foram utilizados na contagem de frutos: '))
                        if frutiferos_contagem <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print('Insira somente números acima de 0')
                        continue
                    except:
                        print('Digite apenas números inteiros positivos.')
                        continue
                while True:
                    try:
                        quantidade_frutos = float(input(f'Digite a quantidade total de tomates produzidos por esses {frutiferos_contagem} tomateiros utilizados na contagem: '))
                        if quantidade_frutos <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print('Insira somente números acima de 0')
                        continue
                    except:
                        print('Digite apenas números positivos.')
                        continue
                
                
                while True:
                    try:
                        quantidade_frutos_pesagem = int(input(f'Digite a quantidade de tomates colhidos para pesagem como solicitado anteriormente: '))
                        if quantidade_frutos_pesagem <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print('Insira somente números acima de 0')
                        continue
                    except:
                        print('Digite apenas números inteiros positivos.')
                        continue
                
                print('Agora sera necessario que voce informe o peso de um tomate por vez EM GRAMAS!.')

                pmf = peso_medio_frutos(quantidade_frutos_pesagem)
                    
            elif iniciar_calculo_tomate == 0:
                menu_tomate == False
                break

            else:
                print('Digite somente 0 ou 1!')
                continue

        except: 
            print('Digite somente 0 ou 1!')
            continue

        # Chama funções/Realiza cálculos:
        total_tomateiros = populacao_plantas(plantas_metro_linear, area_produtiva, espacamento)
        numero_tomates_por_planta = media_frutos(quantidade_frutos, frutiferos_contagem)
        peso_tomates_por_planta = peso_frutos(numero_tomates_por_planta, pmf, quantidade_frutos)
        estimativa_caixas_tomates = estimativa_frutos(peso_tomates_por_planta, total_tomateiros)   

        # Printa resultados na tela:
        print(f'Área produtiva: {area_produtiva} metros quadrados \nPopulação total de tomateiros: {total_tomateiros} tomateiros \nTomateiros por metro linear: {plantas_metro_linear} tomateiros \nQuantidade aproximada de tomates por planta: {numero_tomates_por_planta} tomates \nPeso Medio de Fruto (PMF): {pmf} grmas \nPeso aproximado de tomates por planta: {peso_tomates_por_planta} gramas \nQuantidade aproximada de tomates em caixas de 25 kg: {round(estimativa_caixas_tomates, 2)} caixas')


    return iniciar_calculo_tomate  



# Função menu morangos:

def morango():
    menu_morango = True

    # Dicas iniciais: 
    print('Vale lembrar que é importante que o cálculo seja feito após ou durante a fase de frutificação e desenvolvimento, quando já é possível contar quantos frutos serão gerados por cada planta.')
    print('Para realizar o cálculo com mais precisão, é necessário que: ')
    print('1 - Com o auxílio de uma trena, medir 1 metro linear na plantação, contando o número total de plantas nessa linha.')
    print('2 - Colete entre 5 e 10 morangos para pesagem, lembre-se que quanto maior a quantidade de morangos colhidos, mais precisa é a estimativa.')
    print('3 - Você precisara também de uma balança durante a última etapa da estimativa para obter o PMF (Peso Médio de Fruto)')

    # Coleta informações necessárias:
    while menu_morango == True:
        try:
            iniciar_calculo_morango = int(input('Caso esteja pronto, digite 1 para iniciar o cálculo ou 0 para voltar: '))
            if iniciar_calculo_morango == 1:
                while True:
                    try:
                        plantas_metro_linear = float(input('Digite a quantidade de fragarias existente em 1 metro linear da lavoura: '))
                        if plantas_metro_linear <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print('Insira somente números acima de 0')
                        continue
                    except:
                        print('Digite apenas números positivos.')
                        continue
                while True:
                    try:
                        area_produtiva = float(input('Digite a quantidade em METROS QUADRADOS de área produtiva do seu cultivo de morangos: '))
                        if area_produtiva <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print('Insira somente números acima de 0')
                        continue
                    except:
                        print('Digite apenas números positivos.')
                        continue
                while True:
                    try:
                        espacamento = float(input('Digite o espaçamento entre fileiras em CENTÍMETROS na área indicada anteriormente: '))
                        if espacamento <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print('Insira somente números acima de 0')
                        continue
                    except:
                        print('Digite apenas números positivos.')
                        continue
                while True:
                    try:
                        frutiferos_contagem = int(input('Digite quantas fragarias foram utilizados na contagem de frutos: '))
                        if frutiferos_contagem <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print('Insira somente números acima de 0')
                        continue
                    except:
                        print('Digite apenas números inteiros positivos.')
                        continue
                while True:
                    try:
                        quantidade_frutos = float(input(f'Digite a quantidade total de morangos produzidos por essas {frutiferos_contagem} fragarias utilizadas na contagem: '))
                        if quantidade_frutos <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print('Insira somente números acima de 0')
                        continue
                    except:
                        print('Digite apenas números positivos.')
                        continue
                
                
                while True:
                    try:
                        quantidade_frutos_pesagem = int(input(f'Digite a quantidade de morangos colhidos para pesagem (como solicitado anteriormente): '))
                        if quantidade_frutos_pesagem <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print('Insira somente números acima de 0')
                        continue
                    except:
                        print('Digite apenas números inteiros positivos.')
                        continue
                
                print('Agora sera necessário que você informe o peso de um morango por vez EM GRAMAS!.')

                pmf = peso_medio_frutos(quantidade_frutos_pesagem)
                    
            elif iniciar_calculo_morango == 0:
                menu_morango = False
                break

            else:
                print('Digite somente 0 ou 1!')
                continue

        except: 
            print('Digite somente 0 ou 1!')
            continue

        # Chama funções/Realiza cálculos:
        total_fragarias = populacao_plantas(plantas_metro_linear, area_produtiva, espacamento)
        numero_morango_por_planta = media_frutos(quantidade_frutos, frutiferos_contagem)
        peso_morango_por_planta = peso_frutos(numero_morango_por_planta, pmf, quantidade_frutos)
        estimativa_caixas_morango = estimativa_frutos(peso_morango_por_planta, total_fragarias)   

        # Printa resultados na tela:
        print(f'Área produtiva: {area_produtiva} metros quadrados \nPopulação total de fragarias: {total_fragarias} fragarias \nFragarias por metro linear: {plantas_metro_linear} fragarias \nQuantidade aproximada de morangos por planta: {numero_morango_por_planta} morangos \nPeso Medio de Fruto (PMF): {pmf} grmas \nPeso aproximado de morangos por planta: {peso_morango_por_planta} gramas \nQuantidade aproximada de morangos em caixas de 25 kg: {round(estimativa_caixas_morango, 2)} caixas')


    return iniciar_calculo_morango  










# Menu principal:

executar_programa = True

while executar_programa:
    menu = True
    print('Seja bem-vindo!')
    while menu:
        try:
            print('MENU PRINCIPAL')
            print('0 - Finalizar programa')
            print('1 - Calcular estimativa da produtividade da lavoura vertical de soja')
            print('2 - Calcular estimativa da produtividade da lavoura vertical de tomates')
            print('3 - Calcular estimativa da produtividade da lavoura vertical de morangos')
            print("4 - Para verificar seu histórico de ações no programa")
            menu_principal = int(input('Escolha uma das opções acima: '))
            if menu_principal == 1:
                menu_soja1 = True
                while menu_soja1:
                    iniciar_calculo_soja = soja()
                    listaplanta.append("Calculo da soja") # Adiciona a lista listaplanta a soja
                    if iniciar_calculo_soja == 0:
                        break
                    else:
                        while True:
                            try:
                                menu_soja2 = int(input('Digite 1 para calcular a estimativa novamente ou 0 para retornar ao menu principal: '))
                                if menu_soja2 == 1:
                                    break
                                elif menu_soja2 == 0:
                                    menu_soja1 = False
                                    break
                                else: 
                                    print('Digite somente 0 ou 1!')
                                    continue
                            except:
                                print('Digite somente 0 ou 1!')
                                continue
            elif menu_principal == 2:
                menu_tomate1 = True
                while menu_tomate1:
                    iniciar_calculo_tomate = tomate()
                    listaplanta.append("Calculo de tomate") # Adiciona a lista listaplanta o tomate
                    if iniciar_calculo_tomate == 0:
                        break
                    else:
                        while True:
                            try:
                                menu_tomate2 = int(input('Digite 1 para calcular a estimativa novamente ou 0 para retornar ao menu principal: '))
                                if menu_tomate2 == 1:
                                    break
                                elif menu_tomate2 == 0:
                                    menu_tomate1 = False
                                    break
                                else: 
                                    print('Digite somente 0 ou 1!')
                                    continue
                            except:
                                print('Digite somente 0 ou 1!')
                                continue
            elif menu_principal == 3:
                menu_morango1 = True
                while menu_morango1:
                    iniciar_calculo_morango = morango()
                    listaplanta.append("Calculo de morango") # Adiciona a lista listaplanta o morango
                    if iniciar_calculo_morango == 0:
                        break
                    else:
                        while True:
                            try:
                                menu_morango2 = int(input('Digite 1 para calcular a estimativa novamente ou 0 para retornar ao menu principal: '))
                                if menu_morango2 == 1:
                                    break
                                elif menu_morango2 == 0:
                                    menu_morango1 = False
                                    break
                                else:
                                    print('Digite somente 0 ou 1!')
                                    continue
                            except:
                                print('Digite somente 0 ou 1')
                                continue
            # Opção de visualizar o histórico: 
            elif menu_principal ==  4:
                while True:
                    if(listaplanta == []):
                        print("Você não realizou nenhuma ação, além de tentar visualizar seu histórico de ações")
                    else:
                        resultado = ', '.join(listaplanta)
                        print(f"Obrigado por utilizar o programa, suas ações foram: {resultado}")
                    try:
                        menu_log = int(input('Digite 0 para voltar ao Menu Principal: '))
                        if menu_log == 0:
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print('Digite somente 0!')
                        continue
                    except:
                        print('Digite somente 0!')
                        continue

            elif menu_principal ==  0:
                print('Programa finalizado')
                executar_programa = False
                break
            else:
                print('Digite somente 0, 1 ou 2!')
                continue
        except:
            print('Digite somente 0, 1 ou 2!')
            continue



            