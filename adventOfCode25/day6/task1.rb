def calculate_grand_total(input)
  rows = input.split("\n").map {|e| e.split(" ")}
  operators = rows.last
  rows.pop

  (0..rows.first.length - 1).inject(0) do |acc,i|
    result = 0
    rows.map {|a| a.map(&:to_i)}.each_with_index do |row, y|
      if y == 0
        result = row[i]
        next
      end

      result += row[i] if operators[i] == '+'
      result *= row[i] if operators[i] == '*'
    end
    acc + result
  end
end

puts calculate_grand_total(File.read(File.join(File.dirname(__FILE__), 'input')))