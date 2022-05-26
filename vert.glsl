#version 330

layout (location = 0) in vec3 vertex_positions;
layout (location = 1) in vec3 tex_coords;

out vec3 local_position;
out vec3 interpolated_tex_coords;

uniform mat4 mvp_matrix;

void main(void) {
  local_position = vertex_positions;
  interpolated_tex_coords = tex_coords;
  gl_Position = mvp_matrix * vec4(vertex_positions, 1.0);
}
