import turtle

def koch_snowflake(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(order-1, size/3)
            turtle.left(angle)

def main():
    # Налаштування вікна та черепахи
    turtle.setup(800, 600)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-300, 150)
    turtle.pendown()
    turtle.color("blue")

    # Отримання рівня рекурсії від користувача
    order = int(input("Введіть рівень рекурсії для сніжинки Коха: "))

    # Малювання трьох сторін сніжинки
    for _ in range(3):
        koch_snowflake(order, 400)
        turtle.right(120)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()