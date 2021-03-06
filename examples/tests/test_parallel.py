import paraBEM
from paraBEM import pan3d
from paraBEM.mesh import mesh_object


mesh = mesh_object.from_OBJ("../mesh/box_minimal.obj")
case = pan3d.DirichletDoublet0Case3(mesh.panels)
case.v_inf = paraBEM.Vector3(1, 0, 0)

a = case.panels[0]
b = case.panels[1]

print(a.center, " ", a.n)
print(b.center, " ", b.n)
print(pan3d.doublet_3_0_vsaero(a.center, b))
