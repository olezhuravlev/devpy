def get_parameter(msg, result_type=None, default=None, interval_begin=None, interval_end=None):
    while True:
        try:
            val_raw = input(msg)
            if not val_raw and default:
                val_raw = str(default)
            elif not val_raw:
                val_raw = "0"

            if result_type is int:
                val = int(val_raw)
                check_interval(val, interval_begin, interval_end)
            elif result_type is float:
                val = float(val_raw)
                check_interval(val, interval_begin, interval_end)
            else:
                val = val_raw

        except IndexError:
            print("Wrong interval! The value must be between", interval_begin, "and", interval_end)
            continue
        except ValueError:
            print("Wrong type! Entered \"", type(val_raw).__name__, "\" instead of \"" + result_type.__name__ + "\"!",
                  sep="")
            continue
        else:
            return val


def check_interval(value, interval_begin=None, interval_end=None):
    if interval_begin and value < interval_begin:
        raise IndexError
    elif interval_end and interval_end < value:
        raise IndexError
