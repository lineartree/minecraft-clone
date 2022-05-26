import pyglet
import pyglet.gl as gl

from OpenGL.GL import *
import glm

import shader
import block_type
import texture_manager

pyglet.options["shadow_window"] = False
pyglet.options["debug_gl"] = False

SCR_WIDTH = 800
SCR_HEIGHT = 600

class Window(pyglet.window.Window):
    def __init__(self, **args):
        super().__init__(**args)

        # create blocks
        self.texture_manager = texture_manager.Texture_manager(16, 16, 256)

        self.log = block_type.Block_type(self.texture_manager, "log", {"top": "log_top", "bottom": "log_top", "sides": "log_side"})

        self.texture_manager.generate_mipmaps()
        
        # create vao
        self.vao  = glGenVertexArrays(1)
        glBindVertexArray(self.vao)

        # create vertex position vbo
        self.vertex_position_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vertex_position_vbo)
        glBufferData(GL_ARRAY_BUFFER, self.log.vertex_positions.nbytes, self.log.vertex_positions.ptr, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * glm.sizeof(glm.float32), None)
        glEnableVertexAttribArray(0)
        
        # create tex_coord vao
        self.tex_coord_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.tex_coord_vbo)
        glBufferData(GL_ARRAY_BUFFER, self.log.tex_coords.nbytes, self.log.tex_coords.ptr, GL_STATIC_DRAW)

        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 3 * glm.sizeof(glm.float32), None)
        glEnableVertexAttribArray(1)
        
        # create ibo
        self.ibo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ibo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.log.indices.nbytes, self.log.indices.ptr, GL_STATIC_DRAW)

        # create shader
        self.shader = shader.Shader("vert.glsl", "frag.glsl")
        self.shader.use()

        # call update function every 60th of a second
        self.x = 0
        pyglet.clock.schedule_interval(self.update, 1.0 / 60)

    def update(self, delta_time):
        self.x += delta_time
        
    def on_draw(self):
        self.m_matrix = glm.mat4(1.0)
        self.v_matrix = glm.mat4(1.0)
        self.p_matrix = glm.mat4(1.0)
        
        self.m_matrix = glm.rotate(self.m_matrix, self.x, glm.vec3(0.5, 1.0, 0.0))
        self.v_matrix = glm.translate(self.v_matrix, glm.vec3(0.0, 0.0, -3.0))
        self.p_matrix = glm.perspective(glm.radians(45.0), SCR_WIDTH/SCR_HEIGHT, 0.1, 100.0)
        self.mvp_matrix = self.p_matrix * self.v_matrix * self.m_matrix

        self.shader.setMat4("mvp_matrix", self.mvp_matrix)
        
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        self.clear()

        glDrawElements(GL_TRIANGLES, len(self.log.indices), GL_UNSIGNED_INT, None)

    def on_resize(self, width, height):
        print(f"Resize {width} * {height}")
        glViewport(0, 0, width, height)
        

class Game:
    def __init__(self):
        self.config = gl.Config(double_buffer = True, major_version = 3, minor_version = 3, depth_size = 16)
        self.window = Window(config = self.config, width = SCR_WIDTH, height = SCR_HEIGHT, caption = "Minecraft clone", resizable = True, vsync = False)

    def run(self):
        pyglet.app.run()

if __name__ == "__main__":
    game = Game()
    game.run()
