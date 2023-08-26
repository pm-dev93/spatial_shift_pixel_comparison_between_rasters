#Put the name of loaded raster to be compared
rlayer_1 = QgsProject.instance().mapLayersByName('r_uso_terra_3_2021')[0]
rlayer_2 = QgsProject.instance().mapLayersByName('mapbiomas71_uso_terra_2021')[0]

#GET BBOX OF RASTER 1
ext_1 =rlayer_1.extent()
# get the origin points of the raster
origin_1 = [ext_1.xMinimum(), ext_1.yMaximum()]

#GET BBOX OF RASTER 2
ext_2 = rlayer_2.extent()
# get the origin points of the raster
origin_2 = [ext_2.xMinimum(), ext_2.yMaximum()]


#GET DIFFERENCE BETWEEN RASTER 1 AND RASTER 2
difshift= [origin_2 - origin_1 for origin_2, origin_1 in zip(origin_2, origin_1)]
#PIXEL SIZE:
pixelhightx = rlayer_1.rasterUnitsPerPixelX()
pixelhighty = rlayer_1.rasterUnitsPerPixelY()
#GET DIFFERENCE BETWEEN RASTER 1 AND RASTER 2 as % of pixelheight
difpercentage = [(difshift[0]/pixelhightx)*100, (difshift[1]/pixelhighty)*100]


#print(difunits)
print("X SHIFT units: %s units" %(difshift[0]))
print("Y SHIFT units %s units" %(difshift[1]))

#print(difpercentage)
print("X SHIFT %%: %s%%" %(difpercentage[0]))
print("Y SHIFT %%: %s%%" %(difpercentage[1]))