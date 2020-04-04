from PySide2 import QtWidgets,QtCore

import json



class Parameter_window(QtWidgets.QWidget):
    def __init__(self,parameter_path):
        self.parameter_path = parameter_path
        super().__init__()
        self.setWindowTitle("parametre")
        self.setup_ui()
    def setup_ui(self):
        self.language_list = ["français","English"]
        self.create_widgets()
        self.create_layouts()
        self.modify_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()
        self.load_parameter()

    def create_widgets(self):
        self.pt_path = QtWidgets.QPushButton("chemin de bouton")
        self.pb_btn_1 = QtWidgets.QPushButton("Edit btn1")
        self.le_btn_1 = QtWidgets.QLineEdit()
        self.cb_btn_1 = QtWidgets.QCheckBox("active btn play")
        self.pb_btn_2 = QtWidgets.QPushButton("Edit btn2")
        self.le_btn_2 = QtWidgets.QLineEdit()
        self.cb_btn_2 = QtWidgets.QCheckBox("active btn play")
        self.pb_btn_3 = QtWidgets.QPushButton("Edit btn3")
        self.le_btn_3 = QtWidgets.QLineEdit()
        self.cb_btn_3 = QtWidgets.QCheckBox("active btn play")
        self.pb_btn_4 = QtWidgets.QPushButton("Edit btn4")
        self.le_btn_4 = QtWidgets.QLineEdit()
        self.cb_btn_4 = QtWidgets.QCheckBox("active btn play")
        self.txt_language = QtWidgets.QPushButton("Language")
        self.cb_language = QtWidgets.QComboBox()
    def modify_widgets(self):
        self.cb_language.addItems(self.language_list)
        self.txt_language.setEnabled(False)
        self.pt_path.setEnabled(False)
    def create_layouts(self):
        self.parameterlayout = QtWidgets.QGridLayout(self)
    def add_widgets_to_layouts(self):
        self.parameterlayout.addWidget(self.pt_path, 0, 0, 1, 3)
        self.parameterlayout.addWidget(self.pb_btn_1, 1, 0, 1, 1)
        self.parameterlayout.addWidget(self.le_btn_1, 1, 1, 1, 1)
        self.parameterlayout.addWidget(self.cb_btn_1, 1, 2, 1, 1)
        self.parameterlayout.addWidget(self.pb_btn_2, 2, 0, 1, 1)
        self.parameterlayout.addWidget(self.le_btn_2, 2, 1, 1, 1)
        self.parameterlayout.addWidget(self.cb_btn_2, 2, 2, 1, 1)
        self.parameterlayout.addWidget(self.pb_btn_3, 3, 0, 1, 1)
        self.parameterlayout.addWidget(self.le_btn_3, 3, 1, 1, 1)
        self.parameterlayout.addWidget(self.cb_btn_3, 3, 2, 1, 1)
        self.parameterlayout.addWidget(self.pb_btn_4, 4, 0, 1, 1)
        self.parameterlayout.addWidget(self.le_btn_4, 4, 1, 1, 1)
        self.parameterlayout.addWidget(self.cb_btn_4, 4, 2, 1, 1)
        self.parameterlayout.addWidget(self.txt_language, 5, 0, 1, 3)
        self.parameterlayout.addWidget(self.cb_language, 6, 1, 1, 1)

    def setup_connections(self):
        self.pb_btn_1.clicked.connect(self.edit_path_btn1)
        self.pb_btn_2.clicked.connect(self.edit_path_btn2)
        self.pb_btn_3.clicked.connect(self.edit_path_btn3)
        self.pb_btn_4.clicked.connect(self.edit_path_btn4)
        self.cb_btn_1.clicked.connect(self.edit_play_btn1)
        self.cb_btn_2.clicked.connect(self.edit_play_btn2)
        self.cb_btn_3.clicked.connect(self.edit_play_btn3)
        self.cb_btn_4.clicked.connect(self.edit_play_btn4)
    def edit_path_btn1(self):
        with open(self.parameter_path, "r", encoding="utf-8") as f:
            dico_path_btn = json.load(f)
        path = self.le_btn_1.text()
        path.encode('unicode_escape')


        dico_path_btn["btn1"]["path"] = path
        with open(self.parameter_path, "w", encoding="utf-8") as f:
            json.dump(dico_path_btn, f)

    def edit_path_btn2(self):
        with open(self.parameter_path, "r", encoding="utf-8") as f:
            dico_path_btn = json.load(f)
        path = self.le_btn_2.text()
        path.encode('unicode_escape')


        dico_path_btn["btn2"]["path"] = path
        with open(self.parameter_path, "w", encoding="utf-8") as f:
            json.dump(dico_path_btn, f)

    def edit_path_btn3(self):
        with open(self.parameter_path, "r", encoding="utf-8") as f:
            dico_path_btn = json.load(f)
        path = self.le_btn_3.text()
        path.encode('unicode_escape')


        dico_path_btn["btn3"]["path"] = path
        with open(self.parameter_path, "w", encoding="utf-8") as f:
            json.dump(dico_path_btn, f)

    def edit_path_btn4(self):
        with open(self.parameter_path, "r", encoding="utf-8") as f:
            dico_path_btn = json.load(f)
        path = self.le_btn_4.text()
        path.encode('unicode_escape')


        dico_path_btn["btn4"]["path"] = path
        with open(self.parameter_path, "w", encoding="utf-8") as f:
            json.dump(dico_path_btn, f)

    def edit_play_btn1(self):
        with open(self.parameter_path, "r", encoding="utf-8") as f:
            dico_path_btn = json.load(f)

        if self.cb_btn_1.checkState()== QtCore.Qt.CheckState.Checked:
            dico_path_btn["btn1"]["play_check"] = True
        else:
            dico_path_btn["btn1"]["play_check"] = False
        with open(self.parameter_path, "w", encoding="utf-8") as f:
            json.dump(dico_path_btn, f)

    def edit_play_btn2(self):
        with open(self.parameter_path, "r", encoding="utf-8") as f:
            dico_path_btn = json.load(f)

        if self.cb_btn_2.checkState()== QtCore.Qt.CheckState.Checked:
            dico_path_btn["btn2"]["play_check"] = True
        else:
            dico_path_btn["btn2"]["play_check"] = False
        with open(self.parameter_path, "w", encoding="utf-8") as f:
            json.dump(dico_path_btn, f)

    def edit_play_btn3(self):
        with open(self.parameter_path, "r", encoding="utf-8") as f:
            dico_path_btn = json.load(f)

        if self.cb_btn_3.checkState()== QtCore.Qt.CheckState.Checked:
            dico_path_btn["btn3"]["play_check"] = True
        else:
            dico_path_btn["btn3"]["play_check"] = False
        with open(self.parameter_path, "w", encoding="utf-8") as f:
            json.dump(dico_path_btn, f)

    def edit_play_btn4(self):
        with open(self.parameter_path, "r", encoding="utf-8") as f:
            dico_path_btn = json.load(f)

        if self.cb_btn_4.checkState()== QtCore.Qt.CheckState.Checked:
            dico_path_btn["btn4"]["play_check"] = True
        else:
            dico_path_btn["btn4"]["play_check"] = False
        with open(self.parameter_path, "w", encoding="utf-8") as f:
            json.dump(dico_path_btn, f)

    def load_parameter(self):
        with open(self.parameter_path, "r", encoding="utf-8") as f:
            dico_path_btn = json.load(f)

        self.le_btn_1.setText(dico_path_btn["btn1"]["path"])
        if dico_path_btn["btn1"]["play_check"]== True:
            self.cb_btn_1.setChecked(QtCore.Qt.CheckState.Checked)
        self.le_btn_2.setText(dico_path_btn["btn2"]["path"])
        if dico_path_btn["btn2"]["play_check"] == True:
            self.cb_btn_2.setChecked(QtCore.Qt.CheckState.Checked)
        self.le_btn_3.setText(dico_path_btn["btn3"]["path"])
        if dico_path_btn["btn3"]["play_check"] == True:
            self.cb_btn_3.setChecked(QtCore.Qt.CheckState.Checked)
        self.le_btn_4.setText(dico_path_btn["btn4"]["path"])
        if dico_path_btn["btn4"]["play_check"] == True:
            self.cb_btn_4.setChecked(QtCore.Qt.CheckState.Checked)

    def parameter_window_close(self):
        self.close()