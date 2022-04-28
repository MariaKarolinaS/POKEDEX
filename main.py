from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from pokemons import pokemon
import random

#   CORES
co0 = "#444466"  # PRETO
co1 = "#feffff"  # BRANCO
co2 = "#6f9fbd"  # AZUL
co3 = "#38576b"  # VALOR
co4 = "#403d3d"  # LETRA
co5 = "#ef5350"  # VERMELHO

#   ABRINDO A JANELA
janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

#   CRIANDO O FRAME
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)


def troca_pokemon(i):
    global poke_image, picpoke

    #   TROCANDO A COR DO FRAME
    frame_pokemon['bg'] = pokemon[i]['tipo'][3]

    #   TIPO DE POKEMON
    poke_nome['text'] = i
    poke_nome['bg'] = pokemon[i]['tipo'][3]
    poke_tipo['text'] = pokemon[i]['tipo'][1]
    poke_tipo['bg'] = pokemon[i]['tipo'][3]
    poke_id['text'] = pokemon[i]['tipo'][0]
    poke_id['bg'] = pokemon[i]['tipo'][3]

    picpoke = pokemon[i]['tipo'][2]

    #   PIC POKEMON

    picpoke = Image.open(picpoke)
    picpoke = picpoke.resize((238, 238))
    picpoke = ImageTk.PhotoImage(picpoke)


    poke_image = Label(frame_pokemon, image=picpoke, relief='flat', bg=pokemon[i]['tipo'][3], fg=co1)
    poke_image.place(x=60, y=50)
    poke_tipo.lift()

    #   STATUS POKEMON
    poke_hp['text'] = pokemon[i]['status'][0]
    poke_atk['text'] = pokemon[i]['status'][1]
    poke_df['text'] = pokemon[i]['status'][2]
    poke_vl['text'] = pokemon[i]['status'][3]
    poke_tl['text'] = pokemon[i]['status'][4]

    #   HABILIDADES POKEMON
    poke_hb1['text'] = pokemon[i]['habilidades'][0]
    poke_hb2['text'] = pokemon[i]['habilidades'][1]



#   CRIANDO OS LABEL'S
poke_nome = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 20'), fg=co1)
poke_nome.place(x=12, y=15)

#   CATEGORIA
poke_tipo = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
poke_tipo.place(x=12, y=50)

# ID
#   CATEGORIA
poke_id = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 8 bold'), bg=co1, fg=co1)
poke_id.place(x=12, y=75)

#   ESTATISTICAS DO POKEMON
poke_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
poke_status.place(x=15, y=310)

