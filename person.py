import bpy

# Create a new scene
scene = bpy.data.scenes.new("Scene")

# # Set the scene's properties
# scene.render.resolution_x = 1920
# scene.render.resolution_y = 1080

# # Add a cube to the scene
# cube = bpy.data.objects.new("Cube", bpy.data.meshes.new("CubeMesh"))
# scene.objects.link(cube)

# # Set the cube's properties
# cube.location = (0, 0, 0)
# cube.scale = (1, 1, 1)

# # Add a sphere to the scene
# sphere = bpy.data.objects.new("Sphere", bpy.data.meshes.new("SphereMesh"))
# # scene.objects.link(sphere)

# # Set the sphere's properties
# sphere.location = (0, 0, 1)
# sphere.scale = (1, 1, 1)

# # Add a cylinder to the scene
# cylinder = bpy.data.objects.new("Cylinder", bpy.data.meshes.new("CylinderMesh"))
# scene.objects.link(cylinder)

# # Set the cylinder's properties
# cylinder.location = (0, 0, 2)
# cylinder.scale = (1, 1, 1)

# # Add a camera to the scene
# camera = bpy.data.objects.new("Camera", bpy.data.cameras.new("Camera"))
# # scene.objects.link(camera)

# # Set the camera's properties
# # camera.location = (0, 0, 10)
# # camera.rotation_euler = (0, 0, 0)

# # # Set the scene's active camera
# # scene.camera = camera

# # Render the scene
bpy.ops.render.render(write_still=True)