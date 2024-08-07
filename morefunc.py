import tkinter
import math

def parabola(page,size):
    for x in range(-size,size):
        y=x*x/size
        plot(page,x,-y)

def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill='white')
    canvas.create_line(0, y_origin, 0, -y_origin, fill='white')



def circle(page, radius, g, h):
    for x in range(g, g + radius):
        y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
        plot(page, x, y)
        plot(page, x, 2 * h - y)
        plot(page, 2 * g - x, y)
        plot(page, 2 * g - x, 2 * h  - y)


  
def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill='red')

    
mainWindow = tkinter.Tk()

mainWindow.title('Parabola')
mainWindow.geometry('640x400')

canvas = tkinter.Canvas(mainWindow, width=640, height=480, bg='black')
canvas.grid(row=0, column=0)






draw_axes(canvas)


parabola(canvas,100)
parabola(canvas,200)
mainWindow.mainloop()
