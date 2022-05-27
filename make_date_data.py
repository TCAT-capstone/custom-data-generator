from PIL import Image, ImageDraw, ImageFont
import random

n = 30

font = ImageFont.truetype("font/malgun.ttf", 25)
text_width = 550
text_height = 40
f = open("./data/gt.txt", 'w', encoding="UTF8")

for index in range(n):
  y = random.randrange(2010, 2023)
  m = str(random.randrange(1, 13)).zfill(2)
  d = str(random.randrange(1, 32)).zfill(2)
  w = random.choice(["일", "월", "화", "수", "목", "금", "토"])
  t = random.choice(["오전", "오후"])
  h = random.randrange(1, 13)
  mm = str(random.randrange(0, 6)*10).zfill(2)

  text = '일 시:  {}년 {}월 {}일 [{}] {} {}시 {}분'.format(y, m, d, w, t, h, mm)
  f.write('images/'+str(index)+'.png\t'+text+'\n')

  canvas = Image.new('RGB', (text_width, text_height), "white")
  draw = ImageDraw.Draw(canvas)
  w, h = font.getsize(text)
  draw.text(((text_width-w)/2.0,(text_height-h)/2.0), text, 'black', font)

  canvas.save('./data/'+str(index)+'.png', "PNG")
  print(text)

f.close()