def find_joltage(input)
  input.split("\n").inject(0) do |acc, bank|
    max = 0
    bank_integers = bank.split('').map(&:to_i)
    bank_integers.each_with_index do |decimal, i|
      next if i == bank_integers.length - 1

      (i + 1..bank_integers.length - 1).each do |unit_index|
        joltage = "#{decimal}#{bank_integers[unit_index]}".to_i
        max = joltage if joltage > max
      end
    end
    acc + max
  end
end

puts find_joltage(File.read(File.join(File.dirname(__FILE__), 'input')))
