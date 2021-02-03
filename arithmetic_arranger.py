def arithmetic_arranger(problems, **kwargs):
  if len(problems) >= 5:
    quit('Error: Too many problems.')
    
  tops = []
  bottoms = []
  lines = []
  solved = []

  for probs in problems:
    probs = ''.join(probs.split(' '))
    for prob in probs:
      # Addition Problems
      if prob == '+': 
        addprob = probs.split('+')

        # Quit program if its not only digits.
        if int(addprob[0]) is False:
          quit("Error: Numbers must only contain digits.")
        if int(addprob[1]) is False:
          quit("Error: Numbers must only contain digits.")
        # Quit program if too many digits.
        if len(addprob[0]) >= 5:
          quit("Error: Numbers cannot be more than four digits.")
        if len(addprob[1]) >= 5:
          quit("Error: Numbers cannot be more than four digits.")
        

        if len(addprob[0]) > len(addprob[1]):
          space = (2 + len(addprob[0]))
          tops.append((((2 * ' ') + addprob[0])))
          bottoms.append(('+' + (space - len(addprob[1]) - 1) * ' ' + addprob[1]))
          lines.append('-' * space)
          add = str(int(addprob[0]) - int(addprob[1]))
          solved.append((((space - len(add))) * ' ' + add))

        elif len(addprob[1]) > len(addprob[0]):
          space = (2 + len(addprob[1]))
          tops.append(((((space - len(addprob[0])) * ' ') + addprob[0])))
          bottoms.append(('+' + ' ' + addprob[1]))
          lines.append('-' * space)
          add = str(int(addprob[0]) - int(addprob[1]))
          solved.append((((space - len(add))) * ' ' + add))

        elif len(addprob[1]) == len(addprob[0]):
          space = (2 + len(addprob[1]))
          tops.append(((((2 * ' ') + addprob[0]))))
          bottoms.append(('+' + ' ' + addprob[1]))
          lines.append('-' * space)
          add = str(int(addprob[0]) - int(addprob[1]))
          solved.append((((space - len(add))) * ' ' + add))


      # Subtraction Problems
      if prob == '-':
        subprob = probs.split('-')

        # Quit program if its not only digits
        if int(subprob[0]) is False:
          quit("Error: Numbers must only contain digits.")
        if int(subprob[1]) is False:
          quit("Error: Numbers must only contain digits.")
        # Quit program if too many digits
        if len(subprob[0]) >= 5:
          quit("Error: Numbers cannot be more than four digits.")
        if len(subprob[1]) >= 5:
          quit("Error: Numbers cannot be more than four digits.")
        

        if len(subprob[0]) > len(subprob[1]):
          space = (2 + len(subprob[0]))
          tops.append((((2 * ' ') + subprob[0])))
          bottoms.append(('-' + (space - len(subprob[1]) - 1) * ' ' + subprob[1]))
          lines.append('-' * space)
          sub = str(int(subprob[0]) - int(subprob[1]))
          solved.append((((space - len(sub))) * ' ' + sub))

        elif len(subprob[1]) > len(subprob[0]):
          space = (2 + len(subprob[1]))
          tops.append(((((space - len(subprob[0])) * ' ') + subprob[0])))
          bottoms.append(('-' + ' ' + subprob[1]))
          lines.append('-' * space)
          sub = str(int(subprob[0]) - int(subprob[1]))
          solved.append((((space - len(sub))) * ' ' + sub))

        elif len(subprob[1]) == len(subprob[0]):
          space = (2 + len(subprob[1]))
          tops.append(((((2 * ' ') + subprob[0]))))
          bottoms.append(('-' + ' ' + subprob[1]))
          lines.append('-' * space)
          sub = str(int(subprob[0]) - int(subprob[1]))
          solved.append((((space - len(sub))) * ' ' + sub))


      # Quit program if using incorrect opperator.
      if prob == '/':
        quit("Error: Operator must be '+' or '-'.")
      if prob == '*':
        quit("Error: Operator must be '+' or '-'.")
      if prob == '**':
        quit("Error: Operator must be '+' or '-'.")


    if kwargs.get('solve', False):
        arranged_problems = str(tops)[1:-1].replace(",", " "*3).replace("'", "") + '\n' + str(bottoms)[1:-1].replace(",", " "*3).replace("'", "") + '\n' + str(lines)[1:-1].replace(",", " "*3).replace("'", "") + '\n' + str(solved)[1:-1].replace(",", " "*3).replace("'", "")
        
        arranged_problems = ''.join(arranged_problems)
    else:
        arranged_problems = str(tops)[1:-1].replace(",", " "*3).replace("'", "") + '\n' + str(bottoms)[1:-1].replace(",", " "*3).replace("'", "") + '\n' + str(lines)[1:-1].replace(",", " "*3).replace("'", "")

        arranged_problems = ''.join(arranged_problems)

  return arranged_problems
