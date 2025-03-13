# Diffraction Grating Optimization
### Ansys Optislang Workflow linking Ansys Lumerical and Ansys Speos 

This repository holds the scripts required to be loaded by Optislang to connect Lumerical and Speos.
The associated simulation files are on SimuTech's Onedrive (contact support@simutechgroup.com).

This workflow leverages the interopability of Ansys tools to connect Ansys Lumerical, Ansys Speos, and Ansys Optislang. The combination of the three tools allows for an optimization workflow for diffraction gratings that correlates diffraction grating parameters with figure of mertis of optical systems.

Behind the scenes, the Lumerical simulations is using the [LSWM Plugin](https://optics.ansys.com/hc/en-us/articles/18427154870803-Lumerical-Sub-Wavelength-Model-plugin-Usage-in-Zemax-OpticStudio) (static link) to generate the grating characterization as a JSON file. The python scripts in this repository export the JSON files automatically and import them into the SPEOS simulation. The results of the SPEOS simulation is then returned to the Optimizer.

## Installation
1. Obtain the simulation files from SimuTech Support.
2. Extract the simulation files to a project directory.
3. Optional: Overwrite the script files with the newest from this repository
4. Edit `..\Lumerical_files\lum_to_optislang.lsf` line 3 to point the path at the directory `..\Lumerical_files`. This path allows the Lumerical libaries to be imported properly for the lsf script.
5. Edit `..\Lumerical_files\lum_to_optislang.lsf` line 3 to point the path at the directory `..\Optislang_optimization\output_gratingjson`. This path is the folder location where the JSON files will be saved to.
6. Edit `..\Speos_files\json_swap.py` line 12 to point at the same directory as Step 5.
7. Open `..\Optislang_optimization\gratings_optimization.opf` to update node paths.

### Updating the Lumerical node
8. Open the Lumerical node named `custom_1D_slant.fsp` and navigate to the `Settings` tab, then select `Change Settings`. In the popup window, point your Lumerical executable path at your Lumerical installation directory (default: `C:\Program Files\ANSYS Inc\v251\Lumerical\bin`).
9. Select Solver: RCWA
10. Check the box for "Run Custom Script"
11. Update the Custom Script to point to `..\Lumerical_files\lum_to_optislang.lsf`
12. Check the box for "Skip Solve"
13. Click "Ok" to save the settings
14. In the Lumerical Node window, select "Load" and choose the grating file `..\Lumerical_files\custom_1D_slant.fsp`.
15. Click "Reload Parameterization" and object trees for the Inputs and Ouputs box should appear if the above steps were done correctly.

## Simulation Setup Checklist
TBD


# Old, to format/remove:

## Lumerical
Lumerical will perform a RCWA simulation and export the results to JSON.
The JSON is saved to a user specified directory for use by Speos through Optislang
- It is important to note the JSON directory will need to be manually deleted when rerunning the Optislang optimization.
## Speos
Speos will load in the JSON file from a user specified folder and perform it's simulations. The results will then be returned to Optislang

To do 
 - Create makefile that recreates the 1D diffraction grating file to avoid uploading .fsp file
 - upload lsf files
 - figure out how to upload speos/opitslang files
