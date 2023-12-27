from tkinter import *
from number_entry import IntEntry

# Create the main window.
def main():
  root = Tk()
  main_frame = Frame(root)
  answer_flame = Frame(root)
  main_frame.master.title("Area of a Circle")
  main_frame.pack(padx=4, pady=3, fill=BOTH, expand=1)

  #size of the window
  main_frame.master.minsize(500, 300)
  main_frame.master.configure(bg="#F088F0")
  main_frame.place(relx=0.05, rely=0.05, relheight=0.425, relwidth=0.9)
  answer_flame.place(relx=0.05, rely=0.525, relheight=0.425, relwidth=0.9)

  populate_window(main_frame,answer_flame)
  


  root.mainloop()
# Create populate the main window.

def populate_window(frm_main,frm_ans):

  label_diameter = Label(frm_main, text="Diameter:")
  label_diameter.grid(row=0, column=0, padx=10, pady=10)

  entri_diameter = IntEntry(frm_main, width=30, lower_bound=0, upper_bound=1000)
  entri_diameter.grid(row=0, column=1, padx=10, pady=10)

  btn_clear = Button(frm_main, text="clear")
  btn_clear.place(relx=0.8, rely=0.7, relheight=0.3, relwidth=0.2)

  label_area = Label(frm_ans,text="Area:")
  label_area.grid(row=0, column=0, padx=10, pady=10)

  label_ans = Label(frm_ans, text="")
  label_ans.grid(row=0, column=1, padx=10, pady=10)

  


# Grid all the labels, entry boxes, and buttons in a grid.

# Function that  will calculate the circle area.
  def calculate_area(event):
    diameter = entri_diameter.get()
    area = 3.14 * (diameter / 2) ** 2
    label_ans.config(text=f"{area:.2f}")

  def clear():
    entri_diameter.clear()
    entri_diameter.focus()

  btn_clear.config(command=clear)

  entri_diameter.bind("<KeyRelease>", calculate_area)

if __name__ == "__main__":
  main()
