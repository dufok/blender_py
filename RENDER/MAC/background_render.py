import bpy
import os

# Define camera and view layer pairs
cameras = ["Camera_1", "Camera_2", "Camera_3", "Camera_4", "Camera_5"]
view_layers = ["Layout_1", "Layout_2", "Layout_3", "Layout_4", "Layout_5"]

# Base path for saving renders
base_path = "//Render_Loung_FULL2/"  # Ensure there's a trailing slash

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
#FOR WINDOWS CUDA
prefs.compute_device_type = 'METAL'

class SimpleOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Simple Object Operator"

    def execute(self, context):
        prefs = context.preferences.addons['cycles'].preferences
        print("Available devices:")
        for device in prefs.devices:
            print(f"Device: {device.name}, Type: {device.type}")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SimpleOperator)

def unregister():
    bpy.utils.unregister_class(SimpleOperator)

if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.simple_operator()

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

############### IF ALL GPU ############################

""" # Set the rendering engine to Cycles and use GPU for rendering
bpy.context.scene.render.engine = 'CYCLES'
prefs = bpy.context.preferences.addons['cycles'].preferences
#FOR WINDOWS CUDA
prefs.compute_device_type = 'METAL'

# Enable all GPU devices for rendering
for device in prefs.devices:
    device.use = True
    print(f"Using GPU device: {device.name}")

bpy.context.scene.cycles.device = 'GPU'

# Print current render settings
print('Render Device:', bpy.context.scene.cycles.device)
print('Compute Device Type:', prefs.compute_device_type)
 """
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
