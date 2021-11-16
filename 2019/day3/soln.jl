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
    moves = split(path, ",")
    for move in moves
        coords_hit = [coords_hit; make_move(coords_hit[end], move)]
    end

    return Set(coords_hit)

end


function part1()

    data = readlines(path * "\\input.txt")

    coords = []

    for path in data
        coords = [coords; make_all_moves(path)]
    end

    crossings = intersect(coords[1], coords[2])
    manhattan = minimum([sum(abs.(x)) for x in crossings if x != [0,0]])

    return manhattan

end

print(part1())
