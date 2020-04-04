from PySide2 import QtCore,QtWidgets
import os
import glob



class Secondary_windows(QtWidgets.QWidget):
    def __init__(self, abscisse, ordonnee, width , height):
        super().__init__()
        self.setup_ui()
        # recuperation des coordonnées pour replacement de la fenêtre secondaire en fonction de la fenêtre principal
        self.move(abscisse, ordonnee)
        self.resize(width,height)
    def setup_ui(self):
        self.create_widget()
        self.create_layout()
        self.modify_widget()
        self.add_widget_to_layout()
        self.setup_connection()
        self.create_location()

        self.second_layout.setContentsMargins(0, 0, 0, 0)  # supprimer les marges
        self.second_layout.setSpacing(0)  # supprimer les espaces entre les différent widget

        self.setStyleSheet("border: none")  # supprimer les bordures de fenêtre
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint )  # supprimer les barres de navigation
        self.setStyleSheet("background-color: rgb(42,40,40);color:rgb(80,80,80);")
    def create_widget(self):
        self.ls_view = QtWidgets.QListView()
        self.btn_back = QtWidgets.QPushButton("Back")
        self.btn_play = QtWidgets.QPushButton("play")


    def create_layout(self):
        self.second_layout = QtWidgets.QGridLayout(self)
    def modify_widget(self):
        #chamgement du style d affichage du list view pour avoir des icons
        self.ls_view.setViewMode(QtWidgets.QListView.IconMode)
        self.ls_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ls_view.setUniformItemSizes(True)
        self.ls_view.setIconSize(QtCore.QSize(100, 100))

    def add_widget_to_layout(self):
        self.second_layout.addWidget(self.ls_view, 0,0,12,12)
        self.second_layout.addWidget(self.btn_back,0,13,1,1)
        self.second_layout.addWidget(self.btn_play, 1,13,1,1)
    def setup_connection(self):
        self.ls_view.doubleClicked.connect(self.double_clicked_ls_view)
        self.btn_back.clicked.connect(self.back_directory)
        self.btn_play.clicked.connect(self.play_music)

    def back_directory(self):
        index = self.ls_view.currentIndex() #recuperation de l index en cour
        path = f"{self.model.filePath(index)}" # recuperation du path associée
        path = path.replace(f"/{self.model.fileName(index)}","") # recuperation du nom du fichier et retrait de ce nom au path
        self.change_location(path)



    def change_location(self ,path):
        #chamengment de path du Q model index, et du listview
        self.ls_view.setRootIndex(self.model.index(path))# chagement de root path
        self.ls_view.setCurrentIndex(self.model.index(path))# chamgement d'index

    def show_play_bouton(self,show_play_btn):

        if show_play_btn == True :  # affichage du bouton play si show play btn = True
            self.btn_play.show()
        else:
            self.btn_play.hide()



    def create_location(self):
        #creation du Qmodel
        self.model = QtWidgets.QFileSystemModel()
        root_path = QtCore.QDir.rootPath()
        self.model.setRootPath(root_path)
        #affilitation dun Q model au list view
        self.ls_view.setModel(self.model)
        self.ls_view.setRootIndex(self.model.index(root_path))
    def close(self):
        self.close()
    def double_clicked_ls_view(self,index):
        index_item = self.model.index(index.row(), 0, index.parent()) #recuperation de l index
        item_path = self.model.filePath(index_item) #recuperation du path
        if os.path.isfile(item_path): # verif le documen selectione est un fichier
            os.startfile(item_path) # demarrage du fichier

        else:
            self.ls_view.setRootIndex(index) # sinon c est un dossier, entrer dans le dossier

    def play_music(self):
        extentions = [".mp3", ".wave"]
        playlist = os.path.join(os.path.dirname(__file__), 'playlist.m3u')
        with open(playlist, 'w') as f:
            f.write("#EXTM3U")
        for index in self.ls_view.selectedIndexes():
            index_item = self.model.index(index.row(), 0, index.parent())
            item_path = self.model.filePath(index_item)
            item_name = self.model.fileName(index_item)
            if not os.path.isfile(item_path):
                fichiers = glob.glob(item_path +"/**", recursive=True)
                for fichier in fichiers:
                    for extention in extentions:
                        if fichier.endswith(extention):
                            with open(playlist, 'a') as f:
                                f.write(f"\n#EXTINF:0,{fichier.split('/')[-1]}.mp3\n{fichier}")
                            os.startfile(playlist)
            else:
                for extention in extentions:
                    if item_path.endswith(extention):
                        with open(playlist, 'a') as f:
                            f.write(f"\n#EXTINF:0,{item_name}.mp3\n{item_path}")
                        os.startfile(playlist)

    def app_on_top(self,bool_app_on_top):
        if bool_app_on_top == False:
            self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)

            self.show()
            self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnBottomHint)
            self.show()

        else:
            self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnBottomHint)
            self.show()
            self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
            self.show()

    def secondary_windows_close(self):
        self.close()