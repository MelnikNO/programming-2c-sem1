import os
import pytest
from LR6_1 import write_log
from LR1_3_1 import calculate

def test_write_log_success():
    file_name = "test_log.txt"
    try:
        write_log(1, 2, action="test", result=3, file=file_name)
        with open(file_name, "r") as f:
            content = f.read()
        assert "test: (1, 2) = 3" in content
    finally:
        if os.path.exists(file_name):
           os.remove(file_name)


def test_write_log_permission_error():
    file_name = "/test_log.txt"
    with pytest.raises(Exception) as e:
      write_log(1, 2, action="test", result=3, file=file_name)
    assert "Ошибка записи в файл /test_log.txt. Записать не удалось." in str(e.value)
    assert not os.path.exists(file_name)

    if os.path.exists(file_name + '.txt'):
        os.remove(file_name + '.txt')

def test_write_log_file_readonly():
    file_name = "readonly.txt"
    try:
      with open(file_name, "w") as f:
        f.write("Это тест")
      os.chmod(file_name, 0o444)
      with pytest.raises(Exception) as e:
         write_log(1,2, action="test", result=3, file=file_name)
      assert f'Ошибка записи в файл {file_name}. Записать не удалось.' in str(e.value)
      assert os.path.exists(file_name + '.txt')
    finally:
        os.chmod(file_name, 0o666)
        if os.path.exists(file_name):
           os.remove(file_name)
        if os.path.exists(file_name + '.txt'):
           os.remove(file_name + '.txt')