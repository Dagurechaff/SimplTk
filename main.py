from simpletk import *
from simpletk import TIntEdit
def per(n,z):
    s = ''
    while n > 0:
        s += str(n % z)
        n //= z
    return s[::-1]

app = TApplication('Шестнадцатеричная система')
app.size = (1000, 300)
app.position = (500, 300)

decEdit = TIntEdit(app,
                   width=400,
                   font=('Calibri', 50)
                   )
decEdit.position = (5, 5)
decEdit.text = '1'

decEdit2 = TIntEdit(app,
                   width=400,
                   font=('Calibri', 50)
                   )
decEdit2.position = (5, 100)
decEdit2.text = '2'

hexLabel = TLabel(app,
                  text='-',
                  font=('Calibri', 50),
                  )
hexLabel.position = (500, 5)

cost = TLabel(app)


def on_change(sender):
    if sender.value>=0:
        cost.text=f"{sender.value}"
    else:
        cost.text="ERROR"

def on_change2(sender):
    if cost.text=="ERROR":
        hexLabel.text='negative numbers are not accepted'
    else:
        if sender.value>=2 and sender.value<=32:
            hexLabel.text=f"{per(int(cost.text),sender.value)}"
        else:
            hexLabel.text='The number system is from 2 to 32'


decEdit.onChange = on_change
decEdit2.onChange = on_change2
app.run()