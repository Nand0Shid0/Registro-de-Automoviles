from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox as MessageBox
import sqlite3
#conexion a la base de datos
conexion = sqlite3.connect('BaseCarros.db')
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre, edad , correo ,telefono,curp PRIMARY KEY)")
conexion.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS domicilio (curp PRIMARY KEY,calle,colonia,codigopostal,numerocasa,color)")
conexion.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS carro (curp PRIMARY KEY,marca,modelo,año,placa,color)")
conexion.commit()


 
def Registrar():
    
    n = nombre.get()
    e = edad.get()
    cu = curp.get()
    t = telefono.get()
    co = correo.get()
    ca = calle.get()
    col = colonia.get()
    nc = NumeroCas.get()
    cop = cp.get()
    ch = ColorHouse.get()
    m = Marca.get()
    mo = Modelo.get()
    añ = Año.get()
    coc = ColorCar.get()
    pl = Placa.get()

    if cu == "":
        MessageBox.showerror('Campos Vacios','NO dejes campos vacios')
        pass
    if m  == "":
         MessageBox.showerror('Campos Vacios','NO dejes campos vacios')
         pass

    else:
        cursor.execute('INSERT INTO usuarios values (?,?,?,?,?)',(n,e,co,t,cu))
        cursor.execute('INSERT INTO domicilio values (?,?,?,?,?,?)',(cu,ca,col,cop,nc,ch))
        cursor.execute('INSERT INTO carro values (?,?,?,?,?,?)',(cu,m,mo,añ,pl,coc))
        conexion.commit()

        nombre.set('')
        edad.set('')
        curp.set('')
        telefono.set('')
        correo.set('')
        calle.set('')
        colonia.set('')
        NumeroCas.set('')
        cp.set('')
        ColorHouse.set('')
        Marca.set('')
        Modelo.set('')
        Año.set('')
        ColorCar.set('')
        Placa.set('')

def consultar(cu):
    cursor.execute('SELECT * FROM usuarios WHERE curp = ?',(cu,))
    a = cursor.fetchall()
    return a

def consultar2(cu):
    cursor.execute('SELECT * FROM domicilio WHERE curp = ?',(cu,))
    b = cursor.fetchall()
    return b

def consultar3(plac):
    cursor.execute('SELECT * FROM carro WHERE curp = ?',(plac,))
    c= cursor.fetchall()
    return c


def listar ():
    cu = curp3.get()
    res = consultar (cu)
    res2 = consultar2(cu)
    res3 = consultar3(cu)
    scroll.delete('1.0',END)
    
    for fila in res:
        scroll.insert(END,'Nombre:  '+ str(fila[0]) +"\nEdad:  " + str(fila[1]) + "\nCorreo:  "+ str(fila[2])+"\nTelefono:  " + str(fila[3]) +"\nCURP:  " + str(fila[4]) +  "\n\n",)

    for fila2 in res2:
        scroll.insert(END,'Calle:  '+ str(fila2[1]) +"\nColonia:  " + str(fila2[2]) + "\nCP:  "+ str(fila2[3])+ "\nN Casa:  " + str(fila2[4]) + "\nColor:  "+str(fila2[5])+"\n\n",)

    for fila3 in res3:
        scroll.insert(END,'Marca:  '+ str(fila3[1]) +"\nModelo:  " + str(fila3[2]) + "\nAño:  "+ str(fila3[3])+"\nPlaca:  "+ str(fila3[4]) +"\nColor:  " +str(fila3[5])+"\n\n",)

def eliminar():
    try:
        
        cu2 = curp2.get()
        a = MessageBox.askquestion('¿Seguro?','¿Estas Seguro de eliminar el Usuario?')
        if a == 'yes':
            cursor.execute('DELETE FROM usuarios WHERE curp = ?', (cu2,))
            conexion.commit()
            cursor.execute('DELETE FROM domicilio WHERE curp = ?',(cu2,))
            conexion.commit()
            cursor.execute('DELETE FROM carro WHERE curp = ? ',(cu2,))
            conexion.commit()
            MessageBox.showinfo('Exitoso','¡¡¡Usuario Eliminado de Manera Exitosa!!!')
            curp2.set('')
        else:
            pass
    except:
        MessageBox.showerror('Error','Revisa Bien la Placa o CURP!!!')


