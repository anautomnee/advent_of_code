# frozen_string_literal: true

DIALS_SIZE = 100
STARTING_POINT = 50

TEST_INPUT = "L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"

@zero_point_counter = 0

def find_password(input)
  current_position = STARTING_POINT

  input.split("\n").each do |instruction|
    current_position = rotate(instruction, current_position)
    @zero_point_counter += 1 if current_position.zero?
  end

  puts @zero_point_counter
end

def rotate(instruction, current_position)
  puts current_position,instruction
  steps = instruction[1..].to_i
  case instruction[0]
  when 'R'
    rotation_result = current_position + steps
    @zero_point_counter += rotation_result / DIALS_SIZE
    new_position = rotation_result % DIALS_SIZE
    @zero_point_counter -= 1 if new_position.zero?
    new_position
  when 'L'
    rotation_result = current_position - steps
    @zero_point_counter += (rotation_result / DIALS_SIZE).abs
    new_position = rotation_result % DIALS_SIZE
    @zero_point_counter -= 1 if current_position.zero?
    new_position
  else
    puts('Incorrect instruction')
    current_position
  end
end

# find_password(File.read(File.join(File.dirname(__FILE__), 'input.txt')))
find_password(TEST_INPUT)