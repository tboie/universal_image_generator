# -- coding: utf-8 --`
import argparse
import os
# engine
from stable_diffusion_engine import StableDiffusionEngine
# scheduler
from diffusers import LMSDiscreteScheduler, PNDMScheduler
# utils
import cv2
import numpy as np


def main(args):
    # using default values from demo_orig.py
    scheduler = PNDMScheduler(
        beta_start=0.00085,
        beta_end=0.012,
        beta_schedule="scaled_linear",
        skip_prk_steps=True,
        tensor_format="np"
    )
    engine = StableDiffusionEngine(
        model="bes-dev/stable-diffusion-v1-4-openvino",
        scheduler=scheduler,
        tokenizer="openai/clip-vit-large-patch14"
    )
    image = engine(
        prompt=args["prompt"],
        init_image=None,
        mask=None,
        strength=0.5,
        num_inference_steps=32,
        guidance_scale=7.5,
        eta=0.0
    )
    cv2.imwrite("output/output.png", image)


if __name__ == "__main__":
    main()
