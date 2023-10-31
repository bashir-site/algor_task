import json
from datetime import datetime

with open("data.json", "r") as file:
   data = json.load(file)

for id, data_set in data.items():
  entry_time = None
  exit_time = datetime.strptime("00:00:00", "%H:%M:%S").strftime('%H:%M:%S')
  id_comp = None
  cur_comp_id = data_set[0]['IDComp']
  first_iteration = True
  first_entry_time = None
  for item in data_set:
      if item['HozOrgan'] == 1311:
          entry_time = datetime.fromisoformat(item['TimeVal']).strftime('%H:%M:%S')

          if first_iteration:
              first_entry_time = entry_time
              first_iteration = False

          if cur_comp_id == item['IDComp']:
              print(entry_time, item['IDComp'], item['Mode'])
              if exit_time < entry_time:
                  exit_time = entry_time
          else:
              first_iteration = True
              print("---")
              if cur_comp_id == 1:
                  print("Успенка: ", first_entry_time , exit_time)
              elif cur_comp_id == 2:
                  print("Скоковая: ", first_entry_time , entry_time)
              elif cur_comp_id == 3:
                  print("Овчинка: ", first_entry_time , entry_time)
              elif cur_comp_id == 4:
                  print("Ростовский: ", first_entry_time , entry_time)
              elif cur_comp_id == 5:
                  print("Комсомольский 15: ", first_entry_time , entry_time)
              elif cur_comp_id == 6:
                  print("Арбат: ", first_entry_time , entry_time)
              elif cur_comp_id == 9:
                  print("Скоковая: ", first_entry_time , entry_time)

              first_entry_time = entry_time
              cur_comp_id = item['IDComp']