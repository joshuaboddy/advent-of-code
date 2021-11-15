path = dirname(@__FILE__)

function part1(noun=12, verb=2)

    data = parse.(Int, (split(strip(read(path * "\\input.txt", String)), ",")))

    i = 1
    data[2] = noun
    data[3] = verb

    while i < length(data)
        if data[i] == 1
            data[data[i+3]+1] = data[data[i+1]+1] + data[data[i+2]+1]
            i = i + 4
        elseif data[i] == 2
            data[data[i+3]+1] = data[data[i+1]+1] * data[data[i+2]+1]
            i = i + 4
        elseif data[i] == 99
            break
        end
    end

    return data[1]

end

function part2()

    for i=0:99
        for j=0:99
            if part1(i, j) == 19690720
                return i*100 + j
            end
        end
    end

end

println("part 1 is: ", part1())
println("part 2 is: ", part2())
