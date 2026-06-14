bl_info = {
    "name": "Paint Palette Popup",
    "author": "Liam",
    "version": (0, 5, 0),
    "blender": (5, 1, 0),
    "location": "Texture/Vertex Paint > C (palette), V (brushes)",
    "description": "Quick palette popup and brush asset shelf popover for paint modes",
    "category": "Paint",
}

import bpy


# ── Helpers ────────────────────────────────────────────────────────────────────

def get_paint(context):
    ts = context.tool_settings
    mode = context.mode
    if mode == 'PAINT_TEXTURE':
        return ts.image_paint
    if mode == 'PAINT_VERTEX':
        return ts.vertex_paint
    return None


# ── Palette Popup ──────────────────────────────────────────────────────────────

class PAINT_OT_palette_popup(bpy.types.Operator):
    """Show the active paint palette in a floating popup"""
    bl_idname = "paint.palette_popup"
    bl_label = "Palette Popup"
    bl_options = {'REGISTER'}

    def invoke(self, context, event):
        if get_paint(context) is None:
            self.report({'WARNING'}, "Not in a supported paint mode")
            return {'CANCELLED'}
        return context.window_manager.invoke_popup(self, width=240)

    def execute(self, context):
        return {'FINISHED'}

    def draw(self, context):
        layout = self.layout
        paint = get_paint(context)

        if paint is None:
            layout.label(text="Not in a paint mode.", icon='ERROR')
            return

        layout.template_ID(paint, "palette", new="palette.new")

        if paint.palette:
            layout.template_palette(paint, "palette", color=True)
            row = layout.row(align=True)
            row.operator("palette.color_add", icon='ADD', text="Add")
            row.operator("palette.color_delete", icon='REMOVE', text="Remove")
        else:
            layout.label(text="No palette assigned — create one above.", icon='INFO')


# ── Keymaps ────────────────────────────────────────────────────────────────────
#
# C → palette popup (both paint modes)
# V → brush asset shelf popover (mode-specific shelf so all brushes are shown
#      with thumbnails; Blender's own C code handles brush activation)

_KEYMAP_DEFS = [
    ("Vertex Paint", 'EMPTY', 'C', 'PRESS', "paint.palette_popup",          {}),
    ("Image Paint",  'EMPTY', 'C', 'PRESS', "paint.palette_popup",          {}),
    ("Vertex Paint", 'EMPTY', 'V', 'PRESS', "wm.call_asset_shelf_popover",  {"name": "VIEW3D_AST_brush_vertex_paint"}),
    ("Image Paint",  'EMPTY', 'V', 'PRESS', "wm.call_asset_shelf_popover",  {"name": "VIEW3D_AST_brush_texture_paint"}),
]

_addon_keymaps = []


def _register_keymaps():
    kc = bpy.context.window_manager.keyconfigs.addon
    if not kc:
        return
    for km_name, space_type, key, value, idname, props in _KEYMAP_DEFS:
        km = kc.keymaps.new(name=km_name, space_type=space_type)
        kmi = km.keymap_items.new(idname, type=key, value=value)
        for prop_name, prop_val in props.items():
            setattr(kmi.properties, prop_name, prop_val)
        _addon_keymaps.append((km, kmi))


def _unregister_keymaps():
    for km, kmi in _addon_keymaps:
        km.keymap_items.remove(kmi)
    _addon_keymaps.clear()


# ── Register ───────────────────────────────────────────────────────────────────

_classes = (
    PAINT_OT_palette_popup,
)


def register():
    for cls in _classes:
        bpy.utils.register_class(cls)
    _register_keymaps()
    print("[paint_palette_popup] v0.5 registered — C: palette popup, V: brush shelf.")


def unregister():
    _unregister_keymaps()
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)
    print("[paint_palette_popup] Unregistered.")


if __name__ == "__main__":
    register()
