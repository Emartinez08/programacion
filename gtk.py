import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ButtonWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Cálculo de área de figuras")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button_triangle = Gtk.Button.new_with_label("TRIÁNGULO")
        button_triangle.connect("clicked", self.on_triangle_clicked)
        hbox.pack_start(button_triangle, True, True, 0)

        button_square = Gtk.Button.new_with_label("CUADRADO")
        button_square.connect("clicked", self.on_square_clicked)
        hbox.pack_start(button_square, True, True, 0)

        button_rectangle = Gtk.Button.new_with_label("RECTÁNGULO")
        button_rectangle.connect("clicked", self.on_rectangle_clicked)
        hbox.pack_start(button_rectangle, True, True, 0)

    def create_data_window(self, title, confirm_callback):
        """Crea una ventana de datos reutilizable."""
        data_window = Gtk.Window(title=title)
        data_window.set_border_width(10)

        grid = Gtk.Grid()
        data_window.add(grid)

        # Etiquetas y entradas para la base y la altura
        label_base = Gtk.Label(label="Base:")
        grid.attach(label_base, 0, 0, 1, 1)

        self.entry_base = Gtk.Entry()
        grid.attach(self.entry_base, 1, 0, 1, 1)

        label_height = Gtk.Label(label="Altura:")
        grid.attach(label_height, 0, 1, 1, 1)

        self.entry_height = Gtk.Entry()
        grid.attach(self.entry_height, 1, 1, 1, 1)

        # Botón para confirmar
        button_confirm = Gtk.Button(label="Confirmar")
        button_confirm.connect("clicked", confirm_callback)
        grid.attach(button_confirm, 0, 2, 1, 1)

        # Botón para regresar
        button_return = Gtk.Button(label="Regresar")
        button_return.connect("clicked", self.on_return_clicked, data_window)
        grid.attach(button_return, 1, 2, 1, 1)

        return data_window

    def on_triangle_clicked(self, button):
        self.triangle_window = self.create_data_window(
            title="Datos del Triángulo", confirm_callback=self.on_confirm_clicked_triangle
        )
        self.triangle_window.show_all()
        self.hide()

    def on_square_clicked(self, button):
        self.square_window = self.create_data_window(
            title="Datos del Cuadrado", confirm_callback=self.on_confirm_clicked_square
        )
        self.square_window.show_all()
        self.hide()

    def on_rectangle_clicked(self, button):
        self.rectangle_window = self.create_data_window(
            title="Datos del Rectángulo", confirm_callback=self.on_confirm_clicked_rectangle
        )
        self.rectangle_window.show_all()
        self.hide()

    def on_confirm_clicked_triangle(self, button):
        self.calculate_area("triángulo", 0.5, self.triangle_window)

    def on_confirm_clicked_square(self, button):
        self.calculate_area("cuadrado", 1, self.square_window)

    def on_confirm_clicked_rectangle(self, button):
        self.calculate_area("rectángulo", 1, self.rectangle_window)

    def calculate_area(self, shape, multiplier, current_window):
        try:
            base = int(self.entry_base.get_text())
            height = int(self.entry_height.get_text())
            area = multiplier * base * height

            # Crear una ventana para mostrar el área
            result_window = Gtk.Window(title="Resultado")
            result_window.set_border_width(10)

            grid = Gtk.Grid()
            result_window.add(grid)

            # Etiqueta con el resultado
            label_result = Gtk.Label(label=f"Área del {shape}: {int(area)}")
            grid.attach(label_result, 0, 0, 2, 1)

            # Botón para regresar
            button_return = Gtk.Button(label="Regresar")
            button_return.connect("clicked", self.on_result_return_clicked, current_window, result_window)
            grid.attach(button_return, 0, 1, 2, 1)

            result_window.show_all()
            current_window.hide()
        except ValueError:
            print("Por favor, ingresa valores válidos.")

    def on_return_clicked(self, button, current_window):
        current_window.close()  # Cerrar la ventana actual
        self.show()  # Mostrar la ventana principal

    def on_result_return_clicked(self, button, data_window, result_window):
        result_window.close()  # Cerrar la ventana de resultado
        data_window.close()  # Cerrar la ventana de entrada de datos
        self.show()  # Mostrar la ventana principal


win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
