@echo off
echo Activating virtual environment...
call venv\Scripts\activate

:command_loop
set /p command="(venv) > "
if /i "%command%"=="exit" goto end
%command%
goto command_loop

:end
echo Deactivating virtual environment...
call deactivate
echo Done.