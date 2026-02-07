# 🎮 Juego de Preguntas entre Amigos

## Descripción
Un juego interactivo de preguntas y respuestas donde cada jugador crea preguntas y luego todos responden preguntas hechas por otros jugadores (nunca sus propias preguntas).

## Instalar Python

[URL de instalación de python](https://www.python.org/downloads/)
Descargar última versión disponible, aunque solo es necesario 3.6 o superior.

## Cómo Jugar

### Opción 1: Ejecutar con Python (requiere Python instalado)
1. Asegúrate de tener Python 3.6 o superior instalado
2. Ejecuta el programa:
   ```
   python juego_preguntas.py
   ```

### Opción 2: Crear un Ejecutable (NO requiere Python)

#### En Windows:
1. Instala PyInstaller (solo una vez):
   ```
   pip install pyinstaller
   ```

2. Crea el ejecutable:
   ```
   pyinstaller --onefile --windowed --name "JuegoPreguntas" juego_preguntas.py
   ```

3. El ejecutable estará en la carpeta `dist/`
4. Puedes compartir el archivo `JuegoPreguntas.exe` con cualquier persona
5. ¡No necesitan tener Python instalado!

#### En Mac:
1. Instala PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Crea el ejecutable:
   ```
   pyinstaller --onefile --windowed --name "JuegoPreguntas" juego_preguntas.py
   ```

3. El ejecutable estará en la carpeta `dist/`

#### En Linux:
1. Instala PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Crea el ejecutable:
   ```
   pyinstaller --onefile --windowed --name "JuegoPreguntas" juego_preguntas.py
   ```

3. El ejecutable estará en la carpeta `dist/`

## Reglas del Juego

1. **Configuración Inicial:**
   - Define cuántas preguntas debe crear cada jugador
   - Agrega los nombres de todos los jugadores (mínimo 2)

2. **Creación de Preguntas:**
   - Cada jugador crea sus preguntas en privado
   - Pueden ser preguntas estilo "Verdad o Reto", confesiones, etc.

3. **Juego:**
   - Los jugadores aparecen en orden aleatorio
   - A cada jugador le toca una pregunta al azar
   - **IMPORTANTE:** Nunca te tocará una pregunta que tú mismo creaste
   - Responde honestamente y diviértete

4. **Final:**
   - El juego termina cuando todos han respondido sus preguntas
   - Puedes jugar de nuevo con las mismas u otras personas

## Características

✅ Interfaz gráfica amigable
✅ No requiere conocimientos de programación
✅ Se puede convertir en ejecutable
✅ Sorteo aleatorio de preguntas
✅ Garantiza que no te toque tu propia pregunta
✅ Cuenta regresiva de preguntas restantes

## Notas Técnicas

- Desarrollado en Python con tkinter
- Compatible con Windows, Mac y Linux
- El ejecutable generado es standalone (no requiere instalación)
- Tamaño aproximado del ejecutable: 5-15 MB dependiendo del sistema operativo

## Solución de Problemas

**El programa no inicia:**
- Verifica que Python esté instalado correctamente
- Asegúrate de que tkinter esté disponible (viene por defecto con Python)

**Error al crear el ejecutable:**
- Verifica que PyInstaller esté instalado: `pip install pyinstaller`
- En Linux, podrías necesitar: `sudo apt-get install python3-tk`

**El ejecutable es muy grande:**
- Es normal, PyInstaller empaqueta Python completo
- Puedes comprimir el archivo .exe/.app con un compresor como WinRAR o 7zip para compartirlo

## Créditos
Creado para disfrutar con amigos. ¡Diviértete! 🎉
