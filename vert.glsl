#version 330

layout (location = 0) in vec3 vertex_positions;

out vec3 local_position;

void main(void) {
  local_position = vertex_positions;
  gl_Position = vec4(vertex_positions, 1.0);
}
