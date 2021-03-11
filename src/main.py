import logging, urllib.request as r
from bs4 import BeautifulSoup
from flask import Flask
from flask_restful import Resource, Api
from waitress import serve

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__+".py")

app = Flask(__name__)
api = Api(app)

class DolarHandler(Resource):
  def get(self):
    logger.info("han pedido el precio del dolar.")
    return {"dolar": self.dolar_request()}

  def dolar_request(self):
    try:
      data = r.urlopen("https://exchangemonitor.net/dolar-promedio-venezuela").read().decode()
      soup = BeautifulSoup(data, features="html.parser")
      tags = soup("h2")
      return f"{tags[0].get_text()}"
    except NameError:
      print(NameError)
      return "Sorry, there was an error in the request "

api.add_resource(DolarHandler, '/')

if __name__ == '__main__':
  # app.run(debug=False)
  serve(app)
