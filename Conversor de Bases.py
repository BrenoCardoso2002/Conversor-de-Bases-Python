# importações
import sys
import pyperclip
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QPushButton, QMessageBox, QLabel, QRadioButton, QLineEdit


# classe da janela
class Janela(QWidget):
    def __init__(self):
        super().__init__()

        # dados da tela:
        self.topo = 0
        self.esquerda = 0
        self.largura = 430
        self.altura = 275
        self.titulo = 'Conversor'
        self.setFixedSize(self.largura, self.altura)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon('Logo1.png'))
        self.setWindowOpacity(1)

        # Label Opções:
        OptionClose = QPushButton(self)
        OptionClose.move(400, 0)
        OptionClose.setText('...')
        OptionClose.setStyleSheet(
            'QPushButton {font: bold; font-size: 16px; color:red; background: transparent;}QPushButton::pressed{font: bold; font-size: 16px; color:#610B21; background: transparent; }QPushButton::hover{text-decoration: underline;}')
        OptionClose.setCursor(Qt.PointingHandCursor)
        OptionClose.clicked.connect(self.ClickedOptionClose)
        OptionClose.resize(25, 20)

        # Label Titulo na tela:
        Label1 = QLabel(self)
        Label1.move(10, 10)
        Label1.setText('Conversor de Bases:')
        Label1.setStyleSheet('QLabel {font-size: 20px; color: black}')

        # Label Binario:
        Label2 = QLabel(self)
        Label2.move(20, 52)
        Label2.setText('Binário:')
        Label2.setStyleSheet('QLabel {font-size: 18px; color: black}')

        # Label Octal:
        Label3 = QLabel(self)
        Label3.move(20, 87)
        Label3.setText('Octal:')
        Label3.setStyleSheet('QLabel {font-size: 18px; color: black}')

        # Label Decimal:
        Label4 = QLabel(self)
        Label4.move(20, 122)
        Label4.setText('Decimal:')
        Label4.setStyleSheet('QLabel {font-size: 18px; color: black}')

        # Label HexaDecimal:
        Label5 = QLabel(self)
        Label5.move(20, 157)
        Label5.setText('HexaDecimal:')
        Label5.setStyleSheet('QLabel {font-size: 18px; color: black}')

        # Label BaseX:
        Label6 = QLabel(self)
        Label6.move(20, 192)
        Label6.setText('BaseX:')
        Label6.setStyleSheet('QLabel {font-size: 18px; color: black}')

        # Label BaseY:
        Label7 = QLabel(self)
        Label7.move(20, 227)
        Label7.setText('BaseY:')
        Label7.setStyleSheet('QLabel {font-size: 18px; color: black}')

        # Radio Button Aux:
        self.RbAux = QRadioButton(self)
        self.RbAux.move(0, 0)
        self.RbAux.setVisible(False)

        # Radio Button Binario:
        self.RbBinario = QRadioButton(self)
        self.RbBinario.move(140, 57)
        self.RbBinario.clicked.connect(self.RadioClickBinario)

        # Radio Button Octal:
        self.RbOctal = QRadioButton(self)
        self.RbOctal.move(140, 92)
        self.RbOctal.clicked.connect(self.RadioClTxtOctal)

        # Radio Button Decimal:
        self.RbDecimal = QRadioButton(self)
        self.RbDecimal.move(140, 127)
        self.RbDecimal.clicked.connect(self.RadioClickDecimal)

        # Radio Button HexaDecimal:
        self.RbHexaDecimal = QRadioButton(self)
        self.RbHexaDecimal.move(140, 162)
        self.RbHexaDecimal.clicked.connect(self.RadioClickHexaDecimal)

        # Radio Button BaseX:
        self.RbBaseX = QRadioButton(self)
        self.RbBaseX.move(140, 197)
        self.RbBaseX.clicked.connect(self.RadioClickBaseX)

        # Radio Button BaseY:
        self.RbBaseY = QRadioButton(self)
        self.RbBaseY.move(140, 232)
        self.RbBaseY.clicked.connect(self.RadioClickBaseY)

        # Caixa de texto Binario:
        self.TxtBinario = QLineEdit(self)
        self.TxtBinario.move(175, 50)
        self.TxtBinario.resize(175, 25)
        self.TxtBinario.setStyleSheet('QLineEdit {font: bold; font-size: 14px}')
        self.TxtBinario.setEnabled(False)
        self.TxtBinario.textChanged.connect(self.TxtBinarioChanged)

        # Caixa de texto Octal:
        self.TxtOctal = QLineEdit(self)
        self.TxtOctal.move(175, 85)
        self.TxtOctal.resize(175, 25)
        self.TxtOctal.setStyleSheet('QLineEdit {font: bold; font-size: 14px}')
        self.TxtOctal.setEnabled(False)
        self.TxtOctal.textChanged.connect(self.TxtOctalChanged)

        # Caixa de texto Decimal:
        self.TxtDecimal = QLineEdit(self)
        self.TxtDecimal.move(175, 120)
        self.TxtDecimal.resize(175, 25)
        self.TxtDecimal.setStyleSheet('QLineEdit {font: bold; font-size: 14px}')
        self.TxtDecimal.setEnabled(False)
        self.TxtDecimal.textChanged.connect(self.TxtDecimalChanged)

        # Caixa de texto HexaDecimal:
        self.TxtHexaDecimal = QLineEdit(self)
        self.TxtHexaDecimal.move(175, 155)
        self.TxtHexaDecimal.resize(175, 25)
        self.TxtHexaDecimal.setStyleSheet('QLineEdit {font: bold; font-size: 14px}')
        self.TxtHexaDecimal.setEnabled(False)
        self.TxtHexaDecimal.textChanged.connect(self.TxtHexaDecimalChanged)

        # Caixa de texto BaseX:
        self.TxtBaseX = QLineEdit(self)
        self.TxtBaseX.move(175, 190)
        self.TxtBaseX.resize(175, 25)
        self.TxtBaseX.setStyleSheet('QLineEdit {font: bold; font-size: 14px}')
        self.TxtBaseX.setEnabled(False)
        #self.TxtBaseX.textChanged.connect(self.TxtBasesXChanged)

        # Caixa de texto BaseY:
        self.TxtBaseY = QLineEdit(self)
        self.TxtBaseY.move(175, 225)
        self.TxtBaseY.resize(175, 25)
        self.TxtBaseY.setStyleSheet('QLineEdit {font: bold; font-size: 14px}')
        self.TxtBaseY.setEnabled(False)
        # self.TxtBaseY.textChanged.connect(self.TxtBasesYChanged)

        # Caixa de texto BaseX:
        self.TxtNumeroBaseX = QLineEdit(self)
        self.TxtNumeroBaseX.move(80, 190)
        self.TxtNumeroBaseX.resize(50, 25)
        self.TxtNumeroBaseX.setStyleSheet('QLineEdit {font: bold; font-size: 14px}')
        self.TxtNumeroBaseX.setAlignment(Qt.AlignCenter)
        self.TxtNumeroBaseX.setMaxLength(1)
        self.TxtNumeroBaseX.textChanged.connect(self.TxtNumeroBaseXChanged)
        self.TxtNumeroBaseX.setToolTip('2 a 9')

        # Caixa de texto BaseY:
        self.TxtNumeroBaseY = QLineEdit(self)
        self.TxtNumeroBaseY.move(80, 225)
        self.TxtNumeroBaseY.resize(50, 25)
        self.TxtNumeroBaseY.setStyleSheet('QLineEdit {font: bold; font-size: 14px}')
        self.TxtNumeroBaseY.setAlignment(Qt.AlignCenter)
        self.TxtNumeroBaseY.setMaxLength(1)
        self.TxtNumeroBaseY.textChanged.connect(self.TxtNumeroBaseYChanged)
        self.TxtNumeroBaseY.setToolTip('2 a 9')

        # Img Copia Texto Binario:
        CopiaBinario = QPushButton(self)
        CopiaBinario.move(365, 51)
        CopiaBinario.setStyleSheet('QPushButton {background: transparent; image: url(Copiar.png);} QPushButton::pressed{background: transparent; image: url(CopiarPress.png);}')
        CopiaBinario.setCursor(Qt.PointingHandCursor)
        CopiaBinario.clicked.connect(self.CopyBinario)

        # Img Copia Texto Octal:
        CopiaOctal = QPushButton(self)
        CopiaOctal.move(365, 86)
        CopiaOctal.setStyleSheet('QPushButton {background: transparent; image: url(Copiar.png);} QPushButton::pressed{background: transparent; image: url(CopiarPress.png);}')
        CopiaOctal.setCursor(Qt.PointingHandCursor)
        CopiaOctal.clicked.connect(self.CopyOctal)

        # Img Copia Texto Decimal:
        CopiaDecimal = QPushButton(self)
        CopiaDecimal.move(365, 121)
        CopiaDecimal.setStyleSheet('QPushButton {background: transparent; image: url(Copiar.png);} QPushButton::pressed{background: transparent; image: url(CopiarPress.png);}')
        CopiaDecimal.setCursor(Qt.PointingHandCursor)
        CopiaDecimal.clicked.connect(self.CopyDecimal)

        # Img Copia Texto HexaDecimal:
        CopiaHexaDecimal = QPushButton(self)
        CopiaHexaDecimal.move(365, 156)
        CopiaHexaDecimal.setStyleSheet('QPushButton {background: transparent; image: url(Copiar.png);} QPushButton::pressed{background: transparent; image: url(CopiarPress.png);}')
        CopiaHexaDecimal.setCursor(Qt.PointingHandCursor)
        CopiaHexaDecimal.clicked.connect(self.CopyHexaDecimal)

        # Img Copia Texto BaseN:
        CopiaBaseX = QPushButton(self)
        CopiaBaseX.move(365, 191)
        CopiaBaseX.setStyleSheet('QPushButton {background: transparent; image: url(Copiar.png);} QPushButton::pressed{background: transparent; image: url(CopiarPress.png);}')
        CopiaBaseX.setCursor(Qt.PointingHandCursor)
        CopiaBaseX.clicked.connect(self.CopyBaseX)

        # Img Copia Texto BaseY:
        CopiaBaseY = QPushButton(self)
        CopiaBaseY.move(365, 226)
        CopiaBaseY.setStyleSheet('QPushButton {background: transparent; image: url(Copiar.png);} QPushButton::pressed{background: transparent; image: url(CopiarPress.png);}')
        CopiaBaseY.setCursor(Qt.PointingHandCursor)
        CopiaBaseX.clicked.connect(self.CopyBaseY)

        # Abre a Janela
        self.CarregarJanela()

    # Função que Carrega a Janela
    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.center()
        self.show()

    # Centraliza na tela:
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # Função de Clique das opções:
    def ClickedOptionClose(self):
        box = QMessageBox()
        box.setWindowTitle('Opções!')
        box.setText('Clique no botão com a opcão desejada!')
        box.setIcon(QMessageBox.Question)
        pixmap = QPixmap('Logo.png').scaledToHeight(32, Qt.SmoothTransformation)
        box.setIconPixmap(pixmap)
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        buttonY = box.button(QMessageBox.Yes)
        buttonY.setText('Fechar')
        buttonX = box.button(QMessageBox.No)
        buttonX.setText('Minimizar')
        buttonZ = box.button(QMessageBox.Cancel)
        buttonZ.setText('Cancelar')
        box.exec_()
        # Verifica no que o usuário clicou:
        if box.clickedButton() == buttonY:
            sys.exit(0)
        elif box.clickedButton() == buttonX:
            self.showMinimized()

    # Função que desabilita tudo:
    def DisableAll(self):
        self.TxtBinario.setEnabled(False)
        self.TxtOctal.setEnabled(False)
        self.TxtDecimal.setEnabled(False)
        self.TxtHexaDecimal.setEnabled(False)
        self.TxtBaseX.setEnabled(False)
        self.TxtBaseY.setEnabled(False)
        self.RbBinario.setChecked(False)
        self.RbOctal.setChecked(False)
        self.RbHexaDecimal.setChecked(False)
        self.RbBaseX.setChecked(False)
        self.RbBaseY.setChecked(False)
        self.TxtBinario.setText('')
        self.TxtOctal.setText('')
        self.TxtDecimal.setText('')
        self.TxtHexaDecimal.setText('')
        self.TxtBaseX.setText('')
        self.TxtBaseY.setText('')

    # Função que copia o numero binario:
    def CopyBinario(self):
        Numero = self.TxtBinario.text()
        pyperclip.copy(Numero)

    # Função que copia o octal:
    def CopyOctal(self):
        Numero = self.TxtOctal.text()
        pyperclip.copy(Numero)

    # Função que copia o numero Decimal:
    def CopyDecimal(self):
        Numero = self.TxtDecimal.text()
        pyperclip.copy(Numero)

    # Função que copia o numero HexaDecimal
    def CopyHexaDecimal(self):
        Numero = self.TxtHexaDecimal.text()
        pyperclip.copy(Numero)

    # Função que copia o numero da base X:
    def CopyBaseX(self):
        Numero = self.TxtBaseX.text()
        pyperclip.copy(Numero)

    # Função que copia o numero da base Y:
    def CopyBaseY(self):
        Numero = self.TxtBaseY.text()
        pyperclip.copy(Numero)

    # Função de clique Radio button binario
    def RadioClickBinario(self):
        self.DisableAll()
        self.TxtBinario.setEnabled(True)
        self.TxtBinario.setFocus()

    # Função de clique Radio button octal
    def RadioClTxtOctal(self):
        self.DisableAll()
        self.TxtOctal.setEnabled(True)
        self.TxtOctal.setFocus()

    # Função de clique Radio button Decimal
    def RadioClickDecimal(self):
        self.DisableAll()
        self.TxtDecimal.setEnabled(True)
        self.TxtDecimal.setFocus()

    # Função de clique Radio button HexaDecimal
    def RadioClickHexaDecimal(self):
        self.DisableAll()
        self.TxtHexaDecimal.setEnabled(True)
        self.TxtHexaDecimal.setFocus()

    # Função de clique Radio button BaseY
    def RadioClickBaseY(self):
        self.DisableAll()
        self.TxtBaseY.setEnabled(True)
        self.TxtBaseY.setFocus()

    # Função de clique Radio button Base X:
    def RadioClickBaseX(self):
        self.DisableAll()
        self.TxtBaseX.setEnabled(True)
        self.TxtBaseX.setFocus()

    # Função de mudança de texto binario
    def TxtBinarioChanged(self):
        Numero = self.TxtBinario.text()
        if Numero != '':
            if Numero[len(Numero) - 1] != '0' and Numero[len(Numero) - 1] != '1':
                Numero = Numero[:-1]
        self.TxtBinario.setText(Numero)
        self.ConverteBases(Numero, 2)

    # Função de mudança de texto Octal
    def TxtOctalChanged(self):
        Numero = self.TxtOctal.text()
        if Numero != '':
            if Numero[len(Numero) - 1] != '0' and Numero[len(Numero) - 1] != '1' and Numero[len(Numero) - 1] != '2' and Numero[len(Numero) - 1] != '3' and Numero[len(Numero) - 1] != '4' and Numero[len(Numero) - 1] != '5' and Numero[len(Numero) - 1] != '6' and Numero[len(Numero) - 1] != '7':
                Numero = Numero[:-1]
        self.TxtOctal.setText(Numero)
        self.ConverteBases(Numero, 8)

    # Função de mudança de texto Decimal
    def TxtDecimalChanged(self):
        Numero = self.TxtDecimal.text()
        if Numero != '':
            if Numero[len(Numero) - 1] != '0' and Numero[len(Numero) - 1] != '1' and Numero[len(Numero) - 1] != '2' and Numero[len(Numero) - 1] != '3' and Numero[len(Numero) - 1] != '4' and Numero[len(Numero) - 1] != '5' and Numero[len(Numero) - 1] != '6' and Numero[len(Numero) - 1] != '7' and Numero[len(Numero) - 1] != '8' and Numero[len(Numero) - 1] != '9':
                Numero = Numero[:-1]
        self.TxtDecimal.setText(Numero)
        self.ConverteBases(Numero, 10)

    # Função de mudança de texto HexaDecimal
    def TxtHexaDecimalChanged(self):
        Numero = self.TxtHexaDecimal.text()
        Numero = Numero.upper()
        if Numero != '':
            if Numero[len(Numero) - 1] != '0' and Numero[len(Numero) - 1] != '1' and Numero[len(Numero) - 1] != '2' and Numero[len(Numero) - 1] != '3' and Numero[len(Numero) - 1] != '4' and Numero[len(Numero) - 1] != '5' and Numero[len(Numero) - 1] != '6' and Numero[len(Numero) - 1] != '7' and Numero[len(Numero) - 1] != '8' and Numero[len(Numero) - 1] != '9' and Numero[len(Numero) - 1] != 'A' and Numero[len(Numero) - 1] != 'B' and Numero[len(Numero) - 1] != 'C' and Numero[len(Numero) - 1] != 'D' and Numero[len(Numero) - 1] != 'E' and Numero[len(Numero) - 1] != 'F':
                Numero = Numero[:-1]
        self.TxtHexaDecimal.setText(Numero)
        self.ConverteBases(Numero, 16)

    # Função de mudança de texto Numero BaseX
    def TxtNumeroBaseXChanged(self):
        Numero = self.TxtNumeroBaseX.text()
        if Numero != '':
            Lista = []
            for i in range(10):
                Lista.append('{}'.format(i + 2))
            if Numero[len(Numero) - 1] not in Lista:
                Numero = Numero[:-1]
        self.TxtNumeroBaseX.setText(Numero)
        self.DisableAll()
        self.RbAux.setChecked(True)

    # Função de mudança de texto Numero BaseY
    def TxtNumeroBaseYChanged(self):
        Numero = self.TxtNumeroBaseY.text()
        if Numero != '':
            Lista = []
            for i in range(8):
                Lista.append('{}'.format(i + 2))
            if Numero[len(Numero) - 1] not in Lista:
                Numero = Numero[:-1]
        self.TxtNumeroBaseY.setText(Numero)
        self.DisableAll()
        self.RbAux.setChecked(True)

    # Função de mudança de texto BaseY
    def TxtBasesYChanged(self):
        Numero = self.TxtBaseY.text()
        Base = self.TxtNumeroBaseY.text()
        if Base == '':
            Numero = ''
        else:
            if Numero != '':
                if Base == '2':
                    Lista = ['0', '1', '2']
                elif Base == '3':
                    Lista = ['0', '1', '2', '3']
                elif Base == '4':
                    Lista = ['0', '1', '2', '3']
                elif Base == '5':
                    Lista = ['0', '1', '2', '3', '4']
                elif Base == '6':
                    Lista = ['0', '1', '2', '3', '4', '5']
                elif Base == '7':
                    Lista = ['0', '1', '2', '3', '4', '5', '6']
                elif Base == '8':
                    Lista = ['0', '1', '2', '3', '4', '5', '6', '7']
                else:
                    Lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
                if Numero[len(Numero) - 1] not in Lista:
                    Numero = Numero[:-1]
        self.TxtBaseY.setText(Numero)
        self.ConverteBases(Numero, Base)

    # Função de mudança de texto BaseX
    def TxtBasesXChanged(self):
        Numero = self.TxtBaseX.text()
        Base = self.TxtNumeroBaseX.text()
        if Base == '':
            Numero = ''
        else:
            if Numero != '':
                if Base == '2':
                    Lista = ['0', '1', '2']
                elif Base == '3':
                    Lista = ['0', '1', '2', '3']
                elif Base == '4':
                    Lista = ['0', '1', '2', '3']
                elif Base == '5':
                    Lista = ['0', '1', '2', '3', '4']
                elif Base == '6':
                    Lista = ['0', '1', '2', '3', '4', '5']
                elif Base == '7':
                    Lista = ['0', '1', '2', '3', '4', '5', '6']
                elif Base == '8':
                    Lista = ['0', '1', '2', '3', '4', '5', '6', '7']
                else:
                    Lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
                if Numero[len(Numero) - 1] not in Lista:
                    Numero = Numero[:-1]
        self.TxtBaseX.setText(Numero)
        self.ConverteBases(Numero, Base)

    # Função que Converte as Bases
    def ConverteBases(self, Numero, Base):
        if Base != '' and Numero != '':
            # converte para decimal
            Decimal = int(Numero, Base)
            self.TxtDecimal.setText(str(Decimal))
            # converte para octal:
            Octal = oct(Decimal)
            Octal = Octal.replace('0o', '')
            self.TxtOctal.setText(Octal)
            # converte para binario:
            Bin = bin(Decimal)
            Bin = Bin.replace('0b', '')
            self.TxtBinario.setText(Bin)
            # converte para hexadecimal
            Hexa = hex(Decimal)
            Hexa = Hexa.replace('0x', '')
            Hexa = Hexa.upper()
            self.TxtHexaDecimal.setText(Hexa)
            print('')
            # converte para base X:
            if self.TxtNumeroBaseX.text() != '':
                Num = int(self.ConverteX(Decimal))
                Num = str(Num)
                self.TxtBaseX.setText(Num)
            # converte para base Y:
            if self.TxtNumeroBaseY.text() != '':
                Num = int(self.ConverteY(Decimal))
                Num = str(Num)
                self.TxtBaseY.setText(Num)
        else:
            self.TxtDecimal.setText('')
            self.TxtOctal.setText('')
            self.TxtBinario.setText('')
            self.TxtHexaDecimal.setText('')
            self.TxtBaseX.setText('')
            self.TxtBaseY.setText('')

    # função que converte para base X
    def ConverteX(self, numDecimal):
        base = int(self.TxtNumeroBaseX.text())
        numDecimal = int(numDecimal)
        if numDecimal != 0:
            numConvertido = ''
            while numDecimal > 0:
                resto = numDecimal % base
                numConvertido = str(resto) + numConvertido
                numDecimal = numDecimal // base
        else:
            numConvertido = ''
        return numConvertido

    # função que converte para base Y
    def ConverteY(self, numDecimal):
        base = int(self.TxtNumeroBaseY.text())
        numDecimal = int(numDecimal)
        if numDecimal != 0:
            numConvertido = ''
            while numDecimal > 0:
                resto = numDecimal % base
                numConvertido = str(resto) + numConvertido
                numDecimal = numDecimal // base
        else:
            numConvertido = ''
        return numConvertido


# Inicializa Tela
aplicacao = QApplication(sys.argv)
Window = Janela()
sys.exit(aplicacao.exec_())
