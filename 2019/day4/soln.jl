puzzle_input = "254032-789860"

function part1(string_range)

    range = parse.(Int, split(string_range, "-"))

    cnt = 0
    for i ∈ range[1]:range[2]
        unsorted_i = string(i)
        sorted_i = join(sort(split(unsorted_i, "")))
        for dub ∈ 0:9
            if sorted_i == unsorted_i
                if occursin(string(dub)^2, unsorted_i)
                    cnt+=1
                    break
                end
            end
        end
    end 

    return cnt

end

function part2(string_range)

    range = parse.(Int, split(string_range, "-"))

    cnt = 0
    
    for i ∈ range[1]:range[2]
        unsorted_i = string(i)
        sorted_i = join(sort(split(unsorted_i, "")))
        for dub ∈ 0:9
            if sorted_i == unsorted_i
                if occursin(string(dub)^2, unsorted_i)
                    if !occursin(string(dub)^3, unsorted_i)
                        cnt+=1
                        break
                    end
                end
            end
        end
    end 

    return cnt

end

println(part1(puzzle_input))
println(part2(puzzle_input))