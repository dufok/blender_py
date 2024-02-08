import bpy
import os
import sys

# Define camera and view layer pairs
cameras = ["Camera_1"]
view_layers = ["Layout_1"]

# Base path for saving renders
base_path = "//Render_Recieb/"  # Ensure there's a trailing slash

# Set the resolution
bpy.context.scene.render.resolution_x = 3840
bpy.context.scene.render.resolution_y = 2160

# Set the resolution percentage (50% in this case)
bpy.context.scene.render.resolution_percentage = 100

#################### PNG section #######################
# Set the output format to PNG
bpy.context.scene.render.image_settings.file_format = 'PNG'

# Set the color depth to 16-bit
bpy.context.scene.render.image_settings.color_depth = '16'

# Set color mode to RGBA to include alpha channel
bpy.context.scene.render.image_settings.color_mode = 'RGB'

##################### JPEG section ########################
""" # Set the output format to PNG
bpy.context.scene.render.image_settings.file_format = 'JPEG'

# Set the quality (for JPEG format, the quality is a percentage from 0 to 100)
bpy.context.scene.render.image_settings.quality = 90 """

##################### GPU section ########################

# Set the rendering engine to Cycles and use GPU for rendering
bpy.context.scene.render.engine = 'CYCLES'
prefs = bpy.context.preferences.addons['cycles'].preferences

# Automatically set the compute device type to CUDA or OPTIX based on available devices
if prefs.get_devices('OPTIX'):
    prefs.compute_device_type = 'OPTIX'
else:
    prefs.compute_device_type = 'CUDA'

# Enable all CUDA or OPTIX devices for rendering
for device in prefs.devices:
    if device.type == prefs.compute_device_type:
        device.use = True
        print(f"Enabled device for rendering: {device.name}")

# Ensure Blender uses GPU for rendering
bpy.context.scene.cycles.device = 'GPU'
print(f"Rendering with: {bpy.context.scene.cycles.device}, Compute Device Type: {prefs.compute_device_type}")

#########################################################


# Iterate through each pair and render
for index, (camera_name, layer_name) in enumerate(zip(cameras, view_layers), start=1):
    camera = bpy.data.objects.get(camera_name)
    if camera:
        bpy.context.scene.camera = camera  # Set the camera
        
    # No direct manipulation of bpy.context.window here
    # Instead, ensure the desired view layer is the only one enabled for rendering
    for view_layer in bpy.context.scene.view_layers:
        view_layer.use = (view_layer.name == layer_name)
        
    if camera:
        # Now proceed with rendering as before
        file_path = os.path.join(base_path, f"{layer_name}_{camera_name}.jpg")
        bpy.context.scene.render.filepath = bpy.path.abspath(file_path)
        print(f"File path set to: {bpy.context.scene.render.filepath}")

        # Start rendering
        bpy.ops.render.render(write_still=True)
        print(f"Completed rendering {layer_name} with {camera_name}")

        # Reset the file path to avoid overwriting
        bpy.context.scene.render.filepath = ""
    else:
        if not camera:
            print(f"Camera {camera_name} not found.")
