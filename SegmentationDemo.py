import sys

# CONFIG
# This is the Path to the folder holding the 'WoundSegLib' folder
PATH_TO_LIB = ""
# This is the Path to the PLY file you wish to test
PATH_TO_PLY_FILE = "C:\\Users\\Rima\\Desktop\\bumpy 1.ply"
# paths may require \\ to discern between folder levels under Windows operating systems
# IE: C:\\Users\username\\Desktop\\file.ply
sys.path.append(PATH_TO_LIB)
import WoundSegLib
from WoundSegLib.MeshContainerClass import MeshContainer

# Don't comment out this block
# Importing a file from a path
print("Showing raw imported file")
directImport: MeshContainer = MeshContainer(PATH_TO_PLY_FILE)
# Visualizing it (pauses execution till window is closed)
directImport.VisualizeMesh()

# Comment out various blocks to test them

'''
# Remove Black Points
print("removing black points")
blackPointsRemoved: MeshContainer  # You may see this syntax used to declare variable type hints. This is powerful in
# IDEs such as PyCharm for type hints
blackPointsRemoved, _ = directImport.RemoveCompletelyBlackPoints() # several segmentation functions return arrays, of an
# accepted mesh and a rejected mesh. While useful in many cases, here we use an underscore to toss out the reject
blackPointsRemoved.VisualizeMesh()  # check result
'''

'''
# Cropping box Example
print("demoing manual box cropping")
# Any time you are asked to pick points, a visualizer window pops up, with the additional ability to pick points
# while holding shift. Beware the dragging while holding shift can cause a crash
croppedByBoundingBox: MeshContainer = directImport.CropByBoundingBox()
croppedByBoundingBox.VisualizeMesh()  # check result
'''

'''
# Manual Color band segmentation
print("demoing color band segmentation, both the pass and reject")
colorBandPassed: MeshContainer
colorBandRejected: MeshContainer
colorBandPassed, colorBandRejected = directImport.DivideByColorBandFilter(0.1, 0.5, True, "red")
colorBandPassed.VisualizeMesh()
colorBandRejected.VisualizeMesh()
'''

'''
# Color Ratio example with Saving
# FILL OUT SAVE PARAMS BEFORE RUNNING
print("demoing color Ratios")
colorRatiod: MeshContainer
colorRatiod = directImport.GenerateNewMeshWithColorRatio("blue", "saturation")
# Divide by 0 or invalids are normal and are managed in code with an override value. See docs for more info.
# This error will not cause the program to stop
colorRatiod.VisualizeMesh()
saveFolder: str = ""  # Make sure you have permission to write here! Full file path
saveName: str = "testFile"
colorRatiod.Save(saveFolder, saveName)
'''

'''
# As an example, lets chain together cropping and then removing black points, then islands
print("demoing chaining of multiple steps")
chain1: MeshContainer
chain2: MeshContainer
chain3: MeshContainer
chain1 = directImport.CropByBoundingBox()
chain2, _ = chain1.RemoveCompletelyBlackPoints()
chain3 = chain2.RemoveIslands()
chain3.VisualizeMesh()
'''

'''
# Lets create some picked points, save them within the mesh, then call them up later for the boxcrop function
print("demoing use of manually defined Picked Points")
croppedMeshWithPickedPoints: MeshContainer
directImport.GetPickedPoints("nameOfPickedPointSetHere", 4)  # acquire picked points from the user. They will
# be stored within this specific mesh container by the name defined.
croppedMeshWithPickedPoints = directImport.CropByBoundingBox(boundingBoxInitialPPSName="nameOfPickedPointSetHere")
croppedMeshWithPickedPoints.VisualizeMesh()
'''

'''
# Launches a wizard which lets you run through various segmentations through a CLI
directImport.Wizard()
# At the end of each wizard, steps are exported. You can copy paste them to redo the exact same steps for the same mesh
# This is an example that is loaded via WizardLoad to repeat the experiment
exampleDictionary: list = [{'Command': 'RemoveCompletelyBlackPoints'},{'Command': 'RemoveIslands'}]
wizardTest: MeshContainer = directImport.WizardLoad(exampleDictionary)
wizardTest.VisualizeMesh()
'''
