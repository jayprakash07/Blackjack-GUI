import turtle

background = turtle.Screen()
background.bgcolor("grey")
background.addshape("card-back.png")

card_1 = turtle.Turtle()
card_2 = turtle.Turtle()
card_3 = turtle.Turtle()
card_4 = turtle.Turtle()
card_5 = turtle.Turtle()
card_6 = turtle.Turtle()
card_7 = turtle.Turtle()
card_8 = turtle.Turtle()
card_9 = turtle.Turtle()
card_10 = turtle.Turtle()

def setup_play_area(penny):
  penny.goto(180,165)
  penny.fill(True)
  penny.pendown()
  penny.goto(180,-165)
  penny.right(90)
  penny.circle(-15,90)
  penny.goto(-165,-180)
  penny.circle(-15,90)
  penny.goto(-180,165)
  penny.circle(-15,90)
  penny.goto(165,180)
  penny.circle(-15,90)
  penny.color(66,37,6)
  penny.fill(False)
  
  penny.penup()
  penny.color("black")
  penny.goto(165,160)
  penny.pensize(3)
  penny.fill(True)
  penny.pendown()
  penny.goto(165,-160)
  penny.circle(-5,90)
  penny.goto(-160,-165)
  penny.circle(-5,90)
  penny.goto(-165,160)
  penny.circle(-5,90)
  penny.goto(160,165)
  penny.circle(-5,90)
  penny.color("darkgreen")
  penny.fill(False)
  penny.penup()
  penny.goto(0,0)

deckard = turtle.Turtle()
deckard.penup()
deckard.setheading(90)
deckard.shape("card-back.png")

cards_on_table = []
card_turtles = [card_1,card_2,card_3,card_4,card_5,card_6,card_7,card_8,card_9,card_10]

def reset_turtles():
  global cards_on_table
  cards_on_table = []
  for turtle in card_turtles:
    turtle.hideturtle()
    turtle.penup()
    turtle.setheading(90)
    turtle.goto(0,0)

def create_card_image(hand, player):
  if player == "player":
    table_position = -1
  elif player == "dealer":
    table_position = 1
  for card in hand:
    if card in cards_on_table:
      continue
    else:
      background.addshape(card[2])
      card_turtles[(len(cards_on_table))].showturtle()
      card_turtles[(len(cards_on_table))].shape(card[2])
      card_turtles[(len(cards_on_table))].goto(-130+(65*(len(hand)-1)),(130*table_position))
      cards_on_table.append(card)