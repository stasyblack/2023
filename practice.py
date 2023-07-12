from osgeo import gdal

def split_image(image_path, tile_size):
    dataset = gdal.Open(image_path)
    width = dataset.RasterXSize
    height = dataset.RasterYSize
    k=0
    for i in range(0, width, tile_size):
        for j in range(0, height, tile_size):
                tile = dataset.ReadAsArray(i, j, tile_size, tile_size)
                #вызов функции по обработке




image_path = "NHT.tif"
tile_size = 512
split_image(image_path, tile_size)