def Actualizar():
    try:
        edadd = eda.get()
        tel = num3.get()
        cal = calle2s.get()
        col = colonia2s.get()
        cd = cdp.get()
        ncasa = num2s.get()
        colr = colors.get()
        co= correo2.get()

        cu2 = curup.get()
        cursor.execute("UPDATE usuarios SET edad ='"+ edadd +"'WHERE curp =?",(cu2,))
        cursor.execute("UPDATE usuarios SET correo ='"+ co +"'WHERE curp =?",(cu2,))
        cursor.execute("UPDATE usuarios SET telefono ='"+ tel +"'WHERE curp =?",(cu2,))
        cursor.execute("UPDATE domicilio SET calle ='"+ cal +"'WHERE curp =?",(cu2,))
        cursor.execute("UPDATE domicilio SET colonia ='"+ col +"'WHERE curp =?",(cu2,))
        cursor.execute("UPDATE domicilio SET codigopostal ='"+ cd +"'WHERE curp =?",(cu2,))
        cursor.execute("UPDATE domicilio SET numerocasa ='"+ ncasa +"'WHERE curp =?",(cu2,))
        cursor.execute("UPDATE domicilio SET color ='"+ colr +"'WHERE curp =?",(cu2,))
        conexion.commit()
        MessageBox.showinfo('Exitoso','Datos Actualizados para: ' + cu2 +' :)')

        eda.set('')
        num3.set('')
        calle2s.set('')
        colonia2s.set('')
        cdp.set('')
        num2s.set('')
        colors.set('')  
        correo.set('') 

    except:
        MessageBox.showerror('Error','Revisa Bien la Informacion')
        eda.set('')
        num3.set('')
        calle2s.set('')
        colonia2s.set('')
        cdp.set('')
        num2s.set('')
        colors.set('')  
        correo.set('')



def salir ():
    a = MessageBox.askokcancel('Salir','¿Desae salir?(Recuerda Guardar Cambios)')
    if a == True:
        window.destroy()
    else:
        pass



window = Tk()
window.geometry('1300x600')
window.resizable(0,0)
window.iconbitmap('dgo.ico')
window.title('Registro de Automoviles')

cuaderno1 = ttk.Notebook(window)
cuaderno1.grid(column=0,row=0)
frame1 = Frame(cuaderno1)
frame1.config(height=800,width=1300)
frame1.pack()

'''--------------------------AGREGAR USUARIO--------------------------'''
cuaderno1.add(frame1,text='Agregar')
label1 = LabelFrame(frame1,text='Agregar usuario',fg='white',background='#B22222',font=('Arial',12))
label1.place(x=400,y=0,width=1300,height=800)

labelf = LabelFrame(frame1,text='Carro',fg='white',background='#FF0000',font=('Arial',12))
labelf.place(x=0,y=0,width=400,height=800)

marcalabel = Label(labelf,text='Marca',font=('Arial',12),background='#FF0000',fg='white')
marcalabel.place(x=5,y=5)

Marca = StringVar()
Marca_entry = Entry (labelf, textvariable=Marca,background='#0000CD',font=('Arial',12),justify='center')
Marca_entry.place(x=90,y=5)

modelolabel = Label(labelf,text='Modelo',font=('Arial',12),background='#FF0000',fg='white')
modelolabel.place(x=5,y=60)

Modelo = StringVar()
modelo_entry = Entry(labelf, textvariable=Modelo,background='#0000CD',font=('Arial',13),justify='center')
modelo_entry.place(x=90,y=60)

