from flask import Flask,request,render_template



user_socket_list = []
app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])

@app.route('/searchmovie')
def searchmovie():
  
  return 'Hello World'



if __name__ =='__main__':
 
  app.run(host="0.0.0.0",debug=app.config['DEBUG'],port=81)
