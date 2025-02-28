# -*- coding: utf-8 -*-
"""
Библиотека SIMPLETK
Версия 0.51
07.06.2020

SIMPLETK - это "обертка" над стандартной библиотекой tkinter,
которая используется в языке Python для разработки приложений с
графическим интерфейсом. В ней упрощён доступ ко многим возможностям
библиотеки tkinter, в то же время сохранена возможность использования
всех средств tkinter.

ЛИЦЕНЗИЯ

Copyright (c) 2014-2019, Константин Поляков
Все права защищены.

Разрешается повторное распространение и использование как в виде исходного
кода, так и в двоичной форме, с изменениями или без, при соблюдении
следующих условий:
  1) При повторном распространении исходного кода должно оставаться указанное
     выше уведомление об авторском праве, этот список условий и последующий
     отказ от гарантий.
  2) При повторном распространении двоичного кода должна сохраняться указанная
     выше информация об авторском праве, этот список условий и последующий
     отказ от гарантий в документации и/или в других материалах,
     поставляемых при распространении.
  3) Ни название Организации, ни имена ее сотрудников не могут быть
     использованы в качестве поддержки или продвижения продуктов,
     основанных на этом ПО без предварительного письменного разрешения.

ДАННОЕ ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ «КАК ЕСТЬ», БЕЗ ЛЮБОГО ВИДА
ГАРАНТИЙ, ЯВНО ВЫРАЖЕННЫХ ИЛИ ПОДРАЗУМЕВАЕМЫХ, ВКЛЮЧАЯ, НО НЕ ОГРАНИЧИВАЯСЬ
ГАРАНТИЯМИ ТОВАРНОЙ ПРИГОДНОСТИ, СООТВЕТСТВИЯ ПО ЕГО КОНКРЕТНОМУ НАЗНАЧЕНИЮ
И НЕНАРУШЕНИЯ ПРАВ. НИ В КАКОМ СЛУЧАЕ АВТОРЫ ИЛИ ПРАВООБЛАДАТЕЛИ НЕ НЕСУТ
ОТВЕТСТВЕННОСТИ ПО ИСКАМ О ВОЗМЕЩЕНИИ УЩЕРБА, УБЫТКОВ ИЛИ ДРУГИХ ТРЕБОВАНИЙ
ПО ДЕЙСТВУЮЩИМ КОНТРАКТАМ, ДЕЛИКТАМ ИЛИ ИНОМУ, ВОЗНИКШИМ ИЗ, ИМЕЮЩИМ ПРИЧИНОЙ
ИЛИ СВЯЗАННЫМ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ ИЛИ ИСПОЛЬЗОВАНИЕМ ПРОГРАММНОГО
ОБЕСПЕЧЕНИЯ ИЛИ ИНЫМИ ДЕЙСТВИЯМИ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ.
"""
from tkinter import filedialog
from tkinter.constants import *
CLIENT = "client"

__all__ = [
# Symbolic constants for Tk
# Booleans
'NO', 'FALSE', 'OFF', 'YES', 'TRUE', 'ON',

# -anchor and -sticky
'N', 'S', 'W', 'E', 'NW', 'SW', 'NE', 'SE', 'NS', 'EW', 'NSEW', 'CENTER',

# -fill
'NONE', 'X', 'Y', 'BOTH', 'CLIENT',

# -side
'LEFT', 'TOP', 'RIGHT', 'BOTTOM',

# -relief
'RAISED', 'SUNKEN', 'FLAT', 'RIDGE', 'GROOVE', 'SOLID',

# -orient
'HORIZONTAL', 'VERTICAL',

# -tabs
'NUMERIC',

# -wrap
'CHAR', 'WORD',

# -align
'BASELINE',

# -bordermode
'INSIDE', 'OUTSIDE',

# Special tags, marks and insert positions
'SEL', 'SEL_FIRST', 'SEL_LAST', 'END', 'INSERT', 'CURRENT', 'ANCHOR',
'ALL', # e.g. Canvas.delete(ALL)

# Text widget and button states
'NORMAL', 'DISABLED', 'ACTIVE',
# Canvas state
'HIDDEN',

# Menu item types
'CASCADE', 'CHECKBUTTON', 'COMMAND', 'RADIOBUTTON', 'SEPARATOR',

# Selection modes for list boxes
'SINGLE', 'BROWSE', 'MULTIPLE', 'EXTENDED',

# Activestyle for list boxes
# NONE='none' is also valid
'DOTBOX', 'UNDERLINE',

# Various canvas styles
'PIESLICE', 'CHORD', 'ARC', 'FIRST', 'LAST', 'BUTT', 'PROJECTING',
'ROUND', 'BEVEL', 'MITER',

# Arguments to xview/yview
'MOVETO', 'SCROLL', 'UNITS', 'PAGES',

        'TApplication',
        'TLabel',
        'TButton',
        'TCanvas',
        'TImage',
        'TPanel',
        'TEdit',
        'TMemo',
        'TListBox',
        'TComboBox',
        'TRadioGroup',
        'TCheckBox',
        'TGroupBox',
        'TMenu',
        'TSubmenu',
        'TPopupMenu',
        'TMenuItem',
        'TCheckMenuItem',
        'TMenuRadioGroup',
        'TTrackBar',
        'TStringGrid',
        'PhotoImage'
        ]

import tkinter
from tkinter import ttk
try:
  from PIL import ImageTk, Image
except:
  pass

#-------------------------------------------------------------
#   TAPPLICATION
#-------------------------------------------------------------
class TApplication(tkinter.Tk):

    def __init__(self, title0):
      tkinter.Tk.__init__(self)
      super().title(title0)
      self.__size = (200, 200)
      self.__position = (200, 200)
      self.__resizable = (True, True)
      self.__minsize = (1, 1)
      self.__maxsize = (self.winfo_screenwidth(),
                        self.winfo_screenheight())
      self.__background = ""
      self.__onCloseQuery = None
      self.protocol("WM_DELETE_WINDOW", self.__intOnCloseQuery)
      self.__default = None
      self.bind('<Return>', self.__onReturn)
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onKey = None
      self.bind('<Key>', self.__intOnKey)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)
      self.__onResize = None
      self.bind('<Configure>', self.__intOnResize)

    def __setGeometry (self):
      pos = self.__position
      size = self.__size
      self.geometry("{:d}x{:d}+{:d}+{:d}".format(*(size+pos)))

    def __setPosition (self, pos):
      self.__position = pos
      self.__setGeometry()

    def __setSize (self, size):
      self.__size = size
      self.__setGeometry()

    def __getTitle (self):
      return super().title()
    def __setTitle (self, newTitle):
      super().title(newTitle)

    def __setResizable (self, value):
      self.__resizable = value
      super(TApplication,self).resizable(width=value[0], height=value[1])

    def __setMinsize (self, value):
      self.__minsize = value
      super(TApplication,self).minsize(width=value[0], height=value[1])

    def __setMaxsize (self, value):
      self.__maxsize = value
      super(TApplication,self).maxsize(width=value[0], height=value[1])

    def __setBackground (self, value):
      self.__background = value
      super(TApplication,self).configure(background=value)

    def __onReturn(self, event):
      if self.__default:
        self.__default.invoke()
    def __setDefault(self, obj):
      self.__default = obj

    def __intOnCloseQuery(self):
      if self.__onCloseQuery:
        event = tkinter.Event()
        event.widget = self
        event.width = self.__size[0]
        event.height = self.__size[1]
        event.type = 0
        self.__onCloseQuery( event )
      else:
        self.destroy()
    def __setOnCloseQuery(self, func):
      self.__onCloseQuery = func

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnKey(self, event):
      if self.__onKey:
        self.__onKey(event)
    def __setOnKey(self, func):
      self.__onKey = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    def __intOnResize(self, event):
      if self.__onResize:
        self.__onResize(event)
    def __setOnResize(self, func):
      self.__onResize = func

    def Run(self):
      self.run()
    def run(self):
      self.mainloop()

    position = property(lambda x: x.__position, __setPosition)
    size = property(lambda x: x.__size, __setSize)
    resizable = property(lambda x: x.__resizable, __setResizable)
    minsize = property(lambda x: x.__minsize, __setMinsize)
    maxsize = property(lambda x: x.__maxsize, __setMaxsize)
    default = property(lambda x: x.__default, __setDefault)
    background = property(lambda x: x.__background, __setBackground)
    title = property(__getTitle, __setTitle)

    onCloseQuery = property(lambda x: x.__onCloseQuery, __setOnCloseQuery)
    onResize = property(lambda x: x.__onResize, __setOnResize)

    onKey = property(lambda x: x.__onKey, __setOnKey)

    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

