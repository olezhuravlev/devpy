def get_parameter(msg, result_type=None, default=None):
    while True:
        try:
            val_raw = input(msg)
            if not val_raw and default:
                val_raw = str(default)
            elif not val_raw:
                val_raw = "0"

            if result_type is int:
                val = int(val_raw)
            else:
                val = float(val_raw)
        except ValueError:
            print("Wrong type! Entered \"", type(val_raw).__name__, "\" instead of \"" + result_type.__name__ + "\"!",
                  sep="")
            continue
        else:
            return val
