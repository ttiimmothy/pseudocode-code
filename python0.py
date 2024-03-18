def read_input(file_path):
  with open(file_path, 'r') as file:
    lines = [line.strip().split() for line in file]
  return lines


def construct_pyramid(lines):
  pyramid = []
  current_number = 1
  numbers_count = 1

  while current_number + numbers_count <= len(lines):
    word = []
    for i in range(current_number, current_number + numbers_count):
      for j in lines:
        if int(j[0]) == i:
          word.append(j)
    pyramid.append(word)
    current_number += numbers_count
    numbers_count += 1

  return pyramid


def decode_message(pyramid):
  message = []
  for level in pyramid:
    message.append(level[-1][-1])
  return ' '.join(message)


# Replace with the actual path to your input file
file_path = 'data/coding_qual_input.txt'
lines = read_input(file_path)
# print(lines)
pyramid = construct_pyramid(lines)

for i in pyramid:
  print(i)

decoded_message = decode_message(pyramid)
print(decoded_message)
