import tkinter as tk
from estructuras import Entrenador
from combate import turno
from minimax import elegir_mejor_ataque
from pokemon import POKEMONES

# 🎨 Estilo tipo Pokémon clásico
FUENTE_TITULO = ("Micro 5", 36, "bold")
FUENTE_NORMAL = ("Comic Sans MS", 16)
FONDO_VENTANA = "#7EC8E3"       # Azul claro estilo Game Boy
FONDO_BATALLA = "#F8F8F8"       # Gris muy claro
COLOR_TEXTO = "black"
COLOR_BOTON = "#FFD700"         # Amarillo tipo Pokébola
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

        titulo = tk.Label(
            self.frame_inicio,
            text="Pokeminmax",
            font=FUENTE_TITULO,
            bg=FONDO_VENTANA,
            fg=COLOR_TEXTO
        )
        titulo.pack(pady=40)

        boton_start = tk.Button(
            self.frame_inicio,
            text="Start",
            font=FUENTE_NORMAL,
            width=15,
            bg=COLOR_BOTON,
            fg=COLOR_BOTON_TEXTO,
            command=self.pantalla_seleccion_equipos
        )
        boton_start.pack()

        self.frame_actual = self.frame_inicio

    def pantalla_seleccion_equipos(self):
        self._limpiar_pantalla()

        self.frame_seleccion = tk.Frame(self.root, bg=FONDO_VENTANA)
        self.frame_seleccion.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            self.frame_seleccion,
            text="Selecciona 4 Pokémon para ti",
            font=FUENTE_NORMAL,
            bg=FONDO_VENTANA,
            fg=COLOR_TEXTO
        ).pack(pady=5)

        self.seleccion_jugador = [tk.StringVar(value=list(POKEMONES.keys())[i]) for i in range(4)]
        for var in self.seleccion_jugador:
            tk.OptionMenu(self.frame_seleccion, var, *POKEMONES.keys()).pack()

        tk.Label(
            self.frame_seleccion,
            text="Selecciona 4 Pokémon para la IA",
            font=FUENTE_NORMAL,
            bg=FONDO_VENTANA,
            fg=COLOR_TEXTO
        ).pack(pady=10)

        self.seleccion_ia = [tk.StringVar(value=list(POKEMONES.keys())[i+4]) for i in range(4)]
        for var in self.seleccion_ia:
            tk.OptionMenu(self.frame_seleccion, var, *POKEMONES.keys()).pack()

        tk.Button(
            self.frame_seleccion,
            text="Iniciar Combate",
            font=FUENTE_NORMAL,
            bg=COLOR_BOTON,
            fg=COLOR_BOTON_TEXTO,
            command=self.iniciar_combate
        ).pack(pady=20)

        self.frame_actual = self.frame_seleccion

    def iniciar_combate(self):
        self._limpiar_pantalla()

        # Obtener listas de Pokémon seleccionados
        pokes_jugador = [POKEMONES[var.get()] for var in self.seleccion_jugador]
        pokes_ia = [POKEMONES[var.get()] for var in self.seleccion_ia]

        self.jugador = Entrenador("Jugador", pokes_jugador)
        self.ia = Entrenador("IA", pokes_ia)

        self.pj = self.jugador.pokemon_activo()
        self.ia_poke = self.ia.pokemon_activo()

        self.frame_combate = tk.Frame(self.root, bg=FONDO_BATALLA)
        self.frame_combate.place(relx=0.5, rely=0.5, anchor="center")

        self.label_estado = tk.Label(
            self.frame_combate,
            text="",
            font=FUENTE_NORMAL,
            bg=FONDO_BATALLA,
            fg=COLOR_TEXTO
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
                self.botonera,
                text=ataque.nombre,
                font=FUENTE_NORMAL,
                width=20,
                bg=COLOR_BOTON,
                fg=COLOR_BOTON_TEXTO,
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
