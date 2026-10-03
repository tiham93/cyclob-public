# Cyclob

<!--toc:start-->
- [Get Cyclob](#get-cyclob)
- [Features](#features)
- [Planned Features](#planned-features)
- [Changelog](#changelog)
<!--toc:end-->

**Cyclob** is a QoL addon for Blender, made to solve a very common and annoying problem: walking through a large set of objects, whether for a cleanup pass or quality checking, all the while stressing over
- Trying to remember where I was.
- What's the next object I wanted to work on? What was the last one in case I want to go back?
- Am I sure I didn't miss anything?
- I see something else that needs my attention but if I step away, coming back will be a hassle.

[image: blender collection with numbered object names]

All of which are annoying, OCD triggering, add unnecessary mental load that's better used elsewhere.
So I made this tool to put this problem away for good:

[image: jumping back and forth between objects with Cyclob, highlighting objects]

## Get Cyclob
*   **Source code** for the addon (v1.0) is available here on this github repo
*   **Support the Project:** Get Cyclob for **$2** on [Gumroad](https://gumroad.com) or [Blender Market](https://blendermarket.com) to receive all future updates, fixes, and new features.

## Features

*   **Fixed-Set Registration:** Capture your current selection into a dedicated list. Cyclob keeps track of where you are in your sequence, allowing you to jump back to your progress at any time.
    -   Does not use Blender collection, to not clutter the Outliner. 
    -   As a result, even if you reorganize your scene, move objects between collections, as long as the objects themselves exist, you can effortlessly jump right back.

[image: Cyclob object list]

-   **Prep Work Automation:** Options to eliminate the repetitive operations that need to be done while inspecting individual object:

    *   **Auto-Focus:** Automatically centers the 3D Viewport on selected object so you don't need to constantly zoom out, look around or `View Selected` to find your objects after switching.
    
    [image: auto focus demonstration]
    
    *   **Isolation Modes:**
        *   **Isolate View Mode:** Automatically enter Local View for each object as you cycle through. This keeps me from breaking the Local View button on my keyboard as I work through dense scenes with objects stacked on top of each other.
        *   **Isolate Select Mode:** Instead of entering local view and hiding others, this turns off selection for all other objects in the scene, preventing accidental clicks on background elements while you work.

    [image: side by side isolation view/select modes demonstration]

    *   **Automatic Mode Switching:** Set your preferred working mode (Object, Edit, Sculpt, Vertex Paint, etc.) to enter that mode immediately upon switching to a new object.

    *   **Working with Instances:** Enable "All Instances" to automatically select every object sharing the same mesh data, used for updating modular pieces across your entire scene simultaneously.

*   **Hotkey-Friendly Workflow:** Access all controls from the plugin's panel in the 3D viewport, or map any operation to a hotkey. All functions are also fully accessible via Blender’s search bar (F3) for quick access without cluttering the UI.

## Planned Features
*   Execute custom scripts after switching for more advanced workflows.
*   History tracking for previously registered object sets.
*   Naming registered object sets
*   Add / Remove / Reorder objects in a set. 
*   Saveable register presets for persistent project management.

## Changelog
- v1.0. Add local view option on switching. Publish repo on Github. 
- v0.9. Add isolate view option on switching. 
- v0.8. Add option to switch mode upon switching.
