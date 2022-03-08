class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def on_one_line(self, other1, other2):
        return abs((other2.x - self.x) * (other1.y - self.y) - (other1.x - self.x) * (other2.y - self.y)) < 1e-9


def read_points_from_file(filename):
    points = []
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if line == '':
            break
        else:
            values = list(map(float, line.split()))
            points.append(Point(values[0], values[1]))
    file.close()
    return points


def find_points_max_perimeter(points):
    max_perimeter = 0
    result = []
    for i in range(len(points) - 2):
        for j in range(i + 1, len(points) - 1):
            for k in range(j + 1, len(points)):
                if not points[i].on_one_line(points[j], points[k]):
                    sum_ = points[i].distance_to(points[j]) + points[j].distance_to(points[k]) \
                           + points[k].distance_to(points[i])
                    if sum_ > max_perimeter:
                        max_perimeter = sum_
                        result = [i, j, k]
    if len(result) == 0:
        return None
    return points[result[0]], points[result[1]], points[result[2]]


if __name__ == '__main__':
    filename_ = 'input01.txt'
    points_ = find_points_max_perimeter(read_points_from_file(filename_))
    if points_ is None:
        print('Нет точек, образующих треугольник')
    else:
        for point in points_:
            print('{0}, {1}'.format(point.x, point.y))
