# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon

NewYork= LatLon(112,231)

print(NewYork.lat)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
class Waypoint(LatLon):
    def __init__(self,name,lat,lon):
        super().__init__(lat,lon)
        self.name=name
    def __str__(self):
        return(f'This is called {self.name} with lat  at {self.lat} and lon at {self.lon}')

# YOUR CODE HERE

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self,name,difficulty,size,lat,lon):
        super().__init__(name,lat,lon)
        self.difficulty=difficulty
        self.size=size
   

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
new_way_point=Waypoint('Catacombs',154,233)
print(new_way_point.name)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)
print(str(new_way_point))
# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.4155
Newberry=Geocache('Newberry Views',1.5,2,44,-121)
# YOUR CODE HERE

# Print it--also make this print more nicely
# print(geocache)
print(str(Newberry))