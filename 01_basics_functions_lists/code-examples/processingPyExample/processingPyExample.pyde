def setup():
  size(500,500)
  noStroke()
  background(255)
  
def draw():
  fill(random(255),random(255),random(255))
  ellipse(random(width), random(height), 20,20)
