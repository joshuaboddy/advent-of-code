path = dirname(@__FILE__)
data = parse.(Int, readlines(path * "\\input.txt"))

function part1()

    sum([1 for x in diff(data) if x > 0])

end

function part2()

    threes = [sum(data[1+i:3+i]) for i ∈ 0:length(data)-3]
    sum([1 for x in diff(threes) if x > 0])

end

println(part1())
println(part2())