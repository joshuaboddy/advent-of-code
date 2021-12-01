path = dirname(@__FILE__)
data = parse.(Int, readlines(path * "\\input.txt"))

function part1()

    return sum(diff(data) .> 0)

end

function part2()

    threes = [sum(data[1+i:3+i]) for i ∈ 0:length(data)-3]
    return sum(diff(threes) .> 0)

end

println(part1())
println(part2())