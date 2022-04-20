import math
from tkinter import *
from pygame import mixer

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TEMPO_CAMINHADA = 1.25
TEMPO_EXERCICIOS = 0.35
contador_inicio = 0
marca = ""
cronometro = NONE

mixer.init()


# ---------------------------- RESETAR CRONOMETRO MECANISMO ------------------------------- #


def resetar_cronometro():
	global contador_inicio, marca
	tela.after_cancel(cronometro)
	mixer.music.stop()
	canvas.itemconfig(tempo_texto, text="00:00")
	informacao.configure(padx=0, text="CRONÔMETRO", font=(FONT_NAME, 34, "bold"), bg=GREEN, fg=RED)
	marca = ""
	check.configure(text=marca)
	contador_inicio = 0


# ---------------------------- INICIAR CRONOMETRO MECANISMO ------------------------------- #


def iniciar_cronometro():
	global contador_inicio
	contador_inicio += 1
	if contador_inicio % 2 != 0:
		mixer.music.load("hora-da-caminhada.mp3")
		mixer.music.play()
		informacao.configure(padx=25, pady=0, text="CAMINHAR", font=(FONT_NAME, 35, "bold"), fg="green")
		contagem_regressiva(TEMPO_CAMINHADA * 60)
	elif contador_inicio % 2 == 0:
		mixer.music.load("hora-do-show.mp3")
		mixer.music.play()
		informacao.configure(pady=0, padx=10, text="EXERCITAR", font=(FONT_NAME, 35, "bold"), fg=RED)
		contagem_regressiva(TEMPO_EXERCICIOS * 60)


# ---------------------------- CONTAGEM REGRESSIVA MECANISMO ------------------------------- #

def contagem_regressiva(contador):
	conta_minutos = math.floor(contador / 60)
	conta_segundos = int(contador % 60)
	if conta_minutos <= 9:
		conta_minutos = f"0{conta_minutos}"
	if conta_segundos <= 9:
		conta_segundos = f"0{conta_segundos}"
	canvas.itemconfig(tempo_texto, text=f"{conta_minutos}:{conta_segundos}")
	if contador > 0:
		global cronometro
		cronometro = tela.after(1000, contagem_regressiva, contador - 1)
	elif contador == 0:
		if contador_inicio % 2 != 0:
			global marca
			marca += "✔"
			check.configure(text=marca)
		iniciar_cronometro()


# ---------------------------- INTERFACE GRÁFICA ------------------------------- #

# Configurações de tela
tela = Tk()
tela.title("Cronômetro")
tela.configure(padx=100, pady=100, bg=GREEN)
tela.minsize(width=700, height=560)
tela.maxsize(width=700, height=560)

# Componente de Texto
informacao = Label(text="CRONÔMETRO", font=(FONT_NAME, 34, "bold"), bg=GREEN, fg=RED)
informacao.grid(row=0, column=1)

# Componente de imagem e texto
canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
imagem_tomate = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=imagem_tomate)
tempo_texto = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Componente botão Iniciar
botao_inicio = Button(text="Iniciar", bg=RED, fg="white", font=FONT_NAME, command=iniciar_cronometro)
botao_inicio.configure(padx=10, pady=5)
botao_inicio.grid(row=2, column=0)

# Componente de Texto
check = Label(font=(FONT_NAME, 20, "bold"), bg=GREEN, fg="green")
check.grid(row=3, column=1)

# Componente botão Resetar
botao_resetar = Button(text="Resetar", bg=RED, fg="white", font=FONT_NAME, command=resetar_cronometro)
botao_resetar.configure(padx=10, pady=5)
botao_resetar.grid(row=2, column=2)

tela.mainloop()
