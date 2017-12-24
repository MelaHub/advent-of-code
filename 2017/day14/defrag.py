from day10 import *

def knot_hash_to_binary_row(knot_hash):
  binary_repr = ''
  for hex_value in knot_hash:
    binary_repr += bin(int(hex_value, 16))[2:].zfill(4)
  return binary_repr

def input_to_knot(input_string):
  return knot_hash(range(128), input_string)

