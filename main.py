from tkinter.constants import HORIZONTAL
import PySimpleGUI as sg

# layout Principal
sg.theme("LightGrey")
layout = [  [sg.Text("BEM VINDO !!")],
            [sg.Button('Ver generos'), sg.Button('Cadastrar filme'), sg.Button('Meus filmes'), sg.Button('Sair')], 
            ]

window = sg.Window('Window Title', layout)
evento, values = window.read()

# layout do cadastro do filme
cadastro_filme = [
  [sg.Text("Nome do filme:"), sg.Input(key='titulo')],
  [sg.Combo(values=list('acão'), key='genero'), sg.Checkbox("Favorito", key='like'), sg.Checkbox("Quero assistir", key='assistir'), sg.Checkbox("Assistido", key='assistido')],
  [sg.Text("Avalie:"), sg.Slider(range=(0,10), orientation='horizontal', key="avaliacao")],
  [sg.Text("")],
  [sg.Button("Adicionar"), sg.Button("Voltar")]
]


# Chamada da tela de cadastro do filme
if evento == 'Cadastrar filme':
  c_window = sg.Window('Cadastrar filme', cadastro_filme)
  c_evento, c_values = c_window.read()

elif evento == 'Adicionar':
  # self.listarFilmes(values)
  pass


elif evento == 'Meus filmes':
  arquivo = open('listaFilmes.txt','r')
  filmes = arquivo.read()
  arquivo.close()
  sg.popup_scrolled(filmes)

# Ver Quantidade de flimes/generos
elif evento == 'Ver generos':
  arquivo = open('generos.txt','r')
  gs = arquivo.read()
  arquivo.close()
  sg.popup_scrolled(gs)


# armazenar os generos e a quantidade na biblioteca
generos = {"Acao" : 0,"Aventura" : 0,"Chanchada" : 0,"Comedia" : 0,"Comedia de acao" : 0,"Comedia de terror" : 0,"Comedia Dramatica" : 0,"Comedia Romantica" : 0,"Danca" : 0,"Documentario" : 0,"Ficção" : 0,"Drama" : 0,"Espionagem" : 0,"Faroeste" : 0,"Fantasia" : 0,"Ficção Cientifica" : 0,"Guerra" : 0,"Misterio" : 0,"Musical" : 0,"Policial" : 0,"Romance" : 0,"Terror" : 0}
# armazenar biblioteca
def armazenar():
  with open ('generos.txt', 'a') as arquivo :
    for x in generos:
      arquivo.write(f"{x} : {generos[x]} filmes\n")
    arquivo.close()


# adicionando filmes como favorito, para assistir ou assistido 
def listaFilmes(values):
  favorito = {values['like']}
  assistir = {values['assistir']}
  assistido = {values['assistido']}

  if favorito == True:
    with open ('listaFilmes.txt', 'a') as arquivo:
      arquivo.write(f"FAVORITOS\n")
      arquivo.write(f"{values['titulo']}\n\n")
    arquivo.close()

  elif assistir == True:
    with open ('listaFilmes.txt', 'a') as arquivo:
      arquivo.write(f"LISTA DE DESEJO\n")
      arquivo.write(f"{values['titulo']}\n\n")
    arquivo.close()

  elif assistido == True:
    with open ('listaFilmes.txt', 'a') as arquivo:
      arquivo.write(f"ASSISTIDOS\n")
      arquivo.write(f"{values['titulo']}\n\n")
      arquivo.write(f"Sua avaliação: {values['avaliacao']}\n\n")
    arquivo.close()

