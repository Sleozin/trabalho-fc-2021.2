import PySimpleGUI as sg
#armazenar os generos e a quantidade
generos = {"Acao" : 0,"Aventura" : 0,"Chanchada" : 0,"Comedia" : 0,"Comedia de acao" : 0,"Comedia de terror" : 0,"Comedia Dramatica" : 0,"Comedia Romantica" : 0,"Danca" : 0,"Documentario" : 0,"Ficção" : 0,"Drama" : 0,"Espionagem" : 0,"Faroeste" : 0,"Fantasia" : 0,"Ficção Cientifica" : 0,"Guerra" : 0,"Misterio" : 0,"Musical" : 0,"Policial" : 0,"Romance" : 0,"Terror" : 0}
#armazenar lista
with open ('generos.txt', 'a') as arquivo :
  for x in generos:
    arquivo.write(f"{x} : {generos[x]} filmes\n")
  arquivo.close()

#layout Principal
layout = [  [sg.Text("BEM VINDO !!")],
            [sg.Button('Ok'), sg.Button('Ver generos'), sg.Button('Cadastrar Filme')], 
            ]
#layout do cadastro do filme
cadastro_filme = [[sg.Text("Digite o nome do filme")],
                  [sg.Input()],
]
window = sg.Window('Window Title', layout)
evento, values = window.read()
#Ver Quantidade de flimes/genero
if evento == 'Ver generos':
  arquivo = open('generos.txt','r')
  gs = arquivo.read()
  arquivo.close()
  sg.popup_scrolled(gs)
#Chamada da tela de cadastro do filme (Incompleta)
elif evento == 'Cadastrar Filme':
  c_window = sg.Window('Window Title', cadastro_filme)
  c_evento, c_values = c_window.read()
