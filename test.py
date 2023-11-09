# userInput = input("введите почту")


def is_valid_email(email):
  if email.count("@") == 1:
    username, domain = email.split("@")
    result1 = is_valid_username(username)
    result2 = is_valid_domain(domain)

    if result1 == True and result2 == True:
      return "Email is correct"
    else:
      return "error"


def is_valid_username(username):
  aсcepted_symphols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._"
  for symbol in aсcepted_symphols:
    if symbol not in username:
      return False
  if len(username) < 6 or len(username) > 36:
    return False


def is_valid_domain(domain):
  if domain.count(".") != 1:
    return False
  aсcepted_symphols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._"
  first_part, second_part = domain.split(".")
  for symbol in aсcepted_symphols:
    if symbol not in first_part:
      return False
  if len(first_part) < 6 or first_part > 36:
    return False

  if len(second_part) <= 2 or len(second_part) > 6:
    return False
  banned_symphols = "!@#$%^&*()_+[]{}|;:,.<>?`~ - 1234567890"
  for symbol in banned_symphols:
    if symbol in second_part:
      return False
  return True


test_emails = [
  "example_user@mail.com",  # Валидный email
  "user!name@domain.com",  # Невалидный email: недопустимые символы в имени пользователя
  "example_user@domain!.com",  # Невалидный email: недопустимые символы в домене
  "ex@ample_user@domain.com",  # Невалидный email: более одного символа @
  "example_user@domain",  # Невалидный email: отсутствует домен верхнего уровня
  "example_user@domain.toolongtld",  # Невалидный email: слишком длинный домен верхнего уровня
  "example_user@.com",  # Невалидный email: отсутствует первая часть домена
  "example_user@",  # Невалидный email: отсутствует домен
  "example_user@domain..com",  # Невалидный email: двойная точка в домене
  "example_user@domain.com.",  # Невалmail: домен не может заканчиваться на дефис
  "user@do..main.com",  # Невалиидный email: точка в конце домена
  ".example_user@domain.com",  # Невалидный email: точка в начале имени пользователя
  "user@domain.c",  # Невалидный email: домен верхнего уровня слишком короткий
  "user@-domain.com",  # Невалидный email: домен не может начинаться с дефиса
  "user@domain-.com",  # Невалидный eдный email: две точки подряд в домене
]
for test_email in test_emails:  
   print(f"Проверка {test_email}: {is_valid_email(test_email)}")
