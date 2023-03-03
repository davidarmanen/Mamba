import piexif
from PIL import Image
import struct

# Open the image
image = Image.open("test.jpg")

# Create a new Exif dictionary
exif_dict = {"GPS": {}}

# Convert latitude and longitude from degrees, minutes, seconds to degrees
lat = (51, 45, 12.56)  # latitude as a tuple of degrees, minutes, seconds
lon = (-1, 15, 27.18)  # longitude as a tuple of degrees, minutes, seconds
lat_deg = lat[0] + lat[1]/60 + lat[2]/3600
lon_deg = lon[0] + lon[1]/60 + lon[2]/3600

# Add GPS metadata
gps_dict = {
    piexif.GPSIFD.GPSLatitude: lat,
    piexif.GPSIFD.GPSLongitude: lon
}
exif_dict['GPS'] = gps_dict

# Convert the Exif dictionary to bytes
exif_bytes = piexif.dump(exif_dict)
piexif.insert(exif_bytes, image)
# Save the image with the new Exif data
image.save("done.jpg", exif=exif_bytes)
