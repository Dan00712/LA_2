using DataFrames
using CSV

for arg in ARGS
    df = CSV.read(arg, DataFrame)

    df = df[:, 1:4]
    df[:, "p/bar-1"] = df[:, "p/bar-1"]
    rename!(df, "p/bar-1" => "p/bar")
    rename!(df, "Column4" => "Phase")
    
    CSV.write(arg * ".2", df)
end
