from osgeo import gdal

def split_image(image_path, tile_size):
    dataset = gdal.Open(image_path)
    width = dataset.RasterXSize
    height = dataset.RasterYSize

    for i in range(0, width, tile_size):
        for j in range(0, height, tile_size):
            if (i + tile_size <= width) and (j + tile_size <= height):
                tile = dataset.ReadAsArray(i, j, tile_size, tile_size)
                process_tile(tile)

def process_tile(tile):
    print('Обработка изображения')

def main():
    image_path = "NHT.tif"
    tile_size = 512
    split_image(image_path, tile_size)

main()
