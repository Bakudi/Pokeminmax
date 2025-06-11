import tkinter as tk
from PIL import Image, ImageTk
import os
import unicodedata

from estructuras import Entrenador
from combate import turno
from minimax import elegir_mejor_ataque
from pokemon import POKEMONES

# 🎨 Estilo tipo Pokémon clásico
FUENTE_TITULO = ("Press Start 2P", 36, "bold")
FUENTE_NORMAL = ("Press Start 2P", 16)
FONDO_VENTANA = "#7EC8E3"
FONDO_BATALLA = "#F8F8F8"
COLOR_TEXTO = "black"
COLOR_BOTON = "#FFD700"
COLOR_BOTON_TEXTO = "black"

class JuegoPokemon:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokeminmax")
        self.root.geometry("700x500")
        self.root.resizable(False, False)
        self.root.configure(bg=FONDO_VENTANA)
        self.frame_actual = None
        self.pantalla_inicio()

    def pantalla_inicio(self):
        self._limpiar_pantalla()
        self.frame_inicio = tk.Frame(self.root, bg=FONDO_VENTANA)
        self.frame_inicio.place(relx=0.5, rely=0.5, anchor="center")

        titulo = tk.Label(self.frame_inicio, text="Pokeminmax", font=FUENTE_TITULO,
                          bg=FONDO_VENTANA, fg=COLOR_TEXTO)
        titulo.pack(pady=40)

        boton_start = tk.Button(
            self.frame_inicio, text="Start", font=FUENTE_NORMAL, width=15,
            bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, command=self.pantalla_seleccion_equipos
        )
        boton_start.pack()
        self.frame_actual = self.frame_inicio

    def pantalla_seleccion_equipos(self):
        self._limpiar_pantalla()

        self.nombres_pokemon = list(POKEMONES.keys())
        self.indice_actual = 0
        self.seleccion_jugador = []
        self.seleccion_ia = []
        self.seleccion_actual = []

        self.fase = "jugador"
        self.pokemon_num = 1

        self.frame_seleccion = tk.Frame(self.root, bg=FONDO_VENTANA)
        self.frame_seleccion.place(relx=0.5, rely=0.5, anchor="center")

        self.titulo_seleccion = tk.Label(self.frame_seleccion, text="Selecciona tu Pokémon 1",
                                         font=FUENTE_NORMAL, bg=FONDO_VENTANA, fg=COLOR_TEXTO)
        self.titulo_seleccion.pack(pady=(10, 10))

        # Imagen del Pokémon
        self.label_imagen = tk.Label(self.frame_seleccion, bg=FONDO_VENTANA)
        self.label_imagen.pack(pady=(0, 10))
        self._mostrar_imagen_pokemon(self.nombres_pokemon[self.indice_actual])

        self.label_pokemon = tk.Label(self.frame_seleccion,
                                      text=self.nombres_pokemon[self.indice_actual],
                                      font=FUENTE_NORMAL,
                                      bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                                      width=15, height=2, relief="raised", bd=3)
        self.label_pokemon.pack(pady=10)

        botones_frame = tk.Frame(self.frame_seleccion, bg=FONDO_VENTANA)
        botones_frame.pack()

        self.btn_up = tk.Button(botones_frame, text="⬆", font=FUENTE_NORMAL,
                                width=5, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                                command=lambda: self.cambiar_pokemon(-1))
        self.btn_up.grid(row=0, column=0, padx=10)

        self.btn_down = tk.Button(botones_frame, text="⬇", font=FUENTE_NORMAL,
                                  width=5, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                                  command=lambda: self.cambiar_pokemon(1))
        self.btn_down.grid(row=0, column=1, padx=10)

        self.btn_confirmar = tk.Button(self.frame_seleccion, text="Confirmar",
                                       font=FUENTE_NORMAL, bg=COLOR_BOTON,
                                       fg=COLOR_BOTON_TEXTO, command=self.confirmar_pokemon,
                                       width=15, height=1, relief="raised", bd=3)
        self.btn_confirmar.pack(pady=20)

        self.frame_actual = self.frame_seleccion

    def _formatear_nombre_archivo(self, nombre):
        nombre = unicodedata.normalize('NFD', nombre).encode('ascii', 'ignore').decode('utf-8')
        return nombre.lower().replace(" ", "_").replace(".", "")

    def _mostrar_imagen_pokemon(self, nombre):
        nombre_archivo = self._formatear_nombre_archivo(nombre)
        base_dir = os.path.dirname(__file__)  # src/
        ruta = os.path.join(base_dir, "..", "imagenes", f"{nombre_archivo}.png")
        ruta = os.path.abspath(ruta)

        if os.path.exists(ruta):
            img = Image.open(ruta)
            img = img.resize((150, 150), Image.Resampling.LANCZOS)
            self.imagen_pokemon = ImageTk.PhotoImage(img)
            self.label_imagen.config(image=self.imagen_pokemon, text="")
            self.label_imagen.image = self.imagen_pokemon
        else:
            self.label_imagen.config(image="", text="Sin imagen")

    def cambiar_pokemon(self, delta):
        self.indice_actual = (self.indice_actual + delta) % len(self.nombres_pokemon)
        nuevo_nombre = self.nombres_pokemon[self.indice_actual]
        self.label_pokemon.config(text=nuevo_nombre)
        self._mostrar_imagen_pokemon(nuevo_nombre)

    def confirmar_pokemon(self):
        seleccionado = self.nombres_pokemon[self.indice_actual]
        self.seleccion_actual.append(POKEMONES[seleccionado])

        if self.pokemon_num < 4:
            self.pokemon_num += 1
            self.titulo_seleccion.config(
                text=f"Selecciona tu Pokémon {self.pokemon_num}" if self.fase == "jugador"
                     else f"Selecciona Pokémon de IA {self.pokemon_num}")
        else:
            if self.fase == "jugador":
                self.seleccion_jugador = self.seleccion_actual.copy()
                self.fase = "ia"
                self.pokemon_num = 1
                self.seleccion_actual.clear()
                self.titulo_seleccion.config(text="Selecciona Pokémon de IA 1")
            else:
                self.seleccion_ia = self.seleccion_actual.copy()
                self.iniciar_combate()
                return

        self.indice_actual = 0
        self.label_pokemon.config(text=self.nombres_pokemon[self.indice_actual])
        self._mostrar_imagen_pokemon(self.nombres_pokemon[self.indice_actual])

    def iniciar_combate(self):
        self._limpiar_pantalla()

        self.jugador = Entrenador("Jugador", self.seleccion_jugador)
        self.ia = Entrenador("IA", self.seleccion_ia)

        self.pj = self.jugador.pokemon_activo()
        self.ia_poke = self.ia.pokemon_activo()

        self.frame_combate = tk.Frame(self.root, bg=FONDO_BATALLA)
        self.frame_combate.place(relx=0.5, rely=0.5, anchor="center")

        self.label_estado = tk.Label(
            self.frame_combate, text="", font=FUENTE_NORMAL,
            bg=FONDO_BATALLA, fg=COLOR_TEXTO
        )
        self.label_estado.pack(pady=20)

        self.botonera = tk.Frame(self.frame_combate, bg=FONDO_BATALLA)
        self.botonera.pack()

        self.actualizar_interfaz()
        self.frame_actual = self.frame_combate

    def actualizar_interfaz(self):
        estado = f"{self.pj.nombre}: {self.pj.ps} PS\n{self.ia_poke.nombre}: {self.ia_poke.ps} PS"
        self.label_estado.config(text=estado)

        for widget in self.botonera.winfo_children():
            widget.destroy()

        if self.pj.ps <= 0:
            self.label_estado.config(text="¡Tu Pokémon fue derrotado! La IA gana.")
            return
        elif self.ia_poke.ps <= 0:
            self.label_estado.config(text="¡Has ganado el combate!")
            return

        for ataque in self.pj.ataques:
            btn = tk.Button(
                self.botonera, text=ataque.nombre, font=FUENTE_NORMAL,
                width=20, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                command=lambda atk=ataque: self.turno_completo(atk)
            )
            btn.pack(pady=3)

    def turno_completo(self, ataque_jugador):
        turno(self.pj, self.ia_poke, ataque_jugador)
        if self.ia_poke.ps <= 0:
            self.actualizar_interfaz()
            return

        ataque_ia = elegir_mejor_ataque(self.ia_poke, self.pj)
        turno(self.ia_poke, self.pj, ataque_ia)
        self.actualizar_interfaz()

    def _limpiar_pantalla(self):
        if self.frame_actual:
            self.frame_actual.destroy()
        for widget in self.root.winfo_children():
            widget.pack_forget()


if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoPokemon(root)
    root.mainloop()
