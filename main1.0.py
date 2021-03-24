import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.lang import Builder

kv = '''

<MyGrid>

    ausgabe: ausgabe
    deineeingabe: deineeingabe
    btnhalb: btnhalb
    btndreiviertel: btndreiviertel
    btnviertel: btnviertel
    btnviertelvor: btnviertelvor
    btnviertelnach: btnviertelnach

    btnvormittags: btnvormittags
    btnnachmittags: btnnachmittags

    oben: oben

    btneins: btneins
    btnzwei: btnzwei
    btndrei: btndrei
    btnvier: btnvier
    btnfuenf: btnfuenf
    btnsechs: btnsechs
    btnsieben: btnsieben
    btnacht: btnacht
    btnneun: btnneun
    btnzehn: btnzehn
    btnelf: btnelf
    btnzwoelf: btnzwoelf

    fehler: fehler


    GridLayout:
        cols: 1
        size: root.width -30, root.height -40
        pos: 15, 20


        Label:
            text: "Bitte tippe die Uhrzeit durch die Buttons ein!"

        GridLayout:
            cols:1
            id:oben

        Button:
            on_release: root.btnprinzipien(self, "Halb")
            on_press: root.cleanausgabe()
            on_press: (lambda *largs: setattr(self, 'text', 'OK'))()
            on_release: (lambda *largs: setattr(self, 'text', 'Halb'))()
            id: btnhalb
            text: "Halb"


        GridLayout:
            cols:2

            Button:
                id: btndreiviertel
                text: "Dreiviertel"
                on_release: root.btnprinzipien(self, "Dreiviertel")
                on_press: (lambda *largs: setattr(self, 'text', 'OK'))()
                on_press: root.cleanausgabe()
                on_release: (lambda *largs: setattr(self, 'text', 'Dreiviertel'))()
            Button:
                id: btnviertel
                text: "Viertel"
                on_release: root.btnprinzipien(self, "Viertel")
                on_press: (lambda *largs: setattr(self, 'text', 'OK'))()
                on_press: root.cleanausgabe()
                on_release: (lambda *largs: setattr(self, 'text', 'Viertel'))()

        GridLayout:
            cols:2

            Button:
                id: btnviertelvor
                text: "Viertel_vor"
                on_release: root.btnprinzipien(self, "Viertel_vor")
                on_press: (lambda *largs: setattr(self, 'text', 'OK'))()
                on_press: root.cleanausgabe()
                on_release: (lambda *largs: setattr(self, 'text', 'Viertel_vor'))()
            Button:
                id: btnviertelnach
                text: "Viertel_nach"
                on_release: root.btnprinzipien(self, "Viertel_nach")
                on_press: (lambda *largs: setattr(self, 'text', 'OK'))()
                on_press: root.cleanausgabe()
                on_release: (lambda *largs: setattr(self, 'text', 'Viertel_nach'))()
        Label:
            text:""
        GridLayout:
            cols:6

            Button:
                id: btneins
                on_press: root.zahlenbtnsaction(self, "1"), (lambda *largs: setattr(self, 'text', 'OK'))(), root.cleanausgabe(),
                on_release: root.btnzahlenstundenanpassen(), (lambda *largs: setattr(self, 'text', '1'))()
                text: "1"
            Button:
                id: btnzwei
                on_press: root.zahlenbtnsaction(self, "2"), (lambda *largs: setattr(self, 'text', 'OK'))() , root.cleanausgabe()
                on_release: root.btnzahlenstundenanpassen(), (lambda *largs: setattr(self, 'text', '2'))()
                text: "2"
            Button:
                id: btndrei
                on_press: root.zahlenbtnsaction(self, "3"), (lambda *largs: setattr(self, 'text', 'OK'))(), root.cleanausgabe(),
                on_release: root.btnzahlenstundenanpassen(), (lambda *largs: setattr(self, 'text', '3'))()
                text: "3"
            Button:
                id: btnvier
                on_press: root.zahlenbtnsaction(self, "4"), (lambda *largs: setattr(self, 'text', 'OK'))(), root.cleanausgabe(),
                on_release: root.btnzahlenstundenanpassen(), (lambda *largs: setattr(self, 'text', '4'))()
                text: "4"
            Button:
                id: btnfuenf
                on_press: root.zahlenbtnsaction(self, "5"), (lambda *largs: setattr(self, 'text', 'OK'))(), root.cleanausgabe(),
                on_release: root.btnzahlenstundenanpassen(), (lambda *largs: setattr(self, 'text', '5'))()
                text: "5"
            Button:
                id: btnsechs
                on_press: root.zahlenbtnsaction(self, "6"), (lambda *largs: setattr(self, 'text', 'OK'))(), root.cleanausgabe(),
                on_release: root.btnzahlenstundenanpassen(), (lambda *largs: setattr(self, 'text', '6'))()
                text: "6"

        GridLayout:
            cols:6

            Button:
                id: btnsieben
                on_press: root.zahlenbtnsaction(self, "7"), (lambda *largs: setattr(self, 'text', 'OK'))(), root.cleanausgabe(),
                on_release: root.btnzahlenstundenanpassen(), (lambda *largs: setattr(self, 'text', '7'))()
                text: "7"
            Button:
                id: btnacht
                on_press: root.zahlenbtnsaction(self, "8"), (lambda *largs: setattr(self, 'text', 'OK'))(), root.cleanausgabe(),
                on_release: root.btnzahlenstundenanpassen(), (lambda *largs: setattr(self, 'text', '8'))()
                text: "8"
            Button:
                id: btnneun
                on_press: root.zahlenbtnsaction(self, "9"), (lambda *largs: setattr(self, 'text', 'OK'))(), root.cleanausgabe(),
                on_release: root.btnzahlenstundenanpassen(), (lambda *largs: setattr(self, 'text', '9'))()
                text: "9"
            Button:
                id: btnzehn
                on_press: root.zahlenbtnsaction(self, "10"), (lambda *largs: setattr(self, 'text', 'OK'))(), root.cleanausgabe(),
                on_release: root.btnzahlenstundenanpassen(), (lambda *largs: setattr(self, 'text', '10'))()
                text: "10"
            Button:
                id: btnelf
                on_press: root.zahlenbtnsaction(self, "11"), (lambda *largs: setattr(self, 'text', 'OK'))(), root.cleanausgabe(),
                on_release: root.btnzahlenstundenanpassen(), (lambda *largs: setattr(self, 'text', '11'))()
                text: "11"
            Button:
                id: btnzwoelf
                on_press: root.zahlenbtnsaction(self, "12"), (lambda *largs: setattr(self, 'text', 'OK'))(), root.cleanausgabe(),
                on_release: root.btnzahlenstundenanpassen(), (lambda *largs: setattr(self, 'text', '12'))()
                text: "12"
        Label:
            text: ""

        GridLayout:
            cols:2

            Button:
                text: "vormittags"
                id: btnvormittags
                on_press: (lambda *largs: setattr(self, 'text', 'Berechne...'))()
                on_release: root.btntageszeit(self, "vormittags"), root.anpassen(), root.stundenanpassen(), (lambda *largs: setattr(self, 'text', 'vormittags'))()
            Button:
                text: "nachmittags"
                id: btnnachmittags

                on_press: (lambda *largs: setattr(self, 'text', 'Berechne...'))()
                on_release: root.btntageszeit(self, "nachmittags"), root.anpassen(), root.stundenanpassen(), (lambda *largs: setattr(self, 'text', 'nachmittags'))()


        Label:
            text: ""

        GridLayout:
            cols:3

            TextInput:
                id: deineeingabe
                background_color: (0, 0, 0, 0)
                foreground_color: (1, 1, 1, 1)


            Label:
                text: "="
                font_size: 35


            TextInput:
                id: ausgabe
                multiline:False
                text: "00:00"
                bold:True
                background_color: (0, 0, 0, 0)
                foreground_color: (1, 1, 1, 1)

        GridLayout:
            cols:1
            Label:
                text: "Bitte gib erst einen Ausdruck oder eine Zahl ein!"
                id: fehler
                opacity: 0

'''
Builder.load_string(kv)

