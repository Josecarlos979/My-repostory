import turtle
import colorsys

# Configuração da tela
tela = turtle.Screen()
tela.bgcolor("black")
tela.title("Arte com Turtle")

# Configuração da tartaruga
artista = turtle.Turtle()
artista.speed(0)
artista.width(2)
artista.hideturtle()

# Função para desenhar uma espiral multicolorida
def desenhar_espiral(raios, passos, cores):
    for i in range(passos):
        cor = colorsys.hsv_to_rgb(i / cores, 1, 1)  # Gera cores em RGB
        artista.color(cor)
        artista.forward(raios + i)
        artista.left(59)

# Definir parâmetros
raios = 10
passos = 300
cores = 360

# Executa o desenho
desenhar_espiral(raios, passos, cores)

# Mantém a tela aberta
tela.mainloop()