from turtle import Turtle


class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.level = 1
		self.color("black")
		self.hideturtle()
		self.penup()
		self.goto(-220 , 270)
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()
		self.write(f'Level: {self.level}' , align="left" , font=("Arial" , 14 , "bold"))

	def increase_level(self):
		self.level += 1
		self.write(f'Level: {self.level}' , align="left" , font=("Arial" , 14 , "bold"))

	def game_over(self):
		self.goto(0 , 0)
		self.write("GAME OVER" , align="left" , font=("Arial" , 14 , "bold"))
