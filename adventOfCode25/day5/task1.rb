def get_fresh_ingredients_count(input)
  ranges, ingredients = input.split(/^\n+/).map {|el| el.split("\n")}

  ingredients.map(&:to_i).inject(0) do |acc, el|
    is_fresh = false
    ranges.each do |range|
      next if range.split("-")[0].to_i > el
      is_fresh = true if range.split("-")[0].to_i <= el && range.split("-")[1].to_i >= el
    end
    if is_fresh then acc + 1 else acc end
  end
end

puts get_fresh_ingredients_count(File.read(File.join(File.dirname(__FILE__), 'input')))