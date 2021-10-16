class Worker:
    def __init__(self, pay):
        self.payment_ph = pay

    def earnings(self, days):
        return self.payment_ph * 8 * days

    def taxes(self, days):
        return self.earnings(days) * 0.13

def main():
    a = Worker(1000)
    print(a.earnings(30))
    print(a.taxes(30))



if __name__ == '__main__':
    main()