#-------------------------------------------------------------
#   TPANEL
#-------------------------------------------------------------
class TPanel( tkinter.Frame ):

    def __init__(self, parent, **kw):
      tkinter.Frame.__init__(self, parent, **kw)
      self.__parent = parent
      self.__position = (20, 20)
      self.__align = None
      self.__setSize( (kw.get("width") or 100, kw.get("height") or 50) )
      self.__setAutoSize( False )
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def __setBackground(self, value):
      self["bg"] = value

    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )

    def __setSize (self, size):
      self.__size = size
      self["width"] = size[0]
      self["height"] = size[1]

    def __setAutoSize (self, autoSize):
      self.__autoSize = autoSize
      self.pack_propagate( autoSize )
      self.grid_propagate( autoSize )

    def __setAlign(self, align):
      self.__align = align
      if align in [tkinter.TOP, tkinter.BOTTOM]:
        self.pack( side=align, fill=tkinter.X )
      elif align in [tkinter.LEFT, tkinter.RIGHT]:
        self.pack(side=align, fill=tkinter.Y )
      elif align == "client":
        self.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    def __getRoot( self ):
      if not self.__parent: return None
      if isinstance(self.__parent, TApplication):
        return self.__parent
      else:
        return self.__parent.root

    autoSize  = property(lambda x: x.__autoSize, __setAutoSize)
    size = property(lambda x: x.__size, __setSize)
    position = property(lambda x: x.__position, __setPosition)
    align = property(lambda x: x.__align, __setAlign)
    background = property(lambda x: x["bg"], __setBackground)
    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

    root = property( __getRoot )

#-------------------------------------------------------------
#   TLABEL
#-------------------------------------------------------------
class TLabel( tkinter.Label ):

    def __init__(self, parent, **kw):
      kwPanel = {}
      for param in ["width", "height"]:
        if param in kw:
          kwPanel[param] = kw[param]
          del kw[param]
      self.__panel = TPanel( parent, **kwPanel )
      tkinter.Label.__init__( self, self.__panel, **kw )
      super().pack( fill = tkinter.BOTH, expand = tkinter.YES )
      self.__parent = parent
      self.__panel.root.update_idletasks()
      self.__align = None
      self.__autoSize = [False, False]
      if not "width" in kwPanel:
        self.__panel["width"] = self.winfo_reqwidth()
        self.__autoSize[0] = True
      if not "height" in kwPanel:
        self.__panel["height"] = self.winfo_reqheight()
        self.__autoSize[1] = True
      self.__position = (0, 0)
      self.__size = (self.__panel["width"], self.__panel["height"])
      self.__onClick = None
      self.__align = None
        #self.bind("<ButtonPress-1>", self.__intOnClick)
        #self.bind("<ButtonRelease-1>", self.__intOnClick)
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def config ( self, **kw ):
      result = super().config ( **kw )
      self.__doAutoSize()
      return result

    def place(self, *args, **kwargs):
      self.__panel.place( *args, **kwargs)
      x, y = self.__position
      if "x" in kwargs: x = kwargs["x"]
      if "y" in kwargs: y = kwargs["y"]
      self.__position = (x, y)

    def pack(self, *args, **kwargs):
      self.__panel.pack( *args, **kwargs)

    def grid( self, *args, **kwargs ):
      self.__panel.grid( *args, **kwargs )

    def destroy( self ):
      super().destroy()
      self.__panel.destroy()

    def __setPosition (self, pos = None):
      if pos:
        self.__position = pos
        self.__align = None
      if not self.__align:
        self.__panel.place( x = self.__position[0], y = self.__position[1],
                            width = self.__panel["width"],
                            height = self.__panel["height"] )

    def __doAutoSize( self ):
      if self.__align: return
      self.__panel.root.update_idletasks()
      if self.__autoSize[0]:
        self.__panel["width"] = self.winfo_reqwidth()
      if self.__autoSize[1]:
        self.__panel["height"] = self.winfo_reqheight()
      self.__setPosition()

    def __setSize (self, size):
      self.__size = size
      self.__panel["width"] = size[0]
      self.__panel["height"] = size[1]
      self.__autoSize = [False, False]
      self.__setPosition()

    def __setAlign(self, align):
      self.__align = align
      if align in [tkinter.TOP, tkinter.BOTTOM]:
        self.__autoSize = [True, False]
        self.pack(side=align, fill=tkinter.X )
      elif align in [tkinter.LEFT, tkinter.RIGHT]:
        self.__autoSize = [False, True]
        self.pack(side=align, fill=tkinter.Y )
      elif align == "client":
        self.__autoSize = [False, False]
        self.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    def __setFont (self, value):
      self["font"] = value
      self.__doAutoSize()

    def __setText(self, value):
      self["text"] = value
      self.__doAutoSize()

    def __setBackground(self, value):
      self["bg"] = value

    def __setColor(self, value):
      self["fg"] = value

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    position = property(lambda x: x.__position, __setPosition)
    size = property(lambda x: x.__size, __setSize)
    align = property(lambda x: x.__align, __setAlign)
    text = property(lambda x: x["text"], __setText)
    font = property(lambda x: x["font"], __setFont)
    color = property(lambda x: x["fg"], __setColor)
    background = property(lambda x: x["bg"], __setBackground)

    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

