# lum_speos_optimization
Ansys Lumerical + Ansys Speos + Ansys Optislang Workflow


To do 
 - Create makefile that recreates the 1D diffraction grating file. Don't want to upload fsp here
 - upload lsf files
 - dont include speos and optislang items here. Upload to video repo

Passing strings as a reponse in optislang
- By default, optislang doesn't allow strings to be passed as a response
- The workaround is to set the variable first as a valid format, e.g. int, and add it as a response
- next, update the script to change the variable to a string type
- Then in optislang, you can click update variables, and as long as the reponse variable is not removed and readded, it can just be updated
- not clear if this will cause issues.