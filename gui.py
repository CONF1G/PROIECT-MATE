import PySimpleGUI as gui
import prog
import numpy as np

from prog import *


L_Functie = [
    [gui.Text("Introduceti Functia:")],
    [gui.In(key="-Functie-")],
    [gui.Button("Ok", key="F")]
]

L_Domeniu = [
    [gui.Text("Introduceti Domeniul:")],
    [gui.In(key="-Domeniu-")],
    [gui.Text("Introduceti puncte scoase din domeniu (daca exista)")],
    [gui.Text("(separate prin spatii)")],
    [gui.In(key="-PSD-")],
    [gui.Button("Ok",key="D")]
]

L_Derivata1 = [
    [gui.Text("Introduceti Derivata I")],
    [gui.In(key="-Derivata1-")],
    [gui.Button("Ok", key="D1")]
]

L_Derivata2 = [
    [gui.Text("Introduceti Derivata II")],
    [gui.In(key="-Derivata2-")],
    [gui.Button("Ok", key="D2")]
]

L_BadEnd = [
    [gui.Text("Raspuns Gresit")]
]

L_GoodEnd = [
    [gui.Text("Felicitari!!!")]
]


layout = [
    #[gui.pin(gui.Column([[gui.Text("Punctaj: 0", key="P")]], key="-P-", expand_x=True, expand_y=True))],
    [gui.pin(gui.Column(L_Functie, key="-LF-", expand_x=True, expand_y=True))],
    [gui.pin(gui.Column(L_Domeniu,visible=False, key="-LDom-", expand_x=True, expand_y=True))],
    [gui.pin(gui.Column(L_Derivata1, visible=False, key="-LDeriv1-", expand_x=True, expand_y=True))],
    [gui.pin(gui.Column(L_Derivata2, visible=False, key="-LDeriv2-", expand_x=True, expand_y=True))],
    [gui.pin(gui.Column(L_BadEnd, visible=False, key="-LBadEnd-", expand_x=True, expand_y=True))],
    [gui.pin(gui.Column(L_GoodEnd, visible=False, key="-LGoodEnd-", expand_x=True, expand_y=True))]

]


window = gui.Window(title="Derivate si Functii", layout=layout, )


def reset():
    for i in ["-LF-", "-LDom-", "-LDeriv1-", "-LDeriv2-", "-LBadEnd-", "-LGoodEnd-"]:
        window[i].update(visible=False)

p=0

while True:
    event, values = window.read()
    
    if event == "F":
        reset()
        window["-LDom-"].update(visible=True)

    if event == "D":
        reset()
        if Domain_Chk(values["-Functie-"], values["-Domeniu-"]):
            window["-LDeriv1-"].update(visible=True)
        else:
            window["-LBadEnd-"].update(visible=True)
    
    if event == "D1":
        reset()
        if D1_Chk(values["-Functie-"], values["-Derivata1-"]):
            window["-LDeriv2-"].update(visible=True)
            p = p + 1
        else:
            window["-LBadEnd-"].update(visible=True)

    if event =="D2":
        reset()
        if D2_Chk(values["-Functie-"], values["-Derivata2-"]):
            window["-LGoodEnd-"].update(visible=True)
            y = np.linspace(-5,5)
            Grafic(values["-Functie-"], y, func(values["-Functie-"], y), gf(values["-Functie-"], y))
            gui.popup(title="Graficul Functiei",image="graf.png")
            p = p + 1
        else:
            window["-LBadEnd-"].update(visible=True)

    #window["P"].update(f"Punctaj: {p}")

    if event == gui.WIN_CLOSED:
        break

window.close()

