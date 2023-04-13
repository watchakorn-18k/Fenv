class Colors:
    """
    It's a class that contains a bunch of constants that represent colors.
    Example:
        Colors.RED
        Colors.GREEN
        Colors.YELLOW
        Colors.BLUE
        Colors.CYAN
        Colors.MAGENTA
        Colors.WHITE


    """

    ESCAPE_SEQ = {
        "HEADER": "\033[95m",
        "OKBLUE": "\033[94m",
        "OKGREEN": "\033[92m",
        "WARNING": "\033[93m",
        "FAIL": "\033[91m",
        "ENDC": "\033[0m",
        "BOLD": "\033[1m",
        "UNDERLINE": "\033[4m",
    }

    TEXT_COLORS = {
        "BLACK": "\033[30m",
        "RED": "\033[31m",
        "GREEN": "\033[32m",
        "YELLOW": "\033[33m",
        "BLUE": "\033[34m",
        "MAGENTA": "\033[35m",
        "CYAN": "\033[36m",
        "WHITE": "\033[37m",
    }

    LIGHT_COLORS = {
        "LIGHTBLACK_EX": "\033[90m",
        "LIGHTRED_EX": "\033[91m",
        "LIGHTGREEN_EX": "\033[92m",
        "LIGHTYELLOW_EX": "\033[93m",
        "LIGHTBLUE_EX": "\033[94m",
        "LIGHTMAGENTA_EX": "\033[95m",
        "LIGHTCYAN_EX": "\033[96m",
        "LIGHTWHITE_EX": "\033[97m",
    }

    COLOR256 = {
        "PURPLE": "\033[38;5;129m",
        "ORANGE": "\033[38;5;202m",
        "BROWN": "\033[38;5;130m",
        "OLIVE": "\033[38;5;142m",
        "GOLD": "\033[38;5;214m",
        "SILVER": "\033[38;5;188m",
        "MAROON": "\033[38;5;52m",
        "NAVY": "\033[38;5;21m",
        "TEAL": "\033[38;5;29m",
        "LIME": "\033[38;5;118m",
        "AQUA": "\033[38;5;45m",
        "FUSCHIA": "\033[38;5;161m",
        "PURPLE2": "\033[38;5;98m",
        "PLUM": "\033[38;5;88m",
        "INDIGO": "\033[38;5;54m",
        "TURQUOISE": "\033[38;5;80m",
        "STEEL_BLUE": "\033[38;5;67m",
        "ROSE": "\033[38;5;210m",
        "HOT_PINK": "\033[38;5;200m",
        "SALMON": "\033[38;5;173m",
        "CORAL": "\033[38;5;203m",
        "BEIGE": "\033[38;5;230m",
        "KHAKI": "\033[38;5;143m",
        "FOREST_GREEN": "\033[38;5;34m",
        "OLIVE_GREEN": "\033[38;5;58m",
        "LAVENDER": "\033[38;5;183m",
        "ORCHID": "\033[38;5;170m",
        "LILAC": "\033[38;5;134m",
        "SKY_BLUE": "\033[38;5;117m",
        "BABY_BLUE": "\033[38;5;152m",
        "POWDER_BLUE": "\033[38;5;165m",
        "SEA_GREEN": "\033[38;5;27m",
        "PALE_GREEN": "\033[38;5;120m",
        "SPRING_GREEN": "\033[38;5;48m",
        "MINT_GREEN": "\033[38;5;121m",
        "GRAY_BLUE": "\033[38;5;103m",
        "BLUE_GRAY": "\033[38;5;104m",
    }

    def __getattr__(self, name):
        if name in self.ESCAPE_SEQ:
            return self.ESCAPE_SEQ[name]
        elif name in self.TEXT_COLORS:
            return self.TEXT_COLORS[name]
        elif name in self.LIGHT_COLORS:
            return self.LIGHT_COLORS[name]
        elif name in self.COLOR256:
            return self.COLOR256[name]
        else:
            raise AttributeError

    def notice(self):
        return (
            self.SEA_GREEN
            + "["
            + self.ENDC
            + self.LIME
            + "notice"
            + self.SEA_GREEN
            + "]"
            + self.ENDC
            + " "
        )
