# lum_speos_optimization
Ansys Lumerical + Ansys Speos + Ansys Optislang Workflow

This repository holds the scripts required to be loaded by Optislang to connect Lumerical and Speos.
The associated simulation files are on SimuTech's Onedrive (contact Stephen or Lauren).

The workflow leverages the interopability of Ansys tools to connect Ansys Lumerical, Ansys Speos, and Ansys Optislang. The combination of the three tools allows for an optimization workflow for diffraction gratings that correlates diffraction grating parameters with figure of mertis of optical systems.

## Installation
TBD

## Simulation Setup Checklist
TBD

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
