def calculate_grand_total(input)
  columns = input.split("\n")
                 .then { |lines| lines.map { |line| line.ljust(lines.map(&:length).max).chars } }
                 .transpose

  operator = ''
  numbers = []
  columns.each_with_index.inject(0) do |acc, (column, i)|
    if column.last == '*' || column.last == '+'
      result = operator != '' && !numbers.empty? ? numbers.inject { |acc, n| acc.send(operator, n) } : 0

      numbers.clear
      numbers << column[0..-2].join.to_i
      operator = column.last
      acc + result
    elsif i == columns.length - 1
      numbers << column.join.to_i
      result = numbers.inject { |acc, n| operator == '*' ? acc * n : acc + n }
      acc + result
    elsif column.all? { |e| e == " " }
      acc
    else
      numbers << column.join.to_i
      acc
    end
  end
end

puts calculate_grand_total(File.read(File.join(File.dirname(__FILE__), 'input')))