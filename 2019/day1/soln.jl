path = dirname(@__FILE__)

part1() = sum([x ÷ 3 - 2 for x in parse.(Int, readlines(path * "\\input.txt"))])

function part2()

    total = 0
    input = parse.(Int, readlines(path * "\\input.txt"))

    while length(input) > 0
        input = [x ÷ 3 - 2 for x in input if x ÷ 3 - 2 > 0]
        total += sum(input)
    end

    return total

end
