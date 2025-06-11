import tkinter as tk
from PIL import Image, ImageTk
import os
import unicodedata

from estructuras import Entrenador
from combate import turno, calcular_danio
from minimax import elegir_mejor_ataque
from pokemon import POKEMONES

# 🎨 Estilo tipo Pokémon clásico
FUENTE_TITULO = ("Press Start 2P", 36, "bold")
FUENTE_NORMAL = ("Press Start 2P", 12)
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

    def _mostrar_imagen_pokemon(self, nombre, para_combate=False):
        nombre_archivo = self._formatear_nombre_archivo(nombre)
        base_dir = os.path.dirname(__file__)
        ruta = os.path.join(base_dir, "..", "imagenes", f"{nombre_archivo}.png")
        ruta = os.path.abspath(ruta)
        if os.path.exists(ruta):
            img = Image.open(ruta).resize((150, 150), Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
        return None

    def cambiar_pokemon(self, delta):
        self.indice_actual = (self.indice_actual + delta) % len(self.nombres_pokemon)
        nuevo_nombre = self.nombres_pokemon[self.indice_actual]
        self.label_pokemon.config(text=nuevo_nombre)
        img = self._mostrar_imagen_pokemon(nuevo_nombre)
        if img:
            self.label_imagen.config(image=img, text="")
            self.label_imagen.image = img

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
        self.cambiar_pokemon(0)

    def iniciar_combate(self):
        self._limpiar_pantalla()
        self.jugador = Entrenador("Jugador", self.seleccion_jugador)
        self.ia = Entrenador("IA", self.seleccion_ia)
        self.pj = self.jugador.pokemon_activo()
        self.ia_poke = self.ia.pokemon_activo()

        self.frame_combate = tk.Frame(self.root, bg=FONDO_BATALLA)
        self.frame_combate.pack(fill="both", expand=True)

        self.label_turno = tk.Label(self.frame_combate, text="Es tu turno para atacar", font=FUENTE_NORMAL,
                                    bg=FONDO_BATALLA, fg=COLOR_TEXTO)
        self.label_turno.pack(pady=5)

        self.canvas_combate = tk.Frame(self.frame_combate, bg=FONDO_BATALLA)
        self.canvas_combate.place(relx=0.5, rely=0.4, anchor="center")

        self.img_jugador_label = tk.Label(self.canvas_combate, bg=FONDO_BATALLA)
        self.img_jugador_label.grid(row=1, column=0, padx=50)
        self.img_ia_label = tk.Label(self.canvas_combate, bg=FONDO_BATALLA)
        self.img_ia_label.grid(row=1, column=1, padx=50)

        self.info_jugador = tk.Label(self.canvas_combate, font=("Press Start 2P", 8), bg=FONDO_BATALLA, fg=COLOR_TEXTO)
        self.info_jugador.grid(row=0, column=0)

        self.info_ia = tk.Label(self.canvas_combate, font=("Press Start 2P", 8), bg=FONDO_BATALLA, fg=COLOR_TEXTO)
        self.info_ia.grid(row=0, column=1)

        self.botonera = tk.Frame(self.frame_combate, bg=FONDO_BATALLA)
        self.botonera.pack(side="bottom", pady=10)

        self.actualizar_interfaz()

    def actualizar_interfaz(self):
        self.info_jugador.config(text=f"{self.pj.nombre} - {self.pj.ps} PS")
        self.info_ia.config(text=f"{self.ia_poke.nombre} - {self.ia_poke.ps} PS")

        img_jug = self._mostrar_imagen_pokemon(self.pj.nombre, True)
        img_ia = self._mostrar_imagen_pokemon(self.ia_poke.nombre, True)
        self.img_jugador_label.config(image=img_jug)
        self.img_jugador_label.image = img_jug
        self.img_ia_label.config(image=img_ia)
        self.img_ia_label.image = img_ia

        for widget in self.botonera.winfo_children():
            widget.destroy()

        if not self.jugador.tiene_pokemon_vivo():
            self.mostrar_equipo_final(self.ia.pokemones, "IA")
            return
        if not self.ia.tiene_pokemon_vivo():
            self.mostrar_equipo_final(self.jugador.pokemones, "Jugador")
            return

        for ataque in self.pj.ataques:
            danio = calcular_danio(self.pj, ataque, self.ia_poke)
            btn = tk.Button(self.botonera,
                            text=f"{ataque.nombre}\n({danio} PS)",
                            font=("Press Start 2P", 8),
                            wraplength=100,
                            width=18, height=3,
                            bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                            command=lambda atk=ataque: self.turno_jugador(atk))
            btn.pack(side="left", padx=5, expand=True)

    def turno_jugador(self, ataque):
        danio = calcular_danio(self.pj, ataque, self.ia_poke)
        self.label_turno.config(text=f"¡Lanzaste {ataque.nombre} (daño: {danio})!")
        turno(self.pj, self.ia_poke, ataque)

        if self.ia_poke.esta_debilitado():
            self.label_turno.config(text=f"¡{self.ia_poke.nombre} ha sido debilitado!")
            self.ia.pokemones.remove(self.ia_poke)
            if not self.ia.tiene_pokemon_vivo():
                self.actualizar_interfaz()
                return
            self.ia_poke = self.ia.pokemon_activo()

        self.actualizar_interfaz()
        self.root.after(2000, self.turno_ia)

    def turno_ia(self):
        ataque = elegir_mejor_ataque(self.ia_poke, self.pj)
        danio = calcular_danio(self.ia_poke, ataque, self.pj)
        self.label_turno.config(text=f"La IA usó {ataque.nombre} (daño: {danio})")
        turno(self.ia_poke, self.pj, ataque)

        if self.pj.esta_debilitado():
            self.label_turno.config(text=f"¡{self.pj.nombre} ha sido debilitado!")
            self.jugador.pokemones.remove(self.pj)
            if not self.jugador.tiene_pokemon_vivo():
                self.actualizar_interfaz()
                return
            self.pj = self.jugador.pokemon_activo()

        self.actualizar_interfaz()

    def mostrar_equipo_final(self, equipo, ganador):
        self._limpiar_pantalla()
        frame = tk.Frame(self.root, bg=FONDO_BATALLA)
        frame.pack(fill="both", expand=True)

        titulo = tk.Label(frame, text=f"¡{ganador} ha ganado!", font=("Press Start 2P", 18),
                          bg=FONDO_BATALLA, fg="green" if ganador == "Jugador" else "red")
        titulo.pack(pady=20)

        galeria = tk.Frame(frame, bg=FONDO_BATALLA)
        galeria.pack()

        for i, poke in enumerate(equipo):
            img = self._mostrar_imagen_pokemon(poke.nombre, True)
            if img:
                lbl = tk.Label(galeria, image=img, bg=FONDO_BATALLA)
                lbl.image = img
                row = i // 2
                col = i % 2
                lbl.grid(row=row, column=col, padx=20, pady=10)

    def _limpiar_pantalla(self):
        if self.frame_actual:
            self.frame_actual.destroy()
        for widget in self.root.winfo_children():
            widget.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoPokemon(root)
    root.mainloop()
