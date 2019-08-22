def print_shows(show_list):
  ordered = sorted(show_list, key = lambda x: x[2]+x[1], reverse = False)
  last = 0
  added = []
  for a in range(0,len(show_list)):
    end_time = ordered[a][1] + ordered[a][2]
    if ordered[a][1] >= last:
      added.append(ordered[a])
      print(f"{ordered[a][0]}, {ordered[a][1]}, {ordered[a][1]+ordered[a][2]}")
      last = ordered[a][1] + ordered[a][2]