def find_invalid_ids(input)
  input.split(',').inject(0) do |acc, range|
    range = range.split('-').map(&:to_i)
    (range[0]..range[1]).each do |n|
      s = n.to_s
      (1..s.length / 2).each do |bite|
        next if s.length % bite != 0

        parts = Set.new
        (0..s.length - bite).step(bite).each do |i|
          parts.add(s[i..i + bite - 1])
          break if parts.length > 1
        end

        if parts.length == 1
          acc += n
          break
        end
      end
    end
    acc
  end
end

puts find_invalid_ids(File.read(File.join(File.dirname(__FILE__), 'input')))