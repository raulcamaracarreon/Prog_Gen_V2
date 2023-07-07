import streamlit as st
import random

st.title('Generador de Acordes🎶')
st.markdown('''
    ¡Bienvenido al generador de acordes. Este generador crea progresiones armónicas atractivas con solo unos pocos clics. 

    Así es como funciona:
    1. Selecciona una tonalidad.
    2. Elige cuántos acordes deseas en tu progresión.
    3. ¡Presiona 'Enter' y descubre tu propia melodía única!

    ¿Por qué siempre suena bien? Eso es un secreto que guardamos bajo siete llaves. ¡Disfruta de la música! 🎵
''')


# Define un diccionario con los acordes y los movimientos fuertes asociados.
acordes_movimientos_C = {
    'C': ['Am', 'F'],
    'Dm': ['Bdim', 'G7', 'Fm7', 'Abmaj7', 'Bbmaj7'],
    'Em': ['C', 'Am'],
    'F': ['Dm', 'Bdim'],
    'G7': ['Em', 'C'],
    'Am': ['F', 'Dm'],
    'Bdim': ['G7', 'Fm7', 'Abmaj7', 'Bbmaj7', 'Em'],
    'Fm7' : ['C', 'Em'],
    'Abmaj7': ['C', 'Em'],
    'Bbmaj7' :  ['C', 'Em']
}

acordes_movimientos_D = {
    'D': ['Bm', 'G'],
    'Em': ['C#dim', 'A7', 'Gm7', 'Bbmaj7', 'Cmaj7'],
    'F#m': ['D', 'Bm'],
    'G': ['Em', 'C#dim'],
    'A7': ['F#m', 'D'],
    'Bm': ['G', 'Em'],
    'C#dim': ['A7', 'Gm7', 'Bbmaj7', 'Cmaj7', 'F#m'],
    'Gm7' : ['D', 'F#m'],
    'Bbmaj7': ['D', 'F#m'],
    'Cmaj7' :  ['D', 'F#m']
}

acordes_movimientos_E = {
    'E': ['C#m', 'A'],
    'F#m': ['D#dim', 'B7', 'Am7', 'Cmaj7', 'Dmaj7'],
    'G#m': ['E', 'C#m'],
    'A': ['F#m', 'D#dim'],
    'B7': ['G#m', 'E'],
    'C#m': ['A', 'F#m'],
    'D#dim': ['B7', 'G#m'],
    'D#dim': ['B7', 'Am7', 'Cmaj7', 'Dmaj7', 'G#m'],
    'Am7' : ['E', 'G#m'],
    'Bbmaj7': ['E', 'G#m'],
    'Dmaj7' :  ['E', 'G#m']
}

acordes_movimientos_F = {
    'F': ['Dm', 'Bb'],
    'Gm': ['Edim', 'C7', 'Bbm7', 'Dbmaj7', 'Ebmaj7'],
    'Am': ['F', 'Dm'],
    'Bb': ['Gm', 'Edim'],
    'C7': ['Am', 'F'],
    'Dm': ['Bb', 'Gm'],
    'Edim': ['C7', 'Bbm7', 'Dbmaj7', 'Ebmaj7', 'Am'],
    'Bbm7' : ['F', 'Am'],
    'Dbmaj7': ['F', 'Am'],
    'Ebmaj7' :  ['F', 'Am']
}

acordes_movimientos_G = {
    'G': ['Em', 'C'],
    'Am': ['F#dim', 'D7', 'Cm7', 'Emaj7', 'Fmaj7'],
    'Bm': ['G', 'Em'],
    'C': ['Am', 'F#dim'],
    'D7': ['Bm', 'G'],
    'Em': ['C', 'Am'],
    'F#dim': ['D7', 'Cm7', 'Emaj7', 'Fmaj7', 'Bm'],
    'Cm7' : ['G', 'Bm'],
    'Emaj7': ['G', 'Bm'],
    'Fmaj7' :  ['G', 'Bm']
}

acordes_movimientos_A = {
    'A': ['F#m', 'D'],
    'Bm': ['G#dim', 'E7', 'Dm7', 'F#maj7', 'Gmaj7'],
    'C#m': ['A', 'F#m'],
    'D': ['Bm', 'G#dim'],
    'E7': ['C#m', 'A'],
    'F#m': ['D', 'Bm'],
    'G#dim': ['E7', 'Dm7', 'F#maj7', 'Gmaj7', 'C#m'],
    'Dm7' : ['A', 'C#m'],
    'F#maj7': ['A', 'C#m'],
    'Gmaj7' :  ['A', 'C#m']
}

