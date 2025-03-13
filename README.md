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

### Updating Script Paths
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
<img alt="Lumerical Settings" width="800px" src="/readme_images/lum_settings.png"/>
14. In the Lumerical Node window, select "Load" and choose the grating file `..\Lumerical_files\custom_1D_slant.fsp`.
15. Click "Reload Parameterization" and object trees for the Inputs and Ouputs box should appear if the above steps were done correctly.
<img alt="Lumerical Settings" width="800px" src="/readme_images/lum_node.png"/>

## Updating the Speos node
16. Open the Speos node named `Mode01_demo.scdocx` and navigate to `Execution settings`.
17. Check the box for "Python Script Post update" and update the script file to point to `..\Speos_files\json_swap.py`.
18. Update the speos file to point to `..\Speos_files\Model01_demo.scdocx`
19. If done correctly, the node settings should show the parameters exposed from the Speos file:
<img alt="Lumerical Settings" width="800px" src="/readme_images/speos_node.png"/>
20. Open the node named `Ansys Speos Output` and select `Relative to working dir` for the file load method, and then select `Load` and point to `..\Speos_files\SPEOS isolated files\Direct.1.speos\Direct.1.Report.html`
21. Click the backslash (\) before the `\SPEOS isolated files\Direct.1.speos\Direct.1.Report.html`. This sets the node to look for the results html file in the form of the given folder structure. This is needed by the optimizer to find and report the simulation results.
<img alt="Lumerical Settings" width="800px" src="/readme_images/speos_node2.png"/>
