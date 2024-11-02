from abc import ABC, abstractmethod

# 状態の基底クラス
class State(ABC):
    @abstractmethod
    def play(self, player):
        pass

    @abstractmethod
    def stop(self, player):
        pass

# 「再生中」状態のクラス
class PlayingState(State):
    def play(self, player):
        print("Already playing.")

    def stop(self, player):
        print("Stopping playback.")
        player.set_state(StoppedState())

# 「停止中」状態のクラス
class StoppedState(State):
    def play(self, player):
        print("Starting playback.")
        player.set_state(PlayingState())

    def stop(self, player):
        print("Already stopped.")

# 「一時停止中」状態のクラス
class PausedState(State):
    def play(self, player):
        print("Resuming playback.")
        player.set_state(PlayingState())

    def stop(self, player):
        print("Stopping playback from paused state.")
        player.set_state(StoppedState())

# コンテキストクラス：オーディオプレイヤー
class AudioPlayer:
    def __init__(self):
        self.state = StoppedState()  # 初期状態は停止中

    def set_state(self, state):
        self.state = state

    def play(self):
        self.state.play(self)

    def stop(self):
        self.state.stop(self)

# 使用例
player = AudioPlayer()

player.play()  # "Starting playback."
player.play()  # "Already playing."
player.stop()  # "Stopping playback."
player.stop()  # "Already stopped."
