import bpy
import noise
import os
import bmesh

# Create a new scene
scene = bpy.data.scenes.new("Scene")

scene.render.resolution_x = 1920
scene.render.resolution_y = 1080

size = 10

frequency = 2
octave = 6

plane = bpy.data.objects.new("Plane", bpy.data.meshes.new('PlaneMesh'))

plane.location = (0, 0, 0)
plane.scale = (size, size, 1)

bm = bpy.bmesh.new()

bm.verts.ensure_lookup_table()

for x in range(-size, size):
    for y in range(-size, size):
        z = noise.pnoise2(x /size * frequency, y /size * frequency, octave)
        bm.verts.new((x, y, z))

mesh = bpy.data.meshes.new('Landscape')
bm.to_mesh(mesh)
bm.free()

plane.data = mesh


camera = bpy.data.objects.new('Camera', bpy.data.cameras.new('Camera'))





# Add another cude aside from the default cube




# Direct the render to the repository directory
bpy.data.scenes['Scene'].render.filepath = os.getcwd() + '/render.png'

# Render the scene
bpy.ops.render.render(write_still=True)
