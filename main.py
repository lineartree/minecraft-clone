import pyglet
import pyglet.gl as gl

from OpenGL.GL import *
import glm

pyglet.options["shadow_window"] = False
pyglet.options["debug_gl"] = False

SCR_WIDTH = 800
SCR_HEIGHT = 600

class Window(pyglet.window.Window):
    def __init__(self, **args):
        super().__init__(**args)
        
    def on_draw(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        self.clear()

    def on_resize(self, width, height):
        print(f"Resize {width} * {height}")
        glViewport(0, 0, width, height)
        

class Game:
    def __init__(self):
        self.config = gl.Config(double_buffer = True, major_version = 3, minor_version = 3)
        self.window = Window(config = self.config, width = SCR_WIDTH, height = SCR_HEIGHT, caption = "Minecraft clone", resizable = True, vsync = False)

    def run(self):
        pyglet.app.run()

if __name__ == "__main__":
    game = Game()
    game.run()
