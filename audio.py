import pyaudio
import numpy as np

class Audio:
    def __init__(self, rate=16000, chunk=2048, threshold=800, silence_limit=3):
        """
        Initialize the AudioRecorder class.

        Args:
            rate (int): Sample rate for audio recording (default: 16000).
            chunk (int): Buffer size for audio recording (default: 2048).
            threshold (int): Threshold for detecting silence in audio data (default: 800).
            silence_limit (int): Number of seconds of silence before stopping recording (default: 3).
        """
        self.RATE = rate
        self.CHUNK = chunk
        self.THRESHOLD = threshold
        self.SILENCE_LIMIT = silence_limit
        self.pa = pyaudio.PyAudio()
        self.input_stream = None

    def initialize_input_stream(self):
        """
        Initialize the input audio stream for recording.
        """
        self.input_stream = self.pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK,
        )

    def record_audio(self):
        """
        Record audio from the microphone and return it as a normalized float32 numpy array.

        Returns:
            np.ndarray: Recorded audio as a float32 numpy array, normalized to the range [-1, 1].
        """
        print("Recording...")
        frames = []
        silent_frames = 0
        recording = True

        self.initialize_input_stream()

        while recording:
            data = self.input_stream.read(self.CHUNK, exception_on_overflow=False)
            frames.append(data)

            # Convert audio data to numpy array for silence detection
            audio_data = np.frombuffer(data, dtype=np.int16)
            if self.is_silent(audio_data):
                silent_frames += 1
            else:
                silent_frames = 0

            # Stop recording if silence limit is reached
            if silent_frames > self.RATE / self.CHUNK * self.SILENCE_LIMIT:
                recording = False

        self.input_stream.stop_stream()
        self.input_stream.close()

        # Combine frames into a single numpy array
        audio_data = np.frombuffer(b"".join(frames), dtype=np.int16)

        # Convert to float32 and normalize to the range [-1, 1]
        audio_data = audio_data.astype(np.float32) / 32768.0

        print("Recording finished.")
        return audio_data

    def is_silent(self, audio_data):
        """
        Detect silence in audio data.

        Args:
            audio_data (numpy.ndarray): Audio data as a numpy array.

        Returns:
            bool: True if the audio data is silent, False otherwise.
        """
        return np.max(audio_data) < self.THRESHOLD

    def close(self):
        """
        Close the PyAudio instance.
        """
        self.pa.terminate()
