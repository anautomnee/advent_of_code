def find_invalid_ids(input)
  input.split(',').inject(0) do |acc, range|
    range = range.split('-').map(&:to_i)
    (range[0]..range[1]).each do |n|
      s = n.to_s
      next if s.length.odd?
      acc += n if s[..s.length / 2 - 1] == s[s.length / 2..]
    end
    acc
  end
end

puts find_invalid_ids(File.read(File.join(File.dirname(__FILE__), 'input')))