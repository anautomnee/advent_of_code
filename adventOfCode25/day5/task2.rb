def get_fresh_ingredient_ids_count(input)
  ranges = input.split(/^\n+/).first.split("\n").map {|el| el.split("-").map(&:to_i)}
  fresh_ingredient_ids = Set.new
  ranges.each do |range|
    (range.first...range.last + 1).each {|el| fresh_ingredient_ids << el}
  end
  fresh_ingredient_ids.length
end

puts get_fresh_ingredient_ids_count(File.read(File.join(File.dirname(__FILE__), 'test')))