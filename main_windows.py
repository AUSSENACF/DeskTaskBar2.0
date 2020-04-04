from functools import partial
import os
from pathlib import Path
#import webbrowser
import json

from PySide2 import QtWidgets, QtCore,QtGui
from package.secondarywindow import Secondary_windows
from package.parameterwindow import Parameter_window

""" attaque le placement de l interface en fonction de la taillt de l ecran """


## création d'un fichier Json si besoin est:
path_desk = eval(f"QtCore.QStandardPaths().standardLocations(QtCore.QStandardPaths.DesktopLocation)")

"""btn2_path= "r'"+"test"+"'" #ce que je doit mettre quand je change de destination!!!!!"""
dico_path_btn = {"btn1":{"path":f'{path_desk[0]}',
                          "play_check":True},
                 "btn2":{"path": f"{os.path.join(Path.home(),'.DeskTaskBar_game')}",
                          "play_check":False},
                 "btn3":{"path":f"{os.path.join(Path.home(),'.DeskTaskBar_sound')}",
                          "play_check":True},
                 "btn4":{"path":f"{os.path.join(Path.home(),'.DeskTaskBar_movie')}",
                          "play_check":False}
                }

#print(dico_path_btn["btn1"]["path"])
parameter_path = os.path.join(os.path.dirname(__file__),"paramater.json")
if not os.path.exists(parameter_path):
    with open(parameter_path, "w" , encoding="utf-8") as f:
        json.dump(dico_path_btn,f)
else:
    with open(parameter_path, "r") as f:
        dico_path_btn = json.load(f)
        #print(dico_path_btn)






