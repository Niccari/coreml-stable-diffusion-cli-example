from huggingface_hub import snapshot_download
from huggingface_hub.file_download import repo_folder_name
from pathlib import Path
import shutil

# https://huggingface.co/blog/diffusers-coreml


def download_model(repo_id, variant, output_dir):
    destination = Path(output_dir) / (repo_id.split("/")[-1] + "_" + variant.replace("/", "_"))
    if destination.exists():
        raise FileExistsError(f"Model already exists at {destination}")
    
    downloaded = snapshot_download(
        repo_id, allow_patterns=f"{variant}/*", cache_dir=output_dir
    )
    downloaded_bundle = Path(downloaded) / variant
    shutil.copytree(downloaded_bundle, destination)

    cache_folder = Path(output_dir) / repo_folder_name(repo_id=repo_id, repo_type="model")
    shutil.rmtree(cache_folder)
    return destination


def to_version(input_text: str):
    if input_text == "3":
        return "apple/coreml-stable-diffusion-2-base"
    elif input_text == "2":
        return "apple/coreml-stable-diffusion-v1-5"
    else:
        return "apple/coreml-stable-diffusion-v1-4"


if __name__ == "__main__":
    print("Note: you must log in to Hugging face hub.")
    input_text = input(
        "Model version? - [1,*] v1.4, [2] v1.5, [3] v2.0 > ")
    repo_id = to_version(input_text)

    model_path = download_model(
        repo_id, "original/packages", output_dir="./models")
    print(f"Model downloaded at {model_path}")
