# -*- coding: utf-8 -*-
import os
from libs import menu
from libs.gps import GPS

def limpar_tela():
    os.system('clear')

def main():
    try:
        gps = GPS()
        gps.ler_mapa('mapas/rs.gml')
        origem, destino = menu.mostrar(gps.grafo)
        gps.setar_origem(origem)
        gps.setar_destino(destino)
        limpar_tela()
        gps.processar()
       
        if menu.continuar():
            limpar_tela()
            main()
        else:
            limpar_tela()
            exit()
    except Exception, e:
        print '!!!! Rota impossivel !!!! %s' % e.message
        main()

main()