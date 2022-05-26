#version 330

layout (location = 0) in vec3 vertex_positions;

out vec3 local_position;

uniform mat4 mvp_matrix;

void main(void) {
  local_position = vertex_positions;
  gl_Position = mvp_matrix * vec4(vertex_positions, 1.0);
}
