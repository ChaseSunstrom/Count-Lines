@echo off
setlocal enabledelayedexpansion

REM Set the path to the current directory where the batch script is located
set "script_dir=%~dp0"

REM Set the name of the Python script
set "script_name=count_lines.py"

REM Combine the directory and script name to get the full path
set "full_path=!script_dir!!script_name!"

REM Add the script directory to the PATH
set "current_path=%PATH%"
set "new_path=!script_dir!;%current_path%"
setx PATH "!new_path!"

REM Check if the PATH variable has been updated
if not errorlevel 1 (
    echo "Script directory added to PATH successfully."

    REM Set an environment variable named CLC with the full path
    setx CLC "python \"!full_path!\""

    echo "Environment variable CLC set."

    REM Run the Python script using the full path variable
    call "!full_path!"

    echo "Script executed."
) else (
    echo "Failed to update PATH variable."
)

endlocal
