from calc import add, subtract
from model import Task
from service import TaskService


def main():
    print("Software Engineering Git Branch Experiment")

    result_add = add(10, 5)
    result_subtract = subtract(10, 5)

    print("10 + 5 =", result_add)
    print("10 - 5 =", result_subtract)

    service = TaskService()
    task = Task(task_id=1, title="Finish Git experiment", completed=False)
    service.add_task(task)

    print("Current task list:")
    for item in service.list_tasks():
        print(item)


if __name__ == "__main__":
    main()

print('B3 branch modification')

print('C4 branch modification')

