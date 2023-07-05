from osgeo import gdal

dem = gdal.Open("/home/anastasia/Рабочий стол/practice2023/po_311159_pan_0000000.tif")
gt = dem.GetGeoTransform()

xmin= gt[0]
ymax = gt[3]
res = gt[1]
xlen = res * dem.RasterXSize
ylen =  res* dem.RasterYSize

div = 3
xsize = xlen/div
ysize = ylen/div

xsteps = [xmin + xsize * i for i in range(div+1)]
ysteps = [ymax - ysize * i for i in range(div+1)]

for i in range(div):
    for j in range(div):
        xmin = xsteps[i]
        xmax =  xsteps[i+1]
        ymax = ysteps[j]
        ymin = ysteps[j+1]

        print ("xmin: "+str(xmin))
        print ("xmax: "+str(xmax))
        print ("ymin: "+str(ymin))
        print ("ymax: "+str(ymax))
        print ("\n")

        gdal.Warp("dem"+str(i)+str(j)+".tif", dem, 
            outputBounds = (xmin, ymin, xmax, ymax), dstNodata = -9999)
        gdal.Translate("dem translate"+str(i)+str(j)+".tif", dem, 
            projWin = (xmin, ymax, xmax, ymin))