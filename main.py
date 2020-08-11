from flask import Flask,request,render_template,make_response,jsonify
from service import Service

app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])

@app.route('/searchmovie')
def searchmovie():
    data = request.args.to_dict()
    res ={}
    res['name'] = Service.getmovies(data['name'])
    return make_response(jsonify(res),200)



if __name__ =='__main__':
 
  app.run(host="0.0.0.0",debug=app.config['DEBUG'],port=6000)
