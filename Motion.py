import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

square_pos = pygame.Rect(295, 192, 50, 50)

circle_pos = pygame.Vector2(150, 150)
circle_spd = pygame.Vector2()
circle_rad = 20
circle_acc = 0.01
circle_spd_mul = 0.99
bounce_str = 1.0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        square_pos.y -= 20
    if keys[pygame.K_DOWN]:
        square_pos.y += 20
    if keys[pygame.K_LEFT]:
        square_pos.x -= 20
    if keys[pygame.K_RIGHT]:
        square_pos.x += 20

    # Slow down over time
    circle_spd *= circle_spd_mul

    # Move toward mouse
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    circle_spd += (mouse_pos - circle_pos) * circle_acc

    # Update position
    circle_pos += circle_spd

    # Bounce off walls
    if circle_pos.x < circle_rad:
        circle_pos.x = circle_rad
        circle_spd.x *= -bounce_str

    elif circle_pos.x > screen.get_width() - circle_rad:
        circle_pos.x = screen.get_width() - circle_rad
        circle_spd.x *= -bounce_str

    if circle_pos.y < circle_rad:
        circle_pos.y = circle_rad
        circle_spd.y *= -bounce_str

    elif circle_pos.y > screen.get_height() - circle_rad:
        circle_pos.y = screen.get_height() - circle_rad
        circle_spd.y *= -bounce_str

    screen.fill("black")

    pygame.draw.circle(screen, "blue", circle_pos, circle_rad)
    pygame.draw.rect(screen, "red", square_pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()