#-------------------------------------------------------------
#   TBUTTON
#-------------------------------------------------------------
class TButton( tkinter.Button ):

    def __init__( self, parent, **kw ):
      kwPanel = {}
      for param in ["width", "height"]:
        if param in kw:
          kwPanel[param] = kw[param]
          del kw[param]
      self.__panel = TPanel( parent, **kwPanel )
      if 'image' in kw and not 'compound' in kw:
        kw["compound"] = "left"
      tkinter.Button.__init__( self, self.__panel, **kw )
      super().pack( fill = tkinter.BOTH, expand = tkinter.YES )
      self.__parent = parent
      self.__align = None
      self.__autoSize = [False, False]
      if not "width" in kwPanel:
        self.__panel["width"] = self.winfo_reqwidth()
        self.__autoSize[0] = True
      if not "height" in kwPanel:
        self.__panel["height"] = self.winfo_reqheight()
        self.__autoSize[1] = True
      self.__position = (0, 0)
      self.__size = (self.__panel["width"], self.__panel["height"])
      self.__onClick = None
      self["command"] = self.__intOnClick
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def config ( self, **kw ):
      result = super().config ( **kw )
      self.__doAutoSize()
      return result

    def place(self, *args, **kwargs):
      self.__panel.place( *args, **kwargs)

    def pack(self, *args, **kwargs):
      self.__panel.pack( *args, **kwargs)

    def grid( self, *args, **kwargs ):
      self.__panel.grid( *args, **kwargs )

    def destroy( self ):
      super().destroy()
      self.__panel.destroy()

    def __setPosition (self, pos = None):
      if pos:
        self.__position = pos
        self.__align = None
      if not self.__align:
        self.__panel.place( x = self.__position[0], y = self.__position[1],
                            width = self.__panel["width"],
                            height = self.__panel["height"] )

    def __doAutoSize( self ):
      if self.__align: return
      self.__panel.root.update_idletasks()
      if self.__autoSize[0]:
        self.__panel["width"] = self.winfo_reqwidth()
      if self.__autoSize[1]:
        self.__panel["height"] = self.winfo_reqheight()
      self.__setPosition()

    def __setSize (self, size):
      self.__size = size
      self.__panel["width"] = size[0]
      self.__panel["height"] = size[1]
      self.__autoSize = [False, False]
      self.__setPosition()

    def __setAlign(self, align):
      self.__align = align
      self.__autoSize = [True, True]
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.pack(side=align, fill=tkinter.Y)
      elif align == "client":
        self.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    def __setFont (self, value):
      self["font"] = value

    def __setText(self, value):
      self["text"] = value

    def __setBackground(self, value):
      self["bg"] = value

    def __setColor(self, value):
      self["fg"] = value

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self):
      if self.__onClick:
        self.__onClick(self)
    def click(self):
      self.__onClick(self)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    position = property(lambda x: x.__position, __setPosition)
    size = property(lambda x: x.__size, __setSize)
    align = property(lambda x: x.__align, __setAlign)
    color = property(lambda x: x["fg"], __setColor)
    background = property(lambda x: x["bg"], __setBackground)
    text = property(lambda x: x["text"], __setText)
    font = property(lambda x: x["font"], __setFont)

    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

#-------------------------------------------------------------
#   TCHECKBOX
#-------------------------------------------------------------
class TCheckBox(tkinter.Checkbutton):

    def __init__(self, parent, **kw):
      self.__var = tkinter.IntVar()
      tkinter.Checkbutton.__init__(self, parent, **kw)
      self["onvalue"] = 1
      self["offvalue"] = 0
      self["variable"] = self.__var
      self.__parent = parent
      self.__position = (0, 0)
      self.__size = (self["width"], self["height"])
      self.__onChange = None
      self["command"] = self.__intOnChange
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onKey = None
      self.bind('<Key>', self.__intOnKey)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )

    def __setSize (self, size):
      self.__size = size
      self["width"] = size[0]
      self["height"] = size[1]

    def __setAlign(self, align):
      self.__align = align
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.pack(side=align, fill=tkinter.Y)
      elif align == CLIENT:
        self.pack(fill=tkinter.BOTH, expand=YES)

    def __setText(self, value):
      self["text"] = value

    def __setFont (self, value):
      self["font"] = value

    def __setBackground(self, value):
      self["bg"] = value

    def __setColor(self, value):
      self["fg"] = value

    def __setChecked (self, value):
      if self.__var.get() != value:
        self.__var.set( int(value) )
        if self.__onChange:
          self.__onChange(self)

    def __intOnChange(self):
      if self.__onChange:
        self.__onChange(self)
    def __setOnChange(self, func):
      self.__onChange = func

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnKey(self, event):
      if self.__onKey:
        self.__onKey(event)
    def __setOnKey(self, func):
      self.__onKey = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    position = property(lambda x: x.__position, __setPosition)
    size = property(lambda x: x.__size, __setSize)
    align = property(lambda x: x.__align, __setAlign)
    color = property(lambda x: x["fg"], __setColor)
    background = property(lambda x: x["bg"], __setBackground)
    text = property(lambda x: x["text"], __setText)
    font = property(lambda x: x["font"], __setFont)
    checked = property(lambda x: x.__var.get() == 1, __setChecked)

    onKey = property(lambda x: x.__onKey, __setOnKey)

    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

    onChange = property(lambda x: x.__onChange, __setOnChange)

#-------------------------------------------------------------
#   TCANVAS
#-------------------------------------------------------------
class TCanvas(tkinter.Canvas):

    def __init__(self, parent, **kw):
      tkinter.Canvas.__init__(self, parent, **kw)
      self.__parent = parent
      self.__position = (0, 0)
      self.__size = (self["width"], self["height"])
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def __setAlign(self, align):
      self.__align = align
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.pack(side=align, fill=tkinter.Y)
      elif align == "client":
        self.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )

    def __setSize (self, size):
      self.__size = size
      self["width"] = size[0]
      self["height"] = size[1]

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    align = property(lambda x: x.__align, __setAlign)
    position = property(lambda x: x.__position, __setPosition)
    size = property(lambda x: x.__size, __setSize)

    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

#-------------------------------------------------------------
#   TIMAGE
#-------------------------------------------------------------
def PhotoImage(file):
    return tkinter.PhotoImage(file = file)

