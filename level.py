from pipe import Pipe


class Level:
    def __init__(self, x, y):
        self.pipeList = []
        self.x = x
        self.y = y

    def generate(self, width, height):
        for x in range(width):
            for y in range(height):
                pipe = Pipe(self, x, y)
                self.pipeList.append(pipe)

    def render(self, display):
        for pipe in self.pipeList:
            pipe.render(display)

    def click(self, pos):
        for pipe in self.pipeList:
            pipe.click(pos)
