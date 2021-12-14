using Statistics
using Formatting

path = dirname(@__FILE__)
data = readlines(path * "\\input.txt")[1]

pattern = r"-?\d+"
parsed_data = [parse.(Int64, x) for x in SubString.(data, findall(pattern,data))]

part1(ints) = sum(abs.(ints .- median(ints)))

triangle(n) = n * (n+1) / 2

function part2(ints)

    start = round(mean(ints))
    return minimum([sum(triangle.(abs.(ints .- i))) for i ∈ start-1:start+1])

end

println(format(part1(parsed_data)))
println(format(part2(parsed_data)))