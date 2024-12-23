class Car():
  def __init__(self, brand):
      self.brand = brand
        
      def __str__(self):
        return self.brand
    
    
        
info = Car ("Lexus")
print(info)
del info
print(info)

