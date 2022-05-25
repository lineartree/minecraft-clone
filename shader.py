from OpenGL.GL import *

def create_shader(target, source_path):
    source_file = open(source_path, "rb")
    source = source_file.read()
    source_file.close()

    glShaderSource(target, source)
    glCompileShader(target)

class Shader:
    def __init__(self, vert_path, frag_path):
        vert_shader = glCreateShader(GL_VERTEX_SHADER)
        create_shader(vert_shader, vert_path)
        self.check_compile_error(vert_shader, "VERTEX")
        
        frag_shader = glCreateShader(GL_FRAGMENT_SHADER)
        create_shader(frag_shader, frag_path)
        self.check_compile_error(frag_shader, "FRAGMENT")

        # program
        self.program = glCreateProgram()
        glAttachShader(self.program, vert_shader)
        glAttachShader(self.program, frag_shader)
        glLinkProgram(self.program)
        self.check_compile_error(self.program, "PROGRAM")

        # delete shader
        glDeleteShader(vert_shader)
        glDeleteShader(frag_shader)

    def use(self):
        glUseProgram(self.program)

    def check_compile_error(self, target, type):
        if type != "PROGRAM":
            success = glGetShaderiv(target, GL_COMPILE_STATUS)
            if not success:
                infoLog = glGetShaderInfoLog(target)
                print(f"Error: {type} shader failed to compile: {infoLog}")
        else:
            success = glGetProgramiv(target, GL_LINK_STATUS)
            if not success:
                infoLog = glGetProgramInfoLog(target)
                print(f"Error: Program failed to link: {infoLog}")
                
                
            

