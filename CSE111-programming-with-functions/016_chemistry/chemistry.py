def main():
  periodic_table = make_periodic_table()

  for line in periodic_table:
    element = line[1]
    mass = line[2]
    print(element, mass)
  

def make_periodic_table():
  lines = []
  with open ("data.txt","r") as raw_data:
    raw_lines = raw_data.readlines()
    for raw_line in raw_lines:
      raw_line = raw_line.replace('"', '').replace(",", "")
      line = raw_line.split()
      try:
        line = [line[0], line[1], float(line[2])]
      except:
        continue
      lines.append(line)
  return lines




if __name__ == "__main__":
  main()