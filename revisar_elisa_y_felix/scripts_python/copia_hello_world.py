from datetime import datetime

fecha_hora_actual = datetime.now().strftime("d%-m%-Y% %H:%m:%S")

with open('/workspaces/exercise-terminal-challenge/revisar_elisa_y_felix/scripts_python/resultado/test.txt', 'a')as archivo:
	archivo.write(f'Tarea finalizada a las {fecha_hora_actual}')
