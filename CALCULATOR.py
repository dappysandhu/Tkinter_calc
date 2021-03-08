from tkinter import *

# the main class
class Calc():
  def __init__(self):
    self.total = 0
    self.current = ""
    self.new_num = True
    self.op_pending = False
    self.op = ""
    self.eq = False

  def num_press(self, num):
    self.eq = False
    temp = text_box.get()
    temp2 = str(num)    
    if self.new_num:
      self.current = temp2
      self.new_num = False
    else:
      if temp2 == '.':
        if temp2 in temp:
          return
      self.current = temp + temp2
    self.display(self.current)

  def calc_total(self):
    self.eq = True
    self.current = float(self.current)
    if self.op_pending == True:
      self.do_sum()
    else:
      self.total = float(text_box.get())

  def display(self, value):
    text_box.delete(0, END)
    text_box.insert(0, value)

  def do_sum(self):
    if self.op == "add":
      self.total += self.current
    if self.op == "minus":
      self.total -= self.current
    if self.op == "times":
      self.total *= self.current
    if self.op == "divide":
      self.total /= self.current
    self.new_num = True
    self.op_pending = False
    self.display(self.total)

  def operation(self, op): 
    self.current = float(self.current)
    if self.op_pending:
      self.do_sum()
    elif not self.eq:
      self.total = self.current
    self.new_num = True
    self.op_pending = True
    self.op = op
    self.eq = False

  def cancel(self):
    self.eq = False
    self.current = "0"
    self.display(0)
    self.new_num = True

  def all_cancel(self):
    self.cancel()
    self.total = 0
  
  def sign(self):
    self.eq = False
    self.current = -(float(text_box.get()))
    self.display(self.current)

sum1 = Calc()
root = Tk()
calc = Frame(root)
calc.grid()

root.title("Calculator")
root.iconbitmap('C:/Users/dappy/Desktop/Python_Calculator/Calculator-2.ico')     
root.resizable(width=FALSE, height=FALSE)
text_box = Entry(calc, justify = RIGHT, bd = 10, fg = "white", bg = "black", width = 24, font = ('Helvetica', 20))
text_box.grid(row = 0, column = 0, columnspan = 4, pady = 5)
text_box.insert(0, "0")

# make the buttons
numbers = "789456123"
i = 0
bttn = []
for j in range(2,5):
  for k in range(3):
    bttn.append(Button(calc, text = numbers[i], width=12, height=5))
    bttn[i].grid(row = j, column = k, padx = 1, pady = 1)
    bttn[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
    i += 1

bttn_0 = Button(calc, text = "0", width=12, height=5)
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row = 5, column = 0, padx = 1, pady = 1)

bttn_div = Button(calc, text = chr(247), width=12, height=5, bg = "gray70")
bttn_div["command"] = lambda: sum1.operation("divide")
bttn_div.grid(row = 1, column = 3, padx = 1, pady = 1)

bttn_mult = Button(calc, text = chr(215), width=12, height=5, bg = "gray70")
bttn_mult["command"] = lambda: sum1.operation("times")
bttn_mult.grid(row = 2, column = 3, padx = 1, pady = 1)

minus = Button(calc, text = "-", width=12, height=5, bg = "gray70")
minus["command"] = lambda: sum1.operation("minus")
minus.grid(row = 3, column = 3, padx = 1, pady = 1)

point = Button(calc, text = ".", width=12, height=5)
point["command"] = lambda: sum1.num_press(".")
point.grid(row = 5, column = 1, padx = 1, pady = 1)

add = Button(calc, text = "+", width=12, height=5, bg = "gray70")
add["command"] = lambda: sum1.operation("add")
add.grid(row = 4, column = 3, padx = 1, pady = 1)

neg= Button(calc, text =  chr(177), width=12, height=5)
neg["command"] = sum1.sign
neg.grid(row = 1, column = 2, padx = 1, pady = 1)

clear = Button(calc, text = "C", width=12, height=5, bg = "tomato")
clear["command"] = sum1.cancel
clear.grid(row = 1, column = 1, padx = 1, pady = 1)

all_clear = Button(calc, text = "AC", width=12, height=5, bg ="tomato")
all_clear["command"] = sum1.all_cancel
all_clear.grid(row = 1, column = 0, padx = 1, pady = 1)

equals = Button(calc, text = "=", width=26, height=5, bg = "steel blue")
equals["command"] = sum1.calc_total
equals.grid(row = 5, column = 2, padx = 1, pady = 1, columnspan = 2)

root.mainloop()