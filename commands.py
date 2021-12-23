def _init():
    global _commands
    _commands = ''

def append_command(v: str):
    global _commands
    _commands += v

def set_commands(v: str):
    global _commands
    _commands = v

def get_commands():
    global _commands
    return _commands