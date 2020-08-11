from flask import Flask,request,render_template,make_response,jsonify

class Service:
  @classmethod
  def getmovies(self,name):
    return name