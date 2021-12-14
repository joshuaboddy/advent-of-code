path = dirname(@__FILE__)
data = readlines(path * "\\input.txt")

function read_data()

    pattern = r"-?\d+"
    ints = [Base.parse.(Int64, SubString.(x, findall(pattern,x))) for x in data]
    return ints

end

function part1()

    data = read_data()
    points_touched = Dict()
    for line in data
        if line[1] == line[3]
            x = line[1]
            for y ∈ min(line[2],line[4]):min(line[2],line[4])+max(abs(line[2]-line[4]), 1)
                points_touched[x, y] = get(points_touched, (x, y), 0) + 1 
            end
        elseif line[2] == line[4]
            y = line[2]
            for x ∈ min(line[1],line[3]):min(line[1],line[3])+max(abs(line[1]-line[3]), 1)
                points_touched[x, y] = get(points_touched, (x, y), 0) + 1 
            end
        end
    end

    return sum(values(points_touched) .> 1)

end

function part2()

    data = read_data()
    points_touched = Dict()
    for line in data
        if line[1] == line[3]
            x = line[1]
            for y ∈ min(line[2],line[4]):min(line[2],line[4])+max(abs(line[2]-line[4]), 1)
                points_touched[x, y] = get(points_touched, (x, y), 0) + 1 
            end
        elseif line[2] == line[4]
            y = line[2]
            for x ∈ min(line[1],line[3]):min(line[1],line[3])+max(abs(line[1]-line[3]), 1)
                points_touched[x, y] = get(points_touched, (x, y), 0) + 1 
            end
        elseif abs(line[1]-line[3]) == abs(line[2]-line[4])
            startx = line[1]
            diffx = abs(line[1]-line[3])
            xflag = sign(line[3]-line[1])
            xs = [startx + i*xflag for i in 0:diffx]
            starty = line[2]
            diffy = abs(line[2]-line[4])
            yflag = sign(line[4]-line[2])
            ys = [starty + i*yflag for i in 0:diffy]
            for (x,y) in zip(xs, ys)
                points_touched[x, y] = get(points_touched, (x, y), 0) + 1 
            end
        end
    end

    return sum(values(points_touched) .> 1)

end

println(part1())
println(part2())