from tkinter import * 
from PIL import ImageTk, Image

root = Tk()
root.title("Image Visualizator")
root.iconbitmap("icono.ico")
root.geometry('568x334')
root.resizable(width=0, height=0)

def next_image():
    global miImage
    global index
    if index == 3:
        index = 0
    else:
        index = index + 1
    miImage = image_list[index]
    image_shown = Label(root, image=miImage)
    image_shown.grid(column=1, row=0)

def previous_image():
    global miImage
    global index
    if index == 0:
        index = 3
    else:
        index = index - 1
    print(index)
    miImage = image_list[index]
    image_shown = Label(root, image=miImage)
    image_shown.grid(column=1, row=0)
    

duck1 = ImageTk.PhotoImage(Image.open("duck1.jpg"))
duck2 = ImageTk.PhotoImage(Image.open("duck2.jpg"))
duck3 = ImageTk.PhotoImage(Image.open("duck3.jpg"))
duck4 = ImageTk.PhotoImage(Image.open("duck4.jpg"))

image_list = [duck1, duck2, duck3, duck4]

index = 0

miImage = image_list[index]
image_shown = Label(root, image=miImage)
image_shown.grid(column=1, row=0)

previousButton = Button(root, text="<", height=2, width=2, bg="blue", fg="white", font=("bold"), command=previous_image)
previousButton.grid(column=0, row=0, columnspan=True)

nextButton = Button(root, text=">", height=2, width=2, bg="blue", fg="white", font=("bold"), command=next_image)
nextButton.grid(column=2, row=0, columnspan=True)


root.mainloop()