# frozen_string_literal: true

DIALS_SIZE = 100
STARTING_POINT = 50

TEST_INPUT = "L68
L30
R248
L5
R60
L55
L1
L99
R14
L82"

def find_password(input)
  zero_point_counter = 0
  current_position = STARTING_POINT

  input.split("\n").each do |instruction|
    current_position = rotate(instruction, current_position)
    zero_point_counter += 1 if current_position.zero?
  end

  puts zero_point_counter
end

def rotate(instruction, current_position)
  steps = instruction[1..].to_i
  case instruction[0]
  when 'R'
    (current_position + steps) % DIALS_SIZE
  when 'L'
    (current_position - steps) % DIALS_SIZE
  else
    puts('Incorrect instruction')
    current_position
  end
end

find_password(File.read(File.join(File.dirname(__FILE__), 'input.txt')))
# find_password(TEST_INPUT)