class TImage(TCanvas):

    def __init__(self, parent, **kw):
      TCanvas.__init__(self, parent, **kw)
      self.__parent = parent
      self.__center = tkinter.NO
      self.__picture = None
      self.bind("<Configure>", self.__onResize)

    def __onResize(self, ev):
      self.redrawImage()

    def redrawImage(self):
      self.delete("all")
      pic = self.__picture
      if pic:
        x0, y0 = 0, 0
        if self.__center:
          self.update()
          x0 = max( 0, (self.winfo_width()-pic.width())//2 )
          y0 = max( 0, (self.winfo_height()-pic.height())//2 )
        try:
          self.create_image(x0, y0, anchor=tkinter.NW, image=pic)
        except: pass

    def __setCenter (self, value):
      if self.__center != value:
        self.__center = value
        self.redrawImage()

    def __setPicture (self, fName):
      try:
        if fName.lower().endswith('.gif'):
          self.__picture = tkinter.PhotoImage(file = fName)
        else:
          im = Image.open(fName)
          self.__picture = ImageTk.PhotoImage(im)
        self.redrawImage()
      except:
        self.delete("all")

    center = property(lambda x: x.__center == 1, __setCenter)
    picture = property(lambda x: x.__picture, __setPicture)

#-------------------------------------------------------------
#   TEDIT
#-------------------------------------------------------------
class TEdit( tkinter.Entry ):

    def __init__(self, parent, **kw):
      kwPanel = {}
      for param in ["width", "height"]:
        if param in kw:
          kwPanel[param] = kw[param]
          del kw[param]
      self.__panel = TPanel( parent, **kwPanel )
      tkinter.Entry.__init__( self, self.__panel, **kw )
      super().pack( fill = tkinter.BOTH, expand = tkinter.YES )
      self.__parent = parent
      self.__panel.root.update_idletasks()
      self.__autoSize = [False, False]
      if not "width" in kwPanel:
        self.__panel["width"] = self.winfo_reqwidth()
        self.__autoSize[0] = True
      if not "height" in kwPanel:
        self.__panel["height"] = self.winfo_reqheight()
        self.__autoSize[1] = True
      self.__position = (0, 0)
      self.__size = (self.__panel["width"], self.__panel["height"])
      self.__onChange = None
      self.__onValidate = None
      self.__var = tkinter.StringVar()
      self["textvariable"] = self.__var
      self.__text = self.__var.get()
      self.__var.trace("w", self.__trace)
      self.__align = None
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onKey = None
      self.bind('<Key>', self.__intOnKey)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def config ( self, **kw ):
      result = super().config ( **kw )
      self.__doAutoSize()
      return result

    def place(self, *args, **kwargs):
      self.__panel.place( *args, **kwargs)

    def pack(self, *args, **kwargs):
      self.__panel.pack( *args, **kwargs)

    def grid( self, *args, **kwargs ):
      self.__panel.grid( *args, **kwargs )

    def destroy( self ):
      super().destroy()
      self.__panel.destroy()

    def __setPosition (self, pos = None):
      if pos:
        self.__position = pos
        self.__align = None
      if not self.__align:
        self.__panel.place( x = self.__position[0], y = self.__position[1],
                            width = self.__panel["width"],
                            height = self.__panel["height"] )

    def __doAutoSize( self ):
      if self.__align: return
      self.__panel.root.update_idletasks()
      if self.__autoSize[0]:
        self.__panel["width"] = self.winfo_reqwidth()
      if self.__autoSize[1]:
        self.__panel["height"] = self.winfo_reqheight()
      self.__setPosition()

    def __setAlign(self, align):
      self.__align = align
      if align in [tkinter.TOP, tkinter.BOTTOM]:
        self.__autoSize = [True, False]
        self.pack(side=align, fill=tkinter.X )
      elif align in [tkinter.LEFT, tkinter.RIGHT]:
        self.__autoSize = [False, True]
        self.pack(side=align, fill=tkinter.Y )
      elif align == "client":
        self.__autoSize = [False, False]
        self.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    def __setWidth (self, width):
      self.__panel["width"] = width
      self.__autoSize[0] = False
      self.__setPosition()

    def __trace(self, *args):
      valid = tkinter.YES
      if self.__onValidate:
        valid = self.__onValidate()
      if valid:
        self.__text = self.__var.get()
        if self.__onChange:
          self.__onChange(self)
      else:
        self.__var.set(self.__text)

    def __setFont (self, value):
      self["font"] = value
      self.__doAutoSize()

    def __setText(self, value):
      if self.__var.get() == value: return
      self.__var.set(value)
      self.update()
      if self.__onChange:
        self.__onChange(self)

    def __setBackground(self, value):
      self["bg"] = value

    def __setColor(self, value):
      self["fg"] = value

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnKey(self, event):
      if self.__onKey:
        self.__onKey(event)
    def __setOnKey(self, func):
      self.__onKey = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    def __setOnChange(self, func):
      self.__onChange = func
      if self.__onChange:
        self.__onChange(self)

    def __setOnValidate(self, func):
      self.__onValidate = func

    align = property(lambda x: x.__align, __setAlign)
    position = property(lambda x: x.__position, __setPosition)
    width = property(lambda x: x.__width, __setWidth)
    color = property(lambda x: x["fg"], __setColor)
    background = property(lambda x: x["bg"], __setBackground)
    text = property(lambda x: x.__var.get(), __setText)
    font = property(lambda x: x["font"], __setFont)

    onKey = property(lambda x: x.__onKey, __setOnKey)

    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

    onChange = property(lambda x: x.__onChange, __setOnChange)
    onValidate = property(lambda x: x.__onValidate, __setOnValidate)

#-------------------------------------------------------------
#   TCOMBOBOX
#-------------------------------------------------------------
class TComboBox( ttk.Combobox ):

    def __init__(self, parent, **kw):
      kwPanel = {}
      for param in ["width", "height"]:
        if param in kw:
          kwPanel[param] = kw[param]
          del kw[param]
      self.__panel = TPanel( parent, **kwPanel )
      ttk.Combobox.__init__(self, self.__panel, **kw)
      super().pack( fill = tkinter.BOTH, expand = tkinter.YES )
      self.__parent = parent
      self.__panel.root.update_idletasks()
      self.__align = None
      self.__autoSize = [False, False]
      if not "width" in kwPanel:
        self.__panel["width"] = self.winfo_reqwidth()
        self.__autoSize[0] = True
      if not "height" in kwPanel:
        self.__panel["height"] = self.winfo_reqheight()
        self.__autoSize[1] = True
      self.__position = (0, 0)
      self.__size = (self.__panel["width"], self.__panel["height"])
      self.__onValidate = None
      self.__onChange = None
      self.__var = tkinter.StringVar()
      self["textvariable"] = self.__var
      self.__text = self.__var.get()
      self.__var.trace("w", self.__trace)
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onKey = None
      self.bind('<Key>', self.__intOnKey)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def config ( self, **kw ):
      result = super().config ( **kw )
      self.__doAutoSize()
      return result

    def place(self, *args, **kwargs):
      self.__panel.place( *args, **kwargs)

    def pack(self, *args, **kwargs):
      self.__panel.pack( *args, **kwargs)

    def grid( self, *args, **kwargs ):
      self.__panel.grid( *args, **kwargs )

    def destroy( self ):
      super().destroy()
      self.__panel.destroy()

    def __setPosition (self, pos = None):
      if pos:
        self.__position = pos
        self.__align = None
      if not self.__align:
        self.__panel.place( x = self.__position[0], y = self.__position[1],
                            width = self.__panel["width"],
                            height = self.__panel["height"] )

    def __doAutoSize( self ):
      if self.__align: return
      self.__panel.root.update_idletasks()
      if self.__autoSize[0]:
        self.__panel["width"] = self.winfo_reqwidth()
      if self.__autoSize[1]:
        self.__panel["height"] = self.winfo_reqheight()
      self.__setPosition()

    def __setSize (self, size):
      self.__size = size
      self.__panel["width"] = size[0]
      self.__panel["height"] = size[1]
      self.__autoSize = [False, False]
      self.__setPosition()

    def __setAlign(self, align):
      self.__align = align
      if align in [tkinter.TOP, tkinter.BOTTOM]:
        self.__autoSize = [True, False]
        self.pack(side=align, fill=tkinter.X )
      elif align in [tkinter.LEFT, tkinter.RIGHT]:
        self.__autoSize = [False, True]
        self.pack(side=align, fill=tkinter.Y )
      elif align == "client":
        self.__autoSize = [False, False]
        self.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    def __setText(self, value):
      self.set(value)
      self.update()

    def findItem(self, value):
      if not self["values"]:
        return False
      else:
        return value in self["values"]

    def addItem(self, value):
      if not self["values"]:
        self["values"] = (value,)
      else:
        self["values"] = self["values"] + (value,)

    def __setOnChange(self, func):
      self.__onChange = func
      if self.__onChange:
        self.__onChange(self)

    def __setOnValidate(self, func):
      self.__onValidate = func

    def __doAutoSize( self ):
      self.__panel.root.update_idletasks()
      if self.__autoSize[0]:
        self.__panel["width"] = self.winfo_reqwidth()
      if self.__autoSize[1]:
        self.__panel["height"] = self.winfo_reqheight()
      self.__setPosition()

    def __setFont (self, value):
      self["font"] = value
      root = self.nametowidget(self.winfo_parent())
      root.option_add('*TCombobox*Listbox.font', value)
      self.__doAutoSize()

    def __trace(self, *args):
      valid = tkinter.YES
      if self.__onValidate:
        valid = self.__onValidate(self)
      if valid:
        self.__text = self.__var.get()
        if self.__onChange:
          self.__onChange(self)
      else:
        self.__var.set(self.__text)

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnKey(self, event):
      if self.__onKey:
        self.__onKey(event)
    def __setOnKey(self, func):
      self.__onKey = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    align = property(lambda x: x.__align, __setAlign)
    position = property(lambda x: x.__position, __setPosition)
    size = property(lambda x: x.__size, __setSize)
    text = property(lambda x: x.__var.get(), __setText)
    font = property(lambda x: x["font"], __setFont)

    onKey = property(lambda x: x.__onKey, __setOnKey)

    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

    onChange = property(lambda x: x.__onChange, __setOnChange)
    onValidate = property(lambda x: x.__onValidate, __setOnValidate)

#-------------------------------------------------------------
#   TLISTBOX
#-------------------------------------------------------------
class TListBox( tkinter.Listbox ):

    def __init__(self, parent, values, **kw):
      kwPanel = {}
      for param in ["width", "height"]:
        if param in kw:
          kwPanel[param] = kw[param]
          del kw[param]
      self.__panel = TPanel( parent, **kwPanel )
      tkinter.Listbox.__init__(self, self.__panel, **kw)
      self.__multiple = not kw.get('selectmode','') in [tkinter.SINGLE, tkinter.BROWSE]
      self.__parent = parent
      for item in values:
        self.insert(tkinter.END, item)
      self.__sbar = tkinter.Scrollbar(self.__panel, orient=tkinter.VERTICAL)
      self.__sbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
      super().pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES)
      self.__sbar.config(command=self.yview)
      self.configure(yscrollcommand=self.__sbar.set)
      self.__panel.root.update_idletasks()
      self.__align = None
      self.__autoSize = [False, False]
      if not "width" in kwPanel:
        self.__panel["width"] = self.winfo_reqwidth()
        self.__autoSize[0] = True
      if not "height" in kwPanel:
        self.__panel["height"] = self.winfo_reqheight()
        self.__autoSize[1] = True
      self.__position = (0, 0)
      self.__size = (self.__panel["width"], self.__panel["height"])
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onKey = None
      self.bind('<Key>', self.__intOnKey)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)
      self.__onChange = None
      self.bind('<<ListboxSelect>>', self.__intOnChange)

    def place(self, *args, **kwargs):
      self.__panel.place( *args, **kwargs)

    def pack(self, *args, **kwargs):
      self.__panel.pack( *args, **kwargs)

    def grid( self, *args, **kwargs ):
      self.__panel.grid( *args, **kwargs )

    def destroy( self ):
      super().destroy()
      self.__panel.destroy()

    def __setPosition (self, pos = None):
      if pos:
        self.__position = pos
        self.__align = None
      if not self.__align:
        self.__panel.place( x = self.__position[0], y = self.__position[1],
                            width = self.__panel["width"],
                            height = self.__panel["height"] )

    def __doAutoSize( self ):
      if self.__align: return
      self.__panel.root.update_idletasks()
      if self.__autoSize[0]:
        self.__panel["width"] = self.winfo_reqwidth()
      if self.__autoSize[1]:
        self.__panel["height"] = self.winfo_reqheight()
      self.__setPosition()

    def __setSize (self, size):
      self.__size = size
      self.__panel["width"] = size[0]
      self.__panel["height"] = size[1]
      self.__autoSize = [False, False]
      self.__setPosition()

    def __setAlign(self, align):
      self.__align = align
      if align in [tkinter.TOP, tkinter.BOTTOM]:
        self.__autoSize = [True, False]
        self.pack(side=align, fill=tkinter.X )
      elif align in [tkinter.LEFT, tkinter.RIGHT]:
        self.__autoSize = [False, True]
        self.pack(side=align, fill=tkinter.Y )
      elif align == "client":
        self.__autoSize = [False, False]
        self.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    def __setBackground(self, value):
      self["bg"] = value

    def __setColor(self, value):
      self["fg"] = value

    def __setFont (self, value):
      self["font"] = value
      self.__doAutoSize()

    def __setSelected(self, value):
      self.selection_clear(0, tkinter.END);
      try: iter(value)
      except: value = (value,)
      for val in value:
        self.selection_set(val);

    def item(self, itemNo):
      return self.get(itemNo);

    def itemCount(self):
      return tkinter.Listbox.size(self);

    def items(self, fromItem, toItem):
      return self.get(fromItem, toItem);

    def __intOnChange(self, event):
      if self.__onChange:
        self.__onChange(self)
    def __setOnChange(self, func):
      self.__onChange = func
      if self.__onChange:
        self.__onChange(self)

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnKey(self, event):
      if self.__onKey:
        self.__onKey(event)
    def __setOnKey(self, func):
      self.__onKey = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    def __setMultiple(self, value):
      if self.__multiple != value:
        self.__multiple = value
        if self.__multiple:
          self.config( selectmode = 'multiple' )
        else:
          self.config( selectmode = 'single' )
          self.selected = []

    position = property(lambda x: x.__position, __setPosition)
    size = property(lambda x: x.__size, __setSize)
    align = property(lambda x: x.__align, __setAlign)
    color = property(lambda x: x["fg"], __setColor)
    background = property(lambda x: x["bg"], __setBackground)
    font = property(lambda x: x["font"], __setFont)
    selected = property(lambda x: x.curselection(), __setSelected)
    multiple = property(lambda x: x.__multiple, __setMultiple)

    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onKey = property(lambda x: x.__onKey, __setOnKey)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)
    onChange = property(lambda x: x.__onChange, __setOnChange)

