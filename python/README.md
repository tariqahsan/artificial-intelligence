# check the python and pip versions
python --version
pip --version

# to install all the necessary python libraries
pip install fastapi uvicorn openai

# to check e.g. if fastapi is installed:
PS C:\Users\tariq> pip show fastapi
Name: fastapi
Version: 0.115.12
Summary: FastAPI framework, high performance, easy to learn, fast to code, ready for production
Home-page: https://github.com/fastapi/fastapi
Author:
Author-email: =?utf-8?q?Sebasti=C3=A1n_Ram=C3=ADrez?= <tiangolo@gmail.com>
License:
Location: C:\Users\tariq\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages
Requires: pydantic, starlette, typing-extensions
Required-by:

# to check e.g. if uvicorn is installed:
PS C:\Users\tariq> pip show uvicorn
Name: uvicorn
Version: 0.34.0
Summary: The lightning-fast ASGI server.
Home-page: https://www.uvicorn.org/
Author:
Author-email: Tom Christie <tom@tomchristie.com>, Marcelo Trylesinski <marcelotryle@gmail.com>
License: BSD-3-Clause
Location: C:\Users\tariq\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages
Requires: click, h11
Required-by:

# To run and start the python script for rest api for open ai
C:\Dev\Python>python -m uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['C:\\Dev\\MMA-Training\\Python']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [27488] using StatReload
INFO:     Started server process [11432]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
