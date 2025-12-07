def get_fresh_ingredient_ids_count(input)
  ranges = input.split(/^\n+/).first.split("\n").map {|el| el.split("-").map(&:to_i)}
  ranges = ranges.sort { |x,y| x[0] <=> y[0] }

  fresh_ingredient_ids_count = 0
  current_max = 0
  ranges.each do |r|
    if r.first <= current_max && r.last <= current_max
      next
    elsif r.first <= current_max && r.last > current_max
      fresh_ingredient_ids_count += r.last - current_max
      current_max = r.last
    else
      fresh_ingredient_ids_count += (r.last - r.first) + 1
      current_max = r.last
    end
  end

  fresh_ingredient_ids_count
end

puts get_fresh_ingredient_ids_count(File.read(File.join(File.dirname(__FILE__), 'input')))