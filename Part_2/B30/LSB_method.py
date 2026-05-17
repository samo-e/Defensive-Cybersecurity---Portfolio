from PIL import Image

img = Image.open("original_pic.png")
pixels = img.load()

watermark = "AI_WM_2026"

binary = ''.join(format(ord(c), '08b') for c in watermark)
index = 0

for y in range(img.height):
    for x in range(img.width):
        if index < len(binary):
            r, g, b = pixels[x, y]
            r = (r & ~1) | int(binary[index])
            pixels[x, y] = (r, g, b)
            index += 1

img.save("watermarked_pic.png")