#-------------------------------------------------------------
#   TRADIOGROUP
#-------------------------------------------------------------
class TRadioGroup( TPanel ):

    def __init__(self, parent, values, **kw):
      self.__parent = parent
      if "orient" in kw:
        self.__orientation = kw["orient"]
        del kw["orient"]
      else:
        self.__orientation = tkinter.VERTICAL
      self.__var = tkinter.IntVar()
      TPanel.__init__(self, parent, **kw)
      self.buttons = []
      for code, text in enumerate(values):
        btn = tkinter.Radiobutton(self, text=text,
            variable=self.__var, value=code,
            command=self.__intOnChange)
        if self.__orientation == tkinter.VERTICAL:
          btn.pack( anchor = tkinter.W )
        else: # self.__orientation == HORIZONTAL
          btn.pack( side = tkinter.LEFT )
        self.buttons.append(btn)
      if len(values):
        self.__var.set(values[0])
      self.__onChange = None

    def __setBackground(self, value):
      self["bg"] = value
      for btn in self.buttons:
        btn["bg"] = value

    def __setColor(self, value):
      for btn in self.buttons:
        btn["fg"] = value

    def __setFont (self, value):
      for btn in self.buttons:
        btn["font"] = value

    def __setSelected (self, value):
      self.__var.set(value)

    def __intOnChange(self):
      if self.__onChange:
        self.__onChange(self)
    def __setOnChange(self, func):
      self.__onChange = func
      if self.__onChange:
        self.__onChange(self)

    def item(self, itemNo):
      return self.buttons[itemNo]["text"];

    color = property(lambda x: x["fg"], __setColor)
    background = property(lambda x: x["bg"], __setBackground)
    selected = property(lambda x: x.__var.get(), __setSelected)
    font = property(lambda x: x["font"], __setFont)

    onChange = property(lambda x: x.__onChange, __setOnChange)

#-------------------------------------------------------------
#   TGROUPBOX
#-------------------------------------------------------------
class TGroupBox( tkinter.LabelFrame ):

    def __init__(self, parent, **kw):
      tkinter.LabelFrame.__init__(self, parent, **kw)
      self.__parent = parent
      self.__position = (0, 0)
      self.__size = (self["width"], self["height"])
      self.__align = None
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onKey = None
      self.bind('<Key>', self.__intOnKey)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )

    def __setSize (self, size):
      self.__size = size
      self["width"] = size[0]
      self["height"] = size[1]

    def __setAlign(self, align):
      self.__align = align
      if align in [tkinter.TOP, tkinter.BOTTOM]:
        self.pack(side=align, fill=tkinter.X )
      elif align in [tkinter.LEFT, tkinter.RIGHT]:
        self.pack(side=align, fill=tkinter.Y )
      elif align == "client":
        self.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    def __setFont (self, value):
      self["font"] = value

    def __setText(self, value):
      self["text"] = value

    def __setBackground(self, value):
      self["bg"] = value

    def __setColor(self, value):
      self["fg"] = value

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnKey(self, event):
      if self.__onKey:
        self.__onKey(event)
    def __setOnKey(self, func):
      self.__onKey = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    def __getRoot( self ):
      if not self.__parent: return None
      if isinstance(self.__parent, TApplication):
        return self.__parent
      else:
        return self.__parent.root

    position = property(lambda x: x.__position, __setPosition)
    size = property(lambda x: x.__size, __setSize)
    align = property(lambda x: x.__align, __setAlign)
    text = property(lambda x: x["text"], __setText)
    font = property(lambda x: x["font"], __setFont)
    color = property(lambda x: x["fg"], __setColor)
    background = property(lambda x: x["bg"], __setBackground)
    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onKey = property(lambda x: x.__onKey, __setOnKey)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

    root = property( __getRoot )

