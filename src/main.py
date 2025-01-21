import sys
import os
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QLabel
from PyQt6.QtGui import QPixmap, QTransform
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QUrl
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.statusLabel.setText("GAME PLAYER!")

        self.enemy_ships = []

        # Связываем кнопки с событиями
        self.newGameButton.clicked.connect(self.new_game)
        self.surrenderButton.clicked.connect(self.surrender)
        self.enemy_shipsButton.clicked.connect(self.aussicht_enemy_ships)

    def new_game(self):
        """Начало новой игры"""
        self.newGameButton.setEnabled(False)
        self.statusLabel.setText("NEW GAME!")
        self.playerBoard_bild.setVisible(False)
        self.enemyBoard_bild.setVisible(False)
        self.playerBoard_bildLoser.setVisible(False)
        self.playerBoard_bildWinner.setVisible(False)
        self.enemyBoard_bildLoser.setVisible(False)
        self.enemyBoard_bildWinner.setVisible(False)

        # Очищаем старые элементы
        player_layout = self.playerBoard.layout()
        for i in reversed(range(player_layout.count())):
            item = player_layout.takeAt(i)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

        enemy_layout = self.enemyBoard.layout()
        for i in reversed(range(enemy_layout.count())):
            item = enemy_layout.takeAt(i)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

        player_layout.setContentsMargins(0, 0, 0, 0)
        player_layout.setSpacing(0)
        enemy_layout.setContentsMargins(0, 0, 0, 0)
        enemy_layout.setSpacing(0)

        for x in range(10):
            for y in range(10):
                # Поле игрока
                player_button = QPushButton("")
                player_button.setFixedSize(50, 50)
                player_button.setStyleSheet("""
                                QPushButton {
                                    background-color: rgb(10, 13, 30);
                                    border: 2px solid #1d3557;
                                    border-radius: 6px;
                                }
                                QPushButton:pressed {
                                    background-color: #144c72;
                                    border-radius: 6px;
                                    border: 2px solid #0f3c57;
                                }
                            """)
                player_layout.addWidget(player_button, x, y)

                # Поле противника
                enemy_button = QPushButton("")
                enemy_button.setFixedSize(50, 50)
                enemy_button.setStyleSheet(player_button.styleSheet())
                enemy_button.clicked.connect(self.handle_player_click)
                enemy_layout.addWidget(enemy_button, x, y)

        self.player_ships = self.generate_ships()
        self.enemy_ships = self.generate_ships()

        self.place_ships_on_board(player_layout, self.player_ships)

        self.playerBoard.layout().update()
        self.enemyBoard.layout().update()

        self.player_turn = True

    def generate_ships(self):
        ships = []
        ship_lengths = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        for length in ship_lengths:
            while True:
                start_x = random.randint(0, 9)
                start_y = random.randint(0, 9)
                direction = random.choice(["horizontal", "vertical"])
                if direction == "horizontal":
                    if start_x + length > 10:
                        continue
                else:
                    if start_y + length > 10:
                        continue

                new_ship = []
                for i in range(length):
                    if direction == "horizontal":
                        new_ship.append((start_x + i, start_y))
                    else:
                        new_ship.append((start_x, start_y + i))

                if self.is_valid_ship(ships, new_ship):
                    ships.append(new_ship)
                    break

        return ships

    def is_valid_ship(self, ships, new_ship):
        """
        Проверяет, можно ли разместить корабль, чтобы он не пересекался
        и не находился слишком близко к другим кораблям.
        """
        for x, y in new_ship:
            for ship in ships:
                for sx, sy in ship:
                    if abs(x - sx) <= 1 and abs(y - sy) <= 1:
                        return False
        return True

    def place_ships_on_board(self, board_layout, ships):
        """
        Размещает корабли на игровом поле.
        """
        # Применяем длины корабля к соответствующему изображению
        ship_images = {
            1: "/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/paluba1.png",
            2: "/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/paluba2.png",
            3: "/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/paluba3.png",
            4: "/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/paluba4.png"
        }

        for ship in ships:
            ship_length = len(ship)
            if ship_length not in ship_images:
                continue

            ship_image_path = ship_images[ship_length]
            pixmap = QPixmap(ship_image_path)
            if pixmap.isNull():
                continue

            # Определяем ориентацию корабля
            start_x, start_y = ship[0]
            horizontal = ship[0][1] != ship[-1][1]

            # Если корабль горизонтальный, поворачиваем изображение
            if horizontal:
                transform = QTransform()
                transform.rotate(90)
                pixmap = pixmap.transformed(transform)

            # Создаём QLabel для изображения корабля
            label = QLabel(self)
            label.setPixmap(pixmap)
            label.setScaledContents(True)  # Масштабирование изображения под QLabel

            if horizontal:
                label.setFixedSize(50 * ship_length, 50)
            else:
                label.setFixedSize(50, 50 * ship_length)

            board_layout.addWidget(label, start_x, start_y, 1 if horizontal else ship_length,
                                   ship_length if horizontal else 1)

            label.setStyleSheet("background: transparent;")
            label.lower()
            label.show()

            # Делаем кнопки кораблей визуально прозрачными
            for x, y in ship:
                button = board_layout.itemAtPosition(x, y).widget()
                if button is None:
                    continue

                button.setStyleSheet("""
                    QPushButton {
                        background-color: transparent;
                        border: none;
                    }
                    QPushButton:pressed {
                        background-color: rgba(255, 255, 255, 10);
                    }
                """)

    def is_ship_destroyed(self, ship, layout):
        """
        Проверяет, полностью ли уничтожен данный корабль. Если да, то накладывает на кнопки изображение взрыва,
        а под кнопки — изображение корабля.
        """
        destroyed = True

        # Проверяем состояние кнопок, соответствующих координатам корабля
        for x, y in ship:
            button = layout.itemAtPosition(x, y)
            if button is not None:
                button = button.widget()
                if button and button.isEnabled():
                    destroyed = False

        # Если корабль уничтожен
        if destroyed:
            ship_length = len(ship)
            ship_images = {
                1: "/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/paluba1.png",
                2: "/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/paluba2.png",
                3: "/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/paluba3.png",
                4: "/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/paluba4.png",
            }

            if ship_length not in ship_images:
                return False

            ship_image_path = ship_images[ship_length]
            pixmap = QPixmap(ship_image_path)
            if pixmap.isNull():
                return False

            # Определяем ориентацию корабля
            horizontal = ship[0][1] != ship[-1][1]

            if horizontal:
                transform = QTransform().rotate(90)
                pixmap = pixmap.transformed(transform)

            label = QLabel(self)
            label.setPixmap(pixmap)
            label.setScaledContents(True)

            # Настройка размеров для QLabel
            if horizontal:
                label.setFixedSize(50 * ship_length, 50)
            else:
                label.setFixedSize(50, 50 * ship_length)

            # Опускаем изображение корабля на слой под кнопки
            start_x, start_y = ship[0]
            layout.addWidget(label, start_x, start_y, 1 if horizontal else ship_length,
                             ship_length if horizontal else 1)
            label.lower()
            label.show()

            # Меняем стиль кнопок корабля на взрыв
            for x, y in ship:
                button = layout.itemAtPosition(x, y).widget()
                if button is not None:
                    button.setStyleSheet("""
                        QPushButton {
                            background-color: transparent;
                            border-image: url(/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/explosion.png);
                            border: 0px;
                        }
                    """)
                    button.setEnabled(False)  # Отключаем кнопку

        return destroyed

    def mark_surrounding_area(self, ship, layout):
        """
        Помечает все клетки вокруг корабля, включая диагонали.
        :param ship: Координаты корабля в виде списка [(x1, y1), (x2, y2), ...].
        :param layout: Компоновка (QGridLayout) с кнопками игрового поля.
        """
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        for x, y in ship:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Проверяем, что координаты находятся в пределах игрового поля
                if 0 <= nx < 10 and 0 <= ny < 10:
                    # Пропускаем клетки, которые являются частью самого корабля
                    if (nx, ny) in ship:
                        continue

                    # Получаем кнопку из layout
                    button = layout.itemAtPosition(nx, ny)
                    if button is not None:
                        button = button.widget()
                        if button and button.isEnabled():
                            button.setStyleSheet("""
                                QPushButton {
                                    border-image: url(/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/killer.png);
                                    border: 2px solid #333;
                                    border-radius: 6px;
                                }
                            """)
                            button.setEnabled(False)

    def handle_player_click(self):
        """Обработка кликов игрока на поле противника."""
        if not hasattr(self, "player_turn") or not self.player_turn:
            return  # Игрок не может ходить, если не его очередь

        button = self.sender()
        layout = self.enemyBoard.layout()

        clicked_coordinates = None
        for x in range(10):
            for y in range(10):
                if layout.itemAtPosition(x, y).widget() == button:
                    clicked_coordinates = (x, y)
                    break
            if clicked_coordinates:
                break
        if not clicked_coordinates:
            return

        # Определяем, произошло попадание или промах
        hit = any(clicked_coordinates in ship for ship in self.enemy_ships)

        if hit:
            # Попадание
            button.setStyleSheet("""
                            QPushButton {
                                background: transparent;
                                border-image: url(/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/explosion.png);
                                border: 2px solid black;
                                border-radius: 6px;
                            }
                        """)

            button.setEnabled(False)
            self.statusLabel.setText("HIT! SHOOT AGAIN.")

            # Проверяем, уничтожен ли корабль
            for ship in self.enemy_ships:
                if clicked_coordinates in ship:  # Попали по текущему кораблю
                    if self.is_ship_destroyed(ship, layout):  # Проверяем, уничтожен ли корабль
                        self.mark_surrounding_area(ship, layout)  # Помечаем клетки вокруг уничтоженного корабля
                        self.enemy_ships.remove(ship)  # Удаляем корабль из списка
                        self.statusLabel.setText("ENEMY SHIP DESTROYED! SHOOT AGAIN.")
                        break

        else:
            # Промах
            button.setStyleSheet("""
                            QPushButton {
                                background-color: transparent;
                                border-image: url(/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/mina.png);
                                border: 2px solid black;
                                border-radius: 6px;
                            }
                        """)
            self.statusLabel.setText("MISS! ENEMY'S TURN..")
            self.player_turn = False  # Передача хода компьютеру
            self.enemy_turn()

            button.setEnabled(False)

        self.check_game_over()

    def enemy_turn(self):
        """Интеллектуальный ход компьютера: фокус добивания корабля перед переходом к новому."""
        self.statusLabel.setText("ENEMY IS THINKING...")
        layout = self.playerBoard.layout()

        # Инициализация клетки для обстрела
        if not hasattr(self, "enemy_target_ship"):
            self.enemy_target_ship = None
            self.enemy_shoot_direction = None

        if self.enemy_target_ship and len(self.enemy_target_ship) > 0:
            x, y = self.enemy_target_ship.pop(0)
        else:
            # Если нет цели — выбираем случайную клетку
            available_moves = []
            for i in range(10):
                for j in range(10):
                    button = layout.itemAtPosition(i, j).widget()
                    if button and button.isEnabled():
                        available_moves.append((i, j))

            if len(available_moves) == 0:
                self.statusLabel.setText("ENEMY HAS NO MOVES LEFT!")
                return

            x, y = random.choice(available_moves)

        button = layout.itemAtPosition(x, y).widget()
        if not button or not button.isEnabled():
            self.enemy_turn()
            return

        # Проверяем попадание
        hit = any((x, y) in ship for ship in self.player_ships)

        if hit:
            # Попали в корабль
            button.setStyleSheet("""
                            QPushButton {
                                background: transparent;
                                border-image: url(/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/explosion.png);
                                border: 0px;
                            }
                        """)
            button.setEnabled(False)
            self.statusLabel.setText("ENEMY HIT! ENEMY SHOOTS AGAIN.")

            # Добавляем новые цели в фокус
            if not self.enemy_target_ship:
                self.enemy_target_ship = []

            # Добавляем соседние клетки для удара
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 10 and 0 <= ny < 10:
                    neighbor_button = layout.itemAtPosition(nx, ny).widget()
                    if neighbor_button and neighbor_button.isEnabled():
                        self.enemy_target_ship.append((nx, ny))

            # Проверяем, уничтожен ли корабль
            for ship in self.player_ships:
                if (x, y) in ship:
                    if self.is_ship_destroyed(ship, layout):
                        self.mark_surrounding_area(ship, layout)
                        self.player_ships.remove(ship)

                        self.enemy_target_ship = None
                        self.enemy_shoot_direction = None
                        self.statusLabel.setText("ENEMY DESTROYED YOUR SHIP!")
                    break

            # Если не уничтожен, продолжаем атаку
            self.enemy_turn()
        else:
            # Промах
            button.setStyleSheet("""
                            QPushButton {
                                background-color: transparent;
                                border-image: url(/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/mina.png);
                                border: 2px solid black;
                            }
                        """)
            button.setEnabled(False)

            if self.enemy_target_ship:
                self.enemy_turn()
            else:
                self.statusLabel.setText("ENEMY MISSED! YOUR TURN.")
                self.player_turn = True

    def check_game_over(self):
        """Проверяет, завершилась ли игра."""
        # Проверяем у противника оставшиеся корабли
        enemy_has_ships = any(
            any((x, y) for (x, y) in ship if self.enemyBoard.layout().itemAtPosition(x, y).widget().isEnabled())
            for ship in self.enemy_ships
        )

        # Проверяем у игрока оставшиеся корабли
        player_has_ships = any(
            any((x, y) for (x, y) in ship if self.playerBoard.layout().itemAtPosition(x, y).widget().isEnabled())
            for ship in self.player_ships
        )

        if not enemy_has_ships:
            # Если у противника не осталось активных кораблей - игрок выиграл
            self.statusLabel.setText("YOU WIN!")
            self.enemyBoard_bildLoser.setVisible(True)
            self.playerBoard_bildWinner.setVisible(True)
            self.newGameButton.setEnabled(True)
            return True  # Игра завершена

        if not player_has_ships:
            # Если у игрока не осталось активных кораблей - он проиграл
            self.statusLabel.setText("YOU LOSE!")
            self.playerBoard_bildLoser.setVisible(True)
            self.enemyBoard_bildWinner.setVisible(True)
            self.newGameButton.setEnabled(True)
            return True  # Игра завершена

        return False  # Игра ещё не окончена

    def surrender(self):
        """Сдача"""
        self.statusLabel.setText("YOU GAVE UP AND LOST!")
        self.playerBoard_bildLoser.setVisible(True)
        self.enemyBoard_bildWinner.setVisible(True)
        self.newGameButton.setEnabled(True)

    def aussicht_enemy_ships(self):
        """Отображает или скрывает корабли противника на поле при нажатии кнопки."""
        enemy_layout = self.enemyBoard.layout()

        # Если функция вызывается впервые, добавляем атрибут состояния
        if not hasattr(self, "_enemy_ships_visible"):
            self._enemy_ships_visible = False

        # Логика отображения/скрытия кораблей
        if self._enemy_ships_visible:
            # Скрыть корабли
            for ship in self.enemy_ships:
                for x, y in ship:
                    button = enemy_layout.itemAtPosition(x, y).widget()
                    if button:
                        button.setStyleSheet("""
                            QPushButton {
                                background-color: rgb(10, 13, 30);  /* Цвет пустой клетки */
                                border: 2px solid #1d3557;
                                border-radius: 6px;
                            }
                        """)
            self._enemy_ships_visible = False  # Изменяем состояние на "скрыто"
        else:
            # Показать корабли
            for ship in self.enemy_ships:
                for x, y in ship:
                    button = enemy_layout.itemAtPosition(x, y).widget()
                    if button:
                        # Устанавливаем стиль кнопки, чтобы она отображала корабль
                        button.setStyleSheet("""
                            QPushButton {
                                background; transparent
                                border: 2px solid #264653;
                                border-radius: 6px;
                            }
                        """)
            self._enemy_ships_visible = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
