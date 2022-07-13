def print_msg(msg, error=False, wrap=True):
    """Print message in console."""
    def green_msg(msg):
        """Make message green color in console."""
        return '\033[92m{0}\033[00m'.format(msg)

    def red_msg(msg):
        """Make message red color in console."""
        return '\033[91m{0}\033[00m'.format(msg)

    print_function = red_msg if error else green_msg
    msg = '\n{}\n'.format(msg) if wrap else msg
    print(print_function(msg))