class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,ctx):
        self.width = 1920
        self.height = 1080
        self.bouton_height = self.height/30
        self.dico_path_btn = dico_path_btn
        super().__init__()
        self.ctx = ctx  # import de context app pour pouvoir chercher des ressources
        self.setup_ui()
        self.setStyleSheet("background-color: rgb(42, 40, 40);")
        self.create_tray_icon()
    def setup_ui(self):
        self.bool_app_on_top = False
        self.create_widgets()
        self.create_layouts()
        self.modify_widgets()
        self.add_widgets_to_layouts()
        self.move(self.width/3 , 0)
        # recuperation des coordonnée de la fenetre principale
        main_window_abscisse = self.geometry().x()
        main_windows_ordonnee = self.geometry().y()
        # boolean pour savoir si la fenetre secondaire est ouverte ou fermer
        self.location_secondary_window = "nothing"
        # creation et envois des coordonnées de la deuxième fenêtre pour les raccourcis
        self.secondary_window = Secondary_windows(abscisse=main_window_abscisse, ordonnee=main_windows_ordonnee + self.height/30 , width=self.width/3, height=self.height/3)
        self.parameterwindow = Parameter_window(parameter_path=parameter_path)
        self.setup_connections()


    def create_widgets(self):
        self.main_widget = QtWidgets.QWidget()
        self.btn_desk = QtWidgets.QPushButton()
        self.btn_game = QtWidgets.QPushButton()
        self.btn_sound = QtWidgets.QPushButton()
        self.btn_movie = QtWidgets.QPushButton()
        self.btn_google_searching = QtWidgets.QPushButton()
        self.btn_quit = QtWidgets.QPushButton()
        self.le_google_search = QtWidgets.QLineEdit()
        self.btn_app_on_top = QtWidgets.QPushButton()


    def modify_widgets(self):
        """css_file = self.ctx.get_resource("style.css")
        with open(css_file,"r") as f:                       # lecture defeuille de style potentiel
            self.setStyleSheet(f.read())"""
        self.main_layout.setContentsMargins(0, 0, 0, 0) # supprimer les marges

        self.main_layout.setSpacing(0) # supprimer les espaces entre les différent widget

        self.setStyleSheet("border: none") # supprimer les bordures de fenêtre
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # supprimer la barres de navigation

        # importation des image des boutons
        self.btn_desk.setIcon(((QtGui.QIcon(self.ctx.get_resource("icon_btn1.png")))))
        self.btn_game.setIcon(((QtGui.QIcon(self.ctx.get_resource("icon_btn2.png")))))
        self.btn_sound.setIcon(((QtGui.QIcon(self.ctx.get_resource("icon_btn3.png")))))
        self.btn_movie.setIcon(((QtGui.QIcon(self.ctx.get_resource("icon_btn4.png")))))
        self.btn_google_searching.setIcon(((QtGui.QIcon(self.ctx.get_resource("google.png")))))
        self.btn_quit.setIcon(((QtGui.QIcon(self.ctx.get_resource("Parametre.png")))))
        self.btn_app_on_top.setIcon(((QtGui.QIcon(self.ctx.get_resource("on_top.png")))))

        # taille des boutons
        self.btn_desk.setIconSize(QtCore.QSize(self.bouton_height, self.bouton_height))
        self.btn_game.setIconSize(QtCore.QSize(self.bouton_height, self.bouton_height))
        self.btn_sound.setIconSize(QtCore.QSize(self.bouton_height, self.bouton_height))
        self.btn_movie.setIconSize(QtCore.QSize(self.bouton_height, self.bouton_height))
        self.btn_google_searching.setIconSize(QtCore.QSize(self.bouton_height, self.bouton_height))
        self.btn_quit.setIconSize(QtCore.QSize(self.bouton_height, self.bouton_height))
        self.btn_app_on_top.setIconSize(QtCore.QSize(self.bouton_height, self.bouton_height))
        self.le_google_search.setFixedHeight(self.bouton_height)


    def create_layouts(self):
        self.main_layout = QtWidgets.QHBoxLayout(self.main_widget)

    def add_widgets_to_layouts(self):
        self.setCentralWidget(self.main_widget)
        self.main_layout.addWidget(self.btn_desk)
        self.main_layout.addWidget(self.btn_game)
        self.main_layout.addWidget(self.btn_sound)
        self.main_layout.addWidget(self.btn_movie)
        self.main_layout.addWidget(self.le_google_search)
        self.main_layout.addWidget(self.btn_google_searching)
        #self.main_layout.addStretch() # créer un espace entre les boutons
        self.main_layout.addWidget(self.btn_app_on_top)
        self.main_layout.addWidget(self.btn_quit)


    def setup_connections(self):
        self.btn_desk.clicked.connect(partial(self.directory_validation, btn="btn1"))
        self.btn_game.clicked.connect(partial(self.directory_validation, btn="btn2"))
        self.btn_sound.clicked.connect(partial(self.directory_validation, btn="btn3"))
        self.btn_movie.clicked.connect(partial(self.directory_validation, btn="btn4"))
        QtWidgets.QShortcut(QtGui.QKeySequence("Return"), self.le_google_search, self.search_on_net_browser)
        self.btn_google_searching.clicked.connect(self.search_on_net_browser)
        self.btn_quit.clicked.connect(self.secondary_window.hide)
        self.btn_quit.clicked.connect(self.parameterwindow.show)
        self.btn_app_on_top.clicked.connect(self.app_on_top)

    def directory_validation(self,btn):
        #chargement du chemin de dossier suivant le btn cliqué

        #si desk est cliqué utilisation de la location standardisé
        """if doc_location == ".desk":
            path = eval(f"QtCore.QStandardPaths().standardLocations(QtCore.QStandardPaths.DesktopLocation)")
            path = path[0]
            self.secondary_window_hide_show(doc_location=doc_location,path=path)
            return"""
        # si un autre btn est cliqué utilisation du path.home poiur trouver le dossier utilisateur, verification de la presence du dossier dedans si non creation du dossier
        with open(parameter_path, 'r', encoding='utf-8') as file:
            dico_path_btn= json.load(file)
        doc_location = dico_path_btn[btn]
        show_play_btn = doc_location["play_check"]
        path = doc_location["path"]
        if not os.path.exists(path):
            os.makedirs(path)
            self.secondary_window_hide_show(doc_location=doc_location, path=path)
        else:
            self.secondary_window_hide_show(doc_location=doc_location, path=path, show_play_btn=show_play_btn)

    def search_on_net_browser(self):
        # lancer une recherche google
        print('a')
        """researching = f"https://www.google.com/search?q={self.le_google_search.text()}"
        webbrowser.open_new_tab(researching)
        self.le_google_search.setText("")"""

    def secondary_window_hide_show(self, doc_location, path,  show_play_btn):
        # verification de la position de la fenêtre grace a la var=doc_location + hide ou show suivant le resultat, envoi du path a la "Secondary Window"
        if self.location_secondary_window == doc_location:
            self.secondary_window.hide()
            self.location_secondary_window = "nothing"

        elif self.location_secondary_window == "nothing":
            self.location_secondary_window = doc_location
            self.secondary_window.show()
            self.secondary_window.change_location(path=path)
            self.secondary_window.show_play_bouton(show_play_btn=show_play_btn)


        else:
            self.location_secondary_window = doc_location
            self.secondary_window.change_location(path=path)
            self.secondary_window.show_play_bouton(show_play_btn=show_play_btn)

    def app_on_top(self):
        if self.bool_app_on_top == False:
            self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
            self.show()
            self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnBottomHint)
            self.show()
            self.secondary_window.app_on_top(bool_app_on_top=self.bool_app_on_top)
            self.bool_app_on_top = True
        else:
            self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnBottomHint)
            self.show()
            self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
            self.show()
            self.secondary_window.app_on_top(bool_app_on_top=self.bool_app_on_top)
            self.bool_app_on_top = False



    def create_tray_icon(self):
        self.tray = QtWidgets.QSystemTrayIcon()
        icon_path = self.ctx.get_resource("icon_btn1.png")
        self.tray.setIcon(QtGui.QIcon(icon_path))
        self.tray.setVisible(True)
        self.tray.activated.connect(self.contextMenuEvent)


    def contextMenuEvent(self, event):

        menu = QtWidgets.QMenu(self)
        tray_x = self.tray.geometry().x()
        tray_y = self.tray.geometry().y()
        w, h = self.sizeHint().toTuple()

        menu.move(tray_x, tray_y)

        quit_action = menu.addAction("Quit")
        hide_show_action = menu.addAction("Hide/show")

        action = menu.exec_()

        if action == quit_action:
            if not self.location_secondary_window == "nothing":
                self.secondary_window.hide()

            if not self.parameterwindow.isHidden():
                self.parameterwindow.close()

            self.close()

        elif action == hide_show_action:
            if self.isHidden():
                self.showNormal()
            else:
                self.hide()

