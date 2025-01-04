QSS = '''
QWidget#mainWindow {
    background-color: #400106;  /* Задаємо фон для головного вікна */
}

QWidget {
    font: 20px "Montserrat";  /* Встановлюємо шрифт для всіх віджетів */
}

QPushButton { 
    background-color: #01261C;  /* Задаємо фон для кнопки */
    color: white;  /* Колір тексту на кнопці */
}

QPushButton:pressed {
    background-color: #9e93fc;  /* Задаємо фон кнопки, коли вона натиснута */
}

QListWidget {
    background-color: #01402E;  /* Задаємо фон для списку */
}

QListWidget::item:selected {
    background-color: #73020C;  /* Задаємо фон для вибраного елемента списку */
}
'''
