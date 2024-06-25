import FreeCAD as App
import Part

doc = App.newDocument("GasDistributionManifold")

# Parameters
inlet_diameter = 20  # Main inlet diameter in mm
outlet_diameter = 10  # Outlet diameter in mm
outlet_count = 6  # Number of outlets
manifold_length = 100  # Length of the manifold in mm
outlet_spacing = 20  # Spacing between outlets in mm
outlet_length = 20  # Length of each outlet

# Main cylinder (manifold body)
manifold_radius = inlet_diameter / 2
manifold_body = Part.makeCylinder(manifold_radius, manifold_length)

# Create outlets
outlet_radius = outlet_diameter / 2
angle_step = 360 / outlet_count

for i in range(outlet_count):
    angle = i * angle_step
    outlet = Part.makeCylinder(outlet_radius, outlet_length)
    outlet.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), angle)
    outlet.translate(
        App.Vector(
            manifold_radius + outlet_length,
            0,
            (i - (outlet_count - 1) / 2) * outlet_spacing,
        )
    )
    manifold_body = manifold_body.cut(outlet)

# Create inlet
inlet = Part.makeCylinder(manifold_radius, outlet_length)
inlet.translate(App.Vector(-outlet_length, 0, manifold_length / 2))
manifold_body = manifold_body.fuse(inlet)

# Finalize the manifold
Part.show(manifold_body)
doc.recompute()
