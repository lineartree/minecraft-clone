#version 330

in vec3 local_position;
in vec3 interpolated_tex_coords;

out vec4 frag_color;

uniform sampler2DArray texture_array_sampler;

void main(void) {
  frag_color = texture(texture_array_sampler, interpolated_tex_coords);
}
