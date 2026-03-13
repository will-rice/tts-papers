# tts-papers

A curated, automatically-updated collection of papers on **text-to-speech synthesis**, neural vocoders, voice conversion, voice cloning, prosody, and related topics — starting from the Tacotron/WaveNet era (2017) and growing every week.

## How it works

* Papers are sourced from [arXiv](https://arxiv.org/) via its public API.
* A [GitHub Actions workflow](.github/workflows/fetch_papers.yml) runs every **Monday at 06:00 UTC** to pull papers submitted in the previous week.
* The full paper list is stored in [`papers.csv`](papers.csv) and the table below is regenerated automatically on every update.

## Running locally

```bash
# Incremental fetch (last 8 days)
python scripts/fetch_papers.py

# Full historical fetch (everything since 2017-01-01)
python scripts/fetch_papers.py --full

# Custom window
python scripts/fetch_papers.py --days 30
```

No third-party dependencies are required — the script uses only the Python standard library.

## Triggering a manual update

Open the **Actions** tab → **Fetch TTS Papers** → **Run workflow**.  
Select *full = true* to back-fill from 2017, or leave it as *false* for an incremental update.

## Search terms

The following keyword queries are used against arXiv title and abstract fields:

`text to speech` · `text-to-speech` · `speech synthesis` · `neural text to speech` · `neural vocoder` · `voice conversion` · `voice cloning` · `speech generation` · `acoustic model speech` · `prosody prediction` · `expressive speech synthesis` · `zero-shot TTS` · `end-to-end speech synthesis` · `diffusion speech synthesis`

## Papers

<!-- PAPERS_TABLE_START -->

<!-- PAPERS_TABLE_END -->
