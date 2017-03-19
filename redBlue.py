#!/usr/bin/env python

__author__ = "Saulius Bartkus"
__copyright__ = "Copyright 2017"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Saulius Bartkus"
__email__ = "saulius181@yahoo.com"
__status__ = "Production"

from tkinter import *
import random

class game_controller(object):

	def check_state(self):
		if self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][1], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") != "white":
			return self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill")
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][3], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][5], "fill") != "white":
			return self.canvas.itemcget(self.canvas.data["gameBoard"][3], "fill")
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][7], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") != "white":
			return self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill")
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][3], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") != "white":
			return self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill")
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][1], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][7], "fill") != "white":
			return self.canvas.itemcget(self.canvas.data["gameBoard"][1], "fill")			
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][5], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") != "white":
			return self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill")
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") != "white":
			return self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill")				
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") != "white":
			return self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill")
		else:
			return "white"
			
	def ai(self):
	
		if self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "white":
			cell = 8
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][1], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][7], "fill") == "white":
			cell = 7
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == "white":
			cell = 6
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][3], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][5], "fill") == "white":
			cell = 5
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][5], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][3], "fill") == "white":
			cell = 3
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == "white":
			cell = 2
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][7], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][1], "fill") == "white":
			cell = 1
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == "white":
			cell = 0
			
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][1], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == "white":
			cell = 2
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][1], "fill") == "white":
			cell = 1
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][1], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == "white":
			cell = 0

		elif self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][7], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "white":
			cell = 8
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][7], "fill") == "white":
			cell = 7
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][7], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == "white":
			cell = 6

		elif self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][3], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == "white":
			cell = 6
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][3], "fill") == "white":
			cell = 3
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][3], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == "white":
			cell = 0

		elif self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][5], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "white":
			cell = 8
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][5], "fill") == "white":
			cell = 5
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][5], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == "white":
			cell = 2

		elif self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "white":
			cell = 8
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][1], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][7], "fill") == "white":
			cell = 7
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == "white":
			cell = 6
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][3], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][5], "fill") == "white":
			cell = 5
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][5], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][3], "fill") == "white":
			cell = 3
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == "white":
			cell = 2
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][7], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][1], "fill") == "white":
			cell = 1
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == "white":
			cell = 0
			
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][1], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == "white":
			cell = 2
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][1], "fill") == "white":
			cell = 1
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][1], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == "white":
			cell = 0

		elif self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][7], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "white":
			cell = 8
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][7], "fill") == "white":
			cell = 7
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][7], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == "white":
			cell = 6

		elif self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][3], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == "white":
			cell = 6
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][3], "fill") == "white":
			cell = 3
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][3], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == "white":
			cell = 0

		elif self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][5], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "white":
			cell = 8
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][5], "fill") == "white":
			cell = 5
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][5], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == "white":
			cell = 2
			
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "white":
			cell = 4
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "blue":
			if self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "white":
				cell = 8
			elif self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == "white":
				cell = 6				
			elif self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == "white":
				cell = 2				
			elif self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == "white":
				cell = 0
			
			elif self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][1], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == "white" and self.canvas.itemcget(self.canvas.data["gameBoard"][3], "fill") == "white":
				cell = random.choice([6,3])
			elif self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][3], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == "white" and self.canvas.itemcget(self.canvas.data["gameBoard"][1], "fill") == "white":
				cell = random.choice([1,2])			
			elif self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][1], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "white" and self.canvas.itemcget(self.canvas.data["gameBoard"][5], "fill") == "white":
				cell = random.choice([5,8])						
			elif self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][5], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == "white" and self.canvas.itemcget(self.canvas.data["gameBoard"][1], "fill") == "white":
				cell = random.choice([0,1])	
			elif self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][3], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "white" and self.canvas.itemcget(self.canvas.data["gameBoard"][7], "fill") == "white":
				cell = random.choice([7,8])					
			elif self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][7], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == "white" and self.canvas.itemcget(self.canvas.data["gameBoard"][3], "fill") == "white":
				cell = random.choice([0,3])		
			elif self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][7], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == "white" and self.canvas.itemcget(self.canvas.data["gameBoard"][5], "fill") == "white":
				cell = random.choice([2,5])	
			elif self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == "blue" and self.canvas.itemcget(self.canvas.data["gameBoard"][5], "fill") == "red" and self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == "white" and self.canvas.itemcget(self.canvas.data["gameBoard"][7], "fill") == "white":
				cell = random.choice([6,7])	
				
			elif self.canvas.itemcget(self.canvas.data["gameBoard"][0], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][2], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][8], "fill") == self.canvas.itemcget(self.canvas.data["gameBoard"][6], "fill") == "white":
				cell = random.choice([0,2,6,8])
			else:
				cell = self.canvas.data["openCells"][random.randint(0, len(self.canvas.data["openCells"])-1)]
				
		elif self.canvas.itemcget(self.canvas.data["gameBoard"][4], "fill") == "red":
			corners = []
			for i in [0,2,6,8]:
				if self.canvas.itemcget(self.canvas.data["gameBoard"][i], "fill") == "white":
					corners.append(i)
			if corners:
				cell = random.choice(corners)
			else:
				cell = self.canvas.data["openCells"][random.randint(0, len(self.canvas.data["openCells"])-1)]
		else:
			cell = self.canvas.data["openCells"][random.randint(0, len(self.canvas.data["openCells"])-1)]
			
		self.canvas.itemconfig(self.canvas.data["gameBoard"][cell], fill="blue")
		self.canvas.data["openCells"].remove(cell)
		
		self.canvas.data["game_state"] = self.check_state()
			
		if self.canvas.data["game_state"] != "white":
			self.canvas.itemconfig(self.text, text=self.canvas.data["turn"] + " player wins")
			self.canvas.data["turn"] = "none"
		elif len(self.canvas.data["openCells"]) == 0:
			self.canvas.itemconfig(self.text, text="Draw")
			self.canvas.data["turn"] = "none"
		else:
			self.canvas.data["turn"] = "red"
			self.canvas.itemconfig(self.text, text="Turn: " + self.canvas.data["turn"])
		
	def start(self):
		if random.randint(0, 1):
			self.canvas.data["turn"] = "red"
		else:
			self.canvas.data["turn"] = "blue"
			
		self.canvas.data["openCells"] = [0,1,2,3,4,5,6,7,8]
		
		for row in self.canvas.data["gameBoard"]:
			self.canvas.itemconfig(row, fill="white")
		
		self.canvas.itemconfig(self.text, text="Turn: " + self.canvas.data["turn"])

		if self.canvas.data["turn"] == "blue":
			self.ai()			
		
	def quit(self):
		self.root.destroy()
		
	def mousePressed(self, event):	
		breakBool = False
		if self.canvas.data["turn"] == "red":
			for idx, row in enumerate(self.canvas.data["gameBoard"]):
				if breakBool == True:
					break
				if event.x > self.canvas.coords(row)[0] and event.x < self.canvas.coords(row)[2] and event.y > self.canvas.coords(row)[1] and event.y < self.canvas.coords(row)[3]:
					if self.canvas.itemcget(row, "fill") == "white":
						self.canvas.itemconfig(row, fill="red")
						self.canvas.data["openCells"].remove(idx)
						self.canvas.itemconfig(self.text, text="Turn: " + self.canvas.data["turn"])
						breakBool = True
						
						self.canvas.data["game_state"] = self.check_state()
						
						if self.canvas.data["game_state"] != "white":
							self.canvas.itemconfig(self.text, text=self.canvas.data["turn"] + " player wins")
							self.canvas.data["turn"] = "none"
						elif len(self.canvas.data["openCells"]) == 0:
							self.canvas.itemconfig(self.text, text="Draw")
							self.canvas.data["turn"] = "none"
						else:
							self.canvas.data["turn"] = "blue"
							self.canvas.itemconfig(self.text, text="Turn: " + self.canvas.data["turn"])
							self.ai()						
		
	def __init__(self, root):
		self.root = root
		self.canvas = Canvas(root, width=450, height=310)

		self.canvas.pack()	
		self.button1 = Button(self.canvas, text = "New game", anchor = W, command = self.start)
		self.button1.place(x=310,y=25)
		self.button2 = Button(self.canvas, text = "Quit", anchor = W, command = self.quit)
		self.button2.place(x=380,y=25)		
		
		self.canvas.bind("<Button-1>", self.mousePressed)
		self.canvas.data = { }
		
		if random.randint(0, 1):
			self.canvas.data["turn"] = "red"
		else:
			self.canvas.data["turn"] = "blue"
			
		self.canvas.data["gameBoard"] = []
		self.canvas.data["openCells"] = [0,1,2,3,4,5,6,7,8]	
		
		for y in range(3):
			for x in range(3):
				self.canvas.data["gameBoard"].append(self.canvas.create_rectangle(10 + x*100, 10 +y*100, 100+ x*100, 100 +y*100, fill="white"))
		self.text = self.canvas.create_text(310,10, text="Turn: " + self.canvas.data["turn"], anchor='w')

		if self.canvas.data["turn"] == "blue":
			self.ai()	
				
if __name__ == "__main__":
	root = Tk()
	root.title("RedBlue Tk")
	root.resizable(0,0)
	game = game_controller(root);
	root.mainloop()