añolabel = Label(labelf,text='Año',font=('Arial',12),background='#FF0000',fg='white')
añolabel.place(x=5,y=115)

Año = StringVar()
año_entry = Entry(labelf, textvariable=Año,background='#0000CD',font=('Arial',13),justify='center')
año_entry.place(x=90,y=115)

colorlabel = Label(labelf,text='Color',font=('Arial',12),background='#FF0000',fg='white')
colorlabel.place(x=5,y=165)

ColorCar = StringVar()
colrcar = Entry (labelf, textvariable=ColorCar,background='#0000CD',font=('Arial',13),justify='center')
colrcar.place(x=90,y=165)

placlabel = Label(labelf,text='Placa',font=('Arial',12),background='#FF0000',fg='white')
placlabel.place(x=5,y=220)

Placa = StringVar()
placa_entry = Entry (labelf, textvariable=Placa,background='#0000CD',font=('Arial',13),justify='center')
placa_entry.place(x=90,y=220)

ford = PhotoImage(file='ford.png')
labelimage = Label(labelf, image=ford, bd=0,bg='#FF0000')
labelimage.place(x=5,y=300)

porshe = PhotoImage(file='porshe.png')
labelpor = Label(labelf,image=porshe,bd=0,bg='#FF0000')
labelpor.place(x=250,y=250)

chre = PhotoImage(file='Chevrolet.png')
labelpor = Label(labelf,image=chre,bd=0,bg='#FF0000')
labelpor.place(x=90,y=380)

label_1= Label(label1,text='Nombre',font=('Arial',12),background='#B22222',fg='white')
label_1.place(x=250,y=23)

user = PhotoImage(file='user.png')
labeluser = Label(label1,image=user,bd=0,bg='#B22222')
labeluser.place(x=10,y=10)


nombre=StringVar()
entrynombre=Entry(label1, textvariable=nombre,background='#4169E1',font=('Arial',13),justify='center')
entrynombre.place(x=320,y=23)

label_2= Label(label1,text='Edad',font=('Arial',12),background='#B22222',fg='white')
label_2.place(x=590,y=23)

edad=StringVar()
entryedad=Entry(label1, textvariable=edad,background='#4169E1',font= ('Arial',13),justify='center')
entryedad.place(x=650,y=23)

label_2= Label(label1,text='Correo',font=('Arial',12),background='#B22222',fg='white')
label_2.place(x=250,y=80)

correo = StringVar()
entrycorreo=Entry(label1, textvariable=correo,background='#4169E1',font=('Arial',12),justify='center')
entrycorreo.place(x=320,y=80)

label_tel= Label(label1,text='Telefono',font=('Arial',12),background='#B22222',fg='white')
label_tel.place(x=580,y=80)

telefono = StringVar()
tele_entry = Entry(label1,textvariable=telefono,background='#4169E1',font=('Arial',12),justify='center')
tele_entry.place(x=650,y=83)

curp_label = Label(label1,text= 'CURP',font=('Arial',12),background='#B22222',fg='white')
curp_label.place(x=390,y=150)

curp = StringVar()
curp_entr = Entry (label1,textvariable=curp,background='#4169E1',font=('Arial',12),justify='center')
curp_entr.place(x=450,y=150)

Calle = Label (label1,text='Calle',font=('Arial',12),background='#B22222',fg='white')
Calle.place(x=20,y=255)

calle = StringVar()
calle_entr = Entry (label1,textvariable=calle,background='#4169E1',font=('Arial',12),justify='center')
calle_entr.place(x=90,y=255)

Colonia = Label (label1,text='Colonia',font=('Arial',12),background='#B22222',fg='white')
Colonia.place(x=300,y=255)

colonia = StringVar()
colonia_entr = Entry (label1,textvariable=colonia,background='#4169E1',font=('Arial',12),justify='center')
colonia_entr.place(x=380,y=255)

