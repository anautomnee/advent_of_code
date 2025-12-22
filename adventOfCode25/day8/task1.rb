CONNECTIONS_NEEDED_COUNT = 1000

def multiple_three_largest_circuits(input)
  boxes = input.split("\n").map { |box| box.split(",") }.map { |box| box.map(&:to_i) }
  circuits = []
  distance_hash = build_distance_hash(boxes)
  sorted_values = distance_hash.values.sort
  (0...CONNECTIONS_NEEDED_COUNT).each do |sorted_i|
    closest_boxes = distance_hash.key(sorted_values[sorted_i])

    box_1_circuit_ind = nil
    box_2_circuit_ind = nil

    circuits.each_with_index do |circuit, i|
      if circuit.include? boxes[closest_boxes[0]]
        box_1_circuit_ind = i
      end
      if circuit.include? boxes[closest_boxes[1]]
        box_2_circuit_ind = i
      end
      if !box_1_circuit_ind.nil? && !box_2_circuit_ind.nil?
        break
      end
    end

    already_connected = !box_1_circuit_ind.nil? && box_1_circuit_ind == box_2_circuit_ind

    if already_connected
      next
    end

    if box_1_circuit_ind.nil? && box_2_circuit_ind.nil?
      circuits.push([boxes[closest_boxes[0]], boxes[closest_boxes[1]]])
    elsif !box_1_circuit_ind.nil? && !box_2_circuit_ind.nil?
      if box_1_circuit_ind < box_2_circuit_ind
        circuits[box_1_circuit_ind].concat(circuits[box_2_circuit_ind])
        circuits.delete_at(box_2_circuit_ind)
      else
        circuits[box_2_circuit_ind].concat(circuits[box_1_circuit_ind])
        circuits.delete_at(box_1_circuit_ind)
      end
    elsif !box_1_circuit_ind.nil?
      circuits[box_1_circuit_ind].push(boxes[closest_boxes[1]])
    else
      circuits[box_2_circuit_ind].push(boxes[closest_boxes[0]])
    end
  end

  circuits = circuits.sort { |a, b| b.length <=> a.length }
  circuits.each { |c| puts c.to_s }
  puts circuits.length

  result = 1
  circuits[0..2].each { |circuit| result *= circuit.length }
  result
end

def build_distance_hash(boxes)
  memo_distance = {}
  (0...boxes.length - 1).each do |m|
    (m + 1...boxes.length).each do |n|
      memo_distance[[m, n]] =
        Math.sqrt((boxes[m][0] - boxes[n][0])**2 + (boxes[m][1] - boxes[n][1])**2 + (boxes[m][2] - boxes[n][2])**2)
    end
  end
  memo_distance
end

puts multiple_three_largest_circuits(File.read(File.join(File.dirname(__FILE__), 'input')))