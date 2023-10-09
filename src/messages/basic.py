from uagents import Model

class Message(Model):
  latitude: float 
  longitude: float 
  min_temp: float 
  max_temp: float 
  msg: str

class Response(Model):
  Temp:float
  msg: str

