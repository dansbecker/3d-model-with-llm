import FreeCAD
import FreeCADGui
import Part
import sys
from PySide import QtGui


def render_to_image(script, output_image_path):
    # Initialize QApplication
    app = QtGui.QApplication([])

    # Show the main FreeCAD window
    FreeCADGui.showMainWindow()

    # Create a new document
    doc = FreeCAD.newDocument("Unnamed")

    # Execute the provided script
    exec(script, {"App": FreeCAD, "Gui": FreeCADGui, "Part": Part})

    # Ensure the 3D view is updated
    FreeCADGui.activeDocument().activeView().viewAxometric()
    FreeCADGui.activeDocument().activeView().fitAll()

    # Export the view to an image file
    FreeCADGui.activeDocument().activeView().saveImage(
        output_image_path, 1024, 768, "White"
    )

    # Close the document
    FreeCAD.closeDocument(doc.Name)

    # Exit the application
    QtGui.QApplication.instance().quit()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python render_freecad.py <input_script_path> <output_image_path>")
        sys.exit(1)

    input_script_path = sys.argv[1]
    output_image_path = sys.argv[2]

    # Read the FreeCAD script from the input file
    with open(input_script_path, "r") as file:
        script = file.read()

    render_to_image(script, output_image_path)