class MyGrid(Widget):
# TextInputs für Anzeige von Eingabe und Ergebnis
    deineeingabe = ObjectProperty(None)
    ausgabe = ObjectProperty(None)
# Buttons für die Sonderausdrücke
    btnhalb = ObjectProperty(None)
    btndreiviertel = ObjectProperty(None)
    btnviertel = ObjectProperty(None)
    btnviertelvor = ObjectProperty(None)
    btnviertelnach = ObjectProperty(None)
# Buttons vormittags & nachmittags
    btnvormittags = ObjectProperty(None)
    btnnachmittags = ObjectProperty(None)

    fehler = ObjectProperty(None)

    def hidelabel(self):
        self.fehler.opacity = 0

# Schreibt die Namen der Buttins Halb, Viertel, Dreiviertel, Viertel_vor, Viertel_nach in die Ergebniszeile
    def btnprinzipien(self, *arg):
        self.deineeingabe.text = arg[1]
# Setzt die Ergebnisausgabe bei Neueingabe von Buttons Halb, Viertel, Dreiviertel, Viertel_vor, Viertel_nach wieder auf 00:00
    def cleanausgabe(self):
        self.ausgabe.text = "00:00"
        MyGrid.hidelabel(self)
# Schreibt den Wert der Zahlen Buttons 1 bis 12 in die Eingabezeile (als string)
    def zahlenbtnsaction(self, *arg):
        callenderbtnwert = arg[1]
        deineeingabeliste = self.deineeingabe.text.split()


        if len(deineeingabeliste) == 0:
            self.deineeingabe.text = callenderbtnwert
        elif deineeingabeliste[0] in ["1","2","3","4","5","6","7","8","9","10","11","12"]:
            self.deineeingabe.text = callenderbtnwert
        else:
            self.deineeingabe.text = deineeingabeliste[0] + " " + callenderbtnwert