acordes_movimientos_B = {
    'B': ['G#m', 'E'],
    'C#m': ['A#dim', 'F#7', 'Em7', 'G#maj7', 'Amaj7'],
    'D#m': ['B', 'G#m'],
    'E': ['C#m', 'A#dim'],
    'F#7': ['D#m', 'B'],
    'G#m': ['E', 'C#m'],
    'A#dim': ['F#7', 'Em7', 'G#maj7', 'Amaj7', 'D#m'],
    'Em7' : ['B', 'D#m'],
    'G#maj7': ['B', 'D#m'],
    'Amaj7' :  ['B', 'D#m']
}

# Define un diccionario con las tonalidades y sus respectivos diccionarios de acordes.
tonalidades = {
    'C': acordes_movimientos_C,
    'D': acordes_movimientos_D,
    'E': acordes_movimientos_E,
    'F': acordes_movimientos_F,
    'G': acordes_movimientos_G,
    'A': acordes_movimientos_A,
    'B': acordes_movimientos_B,
}

# Define un diccionario con las tonalidades y sus quintos grados asociados.
quinto_grado = {
    'C': 'G7',
    'F': 'C7',
    'G': 'D7',
    'D': 'A7',
    'E': 'B7',
    'A': 'E7',
    'B': 'F#7',
}

# Pide al usuario que elija una tonalidad y un número de acordes.
tonalidad = st.selectbox('Elige una tonalidad', list(tonalidades.keys()))
num_acordes = st.slider('Elige el número de acordes', 1, 32, 8)

# Selecciona el diccionario de movimientos armónicos correcto en función de la tonalidad elegida.
acordes_movimientos = tonalidades[tonalidad]

# Comienza la progresión en la tónica elegida.
progresion = [tonalidad]

# Para cada acorde restante en la progresión...
for i in range(num_acordes - 1):
    # Si esta es la última posición de acorde, elige el quinto grado.
    if i == num_acordes - 2:
        progresion.append(quinto_grado[tonalidad])
    else:
        # Si no, elige aleatoriamente un acorde que represente un movimiento fuerte desde el acorde actual.
        ultimo_acorde = progresion[-1]
        siguiente_acorde = random.choice(acordes_movimientos[ultimo_acorde])
        
        # Agrega el nuevo acorde a la progresión.
        progresion.append(siguiente_acorde)

# Muestra la progresión generada.
st.write("Progresión generada:")
st.write("")
progresion = '-'.join(progresion)
st.markdown(f'## **{progresion}**')

st.write("")
st.write("")
st.write("")
readme_text = """
# Generador de Acordes Mágico

El Generador de Acordes Mágico es una aplicación diseñada para crear progresiones armónicas hermosas y atractivas de una manera simple y divertida.

## ¿Cómo funciona?

La aplicación se basa en principios de composición musical, en particular, en los movimientos armónicos de los acordes. Seleccionas una tonalidad y el número de acordes que deseas en tu progresión, y la aplicación genera una progresión de acordes. 

## Los movimientos armónicos

Los movimientos armónicos son de tres clases:

1. Movimiento débil: en el cambio de un acorde tríada a otro, una o dos notas cambian, pero no se mantiene la tónica del primer acorde.

2. Movimiento medio: todas las notas cambian.

3. Movimiento fuerte: una o dos notas cambian, pero se mantiene la tónica del primer acorde.

La aplicación utiliza principalmente los movimientos fuertes para generar las progresiones de acordes. Este tipo de movimiento es frecuente en las progresiones famosas. Por ejemplo, en la secuencia C-Am-Dm-G, cada cambio de acorde implica un movimiento fuerte.

## Uso de la aplicación

Para utilizar la aplicación, sigue estos pasos:

1. Selecciona una tonalidad.
2. Elige cuántos acordes deseas en tu progresión.
3. Presiona 'Enter' y descubre tu propia melodía única.

¡Disfruta de la música!
"""

# Muestra el checkbox "Encuentra las 7 llaves"
if st.checkbox('Encuentra las 7 llaves'):
    st.markdown(readme_text, unsafe_allow_html=False)
