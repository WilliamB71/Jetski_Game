import pygame


def image_resize(img, scale):
    new_dimension = round(
        img.get_width() * scale), round(img.get_height() * scale)
    return pygame.transform.scale(img, new_dimension)


def center_rotate_image(surface, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    surface.blit(rotated_image, new_rect.topleft)


def rotated_image_mask(image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    center = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    mask = pygame.mask.from_surface(rotated_image)
    return mask, center


def score_update_display(surface, clock, score):
    score_font = pygame.font.Font('freesansbold.ttf', 24)
    score_display = score_font.render(
        'Level: ' + str(int(score/20 + 1)) + '   Score: ' + str(int(score)), True, (255, 255, 255))
    score_rect = score_display.get_rect()
    score_rect.x = 230
    score_rect.y = 7
    surface.blit(score_display, score_rect)
    score += clock.get_time() / 2000
    return score
