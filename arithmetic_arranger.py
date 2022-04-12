def arithmetic_arranger(problems, answered = False):
    # Check there aren't too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Make a list of problems
    problems_list = []
    for problem in problems:
        problems_list.append(problem.split())

    # Iterate through the problems_list to make sure there are no errors
    for problem in problems_list:
        # Check operand
        if problem[1] != "+" and problem[1] != "-":
            return "Error: Operator must be '+' or '-'."

        # Check that the inputs are of the correct length
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Check that the inputs are all digits
        if problem[0].isdigit() != True or problem[2].isdigit() != True:
            return "Error: Numbers must only contain digits."

    # Make the blanks for the results to go in
    first = ""
    second = ""
    dashes = ""
    result = ""

    # Make the output
    for problem in problems_list:
        # figure out which is longest
        longest = max(len(problem[0]), len(problem[2]))
        # right aline first
        first += " " * (longest - len(problem[0]) + 2) + problem[0]
        # right aline second
        second += problem[1] + " " * (longest - len(problem[2]) + 1) + problem[2]
        # insert the correct amount of dashes
        dashes += "-" * (longest + 2)
        
        # answer if needed
        if answered:
            # calculate answer
            if problem[1] == "+":
                answer = int(problem[0]) + int(problem[2])
            else:
                answer = int(problem[0]) - int(problem[2])
            # right alone answer
            result += " " * (longest - len(str(answer)) + 2) + str(answer)

        # Space between        
        first += " " * 4
        second += " " * 4
        dashes += " " * 4
        result += " " * 4
    # remove extra space from last addition
    first = first[:len(first) -4]
    second = second[:len(second) -4]
    dashes = dashes[:len(dashes) -4]
    result = result[:len(result) -4]
    if answered:
        return first + "\n" + second + "\n" + dashes + "\n" + result
    else:
        return first + "\n" + second + "\n" + dashes