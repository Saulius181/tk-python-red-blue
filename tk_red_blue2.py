#!/usr/bin/env python

__author__ = "Saulius Bartkus"
__copyright__ = "Copyright 2017"

__license__ = "GPL"
__version__ = "2.0.1"
__maintainer__ = "Saulius Bartkus"
__email__ = "saulius181@yahoo.com"
__status__ = "Production"

PLAYER_COLOR = "red"
AI_COLOR = "blue"
EMPTY_COLOR = "white"

from tkinter import *
import random

class game_controller(object):
	
	def clear_data(self):
		self.canvas.data["openCells"] = [0,1,2,3,4,5,6,7,8]	
		for y in range(3):
			for x in range(3):
				self.canvas.itemconfigure(self.canvas.data["gameBoard"][y][x], fill=EMPTY_COLOR, tag=EMPTY_COLOR)

	def get_state(self, a, color):
		if self.canvas.gettags(a+1)[0] == color:
			return True
		else:
			return False
	
	def check_three_states(self, a, b, c):
		if self.canvas.gettags(a+1)[0] == self.canvas.gettags(b+1)[0] == self.canvas.gettags(c+1)[0] != EMPTY_COLOR:
			return True
		else:
			return False	
			
	def check_game_state(self):
		if self.check_three_states(0, 1, 2):
			return True
		elif self.check_three_states(3, 4, 5):
			return True
		elif self.check_three_states(6, 7, 8):
			return True
		elif self.check_three_states(0, 3, 6):
			return True
		elif self.check_three_states(1, 4, 7):
			return True
		elif self.check_three_states(2, 5, 8):
			return True
		elif self.check_three_states(0, 4, 8):
			return True	
		elif self.check_three_states(2, 4, 6):
			return True
		else:
			return False

	def ai(self):
		if self.get_state(0, AI_COLOR) and self.get_state(4, AI_COLOR) and self.get_state(8, EMPTY_COLOR):
			ai_pick = 8
		elif self.get_state(1, AI_COLOR) and self.get_state(4, AI_COLOR) and self.get_state(7, EMPTY_COLOR):
			ai_pick = 7
		elif self.get_state(2, AI_COLOR) and self.get_state(4, AI_COLOR) and self.get_state(6, EMPTY_COLOR):
			ai_pick = 6
		elif self.get_state(3, AI_COLOR) and self.get_state(4, AI_COLOR) and self.get_state(5, EMPTY_COLOR):
			ai_pick = 5
		elif self.get_state(5, AI_COLOR) and self.get_state(4, AI_COLOR) and self.get_state(3, EMPTY_COLOR):
			ai_pick = 3
		elif self.get_state(6, AI_COLOR) and self.get_state(4, AI_COLOR) and self.get_state(2, EMPTY_COLOR):
			ai_pick = 2
		elif self.get_state(7, AI_COLOR) and self.get_state(4, AI_COLOR) and self.get_state(1, EMPTY_COLOR):
			ai_pick = 1
		elif self.get_state(8, AI_COLOR) and self.get_state(4, AI_COLOR) and self.get_state(0, EMPTY_COLOR):
			ai_pick = 0
			
		elif self.get_state(0, AI_COLOR) and self.get_state(1, AI_COLOR) and self.get_state(2, EMPTY_COLOR):
			ai_pick = 2
		elif self.get_state(0, AI_COLOR) and self.get_state(2, AI_COLOR) and self.get_state(1, EMPTY_COLOR):
			ai_pick = 1
		elif self.get_state(1, AI_COLOR) and self.get_state(2, AI_COLOR) and self.get_state(0, EMPTY_COLOR):
			ai_pick = 0			

		elif self.get_state(6, AI_COLOR) and self.get_state(7, AI_COLOR) and self.get_state(8, EMPTY_COLOR):
			ai_pick = 8
		elif self.get_state(6, AI_COLOR) and self.get_state(8, AI_COLOR) and self.get_state(7, EMPTY_COLOR):
			ai_pick = 7
		elif self.get_state(7, AI_COLOR) and self.get_state(8, AI_COLOR) and self.get_state(6, EMPTY_COLOR):
			ai_pick = 6					

		elif self.get_state(0, AI_COLOR) and self.get_state(3, AI_COLOR) and self.get_state(6, EMPTY_COLOR):
			ai_pick = 6
		elif self.get_state(0, AI_COLOR) and self.get_state(6, AI_COLOR) and self.get_state(3, EMPTY_COLOR):
			ai_pick = 3
		elif self.get_state(3, AI_COLOR) and self.get_state(6, AI_COLOR) and self.get_state(0, EMPTY_COLOR):
			ai_pick = 0					

		elif self.get_state(2, AI_COLOR) and self.get_state(5, AI_COLOR) and self.get_state(8, EMPTY_COLOR):
			ai_pick = 8
		elif self.get_state(2, AI_COLOR) and self.get_state(8, AI_COLOR) and self.get_state(5, EMPTY_COLOR):
			ai_pick = 5
		elif self.get_state(5, AI_COLOR) and self.get_state(8, AI_COLOR) and self.get_state(2, EMPTY_COLOR):
			ai_pick = 2					

		elif self.get_state(0, PLAYER_COLOR) and self.get_state(4, PLAYER_COLOR) and self.get_state(8, EMPTY_COLOR):
			ai_pick = 8
		elif self.get_state(1, PLAYER_COLOR) and self.get_state(4, PLAYER_COLOR) and self.get_state(7, EMPTY_COLOR):
			ai_pick = 7
		elif self.get_state(2, PLAYER_COLOR) and self.get_state(4, PLAYER_COLOR) and self.get_state(6, EMPTY_COLOR):
			ai_pick = 6
		elif self.get_state(3, PLAYER_COLOR) and self.get_state(4, PLAYER_COLOR) and self.get_state(5, EMPTY_COLOR):
			ai_pick = 5
		elif self.get_state(5, PLAYER_COLOR) and self.get_state(4, PLAYER_COLOR) and self.get_state(3, EMPTY_COLOR):
			ai_pick = 3
		elif self.get_state(6, PLAYER_COLOR) and self.get_state(4, PLAYER_COLOR) and self.get_state(2, EMPTY_COLOR):
			ai_pick = 2
		elif self.get_state(7, PLAYER_COLOR) and self.get_state(4, PLAYER_COLOR) and self.get_state(1, EMPTY_COLOR):
			ai_pick = 1
		elif self.get_state(8, PLAYER_COLOR) and self.get_state(4, PLAYER_COLOR) and self.get_state(0, EMPTY_COLOR):
			ai_pick = 0

		elif self.get_state(0, PLAYER_COLOR) and self.get_state(1, PLAYER_COLOR) and self.get_state(2, EMPTY_COLOR):
			ai_pick = 2
		elif self.get_state(0, PLAYER_COLOR) and self.get_state(2, PLAYER_COLOR) and self.get_state(1, EMPTY_COLOR):
			ai_pick = 1
		elif self.get_state(1, PLAYER_COLOR) and self.get_state(2, PLAYER_COLOR) and self.get_state(0, EMPTY_COLOR):
			ai_pick = 0			

		elif self.get_state(6, PLAYER_COLOR) and self.get_state(7, PLAYER_COLOR) and self.get_state(8, EMPTY_COLOR):
			ai_pick = 8
		elif self.get_state(6, PLAYER_COLOR) and self.get_state(8, PLAYER_COLOR) and self.get_state(7, EMPTY_COLOR):
			ai_pick = 7
		elif self.get_state(7, PLAYER_COLOR) and self.get_state(8, PLAYER_COLOR) and self.get_state(6, EMPTY_COLOR):
			ai_pick = 6			

		elif self.get_state(0, PLAYER_COLOR) and self.get_state(3, PLAYER_COLOR) and self.get_state(6, EMPTY_COLOR):
			ai_pick = 6
		elif self.get_state(0, PLAYER_COLOR) and self.get_state(6, PLAYER_COLOR) and self.get_state(3, EMPTY_COLOR):
			ai_pick = 3
		elif self.get_state(3, PLAYER_COLOR) and self.get_state(6, PLAYER_COLOR) and self.get_state(0, EMPTY_COLOR):
			ai_pick = 0		
		elif self.get_state(2, PLAYER_COLOR) and self.get_state(5, PLAYER_COLOR) and self.get_state(8, EMPTY_COLOR):
			ai_pick = 8	
		elif self.get_state(2, PLAYER_COLOR) and self.get_state(8, PLAYER_COLOR) and self.get_state(5, EMPTY_COLOR):
			ai_pick = 5
		elif self.get_state(5, PLAYER_COLOR) and self.get_state(8, PLAYER_COLOR) and self.get_state(2, EMPTY_COLOR):
			ai_pick = 2	
			
		elif self.get_state(4, EMPTY_COLOR):
			ai_pick = 4
		elif self.get_state(4, AI_COLOR):
			if self.get_state(0, PLAYER_COLOR) and self.get_state(8, EMPTY_COLOR):
				ai_pick = 8
			elif self.get_state(8, PLAYER_COLOR) and self.get_state(0, EMPTY_COLOR):
				ai_pick = 0
			elif self.get_state(6, PLAYER_COLOR) and self.get_state(2, EMPTY_COLOR):
				ai_pick = 2
			elif self.get_state(2, PLAYER_COLOR) and self.get_state(6, EMPTY_COLOR):
				ai_pick = 6
			
			elif self.get_state(0, AI_COLOR) and self.get_state(1, PLAYER_COLOR) and self.get_state(6, EMPTY_COLOR) and self.get_state(3, EMPTY_COLOR):
				ai_pick = random.choice([6,3])
			elif self.get_state(0, AI_COLOR) and self.get_state(3, PLAYER_COLOR) and self.get_state(2, EMPTY_COLOR) and self.get_state(1, EMPTY_COLOR):
				ai_pick = random.choice([2,1])
			elif self.get_state(2, AI_COLOR) and self.get_state(5, PLAYER_COLOR) and self.get_state(0, EMPTY_COLOR) and self.get_state(1, EMPTY_COLOR):
				ai_pick = random.choice([0,1])
			elif self.get_state(6, AI_COLOR) and self.get_state(3, PLAYER_COLOR) and self.get_state(8, EMPTY_COLOR) and self.get_state(7, EMPTY_COLOR):
				ai_pick = random.choice([8,7])
			elif self.get_state(6, AI_COLOR) and self.get_state(7, PLAYER_COLOR) and self.get_state(0, EMPTY_COLOR) and self.get_state(3, EMPTY_COLOR):
				ai_pick = random.choice([0,3])
			elif self.get_state(8, AI_COLOR) and self.get_state(7, PLAYER_COLOR) and self.get_state(2, EMPTY_COLOR) and self.get_state(5, EMPTY_COLOR):
				ai_pick = random.choice([2,5])
			elif self.get_state(8, AI_COLOR) and self.get_state(5, PLAYER_COLOR) and self.get_state(6, EMPTY_COLOR) and self.get_state(7, EMPTY_COLOR):
				ai_pick = random.choice([6,7])
			
			elif self.get_state(0, EMPTY_COLOR) and self.get_state(2, EMPTY_COLOR) and self.get_state(6, EMPTY_COLOR) and self.get_state(8, EMPTY_COLOR):
				ai_pick = random.choice([0,2,6,8])
			else:
				ai_pick = random.choice(self.canvas.data["openCells"])
		elif self.get_state(4, PLAYER_COLOR):
			corners = []
			for i in [0,2,6,8]:
				if self.get_state(i, EMPTY_COLOR):
					corners.append(i)
			if corners:
				ai_pick = random.choice(corners)
			else:
				ai_pick = random.choice(self.canvas.data["openCells"])
		else:
			ai_pick = random.choice(self.canvas.data["openCells"])			
		
		self.canvas.itemconfig(ai_pick+1, fill=AI_COLOR, tag=AI_COLOR)
		self.canvas.data["openCells"].remove(ai_pick)
		
		if self.check_game_state():
			self.canvas.data["play"] = None
			self.canvas.itemconfigure(self.text, text="AI wins" )
		elif not self.canvas.data["openCells"]:
			self.canvas.data["play"] = None
			self.canvas.itemconfigure(self.text, text="It's a draw" )			
		else:
			self.canvas.data["play"] = True

	def start(self):
		if self.canvas.data["play"] is None:
			self.clear_data()
			if random.randint(0, 1):
				self.canvas.data["play"] = True
			else:
				self.canvas.data["play"] = False
			
			if not self.canvas.data["play"]:
				self.ai()
				self.canvas.data["play"] = True
				
			self.canvas.itemconfigure(self.text, text="Player turn." )
			
		elif self.canvas.data["play"] is False:
			pass
		else:
			pass

	def quit(self):
		self.root.destroy()

	def on_click(self, event):
		if self.canvas.data["play"]:
			if self.canvas.gettags(CURRENT) and self.canvas.gettags(CURRENT)[0] in [EMPTY_COLOR, PLAYER_COLOR]:
				self.canvas.itemconfigure(CURRENT, fill="#550000", tags=self.canvas.gettags(CURRENT))

	def on_release(self, event):
		if self.canvas.data["play"]:
			if self.canvas.gettags(CURRENT) and self.canvas.gettags(CURRENT)[0] == PLAYER_COLOR:
				self.canvas.itemconfigure(CURRENT, fill="#ff5555", tags=(PLAYER_COLOR, "current"))
			elif self.canvas.gettags(CURRENT) and self.canvas.gettags(CURRENT)[0] == EMPTY_COLOR:
				self.canvas.itemconfigure(CURRENT, fill="#ff5555", tags=(PLAYER_COLOR, "current"))
				
				self.canvas.data["openCells"].remove(self.currentID[0]-1)
				
				if self.check_game_state():
					self.canvas.data["play"] = None
					self.canvas.itemconfigure(self.text, text="Player wins" )
				elif not self.canvas.data["openCells"]:
					self.canvas.data["play"] = None
					self.canvas.itemconfigure(self.text, text="It's a draw" )	
				else:
					self.canvas.data["play"] = False
					self.ai()
		
	def on_enter(self, event):
		if self.canvas.data["play"]:
			self.currentID = self.canvas.find_withtag(CURRENT)
			self.canvas.itemconfigure(self.currentID[0], fill="#ff5555")		

	def on_leave(self, event):
		if self.canvas.data["play"]:
			self.canvas.itemconfigure(self.currentID[0], fill=self.canvas.gettags(self.currentID[0])[0])
	
	def __init__(self, root):
		self.root = root
		self.canvas = Canvas(root, width=450, height=310)

		self.canvas.pack()	
		self.button1 = Button(self.canvas, text = "New game", anchor = W, command = self.start)
		self.button1.place(x=310,y=25)
		self.button2 = Button(self.canvas, text = "Quit", anchor = W, command = self.quit)
		self.button2.place(x=380,y=25)		
	
		self.canvas.bind("<Button-1>", self.on_click)
		self.canvas.bind("<ButtonRelease-1>", self.on_release)
		self.canvas.data = { }
		self.canvas.data["play"] = None
		
		self.canvas.data["gameBoard"] = {}
		self.canvas.data["openCells"] = [0,1,2,3,4,5,6,7,8]	
		
		for y in range(3):
			self.canvas.data["gameBoard"][y] = {}
			for x in range(3):
				self.canvas.data["gameBoard"][y][x] = self.canvas.create_rectangle(10 + x*100, 10 +y*100, 100+ x*100, 100 +y*100, fill=EMPTY_COLOR, tag=EMPTY_COLOR)
				self.canvas.tag_bind(self.canvas.data["gameBoard"][y][x], "<Enter>", self.on_enter)
				self.canvas.tag_bind(self.canvas.data["gameBoard"][y][x], "<Leave>", self.on_leave)	
		
		self.text = self.canvas.create_text(310,10, text="Red/Blue", anchor='w')
				
if __name__ == "__main__":
	root = Tk()
	root.title("RedBlue Tk")
	root.resizable(0,0)
	game = game_controller(root);
	root.mainloop()
