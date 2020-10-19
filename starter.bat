@ECHO OFF
:: This batch file activates the venv for the Python project and sets the ENV vars
:: !!! YOU NEED TO HAVE set_env_vars.bat BATCH FILE WITCH SETS THE ENV VARS FOR THE CLI TOOL !!!
start cmd /k ".\venv\Scripts\Activate & set_env_vars.bat"
