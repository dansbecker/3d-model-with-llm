import FreeCAD as App
import Part

doc = App.newDocument("GasDistributionManifold")

# Parameters
inlet_diameter = 20  # Main inlet diameter in mm
outlet_diameter = 10  # Outlet diameter in mm
outlet_count = 6  # Number of outlets
manifold_length = 100  # Length of the manifold in mm
outlet_spacing = 20  # Spacing between outlets in mm

# Main cylinder (manifold body)
manifold_radius = inlet_diameter / 2
manifold_body = Part.makeCylinder(manifold_radius, manifold_length)

# Create outlets
outlet_radius = outlet_diameter / 2
outlet_positions = [
    (
        manifold_radius + outlet_spacing,
        0,
        manifold_length / 2 + (i - outlet_count / 2) * outlet_spacing,
    )
    for i in range(outlet_count)
]

for pos in outlet_positions:
    outlet = Part.makeCylinder(outlet_radius, outlet_spacing)
    outlet.translate(App.Vector(*pos))
    manifold_body = manifold_body.cut(outlet)

# Create inlet
inlet = Part.makeCylinder(manifold_radius, outlet_spacing)
inlet.translate(App.Vector(manifold_radius + outlet_spacing, 0, manifold_length))
manifold_body = manifold_body.fuse(inlet)

# Finalize the manifold
Part.show(manifold_body)
doc.recompute()
