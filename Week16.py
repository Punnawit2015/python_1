import turtle
import random

# จอภาพ
screen = turtle.Screen()
screen.setup(width=800, height=400)
screen.bgcolor("white")
screen.tracer(0)

# โหลดรูปรูป .gif (ต้องมีไฟล์ในโฟลเดอร์เดียวกัน)
screen.addshape("rockv1.gif")
screen.addshape("paperv1.gif")
screen.addshape("scisscorv1.gif")  # ตรวจสอบว่าชื่อไฟล์ตรงกับจริงนะครับ

# แม็ปตัวเลือกไปยังชื่อไฟล์
shape_map = {
    "Rock":    "rockv1.gif",
    "Paper":   "paperv1.gif",
    "Scissors":"scisscorv1.gif"
}

# สุ่มคำตอบคอมพ์
computer = random.choice(list(shape_map.keys()))

# รับคำตอบผู้เล่น แล้ว normalize
raw = input("Enter Rock, Paper, or Scissors: ")
player = raw.strip().title()

print("Computer chose:", computer)
print("Player chose:", player)

# เต่าสำหรับวาดภาพ
t_img = turtle.Turtle(visible=False)
t_img.penup()

# เต่าสำหรับเขียนข้อความ
t_txt = turtle.Turtle(visible=False)
t_txt.penup()

# เช็คว่า valid input ไหม
if player in shape_map:
    # แสดงภาพผู้เล่น
    t_img.goto(-200, 0)
    t_img.shape(shape_map[player])
    t_img.stamp()
    # ข้อความผู้เล่น
    t_txt.goto(-200, -60)
    t_txt.write(f"Player: {player}", align="center", font=("Arial", 16, "normal"))
    
    # แสดงภาพคอมพ์
    t_img.goto(200, 0)
    t_img.shape(shape_map[computer])
    t_img.stamp()
    # ข้อความคอมพ์
    t_txt.goto(200, -60)
    t_txt.write(f"Computer: {computer}", align="center", font=("Arial", 16, "normal"))

    # ตัดสินผล
    if player == computer:
        result = "Draw"
    elif (player=="Rock" and computer=="Scissors") or \
         (player=="Paper" and computer=="Rock") or \
         (player=="Scissors" and computer=="Paper"):
        result = "Player wins"
    else:
        result = "Computer wins"

    # แสดงผลตรงกลาง
    t_txt.goto(0, -150)
    t_txt.write(result, align="center", font=("Arial", 20, "bold"))
    print(result)

else:
    # กรณี invalid input
    t_txt.goto(0, 0)
    t_txt.write("Invalid input!", align="center", font=("Arial", 20, "bold"))
    print("Invalid input. Please enter Rock, Paper, or Scissors.")

screen.update()
turtle.done()
