from osgeo import gdal
import numpy as np

def split_image(image_path, tile_size, overlap):
    dataset = gdal.Open(image_path)
    width = dataset.RasterXSize
    height = dataset.RasterYSize
    num_blocks_x = int(np.ceil((width - overlap) / (tile_size - overlap)))
    num_blocks_y = int(np.ceil((height - overlap) / (tile_size - overlap)))
    tile = np.zeros((num_blocks_y, num_blocks_x, tile_size, tile_size, dataset.RasterCount), dtype=np.uint8)

    for i in range(num_blocks_y):
        for j in range(num_blocks_x):
            y_start = i * (tile_size - overlap)
            x_start = j * (tile_size - overlap)
            y_end = y_start + tile_size
            x_end = x_start + tile_size
            if y_end > height:
                y_end = height
                y_start = y_end - tile_size
            if x_end > width:
                x_end = width
                x_start = x_end - tile_size
            for k in range(dataset.RasterCount):
                band = dataset.GetRasterBand(k+1)
                tile[i, j, :, :, k] = band.ReadAsArray(x_start, y_start, tile_size, tile_size)
    process_tile(tile)

def process_tile(tile):
    print('Обработка массива изображений')

def main():
    image_path = "NHT.tif"
    tile_size = 512
    overlap = 30
    split_image(image_path, tile_size, overlap)

main()
