import unittest
from unittest.mock import patch
from io import StringIO
import hola_mundo
import datetime

class TestHolaMundo(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_hello_world(self, mock_stdout):
        hola_mundo.print_hello_world()
        self.assertEqual(mock_stdout.getvalue().strip(), "Hola, Mundo!")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('random.shuffle')
    def test_play_russian_roulette_loss(self, mock_shuffle, mock_stdout):
        mock_shuffle.side_effect = lambda x: x.insert(0, x.pop())
        hola_mundo.play_russian_roulette()
        self.assertEqual(mock_stdout.getvalue().strip(), "¡Bang! Has perdido.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('random.shuffle')
    def test_play_russian_roulette_survive(self, mock_shuffle, mock_stdout):
        mock_shuffle.side_effect = lambda x: x
        hola_mundo.play_russian_roulette()
        self.assertEqual(mock_stdout.getvalue().strip(), "Clic. Has sobrevivido.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['0'])
    @patch('random.randint', return_value=0)
    def test_play_rock_paper_scissors(self, mock_randint, mock_input, mock_stdout):
        hola_mundo.play_rock_paper_scissors()
        self.assertIn("Empate! Ambos sacan piedra", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['3'])
    def test_play_rock_paper_scissors_invalid(self, mock_input, mock_stdout):
        hola_mundo.play_rock_paper_scissors()
        self.assertIn("Opción no válida, por favor escoge una de las tres posibles.", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('hola_mundo.datetime')
    def test_show_actual_datetime(self, mock_datetime, mock_stdout):
        mock_datetime.datetime.now.return_value = datetime.datetime(2023, 1, 1, 12, 0, 0)
        hola_mundo.show_actual_datetime()
        self.assertEqual(mock_stdout.getvalue().strip(), "Ahora son las 12:00:00 del 01/01/2023")

if __name__ == "__main__":
    unittest.main()
