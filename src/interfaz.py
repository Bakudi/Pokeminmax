import tkinter as tk
from PIL import Image, ImageTk
import os
import unicodedata

from estructuras import Entrenador
from combate import turno, calcular_danio
from minimax import elegir_mejor_ataque
from pokemon import POKEMONES

# Estilo tipo Pokémon clásico
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
        frame = tk.Frame(self.root, bg=FONDO_VENTANA)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame_actual = frame

        tk.Label(frame, text="Pokeminmax", font=FUENTE_TITULO, bg=FONDO_VENTANA, fg=COLOR_TEXTO).pack(pady=40)
        tk.Button(frame, text="Start", font=FUENTE_NORMAL, width=15, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                  command=self.pantalla_seleccion_equipos).pack()

    def pantalla_seleccion_equipos(self):
        self._limpiar_pantalla()
        self.nombres_pokemon = list(POKEMONES.keys())
        self.indice_actual = 0
        self.seleccion_jugador = []
        self.seleccion_ia = []
        self.seleccion_actual = []
        self.fase = "jugador"
        self.pokemon_num = 1

        frame = tk.Frame(self.root, bg=FONDO_VENTANA)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame_actual = frame

        self.titulo_seleccion = tk.Label(frame, text="Selecciona tu Pokémon 1", font=FUENTE_NORMAL, bg=FONDO_VENTANA)
        self.titulo_seleccion.pack(pady=10)

        self.label_imagen = tk.Label(frame, bg=FONDO_VENTANA)
        self.label_imagen.pack()
        self.label_pokemon = tk.Label(frame, font=FUENTE_NORMAL, width=15, height=2,
                                      relief="raised", bd=3, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO)
        self.label_pokemon.pack(pady=10)

        botones = tk.Frame(frame, bg=FONDO_VENTANA)
        botones.pack()
        tk.Button(botones, text="⬆", font=FUENTE_NORMAL, width=5, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                  command=lambda: self.cambiar_pokemon(-1)).grid(row=0, column=0, padx=10)
        tk.Button(botones, text="⬇", font=FUENTE_NORMAL, width=5, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                  command=lambda: self.cambiar_pokemon(1)).grid(row=0, column=1, padx=10)

        tk.Button(frame, text="Confirmar", font=FUENTE_NORMAL, width=15, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                  command=self.confirmar_pokemon).pack(pady=20)

        self._actualizar_selector()

    def _formatear_nombre_archivo(self, nombre):
        nombre = unicodedata.normalize('NFD', nombre).encode('ascii', 'ignore').decode('utf-8')
        return nombre.lower().replace(" ", "_").replace(".", "")

    def _mostrar_imagen_pokemon(self, nombre):
        ruta = os.path.join(os.path.dirname(__file__), "..", "imagenes", f"{self._formatear_nombre_archivo(nombre)}.png")
        if os.path.exists(ruta):
            img = Image.open(ruta).resize((150, 150), Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
        return None

    def cambiar_pokemon(self, delta):
        self.indice_actual = (self.indice_actual + delta) % len(self.nombres_pokemon)
        self._actualizar_selector()

    def _actualizar_selector(self):
        nombre = self.nombres_pokemon[self.indice_actual]
        img = self._mostrar_imagen_pokemon(nombre)
        if img:
            self.label_imagen.config(image=img)
            self.label_imagen.image = img
        self.label_pokemon.config(text=nombre)

    def confirmar_pokemon(self):
        seleccionado = POKEMONES[self.nombres_pokemon[self.indice_actual]]
        self.seleccion_actual.append(seleccionado)

        if len(self.seleccion_actual) < 4:
            self.pokemon_num += 1
            texto = "Selecciona tu Pokémon" if self.fase == "jugador" else "Selecciona Pokémon de IA"
            self.titulo_seleccion.config(text=f"{texto} {self.pokemon_num}")
        else:
            if self.fase == "jugador":
                self.seleccion_jugador = self.seleccion_actual.copy()
                self.seleccion_actual.clear()
                self.fase = "ia"
                self.pokemon_num = 1
                self.titulo_seleccion.config(text="Selecciona Pokémon de IA 1")
            else:
                self.seleccion_ia = self.seleccion_actual.copy()
                self.iniciar_combate()
                return

        self.indice_actual = 0
        self._actualizar_selector()

    def iniciar_combate(self):
        self._limpiar_pantalla()
        self.jugador = Entrenador("Jugador", self.seleccion_jugador)
        self.ia = Entrenador("IA", self.seleccion_ia)
        self.pj = self.jugador.pokemon_activo()
        self.ia_poke = self.ia.pokemon_activo()

        self.frame_combate = tk.Frame(self.root, bg=FONDO_BATALLA)
        self.frame_combate.pack(fill="both", expand=True)
        self.label_turno = tk.Label(self.frame_combate, font=FUENTE_NORMAL, bg=FONDO_BATALLA, fg=COLOR_TEXTO)
        self.label_turno.pack(pady=5)

        self.label_info_ataques_ia = tk.Label(self.frame_combate, font=("Press Start 2P", 8), fg="red", bg=FONDO_BATALLA)
        self.label_info_ataques_ia.pack()

        self.canvas = tk.Frame(self.frame_combate, bg=FONDO_BATALLA, width=700, height=200)
        self.canvas.pack()
        self.img_jugador_label = tk.Label(self.canvas, bg=FONDO_BATALLA)
        self.img_jugador_label.place(x=100, y=60)
        self.img_ia_label = tk.Label(self.canvas, bg=FONDO_BATALLA)
        self.img_ia_label.place(x=400, y=60)
        self.info_jugador = tk.Label(self.canvas, font=("Press Start 2P", 8), bg=FONDO_BATALLA, fg=COLOR_TEXTO)
        self.info_jugador.place(x=100, y=20)
        self.info_ia = tk.Label(self.canvas, font=("Press Start 2P", 8), bg=FONDO_BATALLA, fg=COLOR_TEXTO)
        self.info_ia.place(x=400, y=20)

        self.botonera = tk.Frame(self.frame_combate, bg=FONDO_BATALLA)
        self.botonera.pack(side="bottom", pady=10)

        self.actualizar_interfaz()
        self.label_turno.config(text="¡Es tu turno para atacar!")

    def actualizar_interfaz(self):
        self.info_jugador.config(text=f"{self.pj.nombre} - {self.pj.ps} PS")
        self.info_ia.config(text=f"{self.ia_poke.nombre} - {self.ia_poke.ps} PS")
        self.label_info_ataques_ia.config(text="IA: " + ", ".join([atk.nombre for atk in self.ia_poke.ataques]))

        img_j = self._mostrar_imagen_pokemon(self.pj.nombre)
        img_i = self._mostrar_imagen_pokemon(self.ia_poke.nombre)
        self.img_jugador_label.config(image=img_j)
        self.img_jugador_label.image = img_j
        self.img_ia_label.config(image=img_i)
        self.img_ia_label.image = img_i

        for w in self.botonera.winfo_children():
            w.destroy()

        if not self.jugador.tiene_pokemon_vivo():
            self.label_turno.config(text=f"{self.pj.nombre} ha sido debilitado!")
            self.root.after(1500, lambda: self.mostrar_equipo_final(self.ia.pokemones, "IA"))
            return

        if not self.ia.tiene_pokemon_vivo():
            self.label_turno.config(text=f"{self.ia_poke.nombre} ha sido debilitado!")
            self.root.after(1500, lambda: self.mostrar_equipo_final(self.jugador.pokemones, "Jugador"))
            return

        for atk in self.pj.ataques:
            d = calcular_danio(self.pj, atk, self.ia_poke)
            b = tk.Button(self.botonera,
                          text=f"{atk.nombre}\n({d} PS)",
                          font=("Press Start 2P", 8),
                          wraplength=100,
                          width=18, height=3,
                          bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                          command=lambda a=atk: self.turno_jugador(a))
            b.pack(side="left", padx=5, expand=True)

    def vibrar(self, label, repeticiones=6, distancia=5, intervalo=50, direccion=1, original_x=None):
        if original_x is None:
            original_x = label.winfo_x()
        if repeticiones <= 0:
            label.place(x=original_x)
            return
        desplazamiento = direccion * distancia
        label.place(x=original_x + desplazamiento)
        self.root.after(intervalo, lambda: self.vibrar(label, repeticiones - 1, distancia, intervalo, -direccion, original_x))

    def parpadear(self, label, repeticiones=6, intervalo=100):
        if repeticiones <= 0:
            label.config(bg=FONDO_BATALLA)
            return
        color = "white" if repeticiones % 2 == 0 else FONDO_BATALLA
        label.config(bg=color)
        self.root.after(intervalo, lambda: self.parpadear(label, repeticiones - 1, intervalo))

    def turno_jugador(self, ataque):
        danio = calcular_danio(self.pj, ataque, self.ia_poke)
        self.label_turno.config(text=f"¡Lanzaste {ataque.nombre} (daño: {danio})!")
        turno(self.pj, self.ia_poke, ataque)
        self.vibrar(self.img_ia_label)
        self.parpadear(self.img_ia_label)
        self.actualizar_interfaz()
        self.root.after(1500, self._verificar_ia_debilitada)

    def _verificar_ia_debilitada(self):
        if self.ia_poke.esta_debilitado():
            self.label_turno.config(text=f"¡{self.ia_poke.nombre} ha sido debilitado!")
            self.root.after(1500, self._cambiar_pokemon_ia)
        else:
            self.root.after(1500, self.turno_ia)

    def _cambiar_pokemon_ia(self):
        self.ia.cambiar_pokemon()
        if not self.ia.tiene_pokemon_vivo():
            self.actualizar_interfaz()
            return
        self.ia_poke = self.ia.pokemon_activo()
        self.actualizar_interfaz()
        self.label_turno.config(text=f"La IA envía a {self.ia_poke.nombre}")
        self.root.after(1500, self.turno_ia)

    def turno_ia(self):
        ataque = elegir_mejor_ataque(self.ia_poke, self.pj)
        danio = calcular_danio(self.ia_poke, ataque, self.pj)
        self.label_turno.config(text=f"La IA usó {ataque.nombre} (daño: {danio})")
        turno(self.ia_poke, self.pj, ataque)
        self.vibrar(self.img_jugador_label)
        self.parpadear(self.img_jugador_label)
        self.actualizar_interfaz()
        self.root.after(1500, self._verificar_jugador_debilitado)

    def _verificar_jugador_debilitado(self):
        if self.pj.esta_debilitado():
            self.label_turno.config(text=f"¡{self.pj.nombre} ha sido debilitado!")
            self.root.after(1500, self._cambiar_pokemon_jugador)
        else:
            self.label_turno.config(text="¡Es tu turno para atacar!")
            self.actualizar_interfaz()

    def _cambiar_pokemon_jugador(self):
        self.jugador.cambiar_pokemon()
        if not self.jugador.tiene_pokemon_vivo():
            self.actualizar_interfaz()
            return
        self.pj = self.jugador.pokemon_activo()
        self.actualizar_interfaz()
        self.label_turno.config(text=f"¡Enviaste a {self.pj.nombre}!")
        self.root.after(1500, self.actualizar_interfaz)

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
            img = self._mostrar_imagen_pokemon(poke.nombre)
            if img:
                lbl = tk.Label(galeria, image=img, bg=FONDO_BATALLA)
                lbl.image = img
                row, col = divmod(i, 2)
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
