// Gmsh project created on Tue Apr 30 01:06:36 2019
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 0, 0, 1};
//+
Point(2) = {5.625, 6.5, 0, 1};
//+
Point(3) = {-5.625, 6.5, 0, 1};
//+
Point(4) = {-11.25, 0, 0, 1};
//+
Point(5) = {11.25, 0, 0, 1};
//+
Line(3) = {5, 2};
//+
Line(4) = {2, 3};
//+
Line(6) = {3, 4};
//+
Line(7) = {3, 1};
//+
Line(8) = {1, 2};
//+
Line(11) = {4, 1};
//+
Line(12) = {1, 5};