# Funktionalität der Buttons vormittags und nachmittags
    def btntageszeit(self, *arg):
        tageszeit = arg[1]
        deineeingabetext = self.deineeingabe.text
        deineeingabeliste = deineeingabetext.split()

        if len(deineeingabeliste) > 1 and deineeingabeliste[1] in ["vormittags", "nachmittags"]:
            self.deineeingabe.text = deineeingabeliste[0] + " " + tageszeit
        elif len(deineeingabeliste) > 2:
            self.deineeingabe.text = deineeingabeliste[0] + " " + deineeingabeliste[1] + " " + tageszeit
        else:
            self.deineeingabe.text = self.deineeingabe.text + " " + tageszeit
# Passt bei nachmittags das Format an 24h Format
    def stundenanpassen(self):
        statementlist = self.ausgabe.text.split(":")
        deineeingabelist = self.deineeingabe.text.split()
        uhr = {0:12,1:13, 2:14, 3:15, 4:16, 5:17, 6:18, 7:19, 8:20, 9:21, 10:22, 11:23, 12:12}

        if len(deineeingabelist) == 1:
            self.deineeingabe.text = ""
            self.fehler.opacity = 1
        elif len(deineeingabelist) > 2:
            if "nachmittags" == deineeingabelist[2] and int(statementlist[0]) < 13 and int(statementlist[0]) in uhr:
                self.ausgabe.text = str(uhr[int(statementlist[0])]) + ":" + statementlist[1]
        elif len(deineeingabelist) < 3:
            if "nachmittags" == deineeingabelist[1] and int(deineeingabelist[0]) in uhr:
                self.ausgabe.text = str(uhr[int(deineeingabelist[0])]) + ":00"
            elif "vormittags" == deineeingabelist[1] and int(deineeingabelist[0]) < 10:
                self.ausgabe.text = "0" + deineeingabelist[0] + ":00"
        else:
            self.ausgabe.text = "0" + deineeingabelist[0] + ":00"

