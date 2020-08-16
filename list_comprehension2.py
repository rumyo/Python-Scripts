filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

newfilenames = [e.replace('.hpp','.h') for e in filenames]

print(newfilenames) 

# Replaces .hpp with .h
# ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
