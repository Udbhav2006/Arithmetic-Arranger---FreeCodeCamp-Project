import string


def arithmetic_arranger(problems, show_solution=False):

    arranged_problems = ''
    e = check_for_error(problems)

    first_row = []
    second_row = []
    third_row = []
    solution_row = []
    

    while True:

        if e != 'None':
            arranged_problems = e
            break

        solutions = calculate_solution(problems)

        counter = 1
        for problem in problems:

            num1 = problem.split(' ')[0]
            sign = problem.split(' ')[1]
            num2 = problem.split(' ')[2]

            if len(num1) > len(num2):

                problem_length = len(num1) + 2
                solution = solutions[problems.index(problem)]
                solution_row.append(" " * (problem_length - len(solution)) +
                                    solution)
                third_row.append("-" * problem_length)

                first_row.append(" " * 2 + num1)
                second_row.append(sign + " " * int(len(num1) - len(num2) + 1) +
                                  num2)

                if counter < len(problems):

                    solution_row[problems.index(problem)] = solution_row[
                        problems.index(problem)] + " " * 4
                    third_row[problems.index(problem)] = third_row[
                        problems.index(problem)] + " " * 4
                    first_row[problems.index(problem)] = first_row[
                        problems.index(problem)] + " " * 4
                    second_row[problems.index(problem)] = second_row[
                        problems.index(problem)] + " " * 4

                    counter += 1

            elif len(num1) < len(num2):

                problem_length = len(num2) + 2
                third_row.append("-" * problem_length)
                solution = solutions[problems.index(problem)]
                solution_row.append(" " * (problem_length - len(solution)) +
                                    solution)

                first_row.append(" " * int(len(num2) - len(num1) + 2) + num1)
                second_row.append(sign + " " + num2)

                if counter < len(problems):

                    solution_row[problems.index(problem)] = solution_row[
                        problems.index(problem)] + " " * 4
                    third_row[problems.index(problem)] = third_row[
                        problems.index(problem)] + " " * 4
                    first_row[problems.index(problem)] = first_row[
                        problems.index(problem)] + " " * 4
                    second_row[problems.index(problem)] = second_row[
                        problems.index(problem)] + " " * 4

                    counter += 1

            elif len(num1) == len(num2):

                problem_length = len(num1) + 2
                third_row.append("-" * problem_length)
                solution = solutions[problems.index(problem)]
                solution_row.append(" " * (problem_length - len(solution)) +
                                    solution)

                first_row.append(" " * 2 + num1)
                second_row.append(sign + " " + num2)

                if counter < len(problems):

                    solution_row[problems.index(problem)] = solution_row[
                        problems.index(problem)] + " " * 4
                    third_row[problems.index(problem)] = third_row[
                        problems.index(problem)] + " " * 4
                    first_row[problems.index(problem)] = first_row[
                        problems.index(problem)] + " " * 4
                    second_row[problems.index(problem)] = second_row[
                        problems.index(problem)] + " " * 4

                    counter += 1
    

        for i in first_row:
            arranged_problems += i
        arranged_problems += '\n'
        for i in second_row:
            arranged_problems += i
        arranged_problems += '\n'
        for i in third_row:
            arranged_problems += i

        if show_solution:
            arranged_problems += '\n'
            for i in solution_row:
                arranged_problems += i

        break

    return arranged_problems


def check_for_error(problems):

    error_present = 'None'

    #======= Error Case 1 =========

    if len(problems) > 5:
        error_present = "Error: Too many problems."

#======= Error Case 2 =========

    for problem in problems:
        l = problem.split(' ')

        if l[1] not in ['+', '-']:
            error_present = "Error: Operator must be '+' or '-'."

#======= Error Case 3 =========

    for problem in problems:
        l = problem.split(' ')

        for i in l[0]:
            if i not in string.digits:
                error_present = "Error: Numbers must only contain digits."

        for i in l[2]:
            if i not in string.digits:
                error_present = "Error: Numbers must only contain digits."


#======= Error Case 4 =========

    for problem in problems:
        l = problem.split(' ')

        if len(l[0]) > 4 or len(l[2]) > 4:
            error_present = "Error: Numbers cannot be more than four digits."

    return error_present


def calculate_solution(problems):
    solutions = []

    for problem in problems:
        l = problem.split(' ')
        if l[1] == '+':
            solutions.append(str(int((l[0])) + int(l[2])))
        else:
            solutions.append(str(int((l[0])) - int(l[2])))

    return solutions
