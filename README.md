# spatial_shift_pixel_comparison_between_rasters
IMPORTANT DISCLAIMER: Code 2 with spatial shift, was not made by me. I could not find its source, if you know, please contact me here so I can give the proper credits!

Keep in mind that this code assumes that both rasters have the same dimensions and are georeferenced in the same coordinate system. If your rasters have different dimensions or coordinate systems, you may need to perform additional preprocessing before comparison.

The two code snippets provided are quite different in terms of functionality, but both appear to aim at comparing and reporting differences between two raster datasets. However, they approach the comparison in different ways and measure different aspects of the differences. Let's compare them in more detail:

**Code 1 (using `rasterio`):**

This code reads raster data using the `rasterio` library, calculates the absolute pixel-wise differences between corresponding pixels in the two rasters, and then identifies and reports the locations where the differences exceed a given threshold.

**Code 2 (using QGIS API):**

This code is more focused on geospatial analysis and seems to be written in the context of the QGIS API. It appears to deal with the difference in georeferencing (spatial shift) between the two raster layers. It calculates the spatial shift (in units and percentage of pixel height) between the two raster layers' origins and pixel sizes. It's primarily concerned with understanding how the two rasters are shifted in the geographic space.

The main difference between the two codes lies in the aspect of comparison they focus on:

- Code 1: Compares the pixel values of the two rasters to find significant differences.
- Code 2: Measures the spatial shift (georeferencing) between the two raster layers.

The results they provide will not be the same because they are measuring different things. Code 1 reports differences in pixel values, while Code 2 reports differences in geospatial alignment (shifts in the origin and pixel sizes). Depending on your goal, you should choose the code that best suits your needs.

If you're interested in understanding differences in pixel values and potentially finding areas where the land use has changed, you should use Code 1.

If you're interested in understanding how the two raster layers are spatially shifted relative to each other, you should use Code 2.

If you're looking for a comparison that combines both aspects (pixel value differences and geospatial shifts), you might need to incorporate elements from both codes to achieve your desired outcome.
!!DON'T FORGET TO CHANGE THE RASTER PATH ON CODE 1 AND THE RASTER NAMES EQUAL TO THE QGIS ON CODE 2!!
