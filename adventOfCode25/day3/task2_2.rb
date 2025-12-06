MIN_BATTERIES = 12
def find_joltage(input)
  input.split("\n").inject(0) do |acc, bank|
    extra_batteries = bank.length - MIN_BATTERIES
    bank_integers = bank.split('').map(&:to_i)
    joltage = []
    bank_integers.each_with_index do |integer, i|
      if i == bank_integers.length - 1
        joltage << integer
        next
      end


      if integer >= bank_integers[i + 1]
        joltage << integer
      elsif extra_batteries > 0
        extra_batteries -= 1
        next
      else
        joltage << integer
      end
    end
    puts 'extra_batteries: ' + extra_batteries.to_s
    puts 'bank:  ' + bank

    # If array is too big
    if extra_batteries > 0
      indexes_to_remove = []
      (1..joltage.length - 1).each do |e|
        if extra_batteries > 0 && joltage[-e] <= joltage[-(e + 1)]
          indexes_to_remove << joltage.length - e
          extra_batteries -= 1
        end
      end
      puts joltage.join
      puts 'indexes_to_remove: ' + indexes_to_remove.join(', ')
      joltage = joltage.reject.with_index{|_v, i| indexes_to_remove.include?(i) }
    end
    puts joltage.join
    puts '------'
    acc + joltage.join.to_i
  end
end


puts find_joltage(File.read(File.join(File.dirname(__FILE__), 'input')))