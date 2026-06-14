# Blender Paint Popup

A Blender addon that adds quick-access keybindings for the colour palette and brush selector in Vertex Paint and Texture Paint modes.

By default, both are buried in sub-menus or sidebars. This addon surfaces them instantly with a single keypress.

## Requirements

Blender 5.1 or later

## Installation

1. Download `paint_palette_popup.py`
2. In Blender, go to **Edit > Preferences > Add-ons**
3. Click the dropdown arrow in the top-right corner of the Add-ons panel and choose **Install from Disk...**
4. Navigate to the downloaded file, select it, and click **Install from Disk**
5. Enable the addon by ticking the checkbox next to **Paint Palette Popup**

Blender copies the file into your user scripts folder automatically — no manual file placement needed.

## Usage

These keybindings are active in both **Vertex Paint** and **Texture Paint** modes:

| Key | Action |
|-----|--------|
| `C` | Open the active colour palette in a floating popup |
| `V` | Open the brush asset shelf as a popover |

### Palette popup (`C`)

Shows the active palette with its full colour grid. You can create a new palette, add and remove colours, and click any swatch to make it the active colour — all without leaving the viewport.

### Brush shelf popover (`V`)

Opens Blender's native brush asset shelf as a floating popover. Click any brush thumbnail to activate it. The shelf uses Blender's built-in asset system, so all installed brushes appear automatically.

## Keybinding conflicts

`C` and `V` are free in Blender's default Vertex Paint and Texture Paint keymaps. If you have a custom keymap that uses either key, you can change the bindings under **Edit > Preferences > Keymap**, or edit `_KEYMAP_DEFS` at the bottom of `paint_palette_popup.py`.
