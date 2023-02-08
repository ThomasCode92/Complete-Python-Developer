from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
gray_scale_img = img.convert('L')

print(img)
print(img.format, img.size)

filtered_img.save('blur.png', 'png')
gray_scale_img.save('gray.png', 'png')

img = Image.open('./astro.jpg')
img.thumbnail((400, 400))

img.save('thumbnail.jpg')
print(img.format, img.size)
