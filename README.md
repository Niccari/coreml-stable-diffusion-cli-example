# CoreML Stable Diffusion CLI Example

## Installation
### 1. Install deps
`$ pipenv install`

### 2. (if you haven't already) Log in to Hugging Face
`$ pipenv login` 

Note: needs a writable access token

### 3. Download model
`$ pipenv run fetch_model`

v1.4, v1.5 and 2-base are available.

### 4. Run inference

```
$ pipenv shell
$ python -m python_coreml_stable_diffusion.pipeline \
  --prompt "your prompt here" \
  -i "path_to_model" \
  -o outputs/ \
  --compute-unit ALL \
  --model-version "model_version" \
  --seed 93
```

model_version should be:

- v1.4 -> CompVis/stable-diffusion-v1-4 (default)
- v1.5 -> runwayml/stable-diffusion-v1-5
- 2-base -> stabilityai/stable-diffusion-2-base
