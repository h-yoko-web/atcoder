a,b = gets.to_s.split.map.each do |e|
  e.chomp.chars.map.each {|e| e.to_i}.sum
end

puts a > b ? a : b
