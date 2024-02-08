import bpy

# Print the available CUDA devices
print("CUDA Devices:")
for device in bpy.context.preferences.addons['cycles'].preferences.get_devices_for_type('CUDA'):
    print(f"  - {device.name}")

# Print the available OptiX devices
print("\nOptiX Devices:")
for device in bpy.context.preferences.addons['cycles'].preferences.get_devices_for_type('OPTIX'):
    print(f"  - {device.name}")
