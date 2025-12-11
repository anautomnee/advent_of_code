def calculate_grand_total(input)
  rows = input.split("\n").map(&:chars)
  numbers = []
  operator = ''
  (0...rows.first.length).inject(0) do |acc, column_i|
    column = []
    (0...rows.length).each do |row_i|
      el = rows[row_i][column_i]
      if el == '*' || el == '+'
        operator = el
        next
      end
      column << el
    end
    if column.all? {|e| e == " "} || column_i == rows.first.length - 1
      numbers << column.join.to_i if column_i == rows.first.length - 1
      result = numbers.inject{ | acc, number | operator == '*' ? acc * number : acc + number }
      numbers.clear
      operator = ''
      acc + result
    else
      numbers << column.join.to_i
      acc
    end
  end
end

puts calculate_grand_total(File.read(File.join(File.dirname(__FILE__), 'input')))