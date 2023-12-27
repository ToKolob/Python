import pytest
from datetime import datetime
from unittest.mock import MagicMock, patch
from pomodoro import display_history, calculate_today_focus, main

def create_file_to_test(timer):
  today = datetime.now().strftime("%Y-%m-%d")
  with open("test.txt", "w") as file:
    file.write(f"{today}      12:00:18      {timer}\n")
    file.write(f"{today}      12:00:18      {timer}\n")
    file.write(f"{today}      12:00:18      {timer}\n")

def test_display_history():
  text = MagicMock()
  display_history(text)
  text.delete.assert_called_once()
  text.insert.assert_called_once()

def test_calculate_today_focus_with_data():
  # create data to test with 3 rows with the same input
  create_file_to_test("00:05")
  today_focus = calculate_today_focus("test.txt")
  # 3 times 00:05 = 00:15
  assert today_focus == "00:00:15"

  create_file_to_test("05:00")
  today_focus = calculate_today_focus("test.txt")
  assert today_focus == "00:15:00"

  create_file_to_test("00:30")
  today_focus = calculate_today_focus("test.txt")
  assert today_focus == "00:01:30"

  create_file_to_test("00:30")
  today_focus = calculate_today_focus("test.txt")
  assert today_focus == "00:01:30"

  create_file_to_test("50:30")
  today_focus = calculate_today_focus("test.txt")
  assert today_focus == "02:31:30"

def test_calculate_today_focus_without_data():
  # create data and clear it to make a test
  with open("test.txt", "w") as file:

    file.write("")

  today_focus = calculate_today_focus("test.txt")

  assert today_focus == "00:00:00"

pytest.main(["-v", "--tb=line", "-rN", __file__])