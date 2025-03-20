import os
import sys
import time
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.traceback import install

# Habilita trazas de error mejoradas
install()
console = Console()

# Lista de frameworks GUI con detalles detallados
GUI_FRAMEWORKS = [
    {"name": "wxPython", "version": "4.2.1", "release": "1998", "recommended_for": "Apps de escritorio nativas en Windows y Linux", "usage": "Compatible con widgets nativos del sistema."},
    {"name": "PyQt6", "version": "6.5.0", "release": "2021", "recommended_for": "Aplicaciones profesionales con Qt", "usage": "Gran compatibilidad con el framework Qt y muchas herramientas avanzadas."},
    {"name": "Kivy", "version": "2.1.0", "release": "2011", "recommended_for": "Apps táctiles y móviles", "usage": "Multiplataforma y muy personalizable."},
    {"name": "PySide6", "version": "6.5.0", "release": "2021", "recommended_for": "Aplicaciones Qt con licencia más flexible", "usage": "Alternativa a PyQt con licencia LGPL."},
    {"name": "Dear PyGui", "version": "1.10.0", "release": "2020", "recommended_for": "Interfaz ultra rápida para gráficos interactivos", "usage": "Usa aceleración por GPU para interfaces avanzadas."},
    {"name": "PyForms", "version": "4.0", "release": "2015", "recommended_for": "Aplicaciones rápidas y estructuradas", "usage": "Diseño basado en formularios fácil de usar."},
    {"name": "PyGObject", "version": "3.42", "release": "2010", "recommended_for": "Interfaz con GTK y Gnome", "usage": "Compatibilidad con herramientas GNOME."},
    {"name": "PySimpleGUI", "version": "4.60", "release": "2018", "recommended_for": "Aplicaciones rápidas con menos código", "usage": "Sencillez y rapidez en desarrollo de interfaces."},
    {"name": "Flexx", "version": "0.8.0", "release": "2016", "recommended_for": "Aplicaciones web en Python", "usage": "Uso basado en PyScript y WebAssembly."},
    {"name": "Remi", "version": "2021.10", "release": "2015", "recommended_for": "Interfaces web en Python", "usage": "Permite ejecutar interfaces en un navegador."},
    {"name": "PyQtGraph", "version": "0.12.4", "release": "2010", "recommended_for": "Gráficos científicos avanzados", "usage": "Ideal para visualización de datos en tiempo real."},
    {"name": "PyWebView", "version": "3.6.0", "release": "2014", "recommended_for": "Aplicaciones híbridas con WebView", "usage": "Renderiza contenido web en una ventana nativa."},
    {"name": "Toga", "version": "0.3.0", "release": "2015", "recommended_for": "Interfaces multiplataforma con Python", "usage": "Parte del proyecto BeeWare para interfaces nativas."},
    {"name": "PySide5", "version": "5.15.0", "release": "2020", "recommended_for": "Aplicaciones Qt con soporte moderno", "usage": "Similar a PySide6 pero con soporte a versiones anteriores."},
    {"name": "PyQt5", "version": "5.15.0", "release": "2016", "recommended_for": "Aplicaciones Qt ampliamente usadas", "usage": "Popular en la comunidad de Python para interfaces Qt."},
    {"name": "KivyMD", "version": "1.0.0", "release": "2019", "recommended_for": "Aplicaciones móviles con Material Design", "usage": "Extensión de Kivy para diseño moderno."}
]

# Carpeta de salida para los archivos generados
OUTPUT_DIR = "output"

# Función para mostrar la tabla con opciones de GUI
def show_gui_options():
    table = Table(title="Opciones de Frameworks GUI")
    table.add_column("#", justify="center", style="cyan", no_wrap=True)
    table.add_column("Nombre", style="bold white")
    table.add_column("Versión", justify="center", style="green")
    table.add_column("Lanzamiento", justify="center", style="yellow")
    table.add_column("Recomendado para", style="magenta")
    table.add_column("Uso", style="blue")

    for idx, framework in enumerate(GUI_FRAMEWORKS, 1):
        table.add_row(
            str(idx), framework["name"], framework["version"],
            framework["release"], framework["recommended_for"], framework["usage"]
        )

    console.print(table)

# Función para manejar la selección del usuario
def select_framework():
    while True:
        try:
            choice = Prompt.ask("Seleccione el número del framework que desea usar", choices=[str(i) for i in range(1, len(GUI_FRAMEWORKS) + 1)])
            return GUI_FRAMEWORKS[int(choice) - 1]["name"]
        except (ValueError, IndexError):
            console.print("[red]Selección inválida. Intente de nuevo.[/red]")