numero = Label (label1,text='Numero',font=('Arial',12),background='#B22222',fg='white')
numero.place(x=630,y=255)

NumeroCas = StringVar()
numero_entry = Entry(label1,textvariable=NumeroCas,background='#4169E1',font=('Arial',12),justify='center')
numero_entry.place(x=700,y=255)

codigo = Label (label1, text='C.P',font=('Arial',12),background='#B22222',fg='white')
codigo.place(x=70,y=300)

cp = StringVar()
cp_entry = Entry(label1,textvariable=cp,background='#4169E1',font=('Arial',12),justify='center')
cp_entry.place(x=150,y=300)

colorhouse = Label (label1,text='Color Casa',font=('Arial',12),background='#B22222',fg='white')
colorhouse.place(x=470,y=300)

ColorHouse = StringVar()
color_entry = Entry(label1,textvariable=ColorHouse,background='#4169E1',font=('Arial',12),justify='center')
color_entry.place(x=600,y=300)

boton = Button(label1,text='Enviar',command=Registrar,font=('Arial',13),fg='white',background='red')
boton.place(x=150,y=400)
salirbu = Button(label1,text='   Salir   ',command=salir,font=('Arial',12),fg='black',background='blue')
salirbu.place(x=650,y=400)


'''--------------------ELIMINAR USUARIO--------------------'''

pagina2 = Frame(cuaderno1)
pagina2.config(bg='gray')

imagen = PhotoImage(file = "fondo.png")
background = Label(pagina2,image = imagen)
background.place(x = 250, y = 0)
cuaderno1.add(pagina2,text='Eliminar Usuario')
label11 = LabelFrame(pagina2,text='Eliminar',fg='black',background='gray',font=('Comic Sans MS',12))
label11.place(x=400,y=20,width=500,height=500)

label_curp = Label(label11,text='CURP: ',font=('Arial',12),bg='gray',fg='white')
label_curp.place(x=140,y=45)
#
curp2 = StringVar()
entry_curp = Entry(label11,textvariable=curp2,bg='light gray',justify='center')
entry_curp.place(x=220,y=45)
#
imagen2 = PhotoImage(file = "descargar.png")
background2 = Label(label11,image = imagen2,bg='gray',bd=0)
background2.place(x =140, y = 100)

boton2 = Button(label11,text='Eliminar',command=eliminar)
boton2.place(x=215,y=120)


'''----------------------------MOSTRAR INFO----------------------------'''

pagina4 = Frame(cuaderno1)
pagina4.config(bg='#FF69B4')
cuaderno1.add(pagina4,text='Mostrar Info')
label12 = LabelFrame(pagina4,text='Buscar Usuario',fg='black',background='#FF1493',font=('Comic Sans MS',12))
label12.place(x=50,y=50,width=500,height=500)
#
label_curp2 = Label(label12,text='CURP:',font=('Arial',12),bg='#FF1493',fg='yellow')
label_curp2.place(x=100,y=45)
curp3 = StringVar()

entry_curp2 = Entry(label12,textvariable=curp3,background='#7CFC00',justify='center',font=('Arial',11))
entry_curp2.place(x=200,y=45)

boton3 = Button(label12,text='Buscar',command=listar,font=('Arial',12),fg='yellow',bg='#FF1493')
boton3.place(x=215,y=120)

imagen3 = PhotoImage(file = "search.png")
background3 = Label(pagina4,image = imagen3,bg='#FF1493')
background3.place(x = 200, y = 250)

scroll = st.ScrolledText(pagina4)
scroll.config(bg='#FF1493',fg='white',font=('Arial',12),width=50)
scroll.place(x=600,y=80)




'''----------------------ACTUALIZAR USUARIO----------------------'''

pagina5 = Frame(cuaderno1)
pagina5.config(background='#FF4500')
cuaderno1.add(pagina5,text='Actualizar Info')

