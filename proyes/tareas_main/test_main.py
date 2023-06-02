from io import StringIO
from programa import veri_fecha, DIAS, MESES

def test_veri_fecha(monkeypatch, capsys):
    # Simulamos la entrada del usuario
    input_data = 'Lunes/12/Septiembre/2010\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_data))

    # Ejecutamos la función
    fecha, dia_n, dia, mes, anho, errores = veri_fecha()

    # Verificamos los resultados
    assert fecha == 'Lunes/12/Septiembre/2010'
    assert dia_n == 'Lunes'
    assert dia == 12
    assert mes == 'Septiembre'
    assert anho == 2010
    assert errores == 0

    # Verificamos que no se haya impreso nada en la salida de errores
    captured = capsys.readouterr()
    assert captured.out == ''