import os
from PIL import Image

def watermark_photo(image_path, watermark_image_path, output_image_path):
    base_image = Image.open(image_path)
    watermark_image = Image.open(watermark_image_path).convert('RGBA')

    image_size = base_image.size
    size_watermark = (int(image_size[0]*8/100), int(image_size[0]*8/100))

    watermark_image = watermark_image.resize(size_watermark)
    new_position = image_size[0]-size_watermark[0]-20, image_size[1]-size_watermark[1]-20

    transparent = Image.new(mode='RGBA', size=image_size, color=(0,0,0,0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark_image, new_position, watermark_image)

    image_mode = base_image.mode
    if image_mode == 'RGB':
        transparent = transparent.convert(image_mode)
    else:
        transparent = transparent.convert('P')
    transparent.save(output_image_path, optimize=True)
    print('Saving...')

folder = input('Enter folder path:')
watermark = input('Enter watermark path:')

os.chdir(folder)
files = os.listdir(os.getcwd())
if not os.path.isdir('output'):
    os.mkdir('output')

for f in files:
    if os.path.isfile(os.path.abspath(f)):
        if f.endswith('.png') or f.endswith('jpg'):
            watermark_photo(f, watermark, 'output/'+f)
