import api
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def read_root():
  return {"Hello": "World"}


@app.get("/contact", response_class=HTMLResponse)
def read_root():
  return """
    <h1>Contact us:</h1>
    <p>Email: test@gmail.com</p>
  """


def run():
  api.get_categories()


if __name__ == '__main__':
  run()
