#version 330

in vec3 local_position;

out vec4 frag_color;

void main(void) {
  frag_color = vec4(local_position / 2 + 0.5, 1.0);
}
