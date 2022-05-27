from PIL import Image, ImageDraw, ImageFont
import pandas as pd

font = ImageFont.truetype("font/malgun.ttf", 25)
text_width = 550
text_height = 40
f = open("./data/gt.txt", 'w', encoding="UTF8")

filename = 'place.csv'
df = pd.read_csv(filename, names=['place'], encoding='utf-8')

place_arr = df['place'].values.tolist()
index = 0

for text in place_arr:
  f.write('images/'+str(index)+'.png\t'+text+'\n')

  canvas = Image.new('RGB', (text_width, text_height), "white")
  draw = ImageDraw.Draw(canvas)
  w, h = font.getsize(text)
  draw.text(((text_width-w)/2.0,(text_height-h)/2.0), text, 'black', font)

  canvas.save('./data/'+str(index)+'.png', "PNG")
  index += 1

f.close()