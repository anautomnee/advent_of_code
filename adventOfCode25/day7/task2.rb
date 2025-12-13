def find_timelines_count(input)
  @map = input.split("\n")
  @memo = {}
  start_position = @map.first.split("").index('S')
  continue_beam(start_position, 1)
end

def continue_beam(beam_x, current_row)
  key = [beam_x, current_row]
  return @memo[key] if @memo.key?(key)

  if current_row == @map.length - 1
    @memo[key] = 1
    return 1
  end

  result = if @map[current_row][beam_x] == '.'
    continue_beam(beam_x, current_row + 1)
  elsif @map[current_row][beam_x] == '^'
    continue_beam(beam_x - 1, current_row + 1) + continue_beam(beam_x + 1, current_row + 1)
  end

  @memo[key] = result
end

puts find_timelines_count(File.read(File.join(File.dirname(__FILE__), 'input')))