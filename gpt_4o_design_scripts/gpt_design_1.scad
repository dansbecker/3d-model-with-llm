// Parameters
outlet_diameter = 5.95; // in mm
manifold_length = 100; // in mm
manifold_width = 20; // in mm
manifold_height = 20; // in mm
outlet_spacing = manifold_length / 7; // evenly spaced
outlet_length = 10; // in mm
channel_diameter = outlet_diameter; // internal channels diameter
fillet_radius = 2; // radius for fillets

// Function to create fillets (simple approximation using cylinders)
module fillet(radius) {
    translate([radius, radius, 0])
        cylinder(r = radius, h = manifold_height, center = true);
}

// Main manifold body
difference() {
    cube([manifold_length, manifold_width, manifold_height]);

    // Create holes for outlets
    for (i = [1:6]) {
        translate([i * outlet_spacing, manifold_width / 2, 0]) {
            cylinder(h = manifold_height, d = outlet_diameter, center = true);
        }
    }

    // Create internal channels
    translate([0, manifold_width / 2, manifold_height / 2]) {
        cylinder(h = manifold_length, d = channel_diameter, center = true);
    }

    for (i = [1:6]) {
        translate([i * outlet_spacing, manifold_width / 2, 0]) {
            rotate([90, 0, 0]) {
                cylinder(h = manifold_width, d = channel_diameter, center = true);
            }
        }
    }

    // Add fillets at junctions
    for (i = [1:6]) {
        translate([i * outlet_spacing, manifold_width / 2, manifold_height / 2]) {
            fillet(fillet_radius);
        }
    }
}

// Outlets
for (i = [1:6]) {
    translate([i * outlet_spacing, manifold_width / 2, -outlet_length / 2]) {
        cylinder(h = outlet_length + manifold_height, d = outlet_diameter, center = true);
    }
}