# Eigentliche Funktionalität: Wendet das Prinzip Halb, Viertel, Dreiviertel, Viertel_vor, Viertel_nach auf die Eingabezeile an und gibt das Ergebnis in der Ausgabezeile wieder
    def anpassen(self):
        statementlist = self.deineeingabe.text.split()

        if len(statementlist) > 2:


        #stelllt eine 0 vor Zahlen kleiner 10
            if "Halb" == statementlist[0] and int(statementlist[1]) < 11 and "vormittags" == statementlist[2]:
                self.ausgabe.text = "0" + str(int(statementlist[1]) - 1) + ":30"
        # Regelt den Ausnahmefall Halb 12 nachmittags
            elif "Halb" == statementlist[0] and "00" == statementlist[1] and "nachmittags" == statementlist[2]:
                self.ausgabe.text = "23:30"
            elif "Halb" == statementlist[0]:
                self.ausgabe.text = str(int(statementlist[1]) - 1) + ":30"

    # dreiviertel  2 13:45
        #stelllt eine 0 vor Zahlen kleiner 10
            if "Dreiviertel" == statementlist[0] and int(statementlist[1]) < 11 and "vormittags" == statementlist[2]:
                self.ausgabe.text = "0" + str(int(statementlist[1]) - 1) + ":45"
        # Regelt den Ausnahmefall Dreiviertel 12 nachmittags
            elif "Dreiviertel" == statementlist[0] and "12" == statementlist[1] and "nachmittags" == statementlist[2]:
                self.ausgabe.text = "23:45"
            elif "Dreiviertel" == statementlist[0]:
                self.ausgabe.text = str(int(statementlist[1]) - 1) + ":45"

    # viertel 2 13:15
        #stelllt eine 0 vor Zahlen kleiner 10
            if "Viertel" == statementlist[0] and int(statementlist[1]) < 11 and "vormittags" == statementlist[2]:
                self.ausgabe.text = "0" + str(int(statementlist[1]) - 1) + ":15"
        # Regelt den Ausnahmefall Dreiviertel 12 nachmittags
            elif "Viertel" == statementlist[0] and "12" == statementlist[1] and "nachmittags" == statementlist[2]:
                self.ausgabe.text = "23:15"
            elif "Viertel" == statementlist[0]:
                self.ausgabe.text = str(int(statementlist[1]) - 1) + ":15"

    # Viertel_vor 2 13:45
        #stelllt eine 0 vor Zahlen kleiner 10
            if "Viertel_vor" == statementlist[0] and int(statementlist[1]) < 11 and "vormittags" == statementlist[2]:
                self.ausgabe.text = "0" + str(int(statementlist[1]) - 1) + ":45"
            # Regelt den Ausnahmefall Dreiviertel 12 nachmittags
            elif "Viertel_vor" == statementlist[0] and "12" == statementlist[1] and "nachmittags" == statementlist[2]:
                self.ausgabe.text = "23:45"
            elif "Viertel_vor" == statementlist[0]:
                self.ausgabe.text = str(int(statementlist[1]) - 1) + ":45"

        # Viertel_nach 2 14:15
            #stelllt eine 0 vor Zahlen kleiner 10
            if "Viertel_nach" == statementlist[0] and int(statementlist[1]) < 10 and "vormittags" == statementlist[2]:
                self.ausgabe.text = "0" + str(int(statementlist[1])) + ":15"
            # Regelt den Ausnahmefall Dreiviertel 12 nachmittags
            elif "Viertel_nach" == statementlist[0] and "12" == statementlist[1] and "vormittags" == statementlist[2]:
                self.ausgabe.text = "00:15"
            elif "Viertel_nach" == statementlist[0]:
                self.ausgabe.text = str(int(statementlist[1])) + ":15"

# Regelt die Ergebnisausgabe auf das Format "00:00"
    def btnzahlenstundenanpassen(self):
        deineeingabelist = self.deineeingabe.text.split()

        if len(deineeingabelist) < 2:
            if int(deineeingabelist[0]) < 10:
                self.ausgabe.text = "0" + deineeingabelist[0] + ":00"
            else:
                self.ausgabe.text = deineeingabelist[0] + ":00"


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__== "__main__":
    MyApp().run()