#-------------------------------------------------------------
#   TMEMO
#-------------------------------------------------------------
class TMemo( tkinter.Text ):

    def __init__(self, parent, **kw):
      kwPanel = {}
      for param in ["width", "height"]:
        if param in kw:
          kwPanel[param] = kw[param]
          del kw[param]
      self.__parent = parent
      self.__panel = TPanel( parent, **kwPanel )
      tkinter.Text.__init__(self, self.__panel, **kw)
      self.__sbar = tkinter.Scrollbar(self.__panel, orient=tkinter.VERTICAL)
      self.__sbar.pack(side=tkinter.RIGHT, fill=tkinter.Y )
      super().pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES )
      self.__sbar.config(command=self.yview)
      self.configure(yscrollcommand=self.__sbar.set)
      self.__panel.root.update_idletasks()
      self.__autoSize = [False, False]
      if not "width" in kwPanel:
        self.__panel["width"] = self.winfo_reqwidth()
        self.__autoSize[0] = True
      else:
        self["width"] = 1
      if not "height" in kwPanel:
        self.__panel["height"] = self.winfo_reqheight()
        self.__autoSize[1] = True
      else:
        self["height"] = 1
      self.__align = None
      self.__position = (0, 0)
      self.__size = (self.__panel["width"], self.__panel["height"])
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onKey = None
      self.bind('<Key>', self.__intOnKey)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def place(self, *args, **kwargs):
      self.__panel.place( *args, **kwargs)

    def pack(self, *args, **kwargs):
      self.__panel.pack( *args, **kwargs)

    def grid( self, *args, **kwargs ):
      self.__panel.grid( *args, **kwargs )

    def destroy( self ):
      super().destroy()
      self.__panel.destroy()

    def __setPosition (self, pos = None):
      if pos:
        self.__position = pos
        self.__align = None
      if not self.__align:
        self.__panel.place( x = self.__position[0], y = self.__position[1],
                            width = self.__panel["width"],
                            height = self.__panel["height"] )

    def __doAutoSize( self ):
      if self.__align: return
      self.__panel.root.update_idletasks()
      if self.__autoSize[0]:
        self.__panel["width"] = self.winfo_reqwidth()
      if self.__autoSize[1]:
        self.__panel["height"] = self.winfo_reqheight()
      self.__setPosition()

    def __setSize (self, size):
      self.__size = size
      self.__panel["width"] = size[0]
      self.__panel["height"] = size[1]
      self.__autoSize = [False, False]
      self.__setPosition()

    def __setAlign(self, align):
      self.__align = align
      if align in [tkinter.TOP, tkinter.BOTTOM]:
        self.__autoSize = [True, False]
        self.pack(side=align, fill=tkinter.X )
      elif align in [tkinter.LEFT, tkinter.RIGHT]:
        self.__autoSize = [False, True]
        self.pack(side=align, fill=tkinter.Y )
      elif align == "client":
        self.__autoSize = [False, False]
        self.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    def __getText(self):
      text = self.get(1.0, tkinter.END)
      return text

    def __setText(self, text):
      self.delete(1.0, tkinter.END)
      self.insert(tkinter.INSERT, text)

    def getLine(self, lineNo):
      text = self.get(1.0, tkinter.END).splitlines()
      if lineNo < len(text):
        return text[lineNo]
      else:
        return ""

    def insertLine(self, lineNo, s):
      text = self.get(1.0, tkinter.END).splitlines()
      text.insert(lineNo, s)
      self.text = "\n".join(text)

    def deleteLine(self, lineNo):
      text = self.get(1.0, tkinter.END).splitlines()
      if lineNo < len(text):
        del text[lineNo]
        self.text = "\n".join(text)

    def __setFont (self, value):
      self["font"] = value
      self.__doAutoSize()

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnKey(self, event):
      if self.__onKey:
        self.__onKey(event)
    def __setOnKey(self, func):
      self.__onKey = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    align = property(lambda x: x.__align, __setAlign)
    position = property(lambda x: x.__position, __setPosition)
    text = property(__getText, __setText)
    font = property(lambda x: x["font"], __setFont)

    onKey = property(lambda x: x.__onKey, __setOnKey)

    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

#-------------------------------------------------------------
#   TMENUITEM
#-------------------------------------------------------------
class TMenuItem():

    def __init__( self, parent, text, **kw ):
      self.__text = text
      self.__parent = parent
      self.__onClick = None
      self.__accelerator = None
      self.__var = None  # для флажков и кнопок
      self.__type = 'command'
      if 'command' in kw:
        self.__onClick = kw['command']
      elif 'menu' in kw:
        self.__onClick = kw['menu']
      if 'accelerator' in kw:
        self.__accelerator = kw['accelerator'].replace('Ctrl','Control')
        self.__accelerator = self.__accelerator.replace('+', '-')
        self.__bindAccelerator()

    def __bindAccelerator(self):
      if self.__onClick and self.__accelerator:
        shortCut = self.__accelerator
        shortCut = shortCut[:-1] + shortCut[-1].upper()
        self.__parent.root.bind( '<'+shortCut+'>', self.__onClick )
        if shortCut[-1] != shortCut[-1].lower():
          shortCut = shortCut[:-1] + shortCut[-1].lower()
          self.__parent.root.bind( '<'+shortCut+'>', self.__onClick )

    def __setValue(self, value):
      if self.__var.get() == value: return
      self.__var.set(value)

    def __setText(self, value):
      if self.__text == value: return
      idx = self.__parent.index( self.__text )
      self.__parent.entryconfigure( idx, label = value )
      self.__text = value

    def __setOnClick(self, cmd):
      self.__onClick = cmd
      idx = self.__parent.index(self.__text)
      self.__parent.entryconfigure( idx, command = cmd )
      self.__bindAccelerator()

    var = property(lambda x: x.__var)
    value = property(lambda x: x.__var.get(), __setValue)
    text = property(lambda x: x.__text, __setText)
    onClick = property(lambda x: x.__onClick, __setOnClick)

#-------------------------------------------------------------
#   TMENU
#-------------------------------------------------------------
class TMenu( tkinter.Menu ):

    def __init__( self, parent, **kw ):
      tkinter.Menu.__init__(self, parent, relief = 'raised', **kw)
      try:
        parent.config( menu = self )
      except: pass
      self.__parent = parent

    def __getRoot( self ):
      if not self.__parent: return None
      if isinstance(self.__parent, TApplication):
        return self.__parent
      else:
        return self.__parent.parent

    def addSeparator( self, **kw ):
      self.add_separator( **kw )

    def __modifyParams( self, kw ):
      if 'onClick' in kw:
        kw['command'] = kw['onClick']
        del kw['onClick']
      if 'image' in kw  and  not 'compound' in kw:
        kw['compound'] = 'left'

    def addItem( self, text, **kw ):
      self.__modifyParams( kw )
      item = TMenuItem( self, text, **kw )
      self.add_command( label = text, **kw )
      return item

    def addCheckItem( self, text, **kw ):
      self.__modifyParams( kw )
      item = TCheckMenuItem( self, text, **kw )
      self.add_checkbutton( label = text, variable = item.var, **kw )
      return item

    def addRadioGroup( self, items, **kw ):
      self.__modifyParams( kw )
      group = TMenuRadioGroup( self, items, **kw )
      for text in items:
        self.add_radiobutton( label = text, variable = group.var, **kw )
      return group

    def addSubmenu( self, text, **kw ):
      self.__modifyParams( kw )
      item = TSubmenuItem( self, text, **kw )
      submenu = TSubmenu( self, item )
      self.add_cascade( label = text, menu = submenu, **kw )
      return submenu

    parent = property(lambda x: x.__parent)
    root = property(__getRoot)

