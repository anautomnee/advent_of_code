def find_beam_split_count(input)
  counter = 0
  beams = Set.new
  input.split("\n").each_with_index do |line, i|
    line.split("").each_with_index { |num, idx| beams << idx if num == 'S' } if i == 0
    new_beams = Set.new
    beams.each do |beam|
      if line[beam] == '^'
        counter += 1
        new_beams.merge([beam - 1, beam + 1])
      else
        new_beams << beam
      end
    end
    beams = new_beams
  end
  counter
end

puts find_beam_split_count(File.read(File.join(File.dirname(__FILE__), 'input')))