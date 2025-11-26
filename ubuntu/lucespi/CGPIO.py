import tkinter as tk
import os
from PIL import Image, ImageTk
import time

# ================= FUNCIONES SH =================
def encendersh(opcion):
    rutas = {
        1: "onremoto17.sh",
        2: "onremoto27.sh",
        3: "onremoto22.sh",
        4: "onremoto.sh"
    }
    os.system(f"bash /./home/bh7/lucespi/{rutas[opcion]}")

def apagarsh(opcion):
    rutas = {
        1: "offremoto17.sh",
        2: "offremoto27.sh",
        3: "offremoto22.sh",
        4: "offremoto.sh"
    }
    os.system(f"bash /./home/bh7/lucespi/{rutas[opcion]}")

# ================= FUNCIONES C =================
def encenderc(opcion):
    rutas = {
        1: "onremoto17c.sh",
        2: "onremoto27c.sh",
        3: "onremoto22c.sh",
        4: "onremotoc.sh"
    }
    os.system(f"bash /./home/bh7/lucespi/{rutas[opcion]}")

def apagarc(opcion):
    rutas = {
        1: "offremoto17c.sh",
        2: "offremoto27c.sh",
        3: "offremoto22c.sh",
        4: "offremotoc.sh"
    }
    os.system(f"bash /./home/bh7/lucespi/{rutas[opcion]}")

# ================= FUNCIONES ASM =================
def encenderasm(opcion):
    rutas = {
        1: "onremoto17ASM.sh",
        2: "onremoto27ASM.sh",
        3: "onremoto22ASM.sh",
        4: "onremotoASM.sh"
    }
    os.system(f"bash /./home/bh7/lucespi/{rutas[opcion]}")

def apagarasm(opcion):
    rutas = {
        1: "offremoto17ASM.sh",
        2: "offremoto27ASM.sh",
        3: "offremoto22ASM.sh",
        4: "offremotoASM.sh"
    }
    os.system(f"bash /./home/bh7/lucespi/{rutas[opcion]}")

# ================= FUNCION TIMER =================
def guardar(opcion,mi,hi,mf,hf):
    gpio = {
        1: "17",
        2: "27",
        3: "22",
        4: ""
    }
    print ("Saving...")
    dia="*"
    mes="*"
    ism="*"
    tab=" "
    user="root"
    encender="bash /home/bh7/lucespi/onremoto"+ gpio[opcion] +".sh"
    apagar="bash /home/bh7/lucespi/offremoto"+ gpio[opcion] +".sh"

    inicio=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ism)+''+str(tab)+''+str(user)+''+str(tab)+''+str(encender))
    final=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ism)+''+str(tab)+''+str(user)+''+str(tab)+''+str(apagar))

    os.system("sudo chmod -R 777 /etc/cron.d/evento1")
    os.system("sudo chmod -R 777 /etc/cron.d/evento2")

    pf1=open("/etc/cron.d/evento1","w")
    pf1.write(inicio)
    pf1.write("\n")
    pf1.close()

    pf2=open("/etc/cron.d/evento2","w")
    pf2.write(final)
    pf2.write("\n")
    pf2.close()

    time.sleep(0.1)
           
    os.system("sudo chmod -R 755 /etc/cron.d/evento1")
    os.system("sudo chmod -R 755 /etc/cron.d/evento2")
    time.sleep(0.1)
    os.system("sudo /etc/init.d/cron restart")
   

# ================= VENTANA PRINCIPAL =================
root = tk.Tk()
root.title("Control GPIO")

# ================= CARGAR IMAGEN =================
def cargar_imagen(opcion):
    gpio = {
        1: "17",
        2: "27",
        3: "22",
        4: "0"
    }
    if opcion == 4:
        return  
    pf = open("/home/bh7/lucespi/estado"+ gpio[opcion] +".txt","r")
    estado = pf.readline().strip()
    pf.close()

    if estado == "0":
        img = Image.open("on.png").resize((34, 34))
    else:
        img = Image.open("off.png").resize((34, 34))

    return ImageTk.PhotoImage(img)