#-------------------------------------------------------------
#   TSUBMENU
#-------------------------------------------------------------
class TSubmenu( TMenu ):

    def __init__( self, parent, item, **kw ):
      TMenu.__init__( self, parent, tearoff = 0, **kw )
      self.item = item

    def __setText(self, value):
      self.item.text = value

    text = property(lambda x: self.item.text, __setText)

#-------------------------------------------------------------
#   TCHECKMENUITEM
#-------------------------------------------------------------
class TCheckMenuItem( TMenuItem ):

    def __init__( self, parent, text, **kw ):
      TMenuItem.__init__( self, parent, text, **kw )
      self._TMenuItem__var = tkinter.IntVar()
      self.__type = 'checkbutton'

#-------------------------------------------------------------
#   TMENURADIOGROUP
#-------------------------------------------------------------
class TMenuRadioGroup( TMenuItem ):

    def __init__( self, parent, items, **kw ):
      text = chr(1).join(items)
      TMenuItem.__init__( self, parent, text, **kw )
      self._TMenuItem__var = tkinter.StringVar()
      self._TMenuItem__var.set(items[0])
      self.__type = 'radiogroup'

#-------------------------------------------------------------
#   TSUBMENUITEM
#-------------------------------------------------------------
class TSubmenuItem( TMenuItem ):

    def __init__( self, parent, text, **kw ):
      TMenuItem.__init__( self, parent, text, **kw )
      self.__type = 'cascade'

#-------------------------------------------------------------
#   TPOPUPMENU
#-------------------------------------------------------------
class TPopupMenu( TMenu ):

    def __init__( self, parent, **kw ):
      kw['tearoff'] = 0
      TMenu.__init__(self, parent, **kw)
      parent.bind( '<Button-3>', self.showPopupMenu )

    def showPopupMenu( self, event ):
      self.tk_popup( event.x_root, event.y_root )

#-------------------------------------------------------------
#   TTRACKBAR
#-------------------------------------------------------------
class TTrackBar( tkinter.Scale ):

    def __init__( self, parent, range, **kw ):
      if 'onTrack' in kw:
         kw['command'] = kw['onTrack']
         del kw['onTrack']
      tkinter.Scale.__init__( self, parent, from_ = range[0],
                              to = range[1], **kw  )
      self.__parent = parent
      self.__position = (20, 20)
      self.__size = (kw.get("width") or 200,
                     kw.get("height") or 100)
      self.__align = None
      self.__onTrack = None
      if 'command' in kw:
         self.__onTrack = kw['command']
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def __setBackground(self, value):
      self["bg"] = value

    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )

    def __setSize (self, size):
      self.__size = size
      self["width"] = size[0]
      self["height"] = size[1]

    def __setAlign(self, align):
      self.__align = align
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.pack(side=align, fill=tkinter.Y)
      elif align == CLIENT:
        self.pack(fill=tkinter.BOTH, expand=YES)

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    def __setOnTrack(self, func):
      self.__onTrack = func
      self.configure( command = func )

    def __setValue(self, value):
      if self.get() != value:
        self.set( value )

    size = property(lambda x: x.__size, __setSize)
    position = property(lambda x: x.__position, __setPosition)
    align = property(lambda x: x.__align, __setAlign)
    background = property(lambda x: x["bg"], __setBackground)
    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

    value = property( lambda x: x.get(), __setValue )
    onTrack = property(lambda x: x.__onTrack, __setOnTrack)

