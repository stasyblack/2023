from PIL import Image
import numpy as np

# Размер перекрытия
overlap = 30
#Количество фрагментов по ширине и высоте
number = 3

def split_image(image_path):
    # Открываем изображение
    image = Image.open(image_path)
    
    
    # Получаем размеры изображения
    width, height = image.size
    
    
    # Размер каждой части
    part_width = width // number
    part_height = height // number
    
    
    
    parts = []
    
    for i in range(number):
        for j in range(number):
            # Вырезаем часть изображения с учетом перекрытия
            left = j * part_width - overlap
            top = i * part_height - overlap
            if (top<0):
                top=0
            if (left<0):
                left=0
            right = (j + 1) * part_width + overlap
            if (right>width):
                right=width
            bottom = (i + 1) * part_height + overlap
            if (bottom>height):
                bottom=height
            
            part = image.crop((left, top, right, bottom))
            parts.append(part)
            
            # Сохраняем часть изображения
            part.save(f"part_{i}_{j}.jpg")
    
    return parts

def merge_images(parts):
    # Получаем размеры частей изображения
    part_width, part_height = parts[0].size
    
    # Размеры результирующего изображения с учетом перекрытия
    width = part_width * number - number * overlap
    height = part_height * number - number * overlap
    
    # Создаем новое изображение 
    merged_image = Image.new("RGB", (width, height))
    
    for i in range(number):
        for j in range(number):
            # Вставляем часть изображения в результирующее изображение с учетом перекрытия
            if i == 0 and j == 0:
                merged_image.paste(parts[i * number + j], (0, 0))
            elif i == 0:
                merged_image.paste(parts[i * number + j], (j * part_width - (j+1)*overlap, 0))
            elif j == 0:
                merged_image.paste(parts[i * number + j], (0, i * part_height - (i+1)*overlap))
            else:
                merged_image.paste(parts[i * number + j], (j * part_width - (j+1)*overlap, i * part_height - (i+1)*overlap))
    
    # Сохраняем результирующее изображение
    merged_image.save("merged_image.jpg")


# Разделение изображения на части
parts = split_image("1.jpg")

# Объединение частей в первоначальное изображение
merge_images(parts)
