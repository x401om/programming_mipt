<html lang="ru">
  <head>
    <meta charset="utf-8">
    <title>Домашнее задание 1</title>
    <style>
    body {
      color: black;
      font-family: serif;
      font-size: 12pt;
      line-height: 18pt;
      text-align: justify;
      hyphens: auto;
    }
    a {
      color: black;
      font-weight: normal;
      text-decoration: underline;
      text-decoration-style: dotted;
    }
    @media screen {
      body {
        color: #333333;
        font-family: sans-serif;;
        background-color: #dddddd;
        text-shadow: 0 0 1px rgba(0,0,0,0.3);
      }
      article {
        background-color: white;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 1cm;
        min-width: 3cm;
        max-width: 21cm;
        padding: 1cm;
        box-shadow: 2pt 2pt 2pt #888888;
      }
    }
    header { display: block; border-bottom: 1pt dotted black; padding-bottom: 18pt; margin-bottom: 18pt; }
    titlee, subtitle { display: block; text-align: center; hyphens: none; }
    titlee { font-weight: bold; }
    header titlee { font-size: 30pt; line-height: 36pt; margin-bottom: 18pt; }
    header subtitle { font-size: 12pt; }
    section titlee { text-transform: uppercase; margin-top: 36pt; }
    li { margin-top: 9pt; }
    </style>
  </head>
  <body>
    <article>
      <header>
        <titlee>Вычисление электронных таблиц с использованием формул</titlee>
        <subtitle>Домашнее задание №1</subtitle>
        <subtitle>Языки разработки ПО, 2016</subtitle>
      </header>
      <section>
        <titlee>1. Общие требования</titlee>
        <ol>
          <li>Программа должна быть реализована на языке программирования
            Python&nbsp;3.
            Допускается использование только стандартной библиотеки.
          </li>
          <li>
            Исходные тексты программы должны быть опубликованы в git-репозитории.
          </li>
          <li>
            Нормативный срок отправки решения - до <strong>10:00</strong> по московскому времени
            <strong>28 сентября 2016&nbsp;г.</strong>
          </li>
          <li>
            Устранение найденных преподавателем или ассистентом недостатков и
            ошибок в решении учитывается только в течении <strong>1 недели</strong>
            после нормативного срока.
          </li>
        </ol>
      </section>
      <section>
        <titlee>2. Постановка задачи</titlee>
        <p>Реализовать вычисление формул в электронных таблицах, с возможностью
        адресации ячеек как в старых версиях Excel (или Google Spreadsheets).
      </p>Должна быть предусмотрена и
        возможностью использования математических функций (модуль math стандартной
        библиотеки Python), а также произвольных
        функций, реализованных пользователем на языке Python.</p>
      </section>
      <section>
        <titlee>3. Форматы входных и выходных данных</titlee>
        <ol>
          <li>Входные и выходные данные - это <a target="_blank" href="https://ru.wikipedia.org/wiki/CSV">CSV-файл</a>.
          <li>Программа должна принимать в качестве аргументов командной строки
            имя входного файла первым параметром, и имя выходного файла вторым.
            Третий (опциональный) аргумент - имя файла Python-модуля.
          </li>
          <li>Количество столбцов - не более 26, количество строк - не более 256.
          </li>
          <li>Имена столбцов и номера строк не являются частью CSV-файлов. Столбцы
            именуются заглавными латинскими буквами, строки - десятичными числами.
          </li>
          <li>Вычисляемые значения начинаются с символа '=', после которого следует
          текст вычисляемого выражения.</li>
          <li>Значения некорректных выражений - это строки 'ERROR'.</li>
          <li>Рекурсивная адресация ячеек в выражениях не предполагается.</li>
        </ul>
      </section>
      <section>
        <titlee>4. Критерии оценивания</titlee>
        <p>Задание оценивается по вещественной шкале от 0 до 1.</p>
        <ul>
          <li><strong>0.4 балла</strong> - реализовано вычислений простых
            выражений с использованием констант.
          </li>
          <li><strong>0.5 балла</strong> - поддержка адресации существующих
          ячеек.</li>
          <li><strong>+0.1 балла</strong> - поддержка адресации ячеек, которые
          содержат формулы, а не значения.</li>
          <li><strong>0.6 балла</strong> - поддержка выполнения функций модуля math.</li>
          <li><strong>0.8 балла</strong> - поддержка выполнения пользовательских функций,
            реализованных во внешнем текстовом файле.</li>
          <li><strong>+0.1 балла</strong> - git-репозиторий не содержит мусора.</li>
          <li><strong>+0.1 балла</strong> - Программа не содержит ошибок, выявляемых
            анализаторами PyLint, PyFlakes и PEP-8.</li>
        </ul>
        <p>Штрафные санкции за превышение нормативного срока сдачи:</p>
        <ul>
          <li><strong>1 неделя</strong> - умножение на коэффициент 0.9</li>
          <li><strong>2 недели</strong> - умножение на коэффициент 0.7</li>
          <li><strong>Более 2-х недель</strong> - умножение на коэффициент 0.5</li>
        </ul>
      </section>
    </article>
  </body>
</html>
