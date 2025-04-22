import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton,
                               QHBoxLayout, QListWidget, QListWidgetItem,
                               QMessageBox, QGroupBox, QInputDialog)
from PySide6.QtGui import QColor, QIcon

class TarefaManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon())

        self.setWindowTitle("📱 Gerenciador de Tarefas")
        self.setMinimumSize(700, 500)

        self.tarefas = {
            1: {"titulo": "Estudar Python", "status": "Concluída"},
            2: {"titulo": "Finalizar projeto", "status": "Concluída"},
            3: {"titulo": "Ir ao mercado", "status": "Pendente"},
            4: {"titulo": "Limpar geladeira", "status": "Pendente"}
        }

        self.layout = QHBoxLayout(self)

        # Lista
        self.lista = QListWidget()
        self.lista.setStyleSheet("""
            QListWidget {
                background-color: #f9f9f9;
                border-radius: 12px;
                font-size: 16px;
                padding: 10px;
            }
            QListWidget::item {
                padding: 10px 15px;
                margin: 2px 0;
                border-radius: 10px;
                color: #333;
            }
            QListWidget::item:selected {
                background-color: #e0e0e0;
                color: #000;
            }
        """)
        self.layout.addWidget(self.lista)

        # Painel de botões
        self.painel = QGroupBox("⚙️ Ações")
        self.painel.setStyleSheet("""
            QGroupBox {
                font-size: 16px;
                border: 1px solid #ddd;
                border-radius: 12px;
                margin-left: 10px;
            }
        """)
        self.painel_layout = QVBoxLayout()
        self.painel.setLayout(self.painel_layout)
        self.btn_adicionar = QPushButton("➕ Adicionar")
        self.btn_status = QPushButton("🔁 Alterar Status")
        self.btn_excluir = QPushButton("🗑️ Excluir")

        for btn in [self.btn_adicionar, self.btn_status, self.btn_excluir]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #ffffff;
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    padding: 10px;
                    font-size: 14px;
                    min-width: 140px;
                }
                QPushButton:hover {
                    background-color: #f0f0f0;
                }
            """)
            self.painel_layout.addWidget(btn)

        self.layout.addWidget(self.painel)

        # Conectar botões
        self.btn_adicionar.clicked.connect(self.adicionar_tarefa)
        self.btn_status.clicked.connect(self.alterar_status)
        self.btn_excluir.clicked.connect(self.excluir_tarefa)

        self.listar_tarefas()

    def listar_tarefas(self):
        self.lista.clear()
        for id_tarefa, info in self.tarefas.items():
            status_icon = "✅" if info["status"] == "Concluída" else "⭕"
            texto = f"{status_icon} {info['titulo']}"

            item = QListWidgetItem(texto)
            if info['status'] == "Concluída":
                item.setBackground(QColor("#eef9f0"))  # verde bem claro
            else:
                item.setBackground(QColor("#ffffff"))

            item.setData(1000, id_tarefa)  # salvar ID interno
            self.lista.addItem(item)

    def adicionar_tarefa(self):
        titulo, ok = self.get_text_input("📝 Nova Tarefa", "Título:")
        if not ok or not titulo.strip():
            return
        novo_id = max(self.tarefas.keys()) + 1 if self.tarefas else 1
        self.tarefas[novo_id] = {"titulo": titulo.strip(), "status": "Pendente"}
        self.listar_tarefas()

    def alterar_status(self):
        item = self.lista.currentItem()
        if not item:
            QMessageBox.warning(self, "Aviso", "Selecione uma tarefa.")
            return
        id_tarefa = item.data(1000)
        tarefa = self.tarefas[id_tarefa]
        tarefa["status"] = "Concluída" if tarefa["status"] == "Pendente" else "Pendente"
        self.listar_tarefas()

    def excluir_tarefa(self):
        item = self.lista.currentItem()
        if not item:
            QMessageBox.warning(self, "Aviso", "Selecione uma tarefa.")
            return
        id_tarefa = item.data(1000)
        del self.tarefas[id_tarefa]
        self.listar_tarefas()

    def get_text_input(self, title, label):
        text, ok = QInputDialog.getText(self, title, label)
        return text, ok

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = TarefaManager()
    window.show()
    sys.exit(app.exec())
