import bpy

bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.samples = 64

bpy.ops.render.render()
bpy.data.images['Render Result'].save_render( filepath = '//render.png')