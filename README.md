# CoreML Stable Diffusion CLI Example

## Installation
1. Install deps: `$ pipenv install`
1. Log in to Hugging Face: `$ pipenv login`  (Needs a writable access token)
1. Download model: `$ pipenv run fetch_model`
1. Run inference: `pipenv shell && python -m python_coreml_stable_diffusion.pipeline --prompt "your prompt here" -i "path_to_model" -o outputs/ --compute-unit ALL --seed 93`
