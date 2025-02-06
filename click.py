from simpletk import *
from tkinter import filedialog
def selectfle(sender):
    fname=filedialog.askopenfilename(
        filetypes=[("Все файлы",'*.*'),('Файлы GIF','*.gif')]
    )
    Image.picture=fname
def cbChange(sender):
    if sender.checked:
        Image.center=True
    else:
        Image.center = False
app=TApplication('picture view')
app.position=(500,600)
app.size=(700,400)

panel=TPanel(app,
             relief='raised',
             height=55,
             bd=10)
panel.align='top'
panel.background='purple'
openBtn=TButton(panel,
                width=110,
                height=30,
                text='open file')
openBtn.position=(5,5)
openBtn.background='pink'
openBtn.font=10
centerCb=TCheckBox(panel,
                   text='picture in centre')
centerCb.position=(115,5)
centerCb.font=10
centerCb.background='pink'
centerCb.onChange=cbChange
Image=TImage(app,
             bg='red')
Image.align='client'
openBtn.onClick=selectfle
app.run()