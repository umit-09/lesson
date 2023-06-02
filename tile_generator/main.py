from PIL import Image
import glob
import os

root_dir = "./item/"
output_directory = "./tiles/"
box_size = 16
image_width = 16 * box_size
image_height = 16 * box_size
tile_count = 0
current_tile = 0

def save_image(image, tile_count):
    tileset_path = os.path.join(output_directory, f"unicode_page_{tile_count}.png")
    image.save(tileset_path)

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

im1 = Image.new('RGBA', (image_width, image_height), color='#0000')

for filename in glob.iglob(root_dir + '*.png', recursive=True):
    im2 = Image.open(filename)

    # Check if the image needs to be sliced
    if im2.width > box_size or im2.height > box_size:
        # Slice the image into 16x16 tiles
        for y in range(0, im2.height, box_size):
            for x in range(0, im2.width, box_size):
                tile = im2.crop((x, y, x + box_size, y + box_size))
                tile_x = (current_tile % 16) * box_size
                tile_y = (current_tile // 16) * box_size
                im1.paste(tile, (tile_x, tile_y))
                current_tile += 1

                if current_tile == 16 * 16:
                    save_image(im1, tile_count)
                    im1 = Image.new('RGBA', (image_width, image_height), color='#0000')
                    tile_count += 1
                    current_tile = 0
    else:
        # Paste the whole image into the tileset
        x = (current_tile % 16) * box_size
        y = (current_tile // 16) * box_size
        im1.paste(im2, (x, y))
        current_tile += 1

        if current_tile == 16 * 16:
            save_image(im1, tile_count)
            im1 = Image.new('RGBA', (image_width, image_height), color='#0000')
            tile_count += 1
            current_tile = 0

    print(f"\033[0;31mSet ID:\033[0m \033[0;32m{tile_count}\033[0m  \033[0;31mCurrent image:\033[0m \033[0;32m{filename.split('./item')[1]}\033[0m")

# Save the final image if there are remaining tiles
if current_tile > 0:
    save_image(im1, tile_count)