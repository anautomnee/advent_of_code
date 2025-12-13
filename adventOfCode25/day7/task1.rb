def find_beam_split_count(input)
  initial_map = input.split("\n")
  map = input.split("\n")
  counter = 0
  initial_map.each_with_index do |line, y|
    next if y == 0
    line.split("").each_with_index do |cell, x|
      above = map[y - 1][x]
      next if %w[. ^].include?(above)
      if above == 'S'
        map[y][x] = '|'
      elsif above == '|' && cell != '^'
        map[y][x] = '|'
      elsif above == '|' && cell == '^'
        counter += 1
        map[y][x - 1] = '|'
        map[y][x + 1] = '|'
      else
        next
      end
    end
  end
  # map.each do |line|
  #   puts line
  # end
  counter
end

puts find_beam_split_count(File.read(File.join(File.dirname(__FILE__), 'test')))