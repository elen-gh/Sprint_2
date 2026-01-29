class PointsForPlace:
    def __init__(self):
        self.points = 0
        
    def get_points_for_place(self, place, forclass = True):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            self.points = 0
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            self.points = 0
        else:
            self.points = 101 - place
            if forclass:
                print(self.points)
        return self.points
        
class PointsForMeters:
    def __init__(self):
        self.points = 0
        
    def get_points_for_meters(self, meters, forclass = True):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            self.points = 0
        else:
            self.points = meters * 0.5
            if forclass:
                print(self.points)
            
        return self.points
        

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        self.points = 0
        PointsForPlace.__init__(self)
        PointsForMeters.__init__(self)
        
    def get_total_points(self, place, meters):
    
        total = self.get_points_for_place(place, forclass = False) + self.get_points_for_meters(meters, forclass = False)
        print(total)

points_for_place = PointsForPlace()
points_for_place.get_points_for_place(10)

points_for_meters = PointsForMeters()
points_for_meters.get_points_for_meters(10)

total_points = TotalPoints()
total_points.get_points_for_place(10)
total_points.get_points_for_meters(10)
total_points.get_total_points(100, 10)