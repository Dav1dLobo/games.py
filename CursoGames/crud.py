from tkinter import *
from ventana import *
def main():
    root = Tk()
    root.wm_title("crud python mySQL")
    app = ventana(root)
    app.mainloop()

if __name__ == "__main__":
    main()