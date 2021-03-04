import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from Packages.email.email import oServe_email

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


@app.get("/")
async def send_email():
    try:
        email = await oServe_email.sendEmail()
        return email
    except BaseException as error:
        return f"""{error}"""

uvicorn.run(app, host='0.0.0.0', port=5001)
