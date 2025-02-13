from simpletk import TImageViewer
from simpletk import *



app=TApplication('обои')
app.position=(500,300)
app.size=(1000,1000)
app.resizable=(True,True)

def save(eval):
    with open("Save.txt", "w") as file:
        file.write(f"D={Dlina.text}\n"
                   f"S={Shirina.text}\n"
                   f"V={Visota.text}\n"
                   f"{pLOSHADL.text}\n"
                   f"{Rulon.text}")

def load(eval):
    s=open("Save.txt", "r")
    for i in s:
        if 'D=' in i:
            Dlina.text=i[2:]
        elif 'S=' in i:
            Shirina.text=i[2:]
        elif 'V=' in i:
            Visota.text=i[2:]
        elif 'площадь' in i:
            pLOSHADL.text=i[13:]
        elif 'Нужно' in i:
            s=i[6:]
            Rulon.text=s[:-8]


Save=TButton(app,
             width=100,
             font=('Calibri',30))
Save.position=(600,0)
Save.size=(400,100)
Save.text='Сохранить'

Load=TButton(app,
             width=100,
             font=('Calibri',30))
Load.position=(600,100)
Load.size=(400,100)
Load.text='Загрузить'

Dlina=TEdit(app,
                 width=100,
                 font=('Calibri',30),
                 )
Dlina.position=(300,0)
Dlina.text='0'
DlinaM=TLabel(app,
                 width=200,
                 font=('Calibri',30),
                 )


Shirina=TEdit(app,
                 width=100,
                 font=('Calibri',30),
                 )
Shirina.position=(300,100)
Shirina.text='0'


Visota=TEdit(app,
                 width=100,
                 font=('Calibri',30),
                 )
Visota.position=(300,200)
Visota.text='0'

V_rulon=TEdit(app,
                 width=100,
                 font=('Calibri',30),
                 )
V_rulon.position=(300,300)
V_rulon.text='1'


DlinaM=TLabel(app,
                 width=50,
                 font=('Calibri',30),
                 )
DlinaM.position=(400,0)
DlinaM.text='М'

ShirinaM=TLabel(app,
                 width=50,
                 font=('Calibri',30),
                 )
ShirinaM.position=(400,100)
ShirinaM.text='М'

VisotaL=TLabel(app,
                 width=50,
                 font=('Calibri',30),
                 )
VisotaL.position=(400,200)
VisotaL.text='М'

V_rulonL=TLabel(app,
                 width=50,
                 font=('Calibri',30),
                 )
V_rulonL.position=(400,300)
V_rulonL.text='М'




DlinaL=TLabel(app,
                 width=200,
                 font=('Calibri',30),
                 )
DlinaL.position=(100,0)
DlinaL.text='Длина= '

ShirinaL=TLabel(app,
                 width=200,
                 font=('Calibri',30),
                 )
ShirinaL.position=(100,100)
ShirinaL.text='Ширина= '

VisotaL=TLabel(app,
                 width=200,
                 font=('Calibri',30),
                 )
VisotaL.position=(100,200)
VisotaL.text='Высота= '

V_rulonL=TLabel(app,
                 width=200,
                 font=('Calibri',30),
                 )
V_rulonL.position=(100,300)
V_rulonL.text='В рулоне'


pLOSHADL=TLabel(app,
                 width=400,
                 font=('Calibri',30),
                 )
pLOSHADL.position=(60,400)

Rulon=TLabel(app,
                 width=300,
                 font=('Calibri',30),
                 )
Rulon.position=(60,500)
def on_change(sender):

    d = Dlina.text
    s = Shirina.text
    h = Visota.text
    k= V_rulon.text
    SS=(float(d) * float(h)) * 2 + (float(s) * float(h)) * 2
    pLOSHADL.text=f'площадь стен={SS}'
    KK=round(SS/float(k))
    Rulon.text=f'Нужно {KK} рулонов'

Dlina.onChange=on_change
Shirina.onChange=on_change
Visota.onChange=on_change
V_rulon.onChange=on_change
Save.onClick=save
Load.onClick=load

app.run()