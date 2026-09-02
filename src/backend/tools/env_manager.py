class EnvManager:
    def __init__(self):
        self.__vars = {}

        with open(".env", "r") as file:
            for line in file.readlines():
                k, v = line.split(" = ")
                k = k.strip()
                v = v.strip()

                self.__vars[k] = v

    def get_var(self, key) -> str:
        """Gets var from environment vars"""
        if key in self.__vars:
            return self.__vars[key]
        return ""
