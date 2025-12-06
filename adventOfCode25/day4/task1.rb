def modify_map(input)
  map = input.split("\n").map { |line| line.split('')}
  modified_map = map.map(&:dup)
  max_x = map[0].length - 1
  max_y = map.length - 1

  accessible_rolls = 0
  map.each_with_index do |line, y|
    line.each_with_index do |el, x|
      next if el == '.'

      counter = 0
      (-1..1).each do |dy|
        (-1..1).each do |dx|
          next if x + dx > max_x || x + dx < 0 || y + dy > max_y || y + dy < 0

          counter += 1 if map[y + dy][x + dx] == '@'
        end
      end

      if counter <= 4
        modified_map[y][x] = 'x'
        accessible_rolls += 1
      end
    end
  end
  accessible_rolls
end

puts modify_map(File.read(File.join(File.dirname(__FILE__), 'input')))