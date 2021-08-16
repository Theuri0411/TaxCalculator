import person as pc

workers = []
counter = 0


def all_people():
    if len(workers) > 0:
        print("|No.| Name | Age | Gross Pay | Net Pay |")
        print("|---|------|-----|-----------|---------|")
        for worker in workers:
            print(worker.toString(workers.index(worker) + 1))
    else:
        print("No Workers")


while counter < 2:
    try:
        name = str(input("Enter your name: \n"))
        try:
            age = int(input("Enter your age: \n"))
            gross_pay = int(input("Enter your pay: \n"))
            person = pc.Person(
                name,
                age,
                gross_pay,
            )
            workers.append(person)
            counter += 1
        except ValueError:
            print("Invalid Data")
    except KeyboardInterrupt:
        print('The program was stopped by the user')
        all_people()
        exit()
all_people()
