@echo off

REM 가상 환경 경로 설정
SET "VENV_PATH=%CD%\venv"

REM 가상 환경 활성화
CALL %VENV_PATH%\Scripts\activate.bat

REM 파이썬 파일 실행
python app.py

REM 가상 환경 비활성화
CALL deactivate