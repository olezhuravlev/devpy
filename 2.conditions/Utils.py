def get_parameter(msg, result_type=None):
    while True:
        try:
            val_raw = input(msg)
            if result_type is int:
                val = int(val_raw)
            else:
                val = float(val_raw)
        except ValueError:
            print("Wrong type! Entered \"", type(val_raw).__name__, "\" instead of \"float!\"", sep="")
            continue
        else:
            return val
