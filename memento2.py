class GameState:
    def __init__(self, level: int, lives: int, score: int):
        self.level = level
        self.lives = lives
        self.score = score

    def __str__(self):
        return f"Level: {self.level}, Lives: {self.lives}, Score: {self.score}"


class Game:
    def __init__(self):
        self.current_state = GameState(1, 3, 0)
        self.history = []

    def play(self):
        # ゲームのプレイ中に状態を変更する
        self.current_state.score += 10
        print(f"Playing... {self.current_state}")

    def save(self):
        # 現在の状態を保存
        self.history.append(Memento(self.current_state))
        print("Game saved.")

    def load(self):
        if self.history:
            # 最後のセーブデータを読み込む
            memento = self.history.pop()
            self.current_state = memento.get_state()
            print(f"Game loaded: {self.current_state}")
        else:
            print("No saved game to load.")

    def get_current_state(self) -> GameState:
        return self.current_state


class Memento:
    def __init__(self, state: GameState):
        # ゲームの状態を保存
        self._state = GameState(state.level, state.lives, state.score)

    def get_state(self) -> GameState:
        return self._state


# 使用例
game = Game()
game.play()  # ゲームプレイ中
game.save()  # 現在の状態を保存
game.play()  # ゲームプレイ中
game.save()  # 現在の状態を保存
game.load()  # 最後のセーブデータを読み込む
