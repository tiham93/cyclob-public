# Cyclob

**Cyclob** is a simple QoL tool for Blender, made to solve a simple but common and annoying problem that plagues me everyday: walking through a large set of objects one by one, whether for a cleanup pass, quality checking or refining a collection of assets/pieces. Having to remember where you're at, what's the last/next object you want to work on, forgetting where you were after breaking away to do something else, all of which are annoying and add unnecessary mental load that is better used elsewhere.

## Get Cyclob
*   **Source code** for the addon (v1.0) is available here on this github repo
*   **Support the Project:** Get Cyclob for **$2** on [Gumroad](https://gumroad.com) or [Blender Market](https://blendermarket.com) to receive all future updates, fixes, and new features.

## Features

*   **Fixed-Set Registration:** Capture your current selection into a dedicated list. Cyclob keeps track of where you are in your sequence, allowing you to jump back to your progress at any time.
    -   This does not use Blender collection, in order to not clutter your Outliner. Even if you change how your scene is organized, move objects between collections, as long as the objects exist, you can always go back to the current, next, or previous item in your working set.

*   **Auto-Focus:** Centers the 3D Viewport on selected object so you don't need to constantly zoom out, look around or `View Selected` to find your objects.

*   **Isolation Modes (Toggleable):**
    *   **Isolate View Mode:** Automatically enter Local View for each object as you cycle through. This keeps me from breaking the Local View button on my keyboard as I work through dense scenes with objects obscuring each other.
    *   **Isolate Select Mode:** Instead of entering local view and hiding others, this turns off selection for all other objects in the scene, preventing accidental clicks on background elements while you work.

*   **Automatic Mode Switching:** Set your preferred working mode (Object, Edit, Sculpt, Vertex Paint, etc.) to enter that mode immediately upon switching to a new object.

*   **Working with Instances:** Enable "All Instances" to automatically select every object sharing the same mesh data, used for updating modular pieces across your entire scene simultaneously.

*   **Hotkey-Friendly Workflow:** Access all controls from the plugin's panel in the 3D viewport, or map any operation to a hotkey. All functions are also fully accessible via Blender’s search bar (F3) for quick access without cluttering the UI.

## Planned Features
*   Execute custom scripts after switching for more advanced workflows.
*   History tracking for previously registered object sets.
*   Naming registered object sets
*   Reorder objects in a set. 
*   Saveable register presets for persistent project management.

