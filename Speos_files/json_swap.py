# Python Script, API Version = V251

#Change working directory to the design directory of each optislang iteration
#import os
#fullpath = os.getenv('OSL_DESIGN_DIR')
#seperator = os.getenv('OSL_DESIGN_NAME')
#directory_path = fullpath.rsplit(seperator,1)[0]

#Add the directory to the json output folder.
#backslashes in strings require 2 to escape properly, e.g. `\\`
#make sure the end of the path ends with backslash too, e.g. C:\\examples\\
directory_path = "C:\\Users\\slin\\Desktop\\Lumerical_Examples_Models\\GitHub\\lum_speos_optimization\\Optislang_optimization\\output_gratingjson\\"

# Parameterize variables
period = Parameters.period
duty_cycle = Parameters.duty_cycle
depth = Parameters.depth
slant_angle = Parameters.slant_angle
wavelength = Parameters.wavelength

# Create file name

#format the name in the same way it was one in Lumerical JSON export
json_filename= (
        "p" + str(int(period)) +
        "_dc" + str(int(duty_cycle))  +
        "_d" + str(int(depth)) +
        "_sa" + str(int(slant_angle)) +
        "_wl" + str(int(wavelength)) +
        ".json")     

 # Set the current JSON file path
SopPluginConfigurationPath = directory_path + json_filename #load the json file into the grating object
    
ListSOPIndex = 0
material = SpeosSim.Material.Find("output grating")
SurfaceLayer = material.ListSOP[ListSOPIndex]
SurfaceLayer.SopPluginConfigurationPath = SopPluginConfigurationPath


   