import torch
from transformers import pipeline
from transformers.utils import is_flash_attn_2_available
import time


pipe = pipeline(
    "automatic-speech-recognition",
    model="distil-whisper/distil-medium.en",  # select checkpoint from https://huggingface.co/openai/whisper-large-v3#model-details
    torch_dtype=torch.float16,
    device="mps",  # or mps for Mac devices
    model_kwargs=(
        {"attn_implementation": "flash_attention_2"}
        if is_flash_attn_2_available()
        else {"attn_implementation": "sdpa"}
    ),
)


start = time.time()

outputs = pipe(
    "yes.mp3",
    chunk_length_s=30,
    batch_size=24,
    return_timestamps=False,
)
print(time.time() - start)
print(outputs)
