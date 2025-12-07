def get_fresh_ingredient_ids_count(input)
  ranges = input.split(/^\n+/).first.split("\n").map {|el| el.split("-").map(&:to_i)}
  ranges = ranges.sort { |x,y| x[0] <=> y[0] }

  fresh_ingredient_ids_count = 0
  intersecting_ranges = Set.new
  ranges.each_with_index do |r, i|
    if i != ranges.length - 1 &&  r[1] >= ranges[i + 1][0]
      intersecting_ranges.merge([r, ranges[i + 1]])
    elsif !intersecting_ranges.include?(r)
      fresh_ingredient_ids_count += (r.last - r.first) + 1
    end
  end

  intersecting_ranges_ids_set = Set.new
  intersecting_ranges.each do |range|
    (range.first...range.last + 1).each {|el| intersecting_ranges_ids_set << el}
  end

  fresh_ingredient_ids_count + intersecting_ranges_ids_set.length
end



puts get_fresh_ingredient_ids_count(File.read(File.join(File.dirname(__FILE__), 'input')))