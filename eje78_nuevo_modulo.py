#insertar el paquete comprimir al path
#se necesita el archivo __init__.py 
#para que lo reconosca como un paquete
import sys
#tambien se puede poner en la carpeta lib donde esta instalado python
sys.path.append("C:\Todo\python\Mision TIC\ejercicios\comprimir")

from comprimir import aZip
from comprimir import aRar
from comprimir import aTar

aTar.crear_tar("archivo")
aRar.crear_rar("archivo")
aZip.crear_zip("archivo")