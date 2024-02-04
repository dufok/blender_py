import bpy
import os

# Define camera and view layer pairs
cameras = ["Camera_5", "Camera_6"]
view_layers = ["Scene_5", "Scene_6"]

# Base path for saving renders
base_path = "//Renders_2/"  # Ensure there's a trailing slash

# Set the rendering engine to Cycles and use GPU for rendering
bpy.context.scene.render.engine = 'CYCLES'
prefs = bpy.context.preferences.addons['cycles'].preferences
prefs.compute_device_type = 'METAL'

# Print all available devices
print("Available devices:")
for device in prefs.devices:
    print(f"Device: {device.name}, Type: {device.type}")

# Find the GPU device and enable it
gpu_device_name = "AMD Radeon RX Vega 56"
gpu_found = False
for device in prefs.devices:
    if gpu_device_name in device.name:
        device.use = True
        gpu_found = True
        print(f"Using GPU device: {device.name}")
    else:
        device.use = False  # Disable all other devices for rendering

if not gpu_found:
    print(f"GPU device named {gpu_device_name} not found. Falling back to CPU.")
    bpy.context.scene.cycles.device = 'CPU'
else:
    bpy.context.scene.cycles.device = 'GPU'

# Print current render settings
print('Render Device:', bpy.context.scene.cycles.device)
print('Compute Device Type:', prefs.compute_device_type)


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
