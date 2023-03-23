""" Code module for generating content files """


class Commands:
    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs

    def get_main_py(self):
        return """
def main():
    pass


if __name__ == "__main__":
    main()
        """
