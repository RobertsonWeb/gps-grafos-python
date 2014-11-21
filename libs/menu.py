# -*- coding: utf-8 -*-

def mostrar(grafo):
    print '================================ GPS ================================'
    print '=                                                                   ='
    print '=                        DESTINOS POSSÍVEIS                         ='
    print '====================================================================='

    for n,d in grafo.nodes_iter(data=True):
        print '%s - %s' % (n, d['label'])

    origem, destino = False, False

    while not origem:
        origem = raw_input(u'Informe o codigo da cidade origem: ')

    while not destino:
        destino = raw_input(u'Informe o codigo da cidade destino: ')

    return origem, destino

    print '===================================================================='


def continuar():
    print '================================ GPS ================================'
    print '=         Calculo de rota terminado, continuar no sistema?          ='
    print '====================================================================='
    opcao = ''
    while opcao != 'S' and opcao != 'N':
       opcao = raw_input(u'(S) Sim (N) Nao: ').upper()
    if opcao == 'S':
        return True
    return False