#   HP
poke_hp = Label(janela, text='HP: 300', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_hp.place(x=15, y=360)

#   ATAQUE
poke_atk = Label(janela, text='Ataque: 600', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_atk.place(x=15, y=385)

#   DEFESA
poke_df = Label(janela, text='Defesa: 500', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_df.place(x=15, y=410)

#   VELOCIDADE
poke_vl = Label(janela, text='Velocidade: 300', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_vl.place(x=15, y=435)

#   TOTAL
poke_tl = Label(janela, text='Total: 1700', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_tl.place(x=15, y=460)


#   HABILIDADES
poke_habilidades = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
poke_habilidades.place(x=180, y=310)

#   HP
poke_hb1 = Label(janela, text='Bola elétrica', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_hb1.place(x=195, y=360)

#   ATAQUE
poke_hb2 = Label(janela, text='Thunder', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_hb2.place(x=195, y=385)

#   BOTÕES

#   PIKACHU
pikachu_cabeca = Image.open('images/pikachu/cabeca-pikachu.png')
pikachu_cabeca = pikachu_cabeca.resize((40, 40))
pikachu_cabeca = ImageTk.PhotoImage(pikachu_cabeca)

botao_pikachu = Button(janela, command=lambda:troca_pokemon('Pikachu'), image=pikachu_cabeca, text='Pikachu',width=150 ,relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'),bg=co1, fg=co0)
botao_pikachu.place(x=375, y=10)

#   CHARMANDER
charmander_cabeca = Image.open('images/charmander/cabeca-charmander.png')
charmander_cabeca = charmander_cabeca.resize((40, 40))
charmander_cabeca = ImageTk.PhotoImage(charmander_cabeca)

botao_charmander = Button(janela, command=lambda:troca_pokemon('Charmander'), image=charmander_cabeca, text='Charmander',width=150 ,relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'),bg=co1, fg=co0)
botao_charmander.place(x=375, y=65)

#   DRAGONITE
dragonite_cabeca = Image.open('images/dragonite/cabeca-dragonite.png')
dragonite_cabeca = dragonite_cabeca.resize((40, 40))
dragonite_cabeca = ImageTk.PhotoImage(dragonite_cabeca)

botao_dragonite = Button(janela, command=lambda:troca_pokemon('Dragonite'), image=dragonite_cabeca, text='Dragonite',width=150 ,relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'),bg=co1, fg=co0)
botao_dragonite.place(x=375, y=120)

#   MEOWTH
meowth_cabeca = Image.open('images/meowth/Meowth-Cabeca2.png')
meowth_cabeca = meowth_cabeca.resize((40, 40))
meowth_cabeca = ImageTk.PhotoImage(meowth_cabeca)

botao_meowth = Button(janela, command=lambda:troca_pokemon('Meowth'), image=meowth_cabeca, text='Meowth',width=150 ,relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'),bg=co1, fg=co0)
botao_meowth.place(x=375, y=175)

#   JIGGLYPUFF
jiggly_cabeca = Image.open('images/jigglypuff/Jigglypuff-Cabeca.png')
jiggly_cabeca = jiggly_cabeca.resize((40, 40))
jiggly_cabeca = ImageTk.PhotoImage(jiggly_cabeca)

botao_jiggly = Button(janela, command=lambda:troca_pokemon('Jigglypuff'), image=jiggly_cabeca, text='Jigglypuff',width=150 ,relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'),bg=co1, fg=co0)
botao_jiggly.place(x=375, y=230)

#   BUTTERFREE
butter_cabeca = Image.open('images/butterfree/Butterfree-Cabeca2.png')
butter_cabeca = butter_cabeca.resize((40, 40))
butter_cabeca = ImageTk.PhotoImage(butter_cabeca)

botao_butter = Button(janela, command=lambda:troca_pokemon('Butterfree'), image=butter_cabeca, text='Butterfree',width=150 ,relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'),bg=co1, fg=co0)
botao_butter.place(x=375, y=285)

#   GENGAR
gengar_cabeca = Image.open('images/gengar/cabeca-gengar.png')
gengar_cabeca = gengar_cabeca.resize((40, 40))
gengar_cabeca = ImageTk.PhotoImage(gengar_cabeca)

botao_gengar = Button(janela, command=lambda:troca_pokemon('Gengar'), image=gengar_cabeca, text='Gengar',width=150 ,relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'),bg=co1, fg=co0)
botao_gengar.place(x=375, y=340)


#   BULBASAUR
bulbasaur_cabeca = Image.open('images/bulbasaur/cabeca-bulbasaur.png')
bulbasaur_cabeca = bulbasaur_cabeca.resize((40, 40))
bulbasaur_cabeca = ImageTk.PhotoImage(bulbasaur_cabeca)

botao_bulbasaur = Button(janela, command=lambda:troca_pokemon('Bulbasaur'), image=bulbasaur_cabeca, text='Bulbasaur',width=150 ,relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'),bg=co1, fg=co0)
botao_bulbasaur.place(x=375, y=395)

#   GYARADOS
gyarados_cabeca = Image.open('images/gyarados/cabeca-gyarados.png')
gyarados_cabeca = gyarados_cabeca.resize((40, 40))
gyarados_cabeca = ImageTk.PhotoImage(gyarados_cabeca)

botao_gyarados = Button(janela, command=lambda:troca_pokemon('Gyarados'), image=gyarados_cabeca, text='Gyarados',width=150 ,relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'),bg=co1, fg=co0)
botao_gyarados.place(x=375, y=450)


ListaPokemons = ['Dragonite', 'Pikachu', 'Gyarados', 'Bulbasaur', 'Butterfree', 'Gengar', 'Jigglypuff', 'Meowth', 'Charmander']
pokemon_escolhido = random.sample(ListaPokemons, 1)
troca_pokemon(pokemon_escolhido[0])

janela.mainloop()
