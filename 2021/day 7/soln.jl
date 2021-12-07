using Statistics
using Formatting

path = dirname(@__FILE__)
data = readlines(path * "\\input.txt")[1]

pattern = r"-?\d+"
parsed_data = [parse.(Int64, x) for x in SubString.(data, findall(pattern,data))]

function part1(ints)

   return sum(abs.(ints .- median(ints)))

end

function triangle(n)

    return n * (n+1) / 2

end

function part2(ints)

    m = round(mean(ints))
    return minimum([sum(triangle.(abs.(ints .- i))) for i ∈ m-1:m+1])

end

println(format(part1(parsed_data)))
println(format(part2(parsed_data)))