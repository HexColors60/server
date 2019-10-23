from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()

# FOREST
forestRooms = {title: Room(title=title, description=title) for title in range(100)}

forestGrid = []
tempForestArray = []
keepTrackOfIndex = 9
rows=10
cols=10

for key, value in forestRooms.items():
  if keepTrackOfIndex == key:
    keepTrackOfIndex += rows
    tempForestArray.append(value)
    forestGrid.append(tempForestArray)
    tempForestArray = []
  else:
    tempForestArray.append(value)

for i in range(rows):
  for j in range(cols):
    forestGrid[i][j].save()

for i in range(rows):
  for j in range(cols):
    if i < rows - 1:
      forestGrid[i][j].connectRooms(forestGrid[i + 1][j], "s")
    if i > 0:
      forestGrid[i][j].connectRooms(forestGrid[i - 1][j], "n")  
    if j < cols - 1:
      forestGrid[i][j].connectRooms(forestGrid[i][j + 1], "e")  
    if j > 0:
      forestGrid[i][j].connectRooms(forestGrid[i][j - 1], "w")

# STREET

streetRooms = {title: Room(title=title, description=title) for title in range(100, 200)}

streetGrid = []
tempStreetArray = []
keepTrackOfStreetIndex = 109
# rows=10
# cols=10

for key, value in streetRooms.items():
  if keepTrackOfStreetIndex == key:
    keepTrackOfStreetIndex += rows
    tempStreetArray.append(value)
    streetGrid.append(tempStreetArray)
    tempStreetArray = []
  else:
    tempStreetArray.append(value)

for i in range(rows):
  for j in range(cols):
    streetGrid[i][j].save()

for i in range(rows):
  for j in range(cols):
    if i < rows - 1:
      streetGrid[i][j].connectRooms(streetGrid[i + 1][j], "s")
    if i > 0:
      streetGrid[i][j].connectRooms(streetGrid[i - 1][j], "n")  
    if j < cols - 1:
      streetGrid[i][j].connectRooms(forestGrid[i][j + 1], "e")  
    if j > 0:
      streetGrid[i][j].connectRooms(streetGrid[i][j - 1], "w")

players=Player.objects.all()
for p in players:
  p.currentRoom = forestGrid[0][0].title
  p.save()