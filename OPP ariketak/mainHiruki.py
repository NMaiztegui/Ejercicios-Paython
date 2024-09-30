import hirukiak
print('Hiruki bat goaz sortzera, horretarako hiru aldeen balikoa sartu behr dira')
a_aldea=float(input('Sartu a aldearen balioa\n'))
b_aldea=float(input('Sartu b aldearen balioa\n'))
c_aldea=float(input('Sartu c aldearen balioa\n'))

try:
    trinagulo =hirukiak.Hirukia(a_aldea,b_aldea,c_aldea)
   
except Exception as e:
     print("Ocurrió un error: ", e)

trinagulo.aldeHandiena()
trinagulo.hiruki_mota()