
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QListWidget, QListWidgetItem,
    QLabel, QWidget, QTextEdit, QSplitter
)
from PyQt5.QtCore import Qt
from dataCollection import getCurrent
from fileOpener import extractSampleText

class FileExplorerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Explorer with TF-IDF Sentiment")
        self.setGeometry(100, 100, 800, 600)

        # Splitter for main layout
        splitter = QSplitter(Qt.Horizontal)

        # Left Layout: Vertical Tab Bar
        tab_bar = QVBoxLayout()
        self.search_tab = QPushButton("Search")
        self.file_explore_tab = QPushButton("File Explorer")
        self.settings_tab = QPushButton("Settings")
        tab_bar.addWidget(self.search_tab)
        tab_bar.addWidget(self.file_explore_tab)
        tab_bar.addWidget(self.settings_tab)
        tab_bar.addStretch()

        left_widget = QWidget()
        left_widget.setLayout(tab_bar)
        splitter.addWidget(left_widget)

        # Center Layout: Search and File List
        search_area = QVBoxLayout()
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search...")
        self.file_path_label = QLabel("")
        self.file_path_label.setStyleSheet("font-size: 12px; color: gray;")
        self.search_button = QPushButton("Search")
        self.file_list = QListWidget()
        self.file_list.itemClicked.connect(self.show_file_preview)  # Connect file click event

        search_area.addWidget(self.search_bar)
        search_area.addWidget(self.file_path_label)
        search_area.addWidget(self.search_button)
        search_area.addWidget(self.file_list)

        center_widget = QWidget()
        center_widget.setLayout(search_area)
        splitter.addWidget(center_widget)

        # Right Layout: File Preview (hidden by default)
        self.preview_area = QVBoxLayout()
        self.preview_label = QLabel("File Preview")
        self.preview_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        self.file_preview = QTextEdit()
        self.file_preview.setReadOnly(True)

        self.preview_area.addWidget(self.preview_label)
        self.preview_area.addWidget(self.file_preview)
        self.preview_widget = QWidget()
        self.preview_widget.setLayout(self.preview_area)
        self.preview_widget.setVisible(False)  # Hidden by default
        splitter.addWidget(self.preview_widget)

        # Set splitter as central widget
        self.setCentralWidget(splitter)

        # Connect search button to functionality
        self.search_button.clicked.connect(self.search_files)
 

    def search_files(self):
        # Example function to retrieve files (replace with your actual functionality)
        query = self.search_bar.text()  # Get text from the search bar
        file_results = self.get_files(query)  # Call your file search function
        self.populate_file_list(file_results)
        self.file_path_label.setText("")

    def get_files(self, query):
        # Dummy implementation - replace with your actual search functionality
        res = getCurrent(query)
        res = [(r[1], r[2]) for r in res]
        return res

    def populate_file_list(self, file_results):
        self.file_list.clear()  # Clear existing items
        max_path_length = 40  # Maximum length for file paths

        for file_name, file_path in file_results:
            truncated_path = (
                file_path if len(file_path) <= max_path_length 
                else f"{file_path[:max_path_length - 3]}..."
            )
            display_text = f"{file_name}  -  {truncated_path}"
            item = QListWidgetItem(display_text)
            item.setData(Qt.UserRole, file_path)  # Store the full path for later use
            self.file_list.addItem(item)

    def show_file_preview(self, item):
        # Get the full file path
        file_path = item.data(Qt.UserRole)
        self.preview_widget.setVisible(True)  # Show the preview widget

        # Update the preview content
        content = extractSampleText(file_path) 

        self.file_path_label.setText(file_path)

        self.file_preview.setText(content)


if __name__ == "__main__":
    app = QApplication([])
    window = FileExplorerApp()
    window.show()
    app.exec_()

