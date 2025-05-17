# views/main_window.py

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame
)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SCALE-System")
        self.setGeometry(100, 100, 1000, 700)

        # Widget central
        central = QWidget()
        self.setCentralWidget(central)

        root_layout = QHBoxLayout(central)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        #  Menú lateral
        menu = QFrame()
        menu.setFixedWidth(200)
        menu.setStyleSheet("background-color: #2F3542;")
        menu_layout = QVBoxLayout(menu)
        menu_layout.setContentsMargins(0, 20, 0, 0)
        menu_layout.setSpacing(10)

        title = QLabel("SCALE")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
        menu_layout.addWidget(title)

        # Botones del menú
        self.btn_productos   = QPushButton("Productos")
        self.btn_clientes    = QPushButton("Clientes")
        self.btn_proveedores = QPushButton("Proveedores")
        self.btn_ventas      = QPushButton("Ventas")

        for btn in (
            self.btn_productos,
            self.btn_clientes,
            self.btn_proveedores,
            self.btn_ventas
        ):
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFixedHeight(40)
            btn.setStyleSheet("""
                QPushButton {
                    color: white;
                    background-color: transparent;
                    border: none;
                    text-align: left;
                    padding-left: 20px;
                    font-size: 16px;
                }
                QPushButton:hover {
                    background-color: #57606f;
                }
            """)
            menu_layout.addWidget(btn)

        menu_layout.addStretch()
        root_layout.addWidget(menu)

        # Área de contenido 
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #f1f2f6;")
        content_layout = QVBoxLayout(self.content)
        content_layout.setContentsMargins(20, 20, 20, 20)
        self.content_layout = content_layout
        root_layout.addWidget(self.content)

        # Conectar botones
        self.btn_productos.clicked.connect(self.show_productos)
        self.btn_clientes.clicked.connect(self.show_clientes)
        self.btn_proveedores.clicked.connect(self.show_proveedores)
        self.btn_ventas.clicked.connect(self.show_ventas)

        self.show_home()

    def clear_content(self):
        """Limpia la vista actual."""
        for i in reversed(range(self.content_layout.count())):
            widget = self.content_layout.takeAt(i).widget()
            if widget:
                widget.setParent(None)

    #Nombrar las clases como aparece en los metodos de show
    def show_home(self):
        self.clear_content()
        label = QLabel("Bienvenido a SCALE-System")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 22px;")
        self.content_layout.addWidget(label)

    def show_productos(self):
        from views.productos_view import ProductosView
        self.clear_content()
        self.content_layout.addWidget(ProductosView())

    def show_clientes(self):
        from views.clientes_view import ClientesView
        self.clear_content()
        self.content_layout.addWidget(ClientesView())

    def show_proveedores(self):
        from views.proveedores_view import ProveedoresView 
        self.clear_content()
        self.content_layout.addWidget(ProveedoresView())

    def show_ventas(self):
        from views.ventas_view import VentasView
        self.clear_content()
        self.content_layout.addWidget(VentasView())


