BATTERIES_NEEDED = 12

def find_joltage(input)
  input.split("\n").inject(0) do |acc, bank|
    bank = bank.split('').map(&:to_i)

    joltage = []
    joltage = recursive_find_joltage(joltage, bank, 0)
    acc + joltage.join.to_i
  end
end



def find_max(arr)
  max_value = 0
  index = 0
  arr.each_with_index do |el, i|
    if el > max_value
      max_value = el
      index = i
    end
  end
  return max_value, index
end


def recursive_find_joltage(joltage, bank, current_index)
  return joltage if joltage.length == BATTERIES_NEEDED

  battaries_remaining = bank.length - current_index
  digits_to_fill = BATTERIES_NEEDED - joltage.length
  can_skip = battaries_remaining - digits_to_fill

  if can_skip > 0
    max_value, index = find_max(bank[current_index..current_index + can_skip])
    joltage << max_value
    recursive_find_joltage(joltage, bank, current_index + index + 1)
  else
    joltage << bank[current_index]
    recursive_find_joltage(joltage, bank, current_index + 1)
  end
end

puts find_joltage(File.read(File.join(File.dirname(__FILE__), 'input')))