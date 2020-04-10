from cmath import sqrt


class Utils:
    @staticmethod
    def read_network(filename):
        file = open(filename)
        network = {'noNodes': int(file.readline())}
        matrix = []

        for _ in range(network['noNodes']):
            column = []
            values = file.readline().split(',')
            for value in values:
                column.append(int(value))
            matrix.append(column)
        network['matrix'] = matrix

        grades = []
        no_edges = 0
        for i in range(network['noNodes']):
            grade = 0
            for j in range(network['noNodes']):
                if matrix[i][j] > 0:
                    grade += 1
                    no_edges += matrix[i][j]
            grades.append(grade)
        no_edges /= 2
        network['noEdges'] = no_edges
        network['grades'] = grades
        file.close()
        return network

    @staticmethod
    def euclidean_distance(n1, n2):
        return sqrt((n1[0] - n2[0]) * (n1[0] - n2[0]) + (n1[1] - n2[1]) * (n1[1] - n2[1]))

    @staticmethod
    def read_city(filename):
        matrix = {}
        f = open(filename, "r")
        words = f.readline().split(' ')
        while words[0] != "DIMENSION":
            words = f.readline().split(' ')
        matrix['noNodes'] = int(words[2])
        f.readline()
        f.readline()
        lines = []
        for i in range(0, matrix['noNodes']):
            words = f.readline().split(" ")
            lines.append((float(words[1]), float(words[2])))

        matrix['matrix'] = []
        for i in range(0, matrix['noNodes']):
            matrix['matrix'].append([])
            for j in range(0, matrix['noNodes']):
                matrix['matrix'][i].append(0.0)

        for i in range(matrix['noNodes'] - 1):
            for j in range(i + 1, matrix['noNodes']):
                matrix['matrix'][i][j] = matrix['matrix'][j][i] = (sqrt(
                    (lines[j][0] - lines[i][0]) * (lines[j][0] - lines[i][0]) + (lines[j][1] - lines[i][1]) * (
                                lines[j][1] - lines[i][1]))).real
        return matrix

    @staticmethod
    def modularity(communities, param):
        matrix = param['matrix']
        q = 0.0
        for i in range(len(communities) - 1):
            q += matrix[communities[i]][communities[i + 1]]
        return q + matrix[communities[len(communities) - 1]][communities[0]]
