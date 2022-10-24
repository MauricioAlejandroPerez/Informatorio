alien_0 = {'color': 'green', 'speed': 'slow'}
#print(f"Puntos del alien: {alien_0['points']}")
#alien_0["points"] = 10
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)