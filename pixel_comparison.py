import rasterio
import numpy as np

def compare_rasters(raster1_path, raster2_path, threshold=0.1):
    with rasterio.open(raster1_path) as src1, rasterio.open(raster2_path) as src2:
        # Read raster data
        data1 = src1.read(1)
        data2 = src2.read(1)
        
        # Calculate the absolute difference between rasters
        difference = np.abs(data1 - data2)
        
        # Find where the difference exceeds the threshold
        dislocation_indices = np.where(difference > threshold)
        
        if len(dislocation_indices[0]) > 0:
            print("Dislocation found at the following coordinates:")
            for row, col in zip(*dislocation_indices):
                print(f"X: {col}, Y: {row}, Difference: {difference[row, col]}")
        else:
            print("No significant dislocation found.")

# Specify paths to the raster files
raster1_path = "path/to/first/raster.tif"
raster2_path = "path/to/second/raster.tif"

# Call the function to compare rasters
compare_rasters(raster1_path, raster2_path)
