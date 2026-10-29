temp = pathConfig.GetDir(#userStartupScripts) + "/" + UnityPluginScript_Name;
if not (doesFileExist UnityPluginScript_Source) then (
    throw ("Unity FBX source plugin was not found: " + UnityPluginScript_Source)
)
if (doesFileExist temp) do (deleteFile temp)
if not (copyFile UnityPluginScript_Source temp) then (
    throw ("Unable to install Unity FBX startup script: " + temp)
)

maxIniFile = (GetMAXIniFile())
unityCategory = "Unity"
setINISetting maxIniFile unityCategory "UnityProject" UnityProject
setINISetting maxIniFile unityCategory "UnityFbxExportSettings" UnityFbxExportSettings
setINISetting maxIniFile unityCategory "UnityFbxImportSettings" UnityFbxImportSettings

quitMax()