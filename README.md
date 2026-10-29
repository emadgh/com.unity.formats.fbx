# FbxExporters

Copyright (c) 2021 Unity Technologies. All rights reserved.

See LICENSE.md file in the project root for full license information.

Requirements
------------

* [FBX SDK C# Bindings](https://github.com/Unity-Technologies/com.autodesk.fbx) package

Packaging
---------

Get the source the first time:
```
# clone the source
git clone https://github.com/Unity-Technologies/com.unity.formats.fbx.git
cd com.unity.formats.fbx
```

Build the package.

**On Windows**
```
build.cmd
```

**On Mac/Linux**

```
./build.sh
```

The package will be built in-place in com.unity.formats.fbx.

Testing
-------

Open `TestProjects/FbxTests` in Unity 2018.2+ and run using the Test Runner.

Reporting Bugs
--------------

Please create a minimal project that reproduces the bug and use the Unity Bug Report (built in to the Unity Editor).

## Fork: Unity 6.7 and 3ds Max 2026 (experimental)

This branch adds support for Autodesk's 2025+ CUI menu registration API,
and bundles Max integration scripts in the Git-installable Unity package.
It is based on Unity FBX Exporter 5.1.6.

In **Window > Package Manager > + > Add package from git URL**, enter:

```text
https://github.com/emadgh/com.unity.formats.fbx.git?path=/com.unity.formats.fbx#compat/unity-6.7-max-2026
```

In **Edit > Project Settings > FBX Export**, choose 3ds Max 2026,
click **Install Unity Integration**, and restart Max. See
[integration setup](com.unity.formats.fbx/Documentation~/integration-setup.md).

**Status:** Not runtime-tested on Unity 6.7 and 3ds Max 2026 yet.
This provides FBX integration, **not** automatic Max instance-to-Unity
Prefab conversion.
