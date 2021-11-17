path = dirname(@__FILE__)

function make_move(coords, move)

    move_dict = Dict('R' => [1,0],
                    'L' => [-1,0],
                    'U' => [0,1],
                    'D' => [0,-1])

    return [coords + move_dict[move[1]] * n for n=1:parse(Int64, (move[2:end]))]


end

function make_all_moves(path)

    start = [0,0]
    coords_hit = [start]
    steps = [0]
    moves = split(path, ",")
    for move in moves
        coords_hit = vcat(coords_hit, make_move(coords_hit[end], move))
        steps = [steps; [1 for n=1:parse(Int64, (move[2:end]))]]
    end

    return coords_hit, accumulate(+, steps)

end


function both_parts()

    data = readlines(path * "\\input.txt")

    coords = [[]]
    steps = [[]]

    for path in data
        coords_in_path, steps_in_path = make_all_moves(path)
        coords = hcat(coords, [coords_in_path])
        steps = hcat(steps, [steps_in_path])
    end

    crossings = intersect(coords[2], coords[3])
    manhattan = minimum([sum(abs.(x)) for x in crossings if x != [0,0]])
    min_steps_in_crossing = minimum([steps[2][findfirst(isequal(c), coords[2])] + steps[3][findfirst(isequal(c), coords[3])] for c in crossings if c != [0,0]])
    
    return manhattan, min_steps_in_crossing

end

print(both_parts())
