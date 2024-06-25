import math
import FreeCAD as App
import Part

# Constants
num_outlets = 6
total_flow_rate = 10  # standard liters per minute
outlet_velocity = 1  # m/s

# Calculate outlet diameter
outlet_flow_rate = total_flow_rate / num_outlets  # L/min
outlet_flow_rate_m3s = outlet_flow_rate / (60 * 1000)  # m³/s
outlet_area = outlet_flow_rate_m3s / outlet_velocity  # m²
outlet_diameter = 2 * math.sqrt(outlet_area / math.pi)  # m
outlet_diameter_mm = outlet_diameter * 1000  # mm

# Main manifold parameters
manifold_length = 300  # mm
manifold_diameter = 20  # mm

# Create the main manifold cylinder
manifold = Part.makeCylinder(manifold_diameter / 2, manifold_length)

# Create and position the outlets
for i in range(num_outlets):
    outlet_position = i * (manifold_length / (num_outlets - 1))
    # Create a hole through the manifold
    hole = Part.makeCylinder(
        outlet_diameter_mm / 2,
        manifold_diameter,
        App.Vector(0, -manifold_diameter / 2, outlet_position),
        App.Vector(0, 1, 0),
    )
    manifold = manifold.cut(hole)
    # Create the actual outlet cylinder
    outlet = Part.makeCylinder(
        outlet_diameter_mm / 2,
        manifold_diameter / 2 + 30,
        App.Vector(0, 0, outlet_position),
        App.Vector(0, 1, 0),
    )
    manifold = manifold.fuse(outlet)

# Create the inlet
inlet_diameter = 15  # mm
inlet_length = 50  # mm
inlet_position = App.Vector(0, 0, -inlet_length / 2)
inlet = Part.makeCylinder(
    inlet_diameter / 2, inlet_length, inlet_position, App.Vector(0, 0, 1)
)

# Cut a hole for the inlet
inlet_hole = Part.makeCylinder(
    inlet_diameter / 2,
    manifold_diameter,
    App.Vector(0, -manifold_diameter / 2, 0),
    App.Vector(0, 1, 0),
)
manifold = manifold.cut(inlet_hole)

# Fuse the inlet to the manifold
manifold = manifold.fuse(inlet)

# Create a new document and add the shape
doc = App.newDocument("GasManifold")
obj = doc.addObject("Part::Feature", "GasManifold")
obj.Shape = manifold

# Set the view
App.Gui.ActiveDocument.ActiveView.setAxisCross(True)
App.Gui.SendMsgToActiveView("ViewFit")
App.Gui.activeDocument().activeView().viewAxonometric()

# Save the document
doc.recompute()
