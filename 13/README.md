Задание про адресацию (ip адреса)

ip адрес - уникальный номер устройства, который подключен к интернету
Его, как правило, нам дает провайдер (и у него тоже есть свой адрес - адрес сети)

Пусть есть ip адрес сети:
192.168.16.0

Какие адреса могут быть назначены компьютерам?

Здесь предстоит перевести адрес в двоичную с.с. ( в python через bin(число) )
ip адрес сети: 11000000.10101000.00010000.00000000

Введем такое определение, как маска сети. Она позволит разделить адрес сети от адресов устройств
Например 255.255.240.0, также переведем в двоичную с.с.
маска: 11111111.11111111.11110000.00000000

Как происходит разделение? В месте, где начинаются нули у маски проведем черту
ip адрес сети: 11000000.10101000.0001|0000.00000000
маска:         11111111.11111111.1111|0000.00000000

Все комбинации в адресе сети после черты - возможные ip адреса
(количество адресов в сети - 2**'количество нулей')

Как по адресу компьютера получить адрес сети?
Ответ: применив операцию конъюнкции к каждому числу ip адреса и маски (&)

ip адрес компьютера: 192.168.32.0
маска:               255.255.240.0

ip адрес сети:       192.168.16.0

