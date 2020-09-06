import schemdraw
import schemdraw.elements as elm
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPixmap

from NMOS import NMOS
from PMOS import PMOS

from PySide2.QtWidgets import *

# init circuit elements
d = schemdraw.Drawing()
M6 = d.add(PMOS, label='M6', flip=True)
L1 = d.add(elm.Line(d='d', at=M6.S))
d.add(elm.Line(d='r'))
M1b = d.add(PMOS, label='M1b', anchor='D', reverse=True, flip=True)
d.add(elm.Line(d='l', at=L1.end))
M1a = d.add(PMOS, label='M1a', anchor='D', reverse=True)
d.add(elm.Line(d='d', at=M1b.S))
d.add(elm.Line(d='r'))
L2 = d.add(elm.Line(d='r'))
d.add(elm.Line(d='u', at=L2.end))
M3b = d.add(NMOS, label='M3b', anchor='S', reverse=True, theta=180)
d.add(elm.Line(d='d', at=L2.end))
M2b = d.add(NMOS, label='M2b', anchor='D', reverse=True, theta=180)
d.add(elm.Line(d='d', at=M2b.S))
d.add(elm.Ground())
d.add(elm.Line(d='u', at=M3b.D))
M4b = d.add(PMOS, label='M4b', anchor='S', reverse=True, theta=180)
d.add(elm.Line(d='u', at=M4b.D))
M5b = d.add(PMOS, label='M5b', anchor='D', reverse=True, flip=True, theta=180)
d.add(elm.Line(d='u', at=M5b.S))

d.add(elm.Line(d='d', at=M1a.S))
d.add(elm.Line(d='l'))
L4 = d.add(elm.Line(d='l'))
d.add(elm.Line(d='u', at=L4.end))
M3a = d.add(NMOS, label='M3a', anchor='S', theta=180)
d.add(elm.Line(d='d', at=L4.end))
M2a = d.add(NMOS, label='M2a', anchor='D', theta=180)
d.add(elm.Line(d='d', at=M2a.S))
d.add(elm.Ground())
d.add(elm.Line(d='u', at=M3a.D))
M4a = d.add(PMOS, label='M4a', anchor='S', theta=180)
d.add(elm.Line(d='u', at=M4a.D))
M5a = d.add(PMOS, label='M5a', anchor='D', flip=True, theta=180)
d.add(elm.Line(d='u', at=M5a.S))

d.add(elm.Line(d='r'))
d.add(elm.Line(d='r'))
d.add(elm.Line(d='r'))
d.add(elm.Line(d='r'))
d.add(elm.Line(d='r'))
d.add(elm.Line(d='r'))

d.add(elm.Line(d='u', at=M6.D))
d.add(elm.Line(d='u'))
d.add(elm.Line(d='u'))
d.add(elm.Vdd)

d.add(elm.Line(d='r', at=M5a.G))
d.add(elm.Line(d='r'))
d.add(elm.Line(d='r'))
d.add(elm.Line(d='r'))
d.add(elm.Line(d='r'))

d.add(elm.Line(d='r', at=M2a.G))
d.add(elm.Line(d='r'))
d.add(elm.Line(d='r'))
d.add(elm.Line(d='r'))
d.add(elm.Line(d='r'))


def clear_old_widgets():
    for i in reversed(range(draw_container.count())):
        draw_container.itemAt(i).widget().deleteLater()
    for i in range(1, len(M1a.segments)):
        M1a.segments[i].color = 'black'
        M1b.segments[i].color = 'black'
        M2a.segments[i].color = 'black'
        M2b.segments[i].color = 'black'
        M3a.segments[i].color = 'black'
        M3b.segments[i].color = 'black'
        M4a.segments[i].color = 'black'
        M4b.segments[i].color = 'black'
        M5a.segments[i].color = 'black'
        M5b.segments[i].color = 'black'
        M6.segments[i].color = 'black'



def update_schematic_colors(item):

    for i in range(1, len(M1a.segments)):
        if item == "M1":
            M1a.segments[i].color = 'red'
            M1b.segments[i].color = 'red'
        elif item == "M2":
            M2a.segments[i].color = 'red'
            M2b.segments[i].color = 'red'
        elif item == "M3":
            M3a.segments[i].color = 'red'
            M3b.segments[i].color = 'red'
        elif item == "M4":
            M4a.segments[i].color = 'red'
            M4b.segments[i].color = 'red'
        elif item == "M5":
            M5a.segments[i].color = 'red'
            M5b.segments[i].color = 'red'
        elif item == "M6":
            M6.segments[i].color = 'red'

    d.save('schemdraw.png')
    pixmap = QPixmap("schemdraw.png")
    scroll = QScrollArea()
    schem = QLabel()
    schem.setPixmap(pixmap)
    schem.setAlignment(Qt.AlignCenter)
    # removing old widgets
    clear_old_widgets()
    scroll.setWidget(schem)
    scroll.setAlignment(Qt.AlignCenter)
    draw_container.addWidget(scroll)


# init the application
def item_selected():
    itemData = tools_list.currentItem().text()
    if itemData.__contains__("M1"):
        update_schematic_colors("M1")
    elif itemData.__contains__("M2"):
        update_schematic_colors("M2")
    elif itemData.__contains__("M3"):
        update_schematic_colors("M3")
    elif itemData.__contains__("M4"):
        update_schematic_colors("M4")
    elif itemData.__contains__("M5"):
        update_schematic_colors("M5")
    elif itemData.__contains__("M6"):
        update_schematic_colors("M6")

# init the application
app = QApplication([])
window = QWidget()


# creating widgets
layout = QHBoxLayout()
tools_container = QVBoxLayout()
main_container = QVBoxLayout()
draw_container = QVBoxLayout()
txt_title = QLabel("Smart Schematic")
txt_box_tools = QLabel("ToolBox")
tools_list = QListWidget()
for i in range(1, 7):
    l = "M{}".format(i)
    tools_list.addItem(l)


#widgets properties
tools_list.setFixedWidth(150)
tools_list.itemClicked.connect(item_selected)
txt_title.setAlignment(Qt.AlignTop)

# styling widgets
txt_title.setStyleSheet(
    "color: #456162;"
    "font-size: 30px;"
)
txt_box_tools.setStyleSheet(
    "color: #456162;"
    "font-size: 20px;"
)
tools_list.setStyleSheet(
    "font-size: 17px;"
    "color: #4287f5"
)


# adding the widgets
main_container.addWidget(txt_title)
tools_container.addWidget(txt_box_tools)
tools_container.addWidget(tools_list)
layout.addLayout(tools_container)
layout.addLayout(main_container)
main_container.addLayout(draw_container)

# init draw
d.save('schemdraw.png')
pixmap = QPixmap("schemdraw.png")
scroll = QScrollArea()
old_schematic = QLabel()
old_schematic.setPixmap(pixmap)
scroll.setWidget(old_schematic)
scroll.setAlignment(Qt.AlignCenter)
draw_container.addWidget(scroll)
window.setLayout(layout)
window.setWindowTitle("Smart Schematic")
window.show()
app.exec_()