#-------------------------------------------------------------
#   TSTRINGGRID
#-------------------------------------------------------------
class TStringGrid( ttk.Treeview ):

    def __init__( self, parent, **kw ):
      self.__panel = TPanel(parent)
      if 'oddColor' in kw:
            self.__oddColor = kw['oddColor']
            del kw['oddColor']
      else: self.__oddColor = '#FAFAFA'
      if 'evenColor' in kw:
            self.__evenColor = kw['evenColor']
            del kw['evenColor']
      else: self.__evenColor = 'white'
      ttk.Treeview.__init__( self, self.__panel, **kw  )
      self.__sbar = tkinter.Scrollbar(self.__panel, orient=tkinter.VERTICAL)
      self.__sbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
      self.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES)
      self.__sbar.config(command=self.yview)
      self.configure(yscrollcommand=self.__sbar.set)
      self.__position = (0, 0)
      self.__parent = parent
      self.__panel.root.update_idletasks()
      if not "width" in kw:
        self.__panel["width"] = self.winfo_reqwidth()
      if not "height" in kw:
        self.__panel["height"] = self.winfo_reqheight()
      self.__setSize( (self.__panel["width"], self.__panel["height"]) )
      self.__align = None
      self.__edit = None
      self.__onEditedCell = None
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)
      self.tag_configure( 'odd', background = self.__oddColor )
      self.tag_configure( 'even', background = self.__evenColor )
        # self.__var = tkinter.StringVar()

    def destroy( self ):
      super().destroy()
      self.__panel.destroy()

    def __getBackground( self ):
      style = self.style
      return style['background'] if 'background' in style else None

    def __setBackground( self, value ):
      self.__setStyle( value )

    def __setPosition (self, pos):
      self.__position = pos
      self.__panel.place( x = self.__position[0], y = self.__position[1] )

    def __setSize (self, size):
      self.__size = size
      self.__panel["width"] = size[0]
      self.__panel["height"] = size[1]

    def __setAlign(self, align):
      self.__align = align
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.__panel.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.__panel.pack(side=align, fill=tkinter.Y)
      elif align == CLIENT:
        self.__panel.pack(fill=tkinter.BOTH, expand=YES)

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        event.cell = self.__identifyCell(event)
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __identifyCell(self, event):
      rowId = self.identify_row(event.y)
      colId = self.identify_column(event.x)
      if rowId and colId:
        rowNo = self.get_children().index(rowId)
        colNo = int( colId[1:] )
        return (rowNo, colNo, rowId)
      else:
        return None

    def __intOnClick(self, event):
      if self.__onClick:
        event.cell = self.__identifyCell(event)
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        event.cell = self.__identifyCell(event)
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    def heading( self, column, text, **kw  ):
      if type(column) == int:
        column = '#' + str(column)
      super().heading( column, text = text, **kw )

    def allHeadings( self, items, **kw  ):
      for i, text in enumerate(items):
        super().heading( '#'+str(i), text = text, **kw )

    def __getRowCount(self):
      return len(self.get_children())

    def __setRowCount(self, value):
      allChildren = self.get_children()
      old = len(allChildren)
      while old > value:
        self.delete(allChildren[-1])
        allChildren = allChildren[:-1]
        old -= 1
      while old < value:
        self.insert( '', 'end', text = '' )
        old += 1

    def __getitem__( self, pos ):
      rowNo, colNo = pos
      rowId = self.get_children()[rowNo]
      row = self.item(rowId)
      if colNo == 0:
        return row['text']
      else:
        if len(row['values']) >= colNo:
              return row['values'][colNo-1]
        else: return ''

    def __setitem__( self, pos, value ):
      if type(pos) == str:
        ttk.Treeview.__setitem__(self, pos, value)
        return
      rowNo, colNo = pos
      rowId = self.get_children()[rowNo]
      row = self.item( rowId )
      if colNo == 0:
        row['text'] = str(value)
      else:
        while len(row['values']) < colNo:
          if type(row['values']) == str:
            row['values'] = [row['values']]
          row['values'].append( '' )
        row['values'][colNo-1] = str(value)
      self.delete( rowId )
      self.insert('', rowNo, iid = rowId, text = row['text'], values = row['values'])
      self.__colorize( rowNo )

    def updateRow( self, rowNo, values ):
      rowId = self.get_children()[rowNo]
      row = self.item( rowId )
      if values:
         row['text'] = values[0]
         row['values'] = values[1:]
      self.delete( rowId )
      self.insert( '', rowNo, text = row['text'], values = row['values'] )
      self.__colorize( rowNo )

    def insertRow( self, rowNo, values ):
      self.insert( '', rowNo, text = values[0], values = values[1:] )
      self.__colorize( rowNo )

    def deleteRow( self, rowNo ):
      rowId = self.get_children()[rowNo]
      self.delete( rowId )
      self.__colorize( rowNo )

    def appendRow( self, values ):
      self.insertRow( 'end', values )

    def clear( self ):
      children = self.get_children()
      for rowId in children:
        self.delete( rowId )

    def __colorize( self, startFrom = 0 ):
      allChildren = self.get_children()
      for i, itemId in enumerate(allChildren):
        if i % 2 == 0:
          self.item(itemId, tags=('even',))
        else:
          self.item(itemId, tags=('odd',))

    def __setOddColor( self, value ):
      self.__oddColor = value
      self.tag_configure( 'odd', background = self.__oddColor )

    def __setEvenColor( self, value ):
      self.__evenColor = value
      self.tag_configure( 'even', background = self.__evenColor )

    def __setOnEditedCell( self, func ):
      self.__onEditedCell = func

    def __destroyEdit(self):
      if self.__edit:
          #self.__var.set( "" )
        self.__edit.destroy()
        self.__edit = None

    def __editSelectAll(self):
      self.__edit.selection_range(0, 'end')
      return 'break'

    def __updateCell( self, cell ):
      class cellUpdateEvent():
        def __init__(self, cell, oldData, newData):
          self.cell_row = cell[0]
          self.cell_col = cell[1]
          self.row_id = cell[2]
          self.old_data = oldData
          self.new_data = newData
      rowNo, colNo, rowId = cell
      editedData = self.__edit.text # self.__var.get()
      oldData = self.__getitem__( (rowNo, colNo) )
      self.__setitem__( (rowNo, colNo), editedData )
      self.__destroyEdit()
      if self.__onEditedCell:
        event = cellUpdateEvent( cell, oldData, editedData )
        self.__onEditedCell( event )

    def editCell( self, cell, colNo = None ):
      if not colNo:
        rowNo, colNo, rowId = cell
      else:
        rowNo = cell
        rowId = self.get_children()[rowNo]
        cell = (rowNo, colNo, rowId)
      try:
        x, y, width, height = self.bbox( rowId, '#'+str(colNo) )
      except: return
      self.__destroyEdit()
        #self.__edit = tkinter.Entry(self, exportselection = True, borderwidth = 0 )
        #self.__edit["textvariable"] = self.__var
      self.__edit = TEdit(self, exportselection = True, borderwidth = 0 )
      self.__edit.place( x = x, y = y, width = width, height = height )
      self.__edit.insert( 0, self.__getitem__((rowNo, colNo)) )
      self.__edit.focus_force()
      self.__edit.bind("<Control-a>", lambda event: self.__editSelectAll() )
      self.__edit.bind("<Escape>", lambda event: self.__destroyEdit())
      self.__edit.bind("<FocusOut>", lambda event: self.__destroyEdit())
      self.__edit.bind("<Return>", lambda event: self.__updateCell(cell) )

    def __getFont ( self ):
      style = self.style
      return style['font'] if 'font' in style else None

    def __setFont ( self, value ):
      self.__setStyle( font = value )
      boldFont = value + ('bold',) if not 'bold' in value else value
      self.__setHeadingStyle( font = boldFont )

    def __getStyle( self ):
      style = ttk.Style()
      return style.configure("Treeview")

    def __setStyle( self, **kw ):
      style = ttk.Style()
      style.configure("Treeview", **kw )

    def __getHeadingStyle ( self ):
      return ttk.Style().configure("Treeview.Heading")

    def __setHeadingStyle( self, **kw ):
      style = ttk.Style()
      style.configure("Treeview.Heading", **kw )

    def __getRoot( self ):
      if not self.__parent: return None
      if isinstance(self.__parent, TApplication):
        return self.__parent
      else:
        return self.__parent.root

    size = property(lambda x: x.__size, __setSize)
    position = property(lambda x: x.__position, __setPosition)
    align = property(lambda x: x.__align, __setAlign)
    background = property(__getBackground, __setBackground)
    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

    onEditedCell = property(lambda x: x.__onEditedCell, __setOnEditedCell)

    rowCount = property(__getRowCount, __setRowCount)
    oddColor = property( lambda x: x.__oddColor, __setOddColor)
    evenColor = property( lambda x: x.__evenColor, __setEvenColor)
    font = property(__getFont, __setFont)
    style = property( __getStyle, __setStyle )
    headingStyle = property( __getHeadingStyle, __setHeadingStyle )

    root = property( __getRoot )

class TImageViewer(TApplication):
    def __init__(self):
        TApplication.__init__(self,'picture view')
        self.position=(500,600)
        self.size=(700,400)
        self.panel=TPanel(self,relief='raised',
                                height=55,
                                bd=10
                          )
        self.panel.align = 'top'
        self.panel.background = 'purple'

        self.openBtn=TButton(self,
                width=110,
                height=30,
                text='open file')
        self.openBtn.position = (5, 5)
        self.openBtn.background = 'pink'
        self.openBtn.font = 10

        self.openBtn2 = TButton(self,
                               width=110,
                               height=30,
                               text='open file')
        self.openBtn2.position = (300, 5)
        self.openBtn2.background = 'pink'
        self.openBtn2.font = 10

        self.centerCb=TCheckBox(self,
                                text='picture in centre')
        self.centerCb.position = (115, 5)
        self.centerCb.font = 10
        self.centerCb.background = 'pink'

        self.centerCb2 = TCheckBox(self,
                                  text='picture in centre')
        self.centerCb2.position = (400, 5)
        self.centerCb2.font = 10
        self.centerCb2.background = 'pink'


        self.centerCb.onChange = self.cbChange
        self.centerCb2.onChange = self.cbChange2

        self.Image=TImage(self,
                          bg='red')
        self.Image.align = 'client'

        self.Image2 = TImage(self,
                            bg='red')
        self.Image2.align = 'client'

        self.openBtn.onClick = self.selectfle
        self.openBtn2.onClick = self.selectfle2

    def selectfle(self,sender):
        fname = filedialog.askopenfilename(
            filetypes=[("Все файлы", '*.*'), ('Файлы GIF', '*.gif')]
        )
        self.Image.picture = fname

    def cbChange(self,sender):
        if sender.checked:
            self.Image.center = True
        else:
            self.Image.center = False

    def selectfle2(self,sender):
        fname = filedialog.askopenfilename(
            filetypes=[("Все файлы", '*.*'), ('Файлы GIF', '*.gif')]
        )
        self.Image2.picture = fname

    def cbChange2(self,sender):
        if sender.checked:
            self.Image2.center = True
        else:
            self.Image2.center = False

class TIntEdit(TEdit):
    def __init__(self, parent, **kw):
        TEdit.__init__(self,parent, **kw)
        self.__value = 0
        self.onValidate = self.__validate


    def __validate(self):
        try:
            newValue = int(self.text)
            self.__value = newValue
            return True
        except:
            return False

    def __setValue(self,newvalue):
        self.__value = newvalue
        self.text = str(newvalue)

    value = property(lambda x: x.__value, __setValue)