labeltitle = Label (pagina5,text='Actualizar Usuario',font=('Arial',20),bg=	'#FF4500',fg='yellow')
labeltitle.place(x=500,y=10)


curup = StringVar()
entry_curpup= Entry(pagina5,textvariable=curup,bg='#7CFC00',justify='center',font=('Arial',11))
entry_curpup.place (x=350,y=60)
labelcur= Label(pagina5,text='Curp: ',font=('Arial',12),bg='#FF4500',fg='yellow')
labelcur.place(x=300,y=60)

labelsub = Label(pagina5,text=' Nuevos Datos de Usuario',font=('Arial',12),background='#FF4500',fg='yellow')
labelsub.place(x=460,y=100)

label_color = Label (pagina5,text='Numero:',font=('Arial',12),background='#FF4500',fg='yellow')
label_color.place(x=430,y=150)

num3 = StringVar()
numEntry = Entry (pagina5, textvariable=num3,background='#7CFC00',font=('Arial',12),justify='center')
numEntry.place(x=500,y=150)
#
label_edad = Label(pagina5,text='Edad:',font=('Arial',12),background='#FF4500',fg='yellow')
label_edad.place(x=430,y=200)

eda = StringVar()
edaEntry = Entry (pagina5, textvariable=eda,background='#7CFC00',font=('Arial',12),justify='center')
edaEntry.place(x=500,y=200)
#
label_correo = Label(pagina5,text='Correo:',font=('Arial',12),background='#FF4500',fg='yellow')
label_correo.place(x=430,y=250)

correo2= StringVar()
CalleEntry = Entry (pagina5, textvariable=correo2,background='#7CFC00',font=('Arial',12),justify='center')
CalleEntry.place(x=500,y=250)

labelsub2 = Label(pagina5,text='Nuevo Domicilio',font=('Arial',12),background='#FF4500',fg='yellow')
labelsub2.place(x=250,y=100)

#
label_color = Label (pagina5,text='Color',font=('Arial',12),background='#FF4500',fg='yellow')
label_color.place(x=150,y=150)

colors = StringVar()
ColorEntry = Entry (pagina5, textvariable=colors,background='#7CFC00',font=('Arial',12),justify='center')
ColorEntry.place(x=200,y=150)
#
labelcolonia = Label(pagina5,text='Colonia',font=('Arial',12),background='#FF4500',fg='yellow')
labelcolonia.place(x=140,y=200)

colonia2s = StringVar()
ColoEntry = Entry (pagina5, textvariable=colonia2s,background='#7CFC00',font=('Arial',12),justify='center')
ColoEntry.place(x=200,y=200)
#
labelcalle = Label(pagina5,text='Calle',font=('Arial',12),background='#FF4500',fg='yellow')
labelcalle.place(x=150,y=250)

calle2s = StringVar()
CalleEntry = Entry (pagina5, textvariable=calle2s,background='#7CFC00',font=('Arial',12),justify='center')
CalleEntry.place(x=200,y=250)
#
labelnum = Label(pagina5,text='Numero',font=('Arial',12),background='#FF4500',fg='yellow')
labelnum.place(x=140,y=300)

num2s = StringVar()
umEntry = Entry (pagina5, textvariable=num2s,background='#7CFC00',font=('Arial',12),justify='center')
umEntry.place(x=200,y=300)
#
codigolabel =  Label(pagina5,text='C.P',font=('Arial',12),background='#FF4500',fg='yellow')
codigolabel.place(x=150,y=350)

cdp = StringVar()
cdEntry = Entry (pagina5, textvariable=cdp,background='#7CFC00',font=('Arial',12),justify='center')
cdEntry.place(x=200,y=350)


re = PhotoImage(file='refresh.png')
labelre = Label(pagina5,image=re,bg='#FF4500')
labelre.place(x=800,y=100)

boton3 = Button(pagina5,text='Actualizar',command=Actualizar,font=('Arial Black',15),bg='orange')
boton3.place(x=380,y=400)

window.mainloop()