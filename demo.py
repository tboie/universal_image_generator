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
    # NOTE: these args not being used
    parser = argparse.ArgumentParser()
    # pipeline configure
    parser.add_argument(
        "--model", type=str, default="bes-dev/stable-diffusion-v1-4-openvino", help="model name")
    # randomizer params
    parser.add_argument("--seed", type=int, default=None,
                        help="random seed for generating consistent images per prompt")
    # scheduler params
    parser.add_argument("--beta-start", type=float,
                        default=0.00085, help="LMSDiscreteScheduler::beta_start")
    parser.add_argument("--beta-end", type=float, default=0.012,
                        help="LMSDiscreteScheduler::beta_end")
    parser.add_argument("--beta-schedule", type=str, default="scaled_linear",
                        help="LMSDiscreteScheduler::beta_schedule")
    # diffusion params
    parser.add_argument("--num-inference-steps", type=int,
                        default=32, help="num inference steps")
    parser.add_argument("--guidance-scale", type=float,
                        default=7.5, help="guidance scale")
    parser.add_argument("--eta", type=float, default=0.0, help="eta")
    # tokenizer
    parser.add_argument("--tokenizer", type=str,
                        default="openai/clip-vit-large-patch14", help="tokenizer")
    # prompt
    parser.add_argument(
        "--prompt", type=str, default="Street-art painting of Emilia Clarke in style of Banksy, photorealism", help="prompt")
    # img2img params
    parser.add_argument("--init-image", type=str,
                        default=None, help="path to initial image")
    parser.add_argument("--strength", type=float, default=0.5,
                        help="how strong the initial image should be noised [0.0, 1.0]")
    # inpainting
    parser.add_argument("--mask", type=str, default=None,
                        help="mask of the region to inpaint on the initial image")
    # output name
    parser.add_argument("--output", type=str,
                        default="output.png", help="output image name")
    args = parser.parse_args()
    main(args)
