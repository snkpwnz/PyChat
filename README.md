# PyChat

При разработке учебного проекта использовал такие паттерны проектирования:

- Singletone (так как нам нужно одно соединение с базой данных на протяжении всего жизненного цикла приложения.)
- Factory method (определяет общий интерфейс для создания объектов, позволяет выбирать нужную реализацию во время выполнения программы)
- Adapter (в текущем решении позволяет преобразовать ответ в формате JSON в нужное значение)

Команды пользователя:
/help - вызвать меню помощи
/dollar - узнать текущий курс доллара
/play {game_name} (simple, roulette) - запустить мини-игру
