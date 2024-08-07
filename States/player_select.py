import pygame
from .base import State

class PlayerSelect(State):
    def __init__(self):
        super(PlayerSelect, self).__init__()
        self.player_count = 1
        self.next_state = "GAMEPLAY"
        self.font = pygame.font.Font(None, 50)
        self.screen_rect = pygame.display.get_surface().get_rect()

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if self.increase_rect.collidepoint(mouse_pos):
                self.player_count += 1
            elif self.decrease_rect.collidepoint(mouse_pos):
                self.player_count = max(1, self.player_count - 1)
            elif self.confirm_rect.collidepoint(mouse_pos):
                self.done = True

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        text = self.font.render(f"Player Count: {self.player_count}", True, pygame.Color("white"))
        self.text_rect = text.get_rect(center=self.screen_rect.center)
        surface.blit(text, self.text_rect)

        increase_text = self.font.render("+", True, pygame.Color("green"))
        self.increase_rect = increase_text.get_rect(center=(self.screen_rect.centerx + 200, self.screen_rect.centery))
        surface.blit(increase_text, self.increase_rect)

        decrease_text = self.font.render("-", True, pygame.Color("red"))
        self.decrease_rect = decrease_text.get_rect(center=(self.screen_rect.centerx - 200, self.screen_rect.centery))
        surface.blit(decrease_text, self.decrease_rect)

        confirm_text = self.font.render("Confirm", True, pygame.Color("blue"))
        self.confirm_rect = confirm_text.get_rect(center=(self.screen_rect.centerx, self.screen_rect.centery + 100))
        surface.blit(confirm_text, self.confirm_rect)

    def cleanup(self):
        self.persist['player_count'] = self.player_count
        return super(PlayerSelect, self).cleanup()
