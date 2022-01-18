from Find4JModule import Find4JClass, IntOutOfBounds, PortOutOfBounds

class Find4J():
    def __init__(self):
        """ Initial Script Start """
        Find4JClass.banner()

    def main(self):
        self.get_user_input()
        Find4JClass.create_scan(self.ip, self.ports)

    def get_user_input(self):
        self.sindob = int(input("[*] Subnet [1] Single IP [2]: "))
        if self.sindob == 1:
            self.ip = input("[*] Subnet: ")
        elif self.sindob == 2:
            self.ip = input("[*] IP: ")
        else:
            raise IntOutOfBounds("Please only enter 1 or 2")

        self.ports = input("[*] Ports: ").strip()

run = Find4J()
run.main()