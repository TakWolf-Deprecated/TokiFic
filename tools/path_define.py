from pathlib import Path

project_root_dir = Path(__file__).parent.joinpath('..').resolve()

src_dir = project_root_dir.joinpath('src')

build_dir = project_root_dir.joinpath('build')
outputs_dir = build_dir.joinpath('outputs')
releases_dir = build_dir.joinpath('releases')
