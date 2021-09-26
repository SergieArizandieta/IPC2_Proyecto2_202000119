
from tkinter import * 
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

import main
import cargaMaquina as cm
import cargaSimulacion as s

Nombre = ""

imgOriginal= './IMG_Programa/auxiliar.png'
imgMirrorx= './IMG_Programa/auxiliar.png'
imgMirrory= './IMG_Programa/auxiliar.png'
imgMirrorDouble= './IMG_Programa/auxiliar.png'

opcion = ["No data"]
def ventanas():
    try:
        global imgOriginal
        global imgMirrorx
        global imgMirrory
        global imgMirrorDouble
        global opcion
        

        ventana = Tk()
        ventana.title('Proyecto 1')
        ventana.geometry("1500x800")

        def cerrar():
            exit()

        def CargaMaquina():
            print("Carga Maquina")
            cm.cargarListas(cm.openMaquina())
            ProductosIndividuales['values'] = cm.Lproductos.ListadoProductoss()  
            ReporteSecuencia['values'] = cm.Lproductos.ListadoProductoss()  

        def OperarIndividual():
            global Nombre
            Nombre = ProductosIndividuales.get()
            ComboText= ProductosIndividuales.get()
            #print("Individual - ",ComboText)

            cm.LLineas.ElaborarManual(ComboText,"INDIVIDUAL")
            
        def ReporteSecuenciaIn():
            ComboText= ReporteSecuencia.get()
            Boxtextt = TextBoxSeg.get("1.0",'end-1c')
            
            if Boxtextt == "" or ComboText == "":
                messagebox.showinfo(title="Error", message="Ingrese un valor")
            elif isNumero(Boxtextt) == False:
                messagebox.showinfo(title="Error", message="Ingrese un numero")
            else:
                if int(Boxtextt) > 0:
                    cm.LLineas.ReporteGraphivz(ComboText,int(Boxtextt))
                else:
                    messagebox.showinfo(title="Error", message="Ingrese un numero mayor a 0")
    
        def isNumero(txt):
            try:
                int(txt)
                it_is = True
                return it_is
            except ValueError:
                it_is = False
                return it_is


        def OperarMasivo():
            print("Masivo")
            s.cargarListasSimulacino(s.openSimulacion())
            
        def sustituir():
            global Nombre
            Nombre = ProductosIndividuales.get()
            ComboText= ProductosIndividuales.get()

     
            #print(ComboText)
            #listado =  Op.lista_e.buscar(ImagenesCombo.get())

            #definir(listado)
            #ventana.destroy()
            #destruir()
            #ventanas
            
        notebook = ttk.Notebook(ventana)
        notebook.pack(fill=BOTH, expand=1)

        pes0 = ttk.Frame(notebook)
        notebook.add(pes0,text='Inicio')

        pes1 = ttk.Frame(notebook)
        notebook.add(pes1,text='Cargas')

        pes2 = ttk.Frame(notebook)
        notebook.add(pes2,text='Produto')

        pes3 = ttk.Frame(notebook)
        notebook.add(pes3,text='Generar Reportes')



        #Pestana 1 ------------------------------------------------------------------------------------
        Button(pes0,text="Salir",command= cerrar).place(x=1400, y =0)

        Welcome = ImageTk.PhotoImage(Image.open('./IMG_Programa/Welcome.png').resize((700, 300)))
        lblWlecome = Label(pes0)
        lblWlecome['image'] =  Welcome
        lblWlecome.place(x=400, y =105)

        #Pestana 2 ------------------------------------------------------------------------------------
        Button(pes1,text="Salir",command= cerrar).place(x=1400, y =0)

        Label(pes1,text="Cargar configuracion maquina:",fg="Gray",font=("Popins",12)).place(x=550, y =25)
        Button(pes1,text="Carga Maquina",command= CargaMaquina).place(x=675, y =70)
        
        Config = ImageTk.PhotoImage(Image.open('./IMG_Programa/config.jpg').resize((700, 300)))
        lblMaquina = Label(pes1)
        lblMaquina['image'] =  Config
        lblMaquina.place(x=400, y =255)
       

        #Pesatana 3 -----------------------------------------------------------------------------------
     
        Button(pes2,text="Salir",command= cerrar).place(x=1400, y =0)
        
        Label(pes2,text = "Productos",fg="Gray",font=("Popins",12)).place(x=10, y =25)
        Label(pes2,text = "------------------------------------------------------",fg="Gray",font=("Popins",12)).place(x=15, y= 50)
        Label(pes2,text = "Formas para procesar los productos:",fg="Gray",font=("Popins",12)).place(x=15, y= 75)

        Label(pes2,text = "------------------------------------------------------",fg="Gray",font=("Popins",12)).place(x=25, y= 100)

        Label(pes2,text = "Masiva: selecciona archivo",fg="Gray",font=("Popins",12)).place(x=30, y= 120)
        Button(pes2,text="Carga Masiva",command= OperarMasivo).place(x=30, y= 150)

        Label(pes2,text = "------------------------------------------------------",fg="Gray",font=("Popins",12)).place(x=25, y= 175)

        Label(pes2,text = "Individual: seleccione prodcuto",fg="Gray",font=("Popins",12)).place(x=30, y= 200)
        Button(pes2,text="Producir",command= OperarIndividual).place(x=230, y= 250)

        Label(pes2,text = "------------------------------------------------------",fg="Gray",font=("Popins",12)).place(x=15, y= 275)

        ProductosIndividuales = ttk.Combobox(pes2, width = 27,state="readonly")
        ProductosIndividuales.place(x=30, y= 250)
        #ImagenesCombo.pack( pady=200,)
        ProductosIndividuales.current()
        ProductosIndividuales['values'] = opcion
    
       


        #Pestana 4 ------------------------------------------------------------------------------------
        Button(pes3,text="Salir",command= cerrar).place(x=1400, y =0)
        
        Label(pes3,text = "Generar Reportes",fg="Gray",font=("Popins",12)).place(x=10, y =25)
        Label(pes3,text = "------------------------------------------------------",fg="Gray",font=("Popins",12)).place(x=15, y= 50)
        Label(pes3,text = "Reporte de cola en secuencia:",fg="Gray",font=("Popins",12)).place(x=15, y= 75)

        Label(pes3,text = "------------------------------------------------------",fg="Gray",font=("Popins",12)).place(x=25, y= 100)

        Label(pes3,text = "Seleccione prodcuto",fg="Gray",font=("Popins",12)).place(x=30, y= 120)

        Label(pes3,text = "Ingrese el segundo que desea generrar el reporte",fg="Gray",font=("Popins",12)).place(x=30, y= 200)
        Button(pes3,text="Producir",command= ReporteSecuenciaIn).place(x=230, y= 300)

        TextBoxSeg = Text(pes3, height = 1, width = 10)
        TextBoxSeg.place(x=30, y= 240)

        ReporteSecuencia = ttk.Combobox(pes3, width = 27,state="readonly")
        ReporteSecuencia.place(x=30, y= 150)
        #ImagenesCombo.pack( pady=200,)
        ReporteSecuencia.current()
        ReporteSecuencia['values'] = opcion
       

        Label(pes3,text = "------------------------------------------------------",fg="Gray",font=("Popins",12)).place(x=15, y= 275)

        #Terminar ------------------------------------------------------------------------------------
    
        ventana.mainloop() 
    except Exception:
       
        print("Error, v")
"""
def reportes():
    ReporteTokens()
    ReporteTErrores()
    print("reportes")"""

def destruir():
    main.abrir_ventana()

def definir(listado):

    
    global imgOriginal
    global imgMirrorx
    global imgMirrory
    global imgMirrorDouble
    print(listado)
     
    imgOriginal= listado[0]
    imgMirrorx=  listado[1]
    imgMirrory=  listado[2]
    imgMirrorDouble=  listado[3]

    """ imgOriginal = './IMG_generada/Cubo_ORIGINAL.png'
    imgMirrorx= './IMG_generada/Cubo_MIRRORX.png'
    imgMirrory= './IMG_generada/Cubo_MIRRORY.png'
    imgMirrorx= './IMG_generada/Cubo_DOUBLE.png'"""