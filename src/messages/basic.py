from uagents import Model

class Message(Model):
  min_temp: float 
  max_temp: float 
  city: str
  state: str 
  country: str

class Response(Model):
  Temp:float
  msg: str

