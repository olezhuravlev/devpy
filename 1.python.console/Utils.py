def get_parameter(msg):
    while True:
        try:
            square_length_raw = input(msg)
            square_length = float(square_length_raw)
        except ValueError:
            print("Wrong type! Entered \"", type(square_length_raw).__name__, "\" instead of \"float!\"", sep="")
            continue
        else:
            return square_length