# ================= VENTANA TIMER =================
def abrir_timer(numero_gpio):
    gpio_map = {
        1: "17",
        2: "27",
        3: "22",
        4: "TODO"
    }

    ventana = tk.Toplevel(root)
    ventana.title(f"Timer GPIO {gpio_map[numero_gpio]}")
    ventana.resizable(False, False)
 
    # -------- CENTRAR VENTANA --------
    ancho = 260
    alto = 250

    ventana.update_idletasks()
    screen_w = ventana.winfo_screenwidth()
    screen_h = ventana.winfo_screenheight()

    pos_x = (screen_w // 2) - (ancho // 2)
    pos_y = (screen_h // 2) - (alto // 2)

    ventana.geometry(f"{ancho}x{alto}+{pos_x}+{pos_y}")
    
   # ------------ TITULOS ------------
    tk.Label(ventana, text="Inicio", font=("Helvetica", 12, "bold")).pack(pady=5)

    frame_ini = tk.Frame(ventana)
    frame_ini.pack(pady=5)

    tk.Label(frame_ini, text="Hora:").grid(row=0, column=0)
    spin_hi = tk.Spinbox(frame_ini, from_=0, to=23, width=5)
    spin_hi.grid(row=0, column=1, padx=5)

    tk.Label(frame_ini, text="Minuto:").grid(row=0, column=2)
    spin_mi = tk.Spinbox(frame_ini, from_=0, to=59, width=5)
    spin_mi.grid(row=0, column=3, padx=5)

    tk.Label(ventana, text="Fin", font=("Helvetica", 12, "bold")).pack(pady=5)

    frame_fin = tk.Frame(ventana)
    frame_fin.pack(pady=5)

    tk.Label(frame_fin, text="Hora:").grid(row=0, column=0)
    spin_hf = tk.Spinbox(frame_fin, from_=0, to=23, width=5)
    spin_hf.grid(row=0, column=1, padx=5)

    tk.Label(frame_fin, text="Minuto:").grid(row=0, column=2)
    spin_mf = tk.Spinbox(frame_fin, from_=0, to=59, width=5)
    spin_mf.grid(row=0, column=3, padx=5)

    def ejecutar_guardado():
        guardar(numero_gpio,spin_mi.get(),spin_hi.get(),spin_mf.get(),spin_hf.get())
        ventana.destroy()

    tk.Button(ventana, text="GUARDAR", width=15, command=ejecutar_guardado).pack(pady=15)




# ================= FUNCIÓN PARA CREAR PAQUETES =================
def crear_paquete(nombre, numero_gpio):
    frame = tk.LabelFrame(root, text=nombre, font=("Helvetica", 14), padx=10, pady=10)
    frame.pack(fill="x", pady=5)

    contenido = tk.Frame(frame)
    contenido.pack(side=tk.LEFT)

    # -------- Subpaquete Bash --------
    bash_frame = tk.Frame(contenido, bd=1, relief="solid", padx=10, pady=5)
    bash_frame.pack(side=tk.LEFT, padx=5)
    tk.Label(bash_frame, text="Bash").pack()
    tk.Button(bash_frame, text="ON", width=8, command=lambda: encendersh(numero_gpio)).pack(pady=2)
    tk.Button(bash_frame, text="OFF", width=8, command=lambda: apagarsh(numero_gpio)).pack(pady=2)

    # -------- Subpaquete C ----------
    c_frame = tk.Frame(contenido, bd=1, relief="solid", padx=10, pady=5)
    c_frame.pack(side=tk.LEFT, padx=5)
    tk.Label(c_frame, text="C").pack()
    tk.Button(c_frame, text="ON", width=8, command=lambda: encenderc(numero_gpio)).pack(pady=2)
    tk.Button(c_frame, text="OFF", width=8, command=lambda: apagarc(numero_gpio)).pack(pady=2)

    # -------- Subpaquete ASM ----------
    asm_frame = tk.Frame(contenido, bd=1, relief="solid", padx=10, pady=5)
    asm_frame.pack(side=tk.LEFT, padx=5)
    tk.Label(asm_frame, text="ASM").pack()
    tk.Button(asm_frame, text="ON", width=8, command=lambda: encenderasm(numero_gpio)).pack(pady=2)
    tk.Button(asm_frame, text="OFF", width=8, command=lambda: apagarasm(numero_gpio)).pack(pady=2)

    # -------- Subpaquete TIMER --------
    timer_frame = tk.Frame(contenido, bd=1, relief="solid", padx=10, pady=5)
    timer_frame.pack(side=tk.LEFT, padx=5)
    tk.Label(timer_frame, text="Timer").pack()
    tk.Button(timer_frame, text="TIMER", width=8, height= 3,command=lambda: abrir_timer(numero_gpio)).pack(pady=2)

    # ================= COLUMNA DE IMÁGENES =================
    imagen_col = tk.Frame(frame, padx=10)
    imagen_col.pack(side=tk.RIGHT)

    img = cargar_imagen(numero_gpio)
    lbl = tk.Label(imagen_col, image=img)
    lbl.image = img
    lbl.pack(pady=2)

    # --------- ACTUALIZACIÓN EN TIEMPO REAL ---------
    def actualizar_imagenes():
        img = cargar_imagen(numero_gpio)
        lbl.configure(image=img)
        lbl.image = img
        root.after(500, actualizar_imagenes)

    actualizar_imagenes()


# =============== CREACIÓN DE PAQUETES ===============
crear_paquete("GPIO17", 1)
crear_paquete("GPIO27", 2)
crear_paquete("GPIO22", 3)
crear_paquete("TODO", 4)

root.mainloop()
