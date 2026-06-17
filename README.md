# Cyclob

**Cyclob** is a simple QoL tool for Blender, made to solve a simple but common
and annoying problem that plagues me everyday: walking through a large
set of objects one by one, whether for a cleanup pass, quality checking or
refining a collection of assets/pieces. Having to remember where you're at,
what's the last/next object you want to work on, forgetting where you were
after breaking away to do something else, all of which are annoying and add
unnecessary mental load that is better used elsewhere.

## Key Features

*   **Fixed-Set Registration:** Quickly capture your current selection into a
dedicated list. Cyclob keeps track of exactly where you are in your sequence,
allowing you to jump back to your progress at any time.
    -   The list is managed without using Blender collections. As a result, it
    doesn't clutter your Outliner. No matter how you organize your scene or
    move objects between collections, as long as the objects exist, you can
    always go back to the current, next, or previous item in your working set.
*   **Auto-Focus:** Every time you cycle to the next object, automatically
centers the 3D Viewport on it, ensuring you are always looking exactly at what
you need to work on.
*   **Isolation Modes (Toggleable):**
    *   **Isolate View Mode:** Automatically enter Local View for each object
    as you cycle through. I find myself pressing the Local View button way too
    often as I work through dense scenes.
    *   **Isolate Select Mode:** Locks the selection of all other objects in
    the scene, preventing accidental clicks on background elements while you
    work.
*   **Automatic Mode Switching:** Set your preferred working mode (Object,
Edit, Sculpt, Vertex Paint, etc.) to switch to that mode immediately upon
switching to a new object.
*   **Instance Awareness:** Enable "All Instances" to automatically select
every object sharing the same mesh data, perfect for updating modular pieces
across your entire scene simultaneously.
*   **Hotkey-Friendly Workflow:** Access all controls from the plugin's panel
in the 3D viewport, or map any operation to a hotkey. All functions are also
fully accessible via Blender’s search bar (F3) for quick access without
cluttering the UI.

## Planned Features
*   Execute custom scripts after switching for more advanced and flexible
workflows.
*   History tracking for previously registered object sets.
*   Reorder objects in a set. 
*   Saveable register presets for persistent project management.

## Get Cyclob
*   **Download for Free:** Get the latest version on
[GitHub](https://github.com/longphan8/cyclob).
*   **Support the Project:** Get Cyclob for just **$1** on
[Gumroad](https://gumroad.com) or [Blender Market](https://blendermarket.com)
to receive all future updates, fixes, and new features directly in your inbox.
