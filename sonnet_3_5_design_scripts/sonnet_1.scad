// Constants
num_outlets = 6;
manifold_diameter = 20;
manifold_length = 150;
outlet_diameter = 5;
flange_diameter = 30;
flange_thickness = 5;

// Main manifold
module manifold() {
    rotate([0, 90, 0])
        cylinder(h=manifold_length, d=manifold_diameter, center=true, $fn=50);
}

// Outlet
module outlet() {
    rotate([90, 0, 0])
        cylinder(h=manifold_diameter, d=outlet_diameter, center=false, $fn=30);
}

// Flange
module flange() {
    rotate([0, 90, 0])
        cylinder(h=flange_thickness, d=flange_diameter, center=true, $fn=50);
}

// Complete assembly
module gas_distribution_manifold() {
    difference() {
        union() {
            manifold();
            translate([manifold_length/2 + flange_thickness/2, 0, 0]) flange();
            translate([-manifold_length/2 - flange_thickness/2, 0, 0]) flange();
        }
        for (i = [0:num_outlets-1]) {
            translate([manifold_length/num_outlets * (i - (num_outlets-1)/2), 0, manifold_diameter/2])
                outlet();
        }
    }
}

// Render the manifold
gas_distribution_manifold();