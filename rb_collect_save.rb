puts "Please enter your name:"
name = gets.chomp
puts "Please enter your age:"
age = gets.chomp
puts "Please enter your username:"
usr = gets.chomp
puts "Your name is #{name}, you are #{age} years old, and your username is #{usr}"
collect=File.open('dp1.txt','a')
collect.write(name)
collect.write(',')
collect.write(age)
collect.write(',')
collect.write(usr)
collect.write("\n")
collect.close()