# Función para generar la estructura básica del archivo Python
def generate_gui_code(framework):
    console.print(f"[bold green]Generando código para {framework}...[/bold green]")
    filename = Prompt.ask("Ingrese el nombre del archivo .py a generar")
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# Código generado para {framework}\n")
        if framework == "PyQt6":
            f.write("import sys\n")
            f.write("from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QCheckBox, QRadioButton, QComboBox, QListWidget, QScrollBar, QProgressBar, QSlider, QTabWidget, QMenuBar, QToolBar, QTableWidget, QTreeWidget, QDialog, QFrame, QCalendarWidget, QDateTimeEdit, QFileDialog, QMainWindow, QStatusBar)\n")
            f.write("\n")
            f.write("app = QApplication(sys.argv)\n")
            f.write("window = QMainWindow()\n")
            f.write("window.setWindowTitle('GUI Generada')\n")
            f.write("\n")
            f.write("central_widget = QWidget()\n")
            f.write("layout = QVBoxLayout(central_widget)\n")
            f.write("\n")
            f.write("label = QLabel('¡Hola, Mundo!')\n")
            f.write("button = QPushButton('Presióname')\n")
            f.write("text_field = QLineEdit()\n")
            f.write("text_area = QTextEdit()\n")
            f.write("checkbox = QCheckBox('Acepto los términos')\n")
            f.write("radio_button = QRadioButton('Opción 1')\n")
            f.write("combo_box = QComboBox()\n")
            f.write("combo_box.addItems(['Opción 1', 'Opción 2', 'Opción 3'])\n")
            f.write("list_widget = QListWidget()\n")
            f.write("list_widget.addItems(['Elemento 1', 'Elemento 2', 'Elemento 3'])\n")
            f.write("scroll_bar = QScrollBar()\n")
            f.write("progress_bar = QProgressBar()\n")
            f.write("slider = QSlider()\n")
            f.write("tab_widget = QTabWidget()\n")
            f.write("tab_widget.addTab(QWidget(), 'Pestaña 1')\n")
            f.write("menu_bar = QMenuBar()\n")
            f.write("tool_bar = QToolBar()\n")
            f.write("table_widget = QTableWidget(3, 3)\n")
            f.write("tree_widget = QTreeWidget()\n")
            f.write("dialog = QDialog()\n")
            f.write("frame = QFrame()\n")
            f.write("calendar = QCalendarWidget()\n")
            f.write("date_time_edit = QDateTimeEdit()\n")
            f.write("file_dialog = QFileDialog()\n")
            f.write("status_bar = QStatusBar()\n")
            f.write("\n")
            f.write("layout.addWidget(label)\n")
            f.write("layout.addWidget(button)\n")
            f.write("layout.addWidget(text_field)\n")
            f.write("layout.addWidget(text_area)\n")
            f.write("layout.addWidget(checkbox)\n")
            f.write("layout.addWidget(radio_button)\n")
            f.write("layout.addWidget(combo_box)\n")
            f.write("layout.addWidget(list_widget)\n")
            f.write("layout.addWidget(scroll_bar)\n")
            f.write("layout.addWidget(progress_bar)\n")
            f.write("layout.addWidget(slider)\n")
            f.write("layout.addWidget(tab_widget)\n")
            f.write("layout.addWidget(table_widget)\n")
            f.write("layout.addWidget(tree_widget)\n")
            f.write("layout.addWidget(calendar)\n")
            f.write("layout.addWidget(date_time_edit)\n")
            f.write("\n")
            f.write("window.setCentralWidget(central_widget)\n")
            f.write("window.setMenuBar(menu_bar)\n")
            f.write("window.addToolBar(tool_bar)\n")
            f.write("window.setStatusBar(status_bar)\n")
            f.write("\n")
            f.write("window.show()\n")
            f.write("sys.exit(app.exec())\n")
        elif framework == "Dear PyGui":
            f.write("from dearpygui.core import *\n")
            f.write("from dearpygui.simple import *\n")
            f.write("\n")
            f.write("def main():\n")
            f.write("    with window('Main Window'):\n")
            f.write("        add_text('¡Hola, Mundo!')\n")
            f.write("        add_button('Presióname')\n")
            f.write("        add_input_text('Text Field')\n")
            f.write("        add_input_text('Text Area', multiline=True)\n")
            f.write("        add_checkbox('Acepto los términos')\n")
            f.write("        add_radio_button('Opción 1')\n")
            f.write("        add_combo('Combo Box', items=['Opción 1', 'Opción 2', 'Opción 3'])\n")
            f.write("        add_listbox('List Widget', items=['Elemento 1', 'Elemento 2', 'Elemento 3'])\n")
            f.write("        add_slider_float('Slider')\n")
            f.write("        add_progress_bar('Progress Bar')\n")
            f.write("        add_tab_bar('Tab Widget')\n")
            f.write("        add_menu_bar('Menu Bar')\n")
            f.write("        add_table('Table Widget', ['Columna 1', 'Columna 2', 'Columna 3'])\n")
            f.write("        add_tree_node('Tree Widget')\n")
            f.write("        add_date_picker('Calendar')\n")
            f.write("        add_time_picker('Date Time Edit')\n")
            f.write("\n")
            f.write("    start_dearpygui()\n")
            f.write("\n")
            f.write("if __name__ == '__main__':\n")
            f.write("    main()\n")
        # Agregar más frameworks según sea necesario

    console.print(f"[bold cyan]Archivo guardado en: {filepath}[/bold cyan]")

# Main loop
def main():
    while True:
        show_gui_options()
        framework = select_framework()
        generate_gui_code(framework)
        time.sleep(1)

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    main()
