x,y = gets.split.map(&:to_i)
# if (x - y).abs < 3
#   puts "Yes"
# else
#   puts "No"
# end

puts (x - y).abs < 3 ? "Yes" : "No"
