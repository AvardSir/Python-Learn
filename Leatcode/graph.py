class graph():
    def __init__(self,graphs=[[1, 2], [2, 3], [3, 1], [0, 0]]):

        self.graphs = [graphs]

        #self.graphs = [[1, 2], [2, 3], [3, 1], [0, 0]]
        print('we creat')
    def print_graph(self):
        for i in self.graphs:
            print(i)
    def add_path(self,new_path):
        self.graphs.append(new_path)
    def get_len(self):
        return len(self.graphs)
first_graph=graph([1,23])
first_graph.add_path([0,7])
#tak tak#####YEK voyna
print(first_graph.get_len())
first_graph.print_graph()
#voyna is bad#so bad so b#####a##########Im sick#alsi sick!also sick#SSS#LABAROTIRY#ffsffssf#im in so bad moon#

#fuck it so bad lost 70 day steak..###So bad its in divorce###AAAA