import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget, 
                             QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                             QPushButton, QListWidget, QComboBox, QDateTimeEdit, 
                             QTableWidget, QTableWidgetItem, QTextEdit, QFileDialog)
from PyQt6.QtCore import QDateTime

class TelegramSchedulerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ultimate Telegram Web Profile Scheduler")
        self.setGeometry(100, 100, 1000, 650)
        
        # Main Tab Widget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        # Creating Tabs
        self.init_profile_tab()
        self.init_scheduler_tab()
        self.init_runner_tab()
        self.init_logs_tab()

    # --- TAB 1: PROFILE MANAGER ---
    def init_profile_tab(self):
        tab = QWidget()
        layout = QHBoxLayout()
        
        # Left side: Profile List
        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("<b>Profiles List:</b>"))
        self.profile_list = QListWidget()
        left_layout.addWidget(self.profile_list)
        
        btn_delete = QPushButton("Delete Selected")
        left_layout.addWidget(btn_delete)
        layout.addLayout(left_layout, 1)
        
        # Right side: Profile Controls & Settings
        right_layout = QVBoxLayout()
        
        # Form
        right_layout.addWidget(QLabel("Profile Name:"))
        self.txt_profile_name = QLineEdit()
        right_layout.addWidget(self.txt_profile_name)
        
        right_layout.addWidget(QLabel("Profile Folder Path:"))
        path_layout = QHBoxLayout()
        self.txt_profile_path = QLineEdit()
        btn_browse = QPushButton("Browse")
        btn_browse.clicked.connect(self.browse_folder)
        path_layout.addWidget(self.txt_profile_path)
        path_layout.addWidget(btn_browse)
        right_layout.addLayout(path_layout)
        
        # Action Buttons
        btn_save = QPushButton("Create / Save Profile")
        btn_bulk = QPushButton("Auto Create 5 Profiles")
        btn_bulk.setStyleSheet("background-color: #2ecc71; color: white;")
        right_layout.addWidget(btn_save)
        right_layout.addWidget(btn_bulk)
        
        right_layout.addStretch()
        layout.addLayout(right_layout, 2)
        
        tab.setLayout(layout)
        self.tabs.addTab(tab, "1) Profile Manager")

    # --- TAB 2: UNIVERSAL SCHEDULER ---
    def init_scheduler_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Task Type
        layout.addWidget(QLabel("Task Type:"))
        self.cmb_task_type = QComboBox()
        self.cmb_task_type.addItems(["Text Message", "Single Photo", "Photo Batch"])
        layout.addWidget(self.cmb_task_type)
        
        # Group Link / Chat ID
        layout.addWidget(QLabel("Group Name / Chat ID / Web URL:"))
        self.txt_chat_target = QLineEdit()
        layout.addWidget(self.txt_chat_target)
        
        # Date & Time
        layout.addWidget(QLabel("Schedule Date & Time:"))
        self.date_time_picker = QDateTimeEdit(QDateTime.currentDateTime())
        layout.addWidget(self.date_time_picker)
        
        # Action Buttons
        btn_preview = QPushButton("Preview Plan")
        btn_add_task = QPushButton("Enqueue Scheduled Task")
        btn_add_task.setStyleSheet("background-color: #3498db; color: white;")
        
        layout.addWidget(btn_preview)
        layout.addWidget(btn_add_task)
        layout.addStretch()
        
        tab.setLayout(layout)
        self.tabs.addTab(tab, "2) Universal Scheduler")

    # --- TAB 3: TASKS RUNNER ---
    def init_runner_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Control Buttons
        btn_layout = QHBoxLayout()
        btn_start = QPushButton("Start Parallel Runner")
        btn_start.setStyleSheet("background-color: #2ecc71; color: white;")
        btn_stop = QPushButton("Force Stop")
        btn_stop.setStyleSheet("background-color: #e74c3c; color: white;")
        
        btn_layout.addWidget(btn_start)
        btn_layout.addWidget(btn_stop)
        layout.addLayout(btn_layout)
        
        # Tasks Table
        self.task_table = QTableWidget(0, 5)
        self.task_table.setHorizontalHeaderLabels(["Status", "Time", "Profile", "Group/Chat", "Type"])
        layout.addWidget(self.task_table)
        
        tab.setLayout(layout)
        self.tabs.addTab(tab, "3) Tasks/Runner")

    # --- TAB 4: LOGS ---
    def init_logs_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        self.log_area.setStyleSheet("background-color: #1e1e1e; color: #ffffff; font-family: Consolas;")
        self.log_area.append("[18:23:01] System Initialized. Ready to manage profiles.")
        
        layout.addWidget(self.log_area)
        tab.setLayout(layout)
        self.tabs.addTab(tab, "4) Performance Logs")

    # Helper Functions
    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Profile Folder")
        if folder:
            self.txt_profile_path.setText(folder)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelegramSchedulerApp()
    window.show()
    sys.exit(app.exec())
