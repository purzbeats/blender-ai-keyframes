import bpy

input = '5:(0.0),10:(0.0),20:(0.4),80:(0.5),'

def convert(kf_str):
    kf_in = kf_str.split(',')
    kf_out = []
    for item in kf_in:
        if item != '':
            frame_val = item.split(':')
            frame = int(frame_val[0])
            value = float(frame_val[1][1:-1])
            kf_out.append([frame, value])
    return kf_out
    

def main(context):
    print('_____start_____')
    KEYFRAME_POINTS_ARRAY = []
    fcurves = bpy.context.active_object.animation_data.action.fcurves
    
    kf_data = convert(input)
    for curve in fcurves:
        kfp = curve.keyframe_points
        for i in kf_data:
            kfp.insert(i[0], i[1])
        print('\n')
    return 'woohoo'


class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Simple Object Operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(SimpleOperator.bl_idname, text=SimpleOperator.bl_label)


# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access).
def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.simple_operator()
