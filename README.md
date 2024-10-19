Перейти в директорию с проектом, ввести команду docker build -t my_python_app .
После сборки команду docker run -d -p 8000:8000 --name my_running_app my_python_app

