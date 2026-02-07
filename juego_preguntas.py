import tkinter as tk
from tkinter import messagebox, scrolledtext
import random
from config import *

class JuegoPreguntas:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Preguntas entre Amigos")
        self.root.geometry(f"{VENTANA_ANCHO}x{VENTANA_ALTO}")
        
        # Variables del juego
        self.jugadores = []
        self.preguntas_por_jugador = {}
        self.num_preguntas = 0
        self.jugador_actual = 0
        self.preguntas_restantes = {}
        
        # Estado del juego
        self.estado = "inicio"
        
        self.crear_pantalla_inicio()
    
    def crear_pantalla_inicio(self):
        self.limpiar_pantalla()
        
        frame = tk.Frame(self.root, padx=PADDING_FRAME, pady=PADDING_FRAME)
        frame.pack(expand=True)
        
        tk.Label(frame, text="🎮 Juego de Preguntas entre Amigos 🎮", 
                font=FUENTE_TITULO_PRINCIPAL).pack(pady=PAD_NORMAL)
        
        tk.Label(frame, text="¿Cuántas preguntas debe hacer cada jugador?", 
                font=FUENTE_TEXTO_NORMAL).pack(pady=PAD_NORMAL)
        
        self.entry_num_preguntas = tk.Entry(frame, font=FUENTE_ENTRY, width=ENTRY_ANCHO)
        self.entry_num_preguntas.pack(pady=PAD_PEQUENO)
        self.entry_num_preguntas.bind('<Return>', lambda e: self.configurar_jugadores())
        self.entry_num_preguntas.focus()
        
        tk.Button(frame, text="Continuar", command=self.configurar_jugadores,
                 bg=COLOR_BOTON_PRIMARIO, fg=COLOR_TEXTO_BLANCO, 
                 font=FUENTE_BOTON_NORMAL, 
                 padx=BOTON_PAD_X_NORMAL, pady=BOTON_PAD_Y_NORMAL).pack(pady=PAD_GRANDE)
    
    def configurar_jugadores(self):
        try:
            self.num_preguntas = int(self.entry_num_preguntas.get())
            if self.num_preguntas <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un número válido mayor a 0")
            return
        
        self.limpiar_pantalla()
        
        frame = tk.Frame(self.root, padx=PADDING_FRAME, pady=PADDING_FRAME)
        frame.pack(expand=True)
        
        tk.Label(frame, text="Agregar Jugadores", 
                font=FUENTE_TITULO_PRINCIPAL).pack(pady=PAD_NORMAL)
        
        tk.Label(frame, text="Nombre del jugador:", 
                font=FUENTE_TEXTO_NORMAL).pack(pady=PAD_PEQUENO)
        
        self.entry_jugador = tk.Entry(frame, font=FUENTE_ENTRY, width=ENTRY_JUGADOR_ANCHO)
        self.entry_jugador.pack(pady=PAD_PEQUENO)
        self.entry_jugador.bind('<Return>', lambda e: self.agregar_jugador())
        
        tk.Button(frame, text="Agregar Jugador", command=self.agregar_jugador,
                 bg=COLOR_BOTON_SECUNDARIO, fg=COLOR_TEXTO_BLANCO, 
                 font=FUENTE_BOTON_PEQUENO, 
                 padx=BOTON_PAD_X_PEQUENO, pady=BOTON_PAD_Y_PEQUENO).pack(pady=PAD_NORMAL)
        
        self.label_jugadores = tk.Label(frame, text="Jugadores: 0", 
                                       font=FUENTE_TEXTO_PEQUENO)
        self.label_jugadores.pack(pady=PAD_PEQUENO)
        
        self.text_lista_jugadores = scrolledtext.ScrolledText(frame, 
                                                             height=TEXT_LISTA_JUGADORES_ALTO, 
                                                             width=TEXT_LISTA_JUGADORES_ANCHO,
                                                             font=FUENTE_TEXTO_MUY_PEQUENO)
        self.text_lista_jugadores.pack(pady=PAD_NORMAL)
        self.text_lista_jugadores.config(state=tk.DISABLED)
        
        tk.Button(frame, text="Comenzar a Agregar Preguntas", 
                 command=self.iniciar_preguntas,
                 bg=COLOR_BOTON_PRIMARIO, fg=COLOR_TEXTO_BLANCO, 
                 font=FUENTE_BOTON_NORMAL, 
                 padx=BOTON_PAD_X_NORMAL, pady=BOTON_PAD_Y_NORMAL).pack(pady=PAD_GRANDE)
    
    def agregar_jugador(self):
        nombre = self.entry_jugador.get().strip()
        if not nombre:
            messagebox.showwarning("Advertencia", "Por favor ingresa un nombre")
            return
        
        if nombre in self.jugadores:
            messagebox.showwarning("Advertencia", "Este jugador ya existe")
            return
        
        self.jugadores.append(nombre)
        self.preguntas_por_jugador[nombre] = []
        
        self.entry_jugador.delete(0, tk.END)
        self.actualizar_lista_jugadores()
        self.entry_jugador.focus()
    
    def actualizar_lista_jugadores(self):
        self.label_jugadores.config(text=f"Jugadores: {len(self.jugadores)}")
        
        self.text_lista_jugadores.config(state=tk.NORMAL)
        self.text_lista_jugadores.delete(1.0, tk.END)
        for i, jugador in enumerate(self.jugadores, 1):
            self.text_lista_jugadores.insert(tk.END, f"{i}. {jugador}\n")
        self.text_lista_jugadores.config(state=tk.DISABLED)
    
    def iniciar_preguntas(self):
        if len(self.jugadores) < 2:
            messagebox.showerror("Error", "Se necesitan al menos 2 jugadores")
            return
        
        self.jugador_actual = 0
        self.mostrar_pantalla_preguntas()
    
    def mostrar_pantalla_preguntas(self):
        if self.jugador_actual >= len(self.jugadores):
            self.iniciar_juego()
            return
        
        jugador = self.jugadores[self.jugador_actual]
        preguntas_actuales = len(self.preguntas_por_jugador[jugador])
        
        if preguntas_actuales >= self.num_preguntas:
            self.jugador_actual += 1
            self.mostrar_pantalla_preguntas()
            return
        
        self.limpiar_pantalla()
        
        frame = tk.Frame(self.root, padx=PADDING_FRAME, pady=PADDING_FRAME)
        frame.pack(expand=True)
        
        tk.Label(frame, text=f"Turno de: {jugador}", 
                font=FUENTE_TITULO_TURNO, fg=COLOR_TEXTO_PRIMARIO).pack(pady=PAD_NORMAL)
        
        tk.Label(frame, text=f"Pregunta {preguntas_actuales + 1} de {self.num_preguntas}", 
                font=FUENTE_TEXTO_NORMAL).pack(pady=PAD_PEQUENO)
        
        tk.Label(frame, text="Escribe tu pregunta:", 
                font=FUENTE_TEXTO_PEQUENO).pack(pady=PAD_PEQUENO)
        
        self.text_pregunta = scrolledtext.ScrolledText(frame, 
                                                      height=TEXT_PREGUNTA_ALTO, 
                                                      width=TEXT_PREGUNTA_ANCHO,
                                                      font=FUENTE_TEXTO_PEQUENO, wrap=tk.WORD)
        self.text_pregunta.pack(pady=PAD_NORMAL)
        self.text_pregunta.focus()
        self.text_pregunta.bind('<Control-Return>', lambda e: self.agregar_pregunta())
        
        tk.Button(frame, text="Agregar Pregunta", 
                 command=self.agregar_pregunta,
                 bg=COLOR_BOTON_PRIMARIO, fg=COLOR_TEXTO_BLANCO, 
                 font=FUENTE_BOTON_NORMAL, 
                 padx=BOTON_PAD_X_NORMAL, pady=BOTON_PAD_Y_NORMAL).pack(pady=PAD_GRANDE)
        
        # Mostrar preguntas ya agregadas
        if preguntas_actuales > 0:
            tk.Label(frame, text="Tus preguntas:", 
                    font=FUENTE_TEXTO_MUY_PEQUENO).pack(pady=PAD_PEQUENO)
            text_lista = scrolledtext.ScrolledText(frame, 
                                                  height=TEXT_PREGUNTAS_PREVIAS_ALTO, 
                                                  width=TEXT_PREGUNTAS_PREVIAS_ANCHO,
                                                  font=FUENTE_TEXTO_MINIMO)
            text_lista.pack(pady=PAD_PEQUENO)
            for i, preg in enumerate(self.preguntas_por_jugador[jugador], 1):
                text_lista.insert(tk.END, f"{i}. {preg}\n")
            text_lista.config(state=tk.DISABLED)
    
    def agregar_pregunta(self):
        pregunta = self.text_pregunta.get(1.0, tk.END).strip()
        
        if not pregunta:
            messagebox.showwarning("Advertencia", "Por favor escribe una pregunta")
            return
        
        jugador = self.jugadores[self.jugador_actual]
        self.preguntas_por_jugador[jugador].append(pregunta)
        
        if len(self.preguntas_por_jugador[jugador]) >= self.num_preguntas:
            self.jugador_actual += 1
        
        self.mostrar_pantalla_preguntas()
    
    def iniciar_juego(self):
        # Preparar preguntas para sorteo
        self.preguntas_restantes = {}
        
        for jugador in self.jugadores:
            # Para cada jugador, crear una lista con todas las preguntas
            # EXCEPTO las que él mismo creó
            preguntas_disponibles = []
            for otro_jugador in self.jugadores:
                if otro_jugador != jugador:
                    # Copiar cada pregunta individualmente
                    for pregunta in self.preguntas_por_jugador[otro_jugador]:
                        preguntas_disponibles.append(pregunta)
            
            # Mezclar las preguntas disponibles para este jugador
            random.shuffle(preguntas_disponibles)
            self.preguntas_restantes[jugador] = preguntas_disponibles
        
        # Mezclar el orden de los jugadores
        random.shuffle(self.jugadores)
        self.jugador_actual = 0
        self.mostrar_pregunta_juego()
    
    def mostrar_pregunta_juego(self):
        if self.jugador_actual >= len(self.jugadores):
            # Verificar si algún jugador tiene preguntas pendientes
            hay_preguntas_pendientes = any(len(self.preguntas_restantes[j]) > 0 for j in self.jugadores)
            
            if hay_preguntas_pendientes:
                # Reiniciar el ciclo de jugadores
                self.jugador_actual = 0
                self.mostrar_pregunta_juego()
            else:
                # Ya no hay más preguntas
                self.mostrar_fin_juego()
            return
        
        jugador = self.jugadores[self.jugador_actual]
        
        if not self.preguntas_restantes[jugador]:
            # Este jugador ya no tiene preguntas, pasar al siguiente
            self.jugador_actual += 1
            self.mostrar_pregunta_juego()
            return
        
        # Tomar la primera pregunta de la lista mezclada
        pregunta = self.preguntas_restantes[jugador].pop(0)
        
        self.limpiar_pantalla()
        
        frame = tk.Frame(self.root, padx=PADDING_FRAME, pady=PADDING_FRAME)
        frame.pack(expand=True)
        
        tk.Label(frame, text=f"🎯 Turno de: {jugador} 🎯", 
                font=FUENTE_TITULO_SECCION, fg=COLOR_TEXTO_ACENTO).pack(pady=PAD_GRANDE)
        
        tk.Label(frame, text="Tu pregunta es:", 
                font=FUENTE_SUBTITULO).pack(pady=PAD_NORMAL)
        
        text_pregunta = scrolledtext.ScrolledText(frame, 
                                                 height=TEXT_PREGUNTA_JUEGO_ALTO, 
                                                 width=TEXT_PREGUNTA_JUEGO_ANCHO,
                                                 font=FUENTE_PREGUNTA, wrap=tk.WORD,
                                                 bg=COLOR_FONDO_PREGUNTA)
        text_pregunta.pack(pady=PAD_GRANDE)
        text_pregunta.insert(tk.END, pregunta)
        text_pregunta.config(state=tk.DISABLED)
        
        tk.Label(frame, text=f"Preguntas restantes para ti: {len(self.preguntas_restantes[jugador])}", 
                font=FUENTE_TEXTO_MUY_PEQUENO).pack(pady=PAD_PEQUENO)
        
        tk.Button(frame, text="Siguiente Jugador", 
                 command=self.siguiente_jugador,
                 bg=COLOR_BOTON_PRIMARIO, fg=COLOR_TEXTO_BLANCO, 
                 font=FUENTE_BOTON_GRANDE, 
                 padx=BOTON_PAD_X_GRANDE, pady=BOTON_PAD_Y_GRANDE).pack(pady=PAD_GRANDE)
    
    def siguiente_jugador(self):
        self.jugador_actual += 1
        self.mostrar_pregunta_juego()
    
    def mostrar_fin_juego(self):
        self.limpiar_pantalla()
        
        frame = tk.Frame(self.root, padx=PADDING_FRAME, pady=PADDING_FRAME)
        frame.pack(expand=True)
        
        tk.Label(frame, text="🎉 ¡Juego Terminado! 🎉", 
                font=FUENTE_TITULO_FIN, fg=COLOR_TEXTO_EXITO).pack(pady=PAD_EXTRA_GRANDE)
        
        tk.Label(frame, text="Gracias por jugar", 
                font=FUENTE_TEXTO_NORMAL).pack(pady=PAD_NORMAL)
        
        tk.Button(frame, text="Jugar de Nuevo", 
                 command=self.reiniciar,
                 bg=COLOR_BOTON_SECUNDARIO, fg=COLOR_TEXTO_BLANCO, 
                 font=FUENTE_BOTON_NORMAL, 
                 padx=BOTON_PAD_X_NORMAL, pady=BOTON_PAD_Y_NORMAL).pack(pady=PAD_NORMAL)
        
        tk.Button(frame, text="Salir", 
                 command=self.root.quit,
                 bg=COLOR_BOTON_PELIGRO, fg=COLOR_TEXTO_BLANCO, 
                 font=FUENTE_BOTON_NORMAL, 
                 padx=BOTON_PAD_X_NORMAL, pady=BOTON_PAD_Y_NORMAL).pack(pady=PAD_NORMAL)
    
    def reiniciar(self):
        self.jugadores = []
        self.preguntas_por_jugador = {}
        self.num_preguntas = 0
        self.jugador_actual = 0
        self.preguntas_restantes = {}
        self.crear_pantalla_inicio()
    
    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoPreguntas(root)
    root.mainloop()
