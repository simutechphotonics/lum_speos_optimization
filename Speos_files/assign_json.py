# Python Script, API Version = V251


ListSOPIndex = 0
SopPluginConfigurationPath = r".\SPEOS input files\p474_dc20_d400_sa45_wl624.json"
material = SpeosSim.Material(Selection.Create(GetRootPart().GetChildren[ICustomObject]()[12]).Items[0])
SurfaceLayer = material.ListSOP[ListSOPIndex]
SurfaceLayer.SopPluginConfigurationPath = SopPluginConfigurationPath
