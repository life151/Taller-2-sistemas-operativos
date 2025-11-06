import tkinter as tk
from tkinter import messagebox
import subprocess
import webbrowser

root = tk.Tk()
root.title("shell.grafico-universidad")
root.geometry("600x400")
root.resizable(False, False)
root.configure(bg="#e9ecef")

def crear_boton(texto, comando):
    return tk.Button(
        root,
        text=texto,
        command=comando,
        bg="#0078D7",
        fg="white",
        activebackground="#005A9E",
        activeforeground="white",
        relief="raised",
        width=25,
        height=2,
        bd=4,
        cursor="hand2"
    )
    
def abrir_terminal():
    
    try:    
        subprocess.Popen(["cmd"])
    except FileNotFoundError:
        messagebox.showerror("Error", "No se pudo abrir la terminal.")   

def abrir_navegador():
    try:
        webbrowser.open("https://www.google.com")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir el navegador: {e}")

titulo = tk.Label(              
    root,
    text="BIENVENIDOS A ENTORNO GRAFICO-UNIVERSIDAD",
    bg="#e9eef2",
    fg="#333333",
    font="Arial 16 bold")


titulo.pack(pady=20)

frame_botones= tk.Frame(root, bg="#e9eef2")
frame_botones.pack(pady=30)

btn_navegador= crear_boton("Abrir Navegador Web", abrir_navegador)

def abrir_editor():
    try:
        subprocess.Popen(["notepad"])
    except FileNotFoundError:
        messagebox.showerror("Error", "No se pudo abrir el editor de texto.")

btn_editor=crear_boton("Abrir Editor de Texto", abrir_editor)

btn_terminal=crear_boton("Abrir Terminal", abrir_terminal)  

btn_navegador.pack(pady=10)
btn_editor.pack(pady=10)
btn_terminal.pack(pady=10)

pie=tk.Label(
    root,
    text="Universidad-shell.grafico ",
    bg="#161B1E",
    fg="#777",
    font="Arial 10 italic"
)

root.mainloop()
