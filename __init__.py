bl_info = {
    "name": "Cyclob - LP Object Cycler - testing",
    "author": "Long Phan",
    "version": (0, 1, 0),
    "blender": (3, 6, 0),
    "location": "LP Tools > Cyclob",
    "description": "Cycle through and focus on each object in selection",
    "category": "Object",
}

import bpy

class LP_PT_Cyclob(bpy.types.Panel):
	bl_label = 'Cyclob'
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_category = 'LP Tools'

	def draw(self, context):
		layout = self.layout
		cyclob = context.scene.cyclob_props
		layout.operator(LP_OT_CyclobRegister.bl_idname, text='Register Selection')
		layout.label(text='Registered %s objects' % len(cyclob.collection))
		layout.template_list('UI_UL_list', ' ', cyclob, 'collection', cyclob, 'active', sort_reverse=0)
		row = layout.row()
		row.operator(LP_OT_CyclobNext.bl_idname, text='Next')
		row.operator(LP_OT_CyclobPrev.bl_idname, text='Prev')

		layout.separator()
		layout.label(text='Enter mode on switching:')
		layout.prop(cyclob, 'obmode', text='')
		layout.prop(cyclob, 'isolate', text='Isolate', toggle=1)
		layout.prop(cyclob, 'all_instances', text='All Instances', toggle=1)
		layout.prop(cyclob, 'isolate_select', text='Isolate Select', toggle=1)

class LP_OT_CyclobRegister(bpy.types.Operator):
	bl_label = 'Register Cyclob Selection'
	bl_idname = 'object.cyclob_register'
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		cyclob = context.scene.cyclob_props
		ccol = cyclob.collection
		ccol.clear()
		for o in context.selected_objects:
			item = ccol.add()
			item.name = o.name
			item.ob = o
		cyclob['active'] = 0
		return {'FINISHED'}

class LP_OT_CyclobNext(bpy.types.Operator):
	bl_label = 'Cyclob Next'
	bl_idname = 'object.cyclob_next'
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		context.scene.cyclob_props.active += 1
		return {'FINISHED'}

class LP_OT_CyclobPrev(bpy.types.Operator):
	bl_label = 'Cyclob Prev'
	bl_idname = 'object.cyclob_prev'
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		context.scene.cyclob_props.active -= 1
		return {'FINISHED'}

def cyclob_callback(self, context):
	cyclob = context.scene.cyclob_props
	ccol = cyclob.collection
	index = cyclob.active
	if index < 0:
		cyclob['active'] = -1
		return
	if index >= len(ccol):
		cyclob['active'] = len(ccol)
		return
	ob = ccol[index].ob

	if context.space_data.local_view:
		bpy.ops.view3d.localview()

	try:
		bpy.ops.object.mode_set(mode='OBJECT')
	except RuntimeError:
		print('No active object')
	bpy.ops.object.select_all(action='DESELECT')
	context.view_layer.objects.active = ob
	ob.select_set(1)

	for region in context.area.regions:
		if region.type == 'WINDOW':
			break
	else:
		print('view3d window region not found')
		return
	with context.temp_override(region=region):
		bpy.ops.view3d.view_selected(use_all_regions=True)	
		if cyclob.isolate and (not context.space_data.local_view):
			bpy.ops.view3d.localview()

	if cyclob.all_instances:
		bpy.ops.object.select_linked(type='OBDATA')
		
	try:
		bpy.ops.object.mode_set(mode=cyclob.obmode)
	except:
		bpy.ops.object.mode_set(mode='OBJECT')

def isolate_select_callback(self, context):
	oblist = context.selected_objects
	if context.scene.cyclob_props.isolate_select:
		for o in bpy.data.objects:
			if o not in oblist:
				o.hide_select = True
	else:
		for o in bpy.data.objects:
			if o not in oblist:
				o.hide_select = False

class CyclobItem(bpy.types.PropertyGroup):
	ob: bpy.props.PointerProperty(type=bpy.types.Object)

class CyclobProps(bpy.types.PropertyGroup):
	collection: bpy.props.CollectionProperty(type=CyclobItem)
	active: bpy.props.IntProperty(default=0, update=cyclob_callback)
	isolate: bpy.props.BoolProperty(default=False)
	all_instances: bpy.props.BoolProperty(default=False)
	isolate_select: bpy.props.BoolProperty(default=False, update=isolate_select_callback)
	obmode: bpy.props.EnumProperty(items=[
		('OBJECT', 'Object', ''),
		('EDIT', 'Edit', ''),
		('POSE', 'Pose', ''),
		('SCULPT', 'Sculpt', ''),
		('VERTEX_PAINT', 'Vertex Paint', ''),
		('WEIGHT_PAINT', 'Weight Paint', ''),
		('TEXTURE_PAINT', 'Texture Paint', '')]
	)


classes = [
	LP_OT_CyclobRegister,
	LP_OT_CyclobNext,
	LP_OT_CyclobPrev,
	LP_PT_Cyclob,
	CyclobItem,
	CyclobProps,
]

def register():
	for cls in classes:
		bpy.utils.register_class(cls)
	bpy.types.Scene.cyclob_props = bpy.props.PointerProperty(type=CyclobProps)

def unregister():
	for cls in classes:
		bpy.utils.unregister_class(cls)
	del bpy.types.Scene.cyclob_props

if __name__ == '__main__':
	register()
